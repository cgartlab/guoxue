/* =============================================================
 * 国学课堂 — 全局导航栏组件 (EDIC 设计系统)
 * -------------------------------------------------------------
 * 基于 EDIC Design System 设计令牌构建。
 * 所有页面统一使用首页风格：品牌 + 关于本站。
 * 用法: 在 HTML 中放入
 *   <nav data-navbar="global" class="ds-navbar" aria-label="主导航"></nav>
 * 维护: 修改菜单只需编辑 MENU_ITEMS 数组。
 * ============================================================= */
(function () {
  'use strict';

  /* ===== 配置 ===== */
  var BRAND = '国学课堂';

  // 统一菜单 — 所有页面一致
  var MENU_ITEMS = [
    { label: '关于本站', href: 'about.html', id: 'about' },
  ];

  /* ===== 页面状态检测 ===== */
  var path = window.location.pathname;
  var currentPageId = 'index';
  if (/about\.html/.test(path)) currentPageId = 'about';

  /* ===== 计算相对路径深度 ===== */
  function getBasePath() {
    return /\/lessons\//.test(path) ? '../../' : '.';
  }

  /* ===== 渲染导航栏 ===== */
  function buildNavbarHTML(container) {
    var base = getBasePath();
    var html = '';

    // 内层容器（对齐页面内容）
    html += '<div class="ds-navbar-inner">';

    // 品牌
    html += '<a class="ds-navbar-brand" href="' + base + '/index.html">' +
            esc(BRAND) + '</a>';

    // 菜单
    html += '<ul class="ds-navbar-links">';
    for (var i = 0; i < MENU_ITEMS.length; i++) {
      var item = MENU_ITEMS[i];
      var href = base + '/' + item.href;
      var activeClass = (item.id === currentPageId) ? ' ds-navbar-link--active' : '';
      html += '<li><a class="ds-navbar-link' + activeClass +
              '" href="' + esc(href) + '">' + esc(item.label) + '</a></li>';
    }
    html += '</ul>';

    html += '</div>'; // .ds-navbar-inner

    container.innerHTML = html;
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
