/* =============================================================
 * 国学课堂 — 顶栏菜单 + 抽屉切换 v2.0 (navbar.js)
 * -------------------------------------------------------------
 * 顶栏布局(共 6 项,顺序固定):
 *   [品牌] [抽屉]  ...  [首页 课程 门类]  ...  [菜单] [关于]
 *
 * 行为:
 *   - #menu-toggle ↔ #primary-menu(顶栏菜单)
 *   - #drawer-toggle ↔ #sidebar-nav(侧栏抽屉)
 *   - 桌面端 > 767px 始终保持抽屉展开,菜单按钮隐藏
 *   - 移动端 ≤ 767px 抽屉默认收起,菜单按钮显示
 * ============================================================= */
(function () {
  'use strict';

  var BREAKPOINT = 767;
  var DRAWER_OPEN_CLASS  = 'is-open';
  var DRAWER_COLLAPSED    = 'is-collapsed';
  var MENU_OPEN_CLASS     = 'is-open';

  /* ===== 顶栏主菜单(首页/课程/门类) ===== */
  function initTopMenu() {
    var btn   = document.getElementById('menu-toggle');
    var menu  = document.getElementById('primary-menu');
    if (!btn || !menu) return;

    var firstItem = menu.querySelector('.ds-btn-nav');

    function open() {
      menu.classList.add(MENU_OPEN_CLASS);
      btn.setAttribute('aria-expanded', 'true');
      if (firstItem) firstItem.focus();
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
  function initDrawer() {
    var btn     = document.getElementById('drawer-toggle');
    var sidebar = document.getElementById('sidebar-nav');
    if (!btn || !sidebar) return;

    var iconEl = btn.querySelector('.ds-btn-nav__icon');
    var textEl = btn.querySelector('.ds-btn-nav__text');

    function syncLabel(isOpen) {
      if (textEl) textEl.textContent = isOpen ? '收起' : '目录';
      if (iconEl) iconEl.textContent  = isOpen ? '✕' : '☰';
    }

    function setOpen(isOpen) {
      sidebar.classList.toggle(DRAWER_OPEN_CLASS, isOpen);
      btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      syncLabel(isOpen);
    }

    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      setOpen(!sidebar.classList.contains(DRAWER_OPEN_CLASS));
    });

    // 桌面端:抽屉始终展开,移除 collapsed 类
    // 移动端:抽屉默认收起,点击主内容区可关闭
    function syncToViewport() {
      var isDesktop = window.innerWidth > BREAKPOINT;
      if (isDesktop) {
        sidebar.classList.remove(DRAWER_OPEN_CLASS);
        sidebar.classList.remove(DRAWER_COLLAPSED);
        syncLabel(false);
        btn.setAttribute('aria-expanded', 'false');
      }
    }
    syncToViewport();
    window.addEventListener('resize', syncToViewport);

    // 移动端点击主内容区关闭抽屉
    document.addEventListener('click', function (e) {
      if (window.innerWidth > BREAKPOINT) return;
      if (!sidebar.classList.contains(DRAWER_OPEN_CLASS)) return;
      if (btn.contains(e.target) || sidebar.contains(e.target)) return;
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
