/* =============================================================
 * 国学课堂 — 全局导航栏组件 (navbar-component.js)
 * -------------------------------------------------------------
 * 用法: 在 HTML 中放入
 *   <nav data-navbar="global" class="ds-navbar" aria-label="主导航"></nav>
 * 加载本脚本即可自动渲染。
 * 功能: 根据页面路径自动判断首页/课件页，设置正确的相对路径和菜单。
 * 维护: 修改导航菜单只需编辑本文件中的 HOME_MENU / LESSON_MENU
 * ============================================================= */
(function () {
  'use strict';

  var BRAND = '国学课堂';

  // 首页菜单（简洁） — 首页/about 页使用
  var HOME_MENU = [
    { label: '关于本站', href: 'about.html', id: 'about' },
  ];

  // 课件页菜单（完整） — lessons/ 下的页面使用
  var LESSON_MENU = [
    { label: '首页',    href: 'index.html',              id: 'home' },
    { label: '课程',    href: 'index.html#lesson-cards', id: 'courses' },
    { label: '门类',    href: 'index.html#sidebar-nav',  id: 'categories' },
    { label: '关于本站', href: 'about.html',              id: 'about' },
  ];

  /* ===== 页面类型检测 ===== */
  var path = window.location.pathname;
  var isLessonPage = /\/lessons\//.test(path);
  var currentPage = 'index';
  if (/about\.html/.test(path)) currentPage = 'about';

  /* ===== 计算相对路径深度 ===== */
  function getBasePath() {
    return isLessonPage ? '../../' : '.';
  }

  /* ===== 渲染导航栏 ===== */
  function buildNavbarHTML(container) {
    var base = getBasePath();
    var menu = isLessonPage ? LESSON_MENU : HOME_MENU;
    var html = '';

    // 品牌 + 菜单放在 __inner 容器中，保持原有布局
    html += '<div class="ds-navbar__inner">';
    html += '<a class="ds-btn-nav ds-btn-nav--brand" href="' + base + '/index.html">' +
            esc(BRAND) + '</a>';

    // 菜单
    html += '<ul class="ds-navbar__menu" id="primary-menu">';
    for (var i = 0; i < menu.length; i++) {
      var item = menu[i];
      var href = base + '/' + item.href;
      var active = (item.id === currentPage) ? ' is-active' : '';
      html += '<li><a class="ds-btn-nav ds-btn-nav--ghost' + active +
              '" href="' + esc(href) + '">' + esc(item.label) + '</a></li>';
    }
    html += '</ul>';
    html += '</div>';

    container.innerHTML = html;

    // 课件页添加 ds-navbar--global 样式
    container.classList.toggle('ds-navbar--global', isLessonPage);
  }

  function esc(str) {
    if (str == null) return '';
    var d = document.createElement('div');
    d.textContent = String(str);
    return d.innerHTML;
  }

  /* ===== 启动 ===== */
  function init() {
    var containers = document.querySelectorAll('[data-navbar="global"]');
    for (var i = 0; i < containers.length; i++) {
      buildNavbarHTML(containers[i]);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
