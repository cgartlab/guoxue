/* =============================================================
 * 国学课堂 — 语音朗读（Web Speech API）
 * -------------------------------------------------------------
 * 用法：在课件页面引入本文件即可，脚本会自动在工具栏注入「朗读」按钮。
 *   <script src="../../assets/js/speech.js"></script>
 * 行为：
 *   - 点「朗读」读当前页文字；再点「停止」中断
 *   - 翻页自动停止
 *   - 已对拼音注音（<rt>）、按钮、emoji 符号做清洗，避免读出怪音
 *   - 长文本按句切分逐句朗读，规避 Chrome 长句中断的问题
 * ============================================================= */
(function () {
    'use strict';

    var synth = window.speechSynthesis;
    var Utter = window.SpeechSynthesisUtterance;
    if (!synth || !Utter) { return; }   // 浏览器不支持则静默不显示按钮

    var btn = null;
    var speaking = false;
    var queue = [];
    var voice = null;
    var lastActive = null;
    var RATE = 0.95;

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

    /* ---------- 取当前页文字 ---------- */
    var SKIP_TAGS = { RT: 1, RP: 1, BUTTON: 1, SCRIPT: 1, STYLE: 1, SVG: 1, NOSCRIPT: 1 };
    var SKIP_CLASS = /(ds-tab|ds-badge|dots-row|kbd|retake-btn|score-hero__number|page-indicator)/;
    var BLOCK_TAGS = /^(P|H1|H2|H3|H4|H5|LI|DIV|UL|OL|BR|TR|TD|TH)$/;

    function collectText(node, out) {
        for (var i = 0; i < node.childNodes.length; i++) {
            var n = node.childNodes[i];
            if (n.nodeType === 3) {
                var s = n.nodeValue;
                if (s && s.trim()) { out.push(s.trim()); }
            } else if (n.nodeType === 1) {
                if (SKIP_TAGS[n.tagName]) { continue; }
                if (n.className && typeof n.className === 'string' && SKIP_CLASS.test(n.className)) { continue; }
                var before = out.length;
                collectText(n, out);
                if (BLOCK_TAGS.test(n.tagName) && out.length > before) { out.push('\n'); }
            }
        }
    }

    function clean(t) {
        return t
            .replace(/\u2014{1,2}/g, '，')          // 破折号
            .replace(/\u2026+/g, '。')              // 省略号
            .replace(/[\u2460-\u2473]/g, '，')      // ①②③ … 圈号
            .replace(/[·•]/g, ' ')
            .replace(/[ \t]+/g, ' ')
            .replace(/\n{2,}/g, '\n')
            .trim();
    }

    function pageText() {
        var slide = document.querySelector('.slide-container > .slide.active');
        if (!slide) { return ''; }
        var out = [];
        collectText(slide, out);
        return clean(out.join(' '));
    }

    /* ---------- 分句：块内按标点切，块与块不粘连 ---------- */
    function splitSentences(text) {
        var res = [];
        text.split('\n').forEach(function (chunk) {
            var raw = chunk.replace(/([。！？；!?;])/g, '$1|').split('|');
            var buf = '';
            raw.forEach(function (s) {
                s = s.trim();
                if (!s) { return; }
                buf += s;
                if (buf.length >= 14) { res.push(buf); buf = ''; }
            });
            buf = buf.trim();
            if (!buf) { return; }
            var last = res[res.length - 1];
            if (last && buf.length < 6 && last.length < 20) { res[res.length - 1] = last + buf; }
            else { res.push(buf); }
        });
        return res;
    }

    /* ---------- 朗读控制 ---------- */
    var watchdog = null;

    function speakNext() {
        if (!speaking || !queue.length) { stop(); return; }
        var text = queue.shift();
        var u = new Utter(text);
        u.lang = 'zh-CN';
        if (voice) { u.voice = voice; }
        u.rate = RATE;
        u.pitch = 1;

        var advanced = false;
        function next() {
            if (advanced) { return; }
            advanced = true;
            clearTimeout(watchdog);
            if (speaking) { speakNext(); }
        }

        u.onend = next;
        u.onerror = next;
        synth.speak(u);

        // 兜底：某些浏览器中途不回调 onend，按字数估时强制推进
        clearTimeout(watchdog);
        watchdog = setTimeout(next, Math.max(4000, text.length / 3 * 1000 + 2500));
    }

    function start() {
        var text = pageText();
        if (!text) { flash('这一页没有可朗读的文字'); return; }
        synth.cancel();
        queue = splitSentences(text);
        speaking = true;
        updateBtn();
        speakNext();
    }

    function stop() {
        speaking = false;
        queue = [];
        clearTimeout(watchdog);
        try { synth.cancel(); } catch (e) {}
        updateBtn();
    }

    function toggle() { if (speaking) { stop(); } else { start(); } }

    /* ---------- 按钮 ---------- */
    function updateBtn() {
        if (!btn) { return; }
        btn.innerHTML = speaking
            ? '<span class="ds-btn-nav__icon">⏹</span><span class="ds-btn-nav__text">停止</span>'
            : '<span class="ds-btn-nav__icon">🔊</span><span class="ds-btn-nav__text">朗读</span>';
        btn.title = speaking ? '停止朗读' : '朗读本页';
        btn.setAttribute('aria-label', btn.title);
        btn.classList.toggle('is-speaking', speaking);
    }

    function flash(msg) {
        if (!btn) { return; }
        var old = btn.getAttribute('data-flash');
        btn.setAttribute('data-flash', msg);
        btn.title = msg;
        setTimeout(function () { btn.title = speaking ? '停止朗读' : '朗读本页'; }, 1600);
    }

    function mount() {
        var right = document.querySelector('.ds-toolbar__right');
        if (!right || document.getElementById('read-btn')) { return; }
        btn = document.createElement('button');
        btn.className = 'ds-btn-nav ds-btn-nav--icon';
        btn.id = 'read-btn';
        btn.type = 'button';
        btn.addEventListener('click', function (e) { e.preventDefault(); e.stopPropagation(); toggle(); });
        var fs = document.getElementById('fullscreen-btn');
        if (fs && fs.parentNode === right) { right.insertBefore(btn, fs); }
        else { right.appendChild(btn); }
        updateBtn();
    }

    /* ---------- 翻页自动停止 ---------- */
    function watchPaging() {
        var container = document.getElementById('slide-container');
        if (!container) { return; }
        lastActive = container.querySelector('.slide.active');
        var obs = new MutationObserver(function () {
            var a = container.querySelector('.slide.active');
            if (a !== lastActive) {
                lastActive = a;
                if (speaking) { stop(); }
            }
        });
        obs.observe(container, { attributes: true, attributeFilter: ['class'], subtree: true });
    }

    /* ---------- 初始化 ---------- */
    function init() {
        mount();
        watchPaging();
        window.__guoxueSpeechText = pageText;   // 调试用：取当前页待读文本
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // 离开页面时停止，避免后台继续发声
    window.addEventListener('pagehide', function () { if (speaking) { stop(); } });
})();
