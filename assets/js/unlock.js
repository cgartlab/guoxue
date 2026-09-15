/* =============================================================
 * 国学课堂 — 解锁状态管理模块 (unlock.js)
 * -------------------------------------------------------------
 * 用途:管理课程解锁状态,提供付费弹窗 UI(面包多支付 + 订单号验单)
 * 依赖:无(纯原生 JS)
 * 用法:在 slide-engine.js 之前引入本文件
 *
 * 验单流程:用户在面包多付款后拿到订单号,回站点粘贴订单号,
 *          前端把订单号 POST 到 Cloudflare Worker(pay-worker/),
 *          Worker 调面包多开放接口验单,通过后返回独立解锁码,
 *          前端写入 localStorage 后刷新完成解锁。
 * ============================================================= */
(function () {
    'use strict';

    /* ===== 配置 ===== */
    var CONFIG = {
        // 面包多商品链接
        productUrl: 'https://mbd.pub/o/bread/YZaVlJ5rag==',
        // 显示价格(元)
        price: '9.90',
        // localStorage key
        storageKey: 'guoxue_unlocked',
        // 解锁码存储 key
        codeStorageKey: 'guoxue_unlock_code',
        // 验单接口:部署 Cloudflare Worker 后,把下方占位地址替换成真实 Worker URL;
        // 或在页面加载前设置 window.GUOXUE_REDEEM_API = 'https://xxx.workers.dev/api/redeem'
        redeemApi: (window.GUOXUE_REDEEM_API) || 'https://pay.8023laozhanshi.cc/api/redeem',
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

    /* ===== 付费弹窗 UI ===== */
    var modalEl = null;
    var orderEl = null;
    var emailEl = null;
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
                    '<p class="paywall-subtitle">50+ 门精品课程，一次付费，永久解锁</p>' +
                '</div>' +

                '<div class="paywall-body">' +
                    '<!-- 面包多购买入口 -->' +
                    '<a class="paywall-product-btn" id="paywall-product-btn" ' +
                        'href="' + CONFIG.productUrl + '" target="_blank" rel="noopener noreferrer">' +
                        '去面包多支付 ¥' + CONFIG.price +
                    '</a>' +
                    '<p class="paywall-order-hint">付款后在面包多订单页复制订单号，回到这里粘贴即可解锁</p>' +

                    '<!-- 订单号 / 邮箱 / 解锁 -->' +
                    '<div class="paywall-code-section">' +
                        '<input class="paywall-order-input" id="paywall-order-input" type="text" ' +
                            'placeholder="粘贴 32 位订单号" autocomplete="off" spellcheck="false" aria-label="订单号">' +
                        '<input class="paywall-email-input" id="paywall-email-input" type="email" ' +
                            'placeholder="邮箱（选填，用于接收解锁码）" autocomplete="email" aria-label="邮箱（选填）">' +
                        '<button class="paywall-code-btn" id="paywall-code-btn">解锁</button>' +
                        '<p class="paywall-status" id="paywall-status" role="status" aria-live="polite"></p>' +
                    '</div>' +
                '</div>' +

                '<div class="paywall-footer">' +
                    '<p>解锁码由系统自动生成</p>' +
                '</div>' +
            '</div>';

        document.body.appendChild(modalEl);

        // 绑定事件
        var closeBtn = document.getElementById('paywall-close');
        var codeBtn = document.getElementById('paywall-code-btn');
        orderEl = document.getElementById('paywall-order-input');
        emailEl = document.getElementById('paywall-email-input');
        msgEl = document.getElementById('paywall-status');

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

        // 回车键解锁(订单号/邮箱输入框均可)
        if (orderEl) {
            orderEl.addEventListener('keydown', function (e) {
                if (e.key === 'Enter') handleUnlock();
            });
        }
        if (emailEl) {
            emailEl.addEventListener('keydown', function (e) {
                if (e.key === 'Enter') handleUnlock();
            });
        }
    }

    /* ===== 状态提示(成功/错误/进行中) ===== */
    function setStatus(text, kind) {
        if (!msgEl) return;
        msgEl.textContent = text;
        msgEl.className = 'paywall-status' + (kind ? ' paywall-status--' + kind : '');
    }

    /* ===== 失败 reason → 友好中文 ===== */
    function reasonText(reason) {
        switch (reason) {
            case 'invalid_order_id': return '订单号格式不正确，请输入 32 位订单号';
            case 'not_found':        return '查无此订单，请确认订单号是否正确';
            case 'not_paid':         return '订单尚未支付成功，请先在面包多完成付款';
            case 'amount_mismatch':  return '订单金额异常，请联系站长处理';
            case 'bad_key':          return '服务端验单异常，请联系站长处理';
            case 'upstream_error':   return '验单服务暂不可用，请稍后重试';
            case 'network':          return '网络错误，请检查网络后重试';
            default:                 return '解锁失败，请稍后重试';
        }
    }

    /* ===== 解锁动作 ===== */
    function handleUnlock() {
        if (!orderEl || !msgEl) return;
        var orderId = orderEl.value.trim();
        if (!orderId) {
            setStatus('请输入订单号', 'error');
            orderEl.focus();
            return;
        }
        var email = emailEl ? emailEl.value.trim() : '';
        var btn = document.getElementById('paywall-code-btn');

        setStatus('正在校验订单，请稍候…', 'info');
        if (btn) { btn.disabled = true; }

        fetch(CONFIG.redeemApi, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ order_id: orderId, email: email })
        })
        .then(function (res) {
            return res.json().catch(function () { return null; });
        })
        .then(function (data) {
            if (data && data.ok === true && data.code) {
                saveUnlock();
                try { localStorage.setItem(CONFIG.codeStorageKey, data.code); } catch (e) { /* ignore */ }
                setStatus('解锁成功，解锁码：' + data.code + '（请保存）', 'success');
                // 稍后关闭弹窗并刷新页面加载完整内容
                setTimeout(function () {
                    hidePaywall();
                    window.location.reload();
                }, 1500);
            } else {
                setStatus(reasonText(data && data.reason), 'error');
                if (btn) { btn.disabled = false; }
            }
        })
        .catch(function () {
            setStatus(reasonText('network'), 'error');
            if (btn) { btn.disabled = false; }
        });
    }

    function showPaywall() {
        createModal();
        if (modalEl) {
            modalEl.classList.add('paywall-overlay--show');
            document.body.style.overflow = 'hidden';
            // 聚焦到订单号输入框
            setTimeout(function () {
                if (orderEl) orderEl.focus();
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
        showPaywall: showPaywall,
        hidePaywall: hidePaywall,
        CONFIG: CONFIG
    };

})();