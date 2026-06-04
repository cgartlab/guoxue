/* =============================================================
 * 国学课堂 — 顶栏移动菜单控制 v1.0 (navbar.js)
 * -------------------------------------------------------------
 * 功能:
 *   - 汉堡按钮 toggle(#menu-toggle ↔ #primary-menu)
 *   - 点击外部 / Esc 键关闭
 *   - 跨断点(>767px)同步关闭并清空 aria
 *   - focus 管理:展开时聚焦首项,关闭时回到按钮
 * ============================================================= */
(function () {
  'use strict';

  var BREAKPOINT = 767;
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
    // 聚焦首项便于键盘用户
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
