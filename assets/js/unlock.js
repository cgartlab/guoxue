/* =============================================================
 * 国学课堂 — 解锁状态管理模块 (unlock.js)
 * -------------------------------------------------------------
 * 用途:管理课程解锁状态,提供付费弹窗 UI
 * 依赖:无(纯原生 JS)
 * 用法:在 slide-engine.js 之前引入本文件
 * ============================================================= */
(function () {
    'use strict';

    /* ===== 配置 ===== */
    var CONFIG = {
        unlockCode: 'guoxue666',           // 固定解锁码
        storageKey: 'guoxue_unlocked',     // localStorage key
        price: '9.90',                     // 显示价格
        // 免费课程 ID 列表(前 5 课)
        freeCourses: [
            '01-lunyu',
            '02-lunyu-mixed',
            '03-sanzijing',
            '04-xueer',
            '05-xueer-xiaoti'
        ]
    };

    /* ===== 解锁状态管理 ===== */
    function isUnlocked() {
        try {
            return localStorage.getItem(CONFIG.storageKey) === '1';
        } catch (e) {
            return false;
        }
    }

    function saveUnlock() {
        try {
            localStorage.setItem(CONFIG.storageKey, '1');
        } catch (e) { /* ignore */ }
    }

    function isCourseFree(courseId) {
        for (var i = 0; i < CONFIG.freeCourses.length; i++) {
            if (CONFIG.freeCourses[i] === courseId) return true;
        }
        return false;
    }

    function verifyCode(code) {
        return code === CONFIG.unlockCode;
    }

    /* ===== 付费弹窗 UI ===== */
    var modalEl = null;
    var inputEl = null;
    var msgEl = null;

    function createModal() {
        if (modalEl) return;

        // 遮罩层
        modalEl = document.createElement('div');
        modalEl.className = 'paywall-overlay';
        modalEl.setAttribute('role', 'dialog');
        modalEl.setAttribute('aria-modal', 'true');
        modalEl.setAttribute('aria-label', '解锁课程');

        modalEl.innerHTML =
            '<div class="paywall-modal">' +
                '<button class="paywall-close" id="paywall-close" aria-label="关闭">&times;</button>' +

                '<div class="paywall-header">' +
                    '<h2 class="paywall-title">解锁全部国学课程</h2>' +
                    '<p class="paywall-subtitle">49 门精品课程，一次打赏，永久解锁</p>' +
                '</div>' +

                '<div class="paywall-body">' +
                    '<!-- 微信收款码 -->' +
                    '<div class="paywall-qr-section">' +
                        '<p class="paywall-qr-label">推荐使用微信支付</p>' +
                        '<div class="paywall-qr-wrapper">' +
                            '<img class="paywall-qr-img" src="../../assets/img/wechat-qr.svg" alt="微信收款码">' +
                        '</div>' +
                        '<p class="paywall-price">¥' + CONFIG.price + '</p>' +
                    '</div>' +

                    '<!-- 支付宝收款码(占位) -->' +
                    '<div class="paywall-qr-section paywall-qr-section--alt">' +
                        '<p class="paywall-qr-label">或使用支付宝</p>' +
                        '<div class="paywall-qr-wrapper paywall-qr-wrapper--small">' +
                            '<img class="paywall-qr-img" src="../../assets/img/alipay-qr.svg" alt="支付宝收款码">' +
                        '</div>' +
                    '</div>' +

                    '<!-- 解锁码输入 -->' +
                    '<div class="paywall-code-section">' +
                        '<p class="paywall-code-hint">扫码支付后，输入解锁码：</p>' +
                        '<div class="paywall-code-row">' +
                            '<input class="paywall-code-input" id="paywall-code-input" type="text" placeholder="请输入解锁码" autocomplete="off" maxlength="20">' +
                            '<button class="paywall-code-btn" id="paywall-code-btn">解锁</button>' +
                        '</div>' +
                        '<p class="paywall-code-msg" id="paywall-code-msg"></p>' +
                    '</div>' +
                '</div>' +

                '<div class="paywall-footer">' +
                    '<p>解锁码由站长提供，如有问题请联系站长</p>' +
                '</div>' +
            '</div>';

        document.body.appendChild(modalEl);

        // 绑定事件
        var closeBtn = document.getElementById('paywall-close');
        var codeBtn = document.getElementById('paywall-code-btn');
        inputEl = document.getElementById('paywall-code-input');
        msgEl = document.getElementById('paywall-code-msg');

        if (closeBtn) {
            closeBtn.addEventListener('click', hidePaywall);
        }

        // 点击遮罩层关闭
        modalEl.addEventListener('click', function (e) {
            if (e.target === modalEl) hidePaywall();
        });

        // ESC 键关闭
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && modalEl && modalEl.classList.contains('paywall-overlay--show')) {
                hidePaywall();
            }
        });

        // 解锁按钮
        if (codeBtn) {
            codeBtn.addEventListener('click', handleUnlock);
        }

        // 回车键解锁
        if (inputEl) {
            inputEl.addEventListener('keydown', function (e) {
                if (e.key === 'Enter') handleUnlock();
            });
        }
    }

    function handleUnlock() {
        if (!inputEl || !msgEl) return;
        var code = inputEl.value.trim();
        if (!code) {
            msgEl.textContent = '请输入解锁码';
            msgEl.className = 'paywall-code-msg paywall-code-msg--error';
            return;
        }
        if (verifyCode(code)) {
            saveUnlock();
            msgEl.textContent = '解锁成功！';
            msgEl.className = 'paywall-code-msg paywall-code-msg--success';
            // 延迟关闭弹窗
            setTimeout(function () {
                hidePaywall();
                // 刷新页面以加载完整内容
                window.location.reload();
            }, 1000);
        } else {
            msgEl.textContent = '解锁码不正确，请重试';
            msgEl.className = 'paywall-code-msg paywall-code-msg--error';
            inputEl.value = '';
            inputEl.focus();
        }
    }

    function showPaywall() {
        createModal();
        if (modalEl) {
            modalEl.classList.add('paywall-overlay--show');
            document.body.style.overflow = 'hidden';
            // 聚焦到输入框
            setTimeout(function () {
                if (inputEl) inputEl.focus();
            }, 300);
        }
    }

    function hidePaywall() {
        if (modalEl) {
            modalEl.classList.remove('paywall-overlay--show');
            document.body.style.overflow = '';
        }
    }

    /* ===== 暴露全局接口 ===== */
    window.UNLOCK = {
        isUnlocked: isUnlocked,
        isCourseFree: isCourseFree,
        verifyCode: verifyCode,
        showPaywall: showPaywall,
        hidePaywall: hidePaywall,
        CONFIG: CONFIG
    };

})();
