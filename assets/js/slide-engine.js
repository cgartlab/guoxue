/* =============================================================
 * CGArtLab Slide Engine — 共享课程引擎 v1.0
 * -------------------------------------------------------------
 * 来源:lesson01-lunyu.html (原 lines 1010-1271)
 * 用途:被各课程页 index.html 引用,提供:
 *   - 测验题目渲染与判分
 *   - 章节切换(讲义 / 测验 / 答疑解惑)
 *   - 上一页/下一页 / 键盘左右 / 触屏滑动 / 点击半屏
 *   - 全屏切换
 *   - 进度条 / 圆点导航 / 页码指示
 *
 * 自定义本课数据的方法(推荐):
 *   在引用本文件之后,定义 window.GUOXUE_QUIZ_OVERRIDE = [...],
 *   引擎将优先使用你提供的题目。
 * ============================================================= */
(function () {
    'use strict';

    /* ===== 默认测验数据(可被 GUOXUE_QUIZ_OVERRIDE 覆盖) ===== */
    var DEFAULT_QUIZ = [
        { q: '"学而时习之,不亦说乎?"这句话出自哪部经典著作?', opts: ['《道德经》', '《论语》', '《诗经》'], ans: 1, exp: '出自《论语·学而》,是论语开篇第一句。"说"同"悦",意思是愉快。整句意思是:学了知识并经常复习,不也很愉快吗?' },
        { q: '孔子,名什么?字什么?', opts: ['名丘,字仲尼', '名轲,字子舆', '名明,字孔明'], ans: 0, exp: '孔子名丘,字仲尼。孟子名轲字子舆,诸葛亮字孔明。孔子被尊称为"至圣先师"。' },
        { q: '"三人行,必有我师焉"这句话强调什么道理?', opts: ['三个人一起走路才能学习', '随时随地向身边的人学习,取长补短', '必须要找老师才能学习'], ans: 1, exp: '出自《论语·述而》。孔子教导我们要善于发现别人的优点来学习,看到别人的缺点则反省自己。' },
        { q: '"己所不欲,勿施于人"是什么意思?', opts: ['自己不想要的东西,不要给别人', '自己做不到的事情,不要要求别人', '自己没有的东西,不要羡慕别人'], ans: 0, exp: '出自《论语·卫灵公》,是儒家"仁"的核心表达之一。教导我们做人要懂得换位思考,将心比心。' },
        { q: '孔子提出的"六艺"不包括以下哪一项?', opts: ['礼、乐', '射、御', '诗、词'], ans: 2, exp: '六艺:礼、乐、射、御、书、数。"诗"属六经,"词"是后来的文学形式,不在六艺之列。' },
        { q: '"知之为知之,不知为不知,是知也"告诉我们要怎样对待学习?', opts: ['不懂装懂,显得聪明', '老实承认知道和不知道的,这才是真正的智慧', '知道一点就够了,不需要全部了解'], ans: 1, exp: '出自《论语·为政》,最后一个"知"通"智"。学习要诚实,虚心才能进步。' },
        { q: '"温故而知新,可以为师矣"这句话的意思是什么?', opts: ['温习旧知识就能当老师', '温习学过的知识,能有新体会新发现,就可以做老师了', '只要有经验就能当老师'], ans: 1, exp: '出自《论语·为政》。不仅要用习旧知识,还要在复习中获得新理解和启发,这才具备做老师的条件。' },
        { q: '以下哪句话体现了孔子对"孝"的重视?', opts: ['"有朋自远方来,不亦乐乎"', '"父母在,不远游,游必有方"', '"学而时习之,不亦说乎"'], ans: 1, exp: '出自《论语·里仁》。意思是父母在世时不要远行;如果必须出行,要有明确方向。体现了对孝道的重视。' },
        { q: '孔子的弟子中,以"好学"著称、最得孔子喜爱的是谁?', opts: ['子路', '子贡', '颜回'], ans: 2, exp: '颜回是孔子最得意的弟子,以德行和好学著称。孔子称赞他"不迁怒,不贰过",虽生活贫困却不改好学之乐。' },
        { q: '《论语》一共由多少篇组成?', opts: ['10 篇', '20 篇', '30 篇'], ans: 1, exp: '《论语》共 20 篇,492 章。每篇篇名取自开头第一句话中的两个字,如"学而""为政"等。' }
    ];

    var quizData = Array.isArray(window.GUOXUE_QUIZ_OVERRIDE) && window.GUOXUE_QUIZ_OVERRIDE.length > 0
        ? window.GUOXUE_QUIZ_OVERRIDE
        : DEFAULT_QUIZ;

    /* ===== 渲染测验卡片 ===== */
    var labels = ['A', 'B', 'C', 'D', 'E', 'F'];
    quizData.forEach(function (item, idx) {
        var el = document.getElementById('quiz-' + idx);
        if (!el) return;
        var h = '<span class="ds-badge ds-badge--success">测验第 ' + (idx + 1) + ' 题</span>';
        h += '<h2 style="font-size:1.5rem;margin-bottom:var(--ds-space-5);border:none;">' + item.q + '</h2>';
        h += '<div class="quiz-options-wrap">';
        item.opts.forEach(function (opt, oi) {
            h += '<button class="quiz-option" data-q="' + idx + '" data-o="' + oi + '">';
            h += '<span class="opt-label">' + labels[oi] + '</span><span>' + opt + '</span></button>';
        });
        h += '</div>';
        h += '<div class="quiz-explain" id="exp-' + idx + '"></div>';
        el.innerHTML = h;
    });

    /* ===== 答题逻辑 ===== */
    var quizAnswered = {};
    var quizScore = 0;
    document.addEventListener('click', function (e) {
        var btn = e.target.closest('.quiz-option');
        if (!btn) return;
        var qi = parseInt(btn.dataset.q, 10);
        if (quizAnswered[qi]) return;
        quizAnswered[qi] = true;
        var oi = parseInt(btn.dataset.o, 10);
        var item = quizData[qi];
        var btns = document.querySelectorAll('[data-q="' + qi + '"]');
        var ok = (oi === item.ans);
        btns.forEach(function (b) { b.classList.add('disabled'); });
        if (ok) { btn.classList.add('correct'); quizScore += 10; }
        else { btn.classList.add('wrong'); btns[item.ans].classList.add('correct'); }
        var expEl = document.getElementById('exp-' + qi);
        if (expEl) {
            expEl.className = 'quiz-explain show ' + (ok ? 'correct-exp' : 'wrong-exp');
            expEl.innerHTML = '<b>' + (ok ? '✓ 回答正确' : '✗ 回答错误,正确答案已标出') + '</b><br><br>' + item.exp;
        }
    });

    /* ===== 重新答题 ===== */
    document.addEventListener('click', function(e) {
        var retake = e.target.closest('#retake-btn');
        if (!retake) return;
        quizAnswered = {};
        quizScore = 0;
        document.querySelectorAll('.quiz-option').forEach(function(b) {
            b.classList.remove('disabled','correct','wrong');
        });
        document.querySelectorAll('.quiz-explain').forEach(function(el) {
            el.className = 'quiz-explain'; el.innerHTML = '';
        });
        var scoreDisplay = document.getElementById('score-display');
        if (scoreDisplay) {
            scoreDisplay.textContent = '0';
            document.getElementById('score-message').textContent = '重新答题中...';
            document.getElementById('correct-count').textContent = '0';
            document.getElementById('total-score').textContent = '0';
            document.getElementById('score-percent').textContent = '0%';
        }
        goToPage(10);
    });

    /* ===== 导航逻辑 ===== */
    var allSlides = document.querySelectorAll('.slide');
    var totalPages = allSlides.length;
    var curPage = 0;
    var sections = {
        lecture: { start: 0, end: 9 },
        quiz:    { start: 10, end: 21 },
        review:  { start: 22, end: 24 }
    };

    function $(id) { return document.getElementById(id); }

    function goToPage(n) {
        if (n < 0 || n >= totalPages) return;
        allSlides[curPage].classList.remove('active');
        curPage = n;
        allSlides[curPage].classList.add('active');
        allSlides[curPage].scrollTop = 0;
        if (n === 21) updateScoreDisplay();
        updateUI();
    }

    function updateScoreDisplay() {
        var scoreDisplay = document.getElementById('score-display');
        var scoreMessage = document.getElementById('score-message');
        var correctCount = document.getElementById('correct-count');
        var totalScore = document.getElementById('total-score');
        var scorePercent = document.getElementById('score-percent');
        if (!scoreDisplay) return;
        var correct = quizScore / 10;
        scoreDisplay.textContent = quizScore + ' 分';
        correctCount.textContent = correct;
        totalScore.textContent = quizScore;
        scorePercent.textContent = Math.round(quizScore) + '%';
        if (quizScore >= 90) scoreMessage.textContent = '🎉 太棒了!你是论语小达人!';
        else if (quizScore >= 70) scoreMessage.textContent = '👍 不错!对论语有不错的了解!';
        else if (quizScore >= 60) scoreMessage.textContent = '💪 继续加油!再多复习几遍!';
        else scoreMessage.textContent = '📚 需要加强学习,建议重温讲义部分!';
    }

    function updateUI() {
        var pi = $('page-indicator');
        if (pi) pi.textContent = (curPage + 1) + ' / ' + totalPages;
        var prev = $('nav-prev');
        var next = $('nav-next');
        if (prev) prev.disabled = (curPage === 0);
        if (next) next.disabled = (curPage === totalPages - 1);
        var fill = $('progress-fill');
        if (fill) fill.style.width = ((curPage + 1) / totalPages * 100) + '%';
        document.querySelectorAll('.ds-tab').forEach(function (t) {
            var s = sections[t.dataset.section];
            if (!s) return;
            t.classList.toggle('active', curPage >= s.start && curPage <= s.end);
        });
        renderDots();
    }

    function renderDots() {
        var box = $('dots-row');
        if (!box) return;
        box.innerHTML = '';
        for (var i = 0; i < totalPages; i++) {
            var d = document.createElement('button');
            d.className = 'ds-dot' + (i === curPage ? ' active' : '');
            d.setAttribute('aria-label', '第 ' + (i + 1) + ' 页');
            (function (n) {
                d.addEventListener('click', function () { goToPage(n); });
            })(i);
            box.appendChild(d);
        }
    }

    /* ===== 板块切换 ===== */
    document.querySelectorAll('.ds-tab').forEach(function (t) {
        t.addEventListener('click', function () {
            var s = sections[t.dataset.section];
            if (s) goToPage(s.start);
        });
    });

    /* ===== 翻页按钮 ===== */
    var prevBtn = $('nav-prev');
    var nextBtn = $('nav-next');
    if (prevBtn) prevBtn.addEventListener('click', function () { goToPage(curPage - 1); });
    if (nextBtn) nextBtn.addEventListener('click', function () { goToPage(curPage + 1); });

    /* ===== 键盘 ===== */
    document.addEventListener('keydown', function (e) {
        if (e.target && /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName)) return;
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {
            e.preventDefault(); goToPage(curPage + 1);
        } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
            e.preventDefault(); goToPage(curPage - 1);
        }
    });

    /* ===== 全屏切换 ===== */
    var fullscreenBtn = $('fullscreen-btn');
    var slideContainer = document.querySelector('.slide-container');

    function toggleFullscreen() {
        if (!document.fullscreenElement) {
            var p = slideContainer && slideContainer.requestFullscreen && slideContainer.requestFullscreen();
            if (p && p.then) p.then(function () { updateFullscreenBtn(true); }).catch(function () { updateFullscreenBtn(true); });
            else updateFullscreenBtn(true);
        } else {
            var q = document.exitFullscreen && document.exitFullscreen();
            if (q && q.then) q.then(function () { updateFullscreenBtn(false); });
            else updateFullscreenBtn(false);
        }
    }

    function updateFullscreenBtn(isFullscreen) {
        if (!fullscreenBtn) return;
        if (isFullscreen) {
            fullscreenBtn.classList.add('exit');
            fullscreenBtn.title = '退出全屏';
        } else {
            fullscreenBtn.classList.remove('exit');
            fullscreenBtn.title = '切换全屏显示';
        }
        fullscreenBtn.textContent = '⛶';
    }

    if (fullscreenBtn) {
        fullscreenBtn.addEventListener('click', function (e) {
            e.preventDefault(); e.stopPropagation(); toggleFullscreen();
        });
    }
    document.addEventListener('fullscreenchange', function () {
        updateFullscreenBtn(!!document.fullscreenElement);
    });

    /* ===== 触屏滑动 ===== */
    (function () {
        var touchStartX = 0, touchStartY = 0;
        var swipeThreshold = 50;
        var container = document.querySelector('.slide-viewport');
        if (!container) return;
        container.addEventListener('touchstart', function (e) {
            touchStartX = e.changedTouches[0].screenX;
            touchStartY = e.changedTouches[0].screenY;
        }, { passive: true });
        container.addEventListener('touchend', function (e) {
            var deltaX = e.changedTouches[0].screenX - touchStartX;
            var deltaY = e.changedTouches[0].screenY - touchStartY;
            if (Math.abs(deltaX) > Math.abs(deltaY) && Math.abs(deltaX) > swipeThreshold) {
                if (deltaX > 0) goToPage(curPage - 1);
                else goToPage(curPage + 1);
            }
        }, { passive: true });
    })();

    /* ===== 移动端点击半屏翻页 ===== */
    (function () {
        var viewport = document.querySelector('.slide-viewport');
        if (!viewport) return;
        viewport.addEventListener('click', function (e) {
            if (e.target.closest('button, a, input, textarea, .quiz-option, .ds-btn-nav')) return;
            var rect = viewport.getBoundingClientRect();
            var clickX = e.clientX - rect.left;
            if (clickX < rect.width / 2) goToPage(curPage - 1);
            else goToPage(curPage + 1);
        });
    })();

    updateUI();
})();
