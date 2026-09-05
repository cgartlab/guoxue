/* =============================================================
 * 国学课堂 — 顶栏菜单 + 抽屉切换 v2.1 (navbar.js)
 * -------------------------------------------------------------
 * 顶栏布局:
 *   [品牌]  ...  [首页 课程 门类]  ...  [菜单] [关于]
 *
 * 桌面端: 导航栏无目录按钮, 目录抽屉默认展开,
 *         抽屉内顶部有折叠按钮。
 * 移动端: 导航栏动态添加目录按钮(☰ 目录), 抽屉默认收起。
 *
 * 行为:
 *   - #menu-toggle ↔ #primary-menu(顶栏菜单)
 *   - 移动端: 动态创建 #drawer-toggle → 控制 #sidebar-nav
 *   - 桌面端: 抽屉默认展开, 抽屉内折叠按钮控制
 * ============================================================= */
(function () {
  'use strict';

  var BREAKPOINT = 767;
  var DRAWER_OPEN_CLASS  = 'is-open';
  var DRAWER_COLLAPSED   = 'is-collapsed';
  var MENU_OPEN_CLASS    = 'is-open';

  /* ===== 顶栏主菜单 ===== */
  function initTopMenu() {
    var btn   = document.getElementById('menu-toggle');
    var menu  = document.getElementById('primary-menu');
    if (!btn || !menu) return;

    var firstItem = menu.querySelector('.ds-btn-nav');

    function open() {
      menu.classList.add(MENU_OPEN_CLASS);
      btn.setAttribute('aria-expanded', 'true');
      if (window.innerWidth <= BREAKPOINT && firstItem) firstItem.focus();
    }
    function close() {
      menu.classList.remove(MENU_OPEN_CLASS);
      btn.setAttribute('aria-expanded', 'false');
    }
    function toggle() {
      if (menu.classList.contains(MENU_OPEN_CLASS)) close(); else open();
    }

    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      toggle();
    });

    document.addEventListener('click', function (e) {
      if (!menu.classList.contains(MENU_OPEN_CLASS)) return;
      if (btn.contains(e.target) || menu.contains(e.target)) return;
      close();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains(MENU_OPEN_CLASS)) {
        close();
        btn.focus();
      }
    });
  }

  /* ===== 侧栏抽屉(目录) ===== */
  // 桌面端: 默认展开, 抽屉内折叠按钮控制
  // 移动端: 默认收起, 动态添加导航栏按钮(☰ 目录)
  function initDrawer() {
    var sidebar = document.getElementById('sidebar-nav');
    if (!sidebar) return; // 不是首页

    var btn = null;    // 动态创建的导航栏按钮
    var inserted = false; // 按钮是否已插入 DOM

    /* ----- 动态创建/移除导航栏按钮 ----- */
    function ensureNavBtn(visible) {
      if (visible && !inserted) {
        // 在品牌和菜单按钮之间插入
        var brand = document.querySelector('.ds-navbar .ds-btn-nav--brand');
        if (!brand) return;
        btn = document.createElement('button');
        btn.className = 'ds-btn-nav ds-btn-nav--icon';
        btn.id = 'drawer-toggle';
        btn.type = 'button';
        btn.setAttribute('aria-label', '展开课程目录');
        btn.setAttribute('aria-expanded', 'false');
        btn.innerHTML = '<span class="ds-btn-nav__icon">☰</span><span class="ds-btn-nav__text">目录</span>';
        brand.parentNode.insertBefore(btn, brand.nextSibling);
        inserted = true;

        // 绑定事件
        btn.addEventListener('click', function (e) {
          e.preventDefault();
          e.stopPropagation();
          setOpen(!isOpen());
        });
      } else if (!visible && inserted) {
        if (btn && btn.parentNode) btn.parentNode.removeChild(btn);
        btn = null;
        inserted = false;
      }
    }

    /* ----- 状态控制 ----- */
    function syncLabel(isOpen) {
      if (!btn) return;
      var iconEl = btn.querySelector('.ds-btn-nav__icon');
      var textEl = btn.querySelector('.ds-btn-nav__text');
      if (textEl) textEl.textContent = isOpen ? '收起' : '目录';
      if (iconEl) iconEl.textContent  = isOpen ? '✕' : '☰';
    }

    function setOpen(isOpen) {
      sidebar.classList.toggle(DRAWER_OPEN_CLASS, isOpen);
      sidebar.classList.toggle(DRAWER_COLLAPSED, !isOpen);
      if (btn) {
        btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        syncLabel(isOpen);
      }
    }

    function isOpen() {
      return sidebar.classList.contains(DRAWER_OPEN_CLASS);
    }

    /* ----- 视口响应 ----- */
    function syncToViewport() {
      var isDesktop = window.innerWidth > BREAKPOINT;
      if (isDesktop) {
        // 桌面端: 默认展开, 移除导航栏按钮
        sidebar.classList.add(DRAWER_OPEN_CLASS);
        sidebar.classList.remove(DRAWER_COLLAPSED);
        ensureNavBtn(false);
      } else {
        // 移动端: 默认收起, 显示导航栏按钮
        sidebar.classList.remove(DRAWER_OPEN_CLASS);
        sidebar.classList.add(DRAWER_COLLAPSED);
        ensureNavBtn(true);
        if (btn) {
          btn.setAttribute('aria-expanded', 'false');
          syncLabel(false);
        }
      }
    }

    // 抽屉内折叠按钮
    var closeBtn = document.getElementById('drawer-close-btn');
    if (closeBtn) {
      closeBtn.addEventListener('click', function (e) {
        e.preventDefault();
        setOpen(false);
      });
    }

    // 初始化
    syncToViewport();

    // 防抖 resize
    var resizeTimer;
    window.addEventListener('resize', function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(syncToViewport, 100);
    });

    // 移动端点击主内容区关闭抽屉
    document.addEventListener('click', function (e) {
      if (window.innerWidth > BREAKPOINT) return;
      if (!isOpen()) return;
      if (sidebar.contains(e.target)) return;
      if (btn && btn.contains(e.target)) return;
      setOpen(false);
    });
  }

  function init() {
    initTopMenu();
    initDrawer();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
