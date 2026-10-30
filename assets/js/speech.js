/* =============================================================
 * 国学课堂 — 听书模式（仿微信读书朗读体验，Web Speech API）
 * -------------------------------------------------------------
 * 用法：课件页引入 <script src="../../assets/js/speech.js"></script>
 *   - 工具栏自动出现「🔊 听书」按钮
 *   - 点按钮：从当前页开始连读整课，读到哪句哪句高亮，自动翻页
 *   - 底部播放条：上一句 / 暂停继续 / 下一句 / 语速 / 进度 / 退出
 *   - 朗读中点任意句子可直接跳到那句
 *   - 测验页自动跳过（不作答的题不朗读）
 *   - 浏览器不支持语音时按钮不出现
 * ============================================================= */
(function () {
    'use strict';

    var synth = window.speechSynthesis;
    var Utter = window.SpeechSynthesisUtterance;
    if (!synth || !Utter) { return; }

    /* ---------- 状态 ---------- */
    var state = 'idle';            // idle | playing | paused
    var RATE_STEPS = [0.8, 1.0, 1.25];
    var rateIdx = 1;
    var voice = null;
    var cur = null;                // { slide, list:[{text,els,blockId,si}], i }
    var gen = 0;                   // 朗读代次：换句/暂停后旧回调作废
    var watchdog = null;
    var btn = null, bar = null;

    /* ---------- 语音选择：优先中文女声 ---------- */
    var PREFERRED = ['Xiaoxiao', 'Xiaoyi', 'Yaoyao', 'Huihui', 'Tingting', 'Meijia', '普通话', 'Chinese'];
    function pickVoice() {
        var list = synth.getVoices() || [];
        var zh = list.filter(function (v) { return /^zh/i.test(v.lang); });
        if (!zh.length) { voice = null; return; }
        for (var i = 0; i < PREFERRED.length; i++) {
            for (var j = 0; j < zh.length; j++) {
                if (zh[j].name.indexOf(PREFERRED[i]) >= 0) { voice = zh[j]; return; }
            }
        }
        voice = zh[0];
    }
    pickVoice();
    if (synth.onvoiceschanged !== undefined) {
        synth.onvoiceschanged = function () { if (!voice) { pickVoice(); } };
    }

    /* ---------- 文本工具 ---------- */
    var SKIP_TAGS = { RT: 1, RP: 1, BUTTON: 1, SCRIPT: 1, STYLE: 1, SVG: 1, NOSCRIPT: 1 };
    var SKIP_CLASS = /(ds-tab|ds-badge|dots-row|kbd|retake-btn|page-indicator|tts-bar)/;

    function clean(t) {
        return t
            .replace(/\u2014{1,2}/g, '，')
            .replace(/\u2026+/g, '。')
            .replace(/[\u2460-\u2473]/g, '，')
            .replace(/[·•]/g, ' ')
            .replace(/[ \t]+/g, ' ')
            .trim();
    }

    function splitRaw(text) {
        var out = [], buf = '';
        for (var i = 0; i < text.length; i++) {
            var ch = text.charAt(i);
            buf += ch;
            if ('。！？；!?;'.indexOf(ch) >= 0) { out.push(buf); buf = ''; }
        }
        if (buf.trim()) { out.push(buf); }
        return out.map(function (s) { return s.trim(); }).filter(Boolean);
    }

    function collectTextNodes(root, out) {
        for (var i = 0; i < root.childNodes.length; i++) {
            var n = root.childNodes[i];
            if (n.nodeType === 3) {
                if (n.nodeValue.trim()) { out.push(n); }
            } else if (n.nodeType === 1) {
                if (SKIP_TAGS[n.tagName]) { continue; }
                if (n.className && typeof n.className === 'string' && SKIP_CLASS.test(n.className)) { continue; }
                collectTextNodes(n, out);
            }
        }
        return out;
    }

    /* ---------- 高亮包裹：把每个块里的文字按句包进 span ---------- */
    var BLOCK_SEL = 'p, h1, h2, h3, h4, h5, li, blockquote, .end-quote, .cover-desc, .cover-subtitle';
    var blockSeq = 0;

    function wrapBlock(block) {
        var nodes = collectTextNodes(block, []);
        if (!nodes.length) { return; }
        var full = nodes.map(function (n) { return n.nodeValue; }).join('');
        var sents = splitRaw(full);
        if (!sents.length) { return; }
        var spans = sents.map(function () { return []; });
        var si = 0, consumed = 0;
        nodes.forEach(function (node) {
            var text = node.nodeValue;
            var pos = 0;
            while (pos < text.length && si < sents.length) {
                var take = Math.min(sents[si].length - consumed, text.length - pos);
                var el = wrapRange(node, pos, pos + take, si);
                if (el) { spans[si].push(el); }
                consumed += take;
                pos += take;
                if (consumed >= sents[si].length) { si++; consumed = 0; }
            }
        });
        block.__ttsId = 'tts-b' + (blockSeq++);
        block.__ttsSents = sents;
        block.__ttsSpans = spans;
    }

    function wrapRange(node, start, end, si) {
        if (end <= start) { return null; }
        try {
            var range = document.createRange();
            range.setStart(node, start);
            range.setEnd(node, end);
            var span = document.createElement('span');
            span.className = 'tts-sent';
            span.setAttribute('data-sent', si);
            range.surroundContents(span);
            return span;
        } catch (e) { return null; }
    }

    function buildPlaylist(slide) {
        var blocks = slide.querySelectorAll(BLOCK_SEL);
        var seen = {};
        var list = [];
        blocks.forEach(function (block) {
            if (seen[block.__ttsId]) { return; }
            seen[block.__ttsId] = true;
            if (!block.__ttsSents) { return; }
            block.__ttsSents.forEach(function (raw, si) {
                list.push({
                    text: clean(raw),
                    els: block.__ttsSpans[si],
                    blockId: block.__ttsId,
                    si: si
                });
            });
        });
        return { slide: slide, list: list, i: 0 };
    }

    function prepareSlide(slide) {
        if (!slide.dataset.ttsPrepared) {
            slide.querySelectorAll(BLOCK_SEL).forEach(wrapBlock);
            slide.dataset.ttsPrepared = '1';
        }
        return buildPlaylist(slide);
    }

    /* ---------- 页面导航 ---------- */
    function activeSlide() { return document.querySelector('.slide-container > .slide.active'); }
    function nextBtn() { return document.getElementById('nav-next'); }

    function isQuizSlide(slide) { return slide && slide.getAttribute('data-section') === 'quiz'; }

    // 从 fromSlide 起向后找第一个可读页（含自身）；找不到返回 null
    function findReadable(fromSlide) {
        var el = fromSlide;
        while (el && isQuizSlide(el)) { el = el.nextElementSibling; }
        return el;
    }

    function jumpTo(el) {
        var btnNext = nextBtn();
        if (!btnNext) { return false; }
        var guard = 0;
        while (activeSlide() !== el && guard++ < 40) { btnNext.click(); }
        return activeSlide() === el;
    }

    /* ---------- 高亮 ---------- */
    function clearHighlight() {
        document.querySelectorAll('.tts-sent.on').forEach(function (el) { el.classList.remove('on'); });
    }

    function highlight(item) {
        clearHighlight();
        if (!item || !item.els) { return; }
        item.els.forEach(function (el) { el.classList.add('on'); });
        var last = item.els[item.els.length - 1];
        if (last && last.scrollIntoView) {
            try { last.scrollIntoView({ block: 'center', behavior: 'smooth' }); } catch (e) {}
        }
    }

    /* ---------- 播放核心 ---------- */
    function speakCur() {
        if (state !== 'playing' || !cur) { return; }
        if (cur.i >= cur.list.length) { pageEnd(); return; }
        gen++;
        var myGen = gen;
        var item = cur.list[cur.i];
        highlight(item);
        updateBar();

        var u = new Utter(item.text);
        u.lang = 'zh-CN';
        if (voice) { u.voice = voice; }
        u.rate = RATE_STEPS[rateIdx];
        u.pitch = 1;

        var advanced = false;
        function done() {
            if (advanced || myGen !== gen || state !== 'playing') { return; }
            advanced = true;
            clearTimeout(watchdog);
            cur.i++;
            speakCur();
        }
        u.onend = done;
        u.onerror = done;
        synth.speak(u);

        // 兜底：个别浏览器不回调 onend，按字数估时强制推进
        clearTimeout(watchdog);
        watchdog = setTimeout(done, Math.max(4000, item.text.length / 3 * 1000 + 2500));
    }

    function pageEnd() {
        var el = findReadable(cur.slide.nextElementSibling);
        if (!el || !jumpTo(el)) { exit(); }
        // 翻页后 observer 会接管：prepare 新页继续读
    }

    function start() {
        var slide = activeSlide();
        if (!slide) { return; }
        if (isQuizSlide(slide)) {
            var el = findReadable(slide);
            if (!el || !jumpTo(el)) { return; }
            slide = activeSlide();
        }
        cur = prepareSlide(slide);
        cur.i = 0;
        state = 'playing';
        showBar();
        updateBtn();
        speakCur();
    }

    function pause() {
        state = 'paused';
        gen++;
        clearTimeout(watchdog);
        try { synth.cancel(); } catch (e) {}
        updateBar();
    }

    function resume() {
        if (!cur) { start(); return; }
        state = 'playing';
        speakCur();
        updateBar();
    }

    function stopSpeech() {
        gen++;
        clearTimeout(watchdog);
        try { synth.cancel(); } catch (e) {}
    }

    function exit() {
        state = 'idle';
        stopSpeech();
        clearHighlight();
        if (bar) { bar.style.display = 'none'; }
        updateBtn();
    }

    function seek(delta) {
        if (!cur) { return; }
        stopSpeech();
        var i = cur.i + delta;
        if (i < 0) { i = 0; }
        if (i >= cur.list.length) {
            // 跳到下一页开头
            var el = findReadable(cur.slide.nextElementSibling);
            if (el && jumpTo(el)) {
                if (state === 'paused') {           // 暂停中跳页：停在新页第 0 句，不播放
                    cur = prepareSlide(el);
                    cur.i = 0;
                    highlight(cur.list[0]);
                    updateBar();
                }
                return;                              // 播放中交给 observer 接管
            }
            cur.i = cur.list.length - 1;
            if (state === 'playing') { speakCur(); }
            return;
        }
        cur.i = i;
        if (state === 'paused') { highlight(cur.list[i]); updateBar(); }
        else { speakCur(); }
    }

    function changeRate() {
        rateIdx = (rateIdx + 1) % RATE_STEPS.length;
        if (state === 'playing') { stopSpeech(); speakCur(); }   // 当前句按新语速重读
        updateBar();
    }

    /* ---------- 界面 ---------- */
    var CSS = [
        '#tts-bar{position:fixed;bottom:16px;left:50%;transform:translateX(-50%);',
        'background:rgba(28,28,32,.94);color:#fff;border-radius:999px;padding:8px 12px;',
        'display:flex;align-items:center;gap:2px;z-index:9999;box-shadow:0 6px 24px rgba(0,0,0,.28);',
        'font-family:inherit;max-width:96vw;}',
        '#tts-bar button{background:none;border:none;color:#fff;font-size:17px;line-height:1;',
        'padding:6px 9px;cursor:pointer;border-radius:999px;}',
        '#tts-bar button:hover{background:rgba(255,255,255,.14);}',
        '#tts-bar #tts-rate{font-size:13px;font-weight:700;min-width:46px;text-align:center;}',
        '#tts-bar #tts-pos{font-size:12px;color:rgba(255,255,255,.65);min-width:52px;text-align:center;',
        'font-variant-numeric:tabular-nums;}',
        '.tts-sent{border-radius:3px;}',
        '.tts-sent.on{background:rgba(245,158,11,.38);box-shadow:0 0 0 2px rgba(245,158,11,.38);}'
    ].join('');

    function ensureStyle() {
        if (document.getElementById('tts-style')) { return; }
        var st = document.createElement('style');
        st.id = 'tts-style';
        st.textContent = CSS;
        document.head.appendChild(st);
    }

    function ensureBar() {
        if (bar) { return; }
        ensureStyle();
        bar = document.createElement('div');
        bar.id = 'tts-bar';
        bar.style.display = 'none';
        bar.innerHTML =
            '<button id="tts-prev" title="上一句" aria-label="上一句">⏮</button>' +
            '<button id="tts-play" title="暂停" aria-label="暂停或继续">⏸</button>' +
            '<button id="tts-next" title="下一句" aria-label="下一句">⏭</button>' +
            '<button id="tts-rate" title="切换语速">1.0x</button>' +
            '<span id="tts-pos">0/0</span>' +
            '<button id="tts-exit" title="退出听书" aria-label="退出听书">✕</button>';
        document.body.appendChild(bar);
        bar.querySelector('#tts-play').addEventListener('click', function () {
            if (state === 'playing') { pause(); } else { resume(); }
        });
        bar.querySelector('#tts-prev').addEventListener('click', function () { seek(-1); });
        bar.querySelector('#tts-next').addEventListener('click', function () { seek(1); });
        bar.querySelector('#tts-rate').addEventListener('click', changeRate);
        bar.querySelector('#tts-exit').addEventListener('click', exit);
    }

    function updateBar() {
        if (!bar || !cur) { return; }
        bar.querySelector('#tts-play').textContent = state === 'playing' ? '⏸' : '▶';
        bar.querySelector('#tts-rate').textContent = RATE_STEPS[rateIdx].toFixed(1) + 'x';
        bar.querySelector('#tts-pos').textContent = (cur.i + 1) + '/' + cur.list.length;
    }

    function showBar() {
        ensureBar();
        bar.style.display = 'flex';
        updateBar();
    }

    function updateBtn() {
        if (!btn) { return; }
        var active = state !== 'idle';
        btn.innerHTML = active
            ? '<span class="ds-btn-nav__icon">⏹</span><span class="ds-btn-nav__text">听书中</span>'
            : '<span class="ds-btn-nav__icon">🔊</span><span class="ds-btn-nav__text">听书</span>';
        btn.title = active ? '退出听书' : '从当前页开始连读整课';
        btn.setAttribute('aria-label', btn.title);
    }

    /* ---------- 翻页观察：自动翻页 / 手动翻页都从这里接管 ---------- */
    function watchPaging() {
        var container = document.getElementById('slide-container');
        if (!container) { return; }
        var obs = new MutationObserver(function () {
            var slide = activeSlide();
            if (!slide) { return; }
            if (state === 'idle') { clearHighlight(); return; }
            if (cur && slide === cur.slide) { return; }        // 本页已在读
            if (isQuizSlide(slide)) {                          // 翻到测验页：跳过
                var el = findReadable(slide);
                if (el && jumpTo(el)) { return; }
                exit();
                return;
            }
            stopSpeech();
            var wasPaused = (state === 'paused');
            cur = prepareSlide(slide);
            cur.i = 0;
            if (wasPaused) {                     // 暂停中翻页：停在新页第 0 句
                highlight(cur.list[0]);
                updateBar();
            } else {
                speakCur();
            }
        });
        obs.observe(container, { attributes: true, attributeFilter: ['class'], subtree: true });
    }

    /* ---------- 朗读中点句子跳读 ---------- */
    function watchSeekClick() {
        document.addEventListener('click', function (e) {
            if (state === 'idle' || !cur) { return; }
            var t = e.target;
            if (!t || !t.closest) { return; }
            var span = t.closest('.tts-sent');
            if (!span) { return; }
            var slide = span.closest('.slide');
            if (!slide || slide !== activeSlide()) { return; }
            var node = span.parentNode, blockEl = null;
            while (node && node !== slide) {
                if (node.__ttsId) { blockEl = node; break; }
                node = node.parentNode;
            }
            if (!blockEl) { return; }
            var si = parseInt(span.getAttribute('data-sent'), 10);
            for (var i = 0; i < cur.list.length; i++) {
                if (cur.list[i].blockId === blockEl.__ttsId && cur.list[i].si === si) {
                    stopSpeech();
                    cur.i = i;
                    if (state === 'paused') { highlight(cur.list[i]); updateBar(); }
                    else { speakCur(); }
                    break;
                }
            }
        });
    }

    /* ---------- 入口按钮 ---------- */
    function mount() {
        var right = document.querySelector('.ds-toolbar__right');
        if (!right || document.getElementById('read-btn')) { return; }
        btn = document.createElement('button');
        btn.className = 'ds-btn-nav ds-btn-nav--icon';
        btn.id = 'read-btn';
        btn.type = 'button';
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            if (state === 'idle') { start(); } else { exit(); }
        });
        var fs = document.getElementById('fullscreen-btn');
        if (fs && fs.parentNode === right) { right.insertBefore(btn, fs); }
        else { right.appendChild(btn); }
        updateBtn();
    }

    function init() {
        mount();
        watchPaging();
        watchSeekClick();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    window.addEventListener('pagehide', function () { if (state !== 'idle') { exit(); } });
})();
