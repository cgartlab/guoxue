/* =============================================================
 * 国学课堂 — 顶栏移动菜单控制 v1.1 (navbar.js)
 * -------------------------------------------------------------
 * 功能:
 *   - 汉堡按钮 toggle(#menu-toggle ↔ #primary-menu)
 *   - 点击外部 / Esc 键关闭
 *   - 跨断点(>767px)同步关闭并清空 aria
 *   - focus 管理:展开时聚焦首项,关闭时回到按钮
 *   - 抽屉切换(#drawer-toggle ↔ #sidebar-nav)
 * ============================================================= */
(function () {
  'use strict';

  var BREAKPOINT = 767;

  /* ===== 顶栏菜单 ===== */
  (function () {
    var toggleBtn = null;
    var menuEl    = null;
    var firstItem = null;

    function isDesktop() {
      return window.innerWidth > BREAKPOINT;
    }

    function openMenu() {
      if (!toggleBtn || !menuEl) return;
      menuEl.classList.add('is-open');
      toggleBtn.setAttribute('aria-expanded', 'true');
      if (firstItem) firstItem.focus();
    }

    function closeMenu() {
      if (!toggleBtn || !menuEl) return;
      menuEl.classList.remove('is-open');
      toggleBtn.setAttribute('aria-expanded', 'false');
    }

    function onToggleClick(e) {
      e.preventDefault();
      e.stopPropagation();
      if (menuEl.classList.contains('is-open')) {
        closeMenu();
      } else {
        openMenu();
      }
    }

    function onDocumentClick(e) {
      if (!menuEl || !menuEl.classList.contains('is-open')) return;
      if (toggleBtn && toggleBtn.contains(e.target)) return;
      if (menuEl.contains(e.target)) return;
      closeMenu();
    }

    function onKeydown(e) {
      if (e.key === 'Escape' && menuEl && menuEl.classList.contains('is-open')) {
        closeMenu();
        if (toggleBtn) toggleBtn.focus();
      }
    }

    function onResize() {
      if (isDesktop() && menuEl && menuEl.classList.contains('is-open')) {
        closeMenu();
      }
    }

    function init() {
      toggleBtn = document.getElementById('menu-toggle');
      menuEl    = document.getElementById('primary-menu');
      if (!toggleBtn || !menuEl) return;

      firstItem = menuEl.querySelector('.ds-navbar__menu-item');

      toggleBtn.addEventListener('click', onToggleClick);
      document.addEventListener('click', onDocumentClick);
      document.addEventListener('keydown', onKeydown);
      window.addEventListener('resize', onResize);
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', init);
    } else {
      init();
    }
  })();

  /* ===== 抽屉切换 ===== */
  (function () {
    var drawerBtn = null;
    var sidebar   = null;

    function openDrawer() {
      if (!drawerBtn || !sidebar) return;
      sidebar.classList.add('is-open');
      drawerBtn.setAttribute('aria-expanded', 'true');
      var openIcon = drawerBtn.querySelector('.drawer-icon-open');
      var closeIcon = drawerBtn.querySelector('.drawer-icon-close');
      if (openIcon) openIcon.hidden = true;
      if (closeIcon) closeIcon.hidden = false;
    }

    function closeDrawer() {
      if (!drawerBtn || !sidebar) return;
      sidebar.classList.remove('is-open');
      drawerBtn.setAttribute('aria-expanded', 'false');
      var openIcon = drawerBtn.querySelector('.drawer-icon-open');
      var closeIcon = drawerBtn.querySelector('.drawer-icon-close');
      if (openIcon) openIcon.hidden = false;
      if (closeIcon) closeIcon.hidden = true;
    }

    function toggleDrawer() {
      if (!drawerBtn || !sidebar) return;
      if (sidebar.classList.contains('is-open')) {
        closeDrawer();
      } else {
        openDrawer();
      }
    }

    function onResize() {
      // 桌面端:收起时恢复正常宽度
      if (window.innerWidth > BREAKPOINT) {
        sidebar && sidebar.classList.remove('is-collapsed');
      }
    }

    function init() {
      drawerBtn = document.getElementById('drawer-toggle');
      sidebar   = document.getElementById('sidebar-nav');
      if (!drawerBtn || !sidebar) return;

      // 桌面端默认展开,移动端默认收起
      if (window.innerWidth <= BREAKPOINT) {
        closeDrawer();
      } else {
        openDrawer();
      }

      drawerBtn.addEventListener('click', toggleDrawer);

      // 点击侧栏外部(主内容区)关闭抽屉(移动端)
      document.addEventListener('click', function (e) {
        if (window.innerWidth > BREAKPOINT) return;
        if (!sidebar || !sidebar.classList.contains('is-open')) return;
        if (sidebar.contains(e.target)) return;
        if (drawerBtn.contains(e.target)) return;
        closeDrawer();
      });

      window.addEventListener('resize', onResize);
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', init);
    } else {
      init();
    }
  })();

})();
