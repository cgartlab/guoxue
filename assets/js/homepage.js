/* =============================================================
 * 国学课堂 — 首页渲染引擎 v1.0 (homepage.js)
 * -------------------------------------------------------------
 * 依赖: lessons-manifest.js (window.GUOXUE_LESSONS),
 *       ds-design-system.css (.home-sidebar, .home-aside, .featured-item)
 * 提供: 侧栏导航、课程分组、搜索过滤、精选推荐面板
 * ============================================================= */
(function () {
  'use strict';

  var LESSONS = window.GUOXUE_LESSONS || [];

  /* ===== 常量 ===== */
  var CATEGORIES = [
    { key: 'core',       label: '📖 核心课程'   },
    { key: 'advanced',   label: '🔥 进阶拓展'   },
    { key: 'supplement', label: '🌿 补充材料'   },
    { key: 'coming',     label: '⏳ 即将上线'   }
  ];

  /* ===== 工具函数 ===== */
  function esc(str) {
    if (!str) return '';
    var d = document.createElement('div');
    d.textContent = String(str);
    return d.innerHTML;
  }

  function groupByCategory(list) {
    var groups = {};
    CATEGORIES.forEach(function (c) { groups[c.key] = []; });
    list.forEach(function (lesson) {
      var cat = lesson.category || 'core';
      if (!groups[cat]) groups[cat] = [];
      groups[cat].push(lesson);
    });
    // "coming" group also includes status==='coming' entries
    list.forEach(function (lesson) {
      if (lesson.status === 'coming' && lesson.category !== 'coming') {
        if (!groups['coming']) groups['coming'] = [];
        groups['coming'].push(lesson);
      }
    });
    return groups;
  }

  function getFeatured(list) {
    return list.filter(function (l) { return l.featured === true; }).slice(0, 4);
  }

  function buildCardHTML(lesson) {
    var isComing = lesson.status === 'coming';
    var gradeBadge = '<span class="lesson-grade">' + esc(lesson.grade || '') + '</span>';
    var iconDiv    = '<div class="lesson-icon">' + esc(lesson.icon || '📚') + '</div>';
    var titleEl    = '<h3 class="lesson-title">' + esc(lesson.title || '') + '</h3>';
    var subtitleEl = '<p class="lesson-subtitle">' + esc(lesson.subtitle || '') + '</p>';
    if (lesson.duration) {
      subtitleEl += ' · ' + esc(lesson.duration);
    }
    var descEl     = '<p class="lesson-desc" style="margin-bottom:var(--ds-space-5)">' + esc(lesson.description || '') + '</p>';
    var ctaText    = isComing ? '即将上线' : '开始学习';
    var arrowText  = isComing ? '' : ' →';
    var ctaEl      = '<div class="lesson-cta"><span>' + esc(ctaText) + '</span><span class="arrow">' + esc(arrowText) + '</span></div>';
    var overlay    = '';
    if (isComing) {
      overlay = '<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:1.25rem;font-weight:700;color:var(--ds-color-muted);background:oklch(100% 0 0 / 0.7);backdrop-filter:blur(2px);-webkit-backdrop-filter:blur(2px);border-radius:var(--ds-radius-2xl);z-index:2;pointer-events:none;letter-spacing:0.1em;">即将上线</div>';
    }
    return '<a class="ds-lesson-card" href="' + esc(lesson.path) + '"' +
           (isComing ? ' style="pointer-events:none;opacity:0.5;"' : '') + '>' +
           iconDiv + gradeBadge + titleEl + subtitleEl + descEl + ctaEl + overlay +
           '</a>';
  }

  /* ===== 渲染：侧栏 ===== */
  function renderSidebar(container) {
    if (!container) return;
    var groups = groupByCategory(LESSONS);
    var html = '<div class="home-sidebar__brand">📜 课程导航</div>';
    html += '<div class="search-box"><input class="search-box__input" id="sidebar-search" type="text" placeholder="🔍 搜索课程…" autocomplete="off"></div>';
    CATEGORIES.forEach(function (cat) {
      var items = groups[cat.key] || [];
      if (!items.length) return;
      html += '<div class="home-sidebar__category">' + esc(cat.label) + '</div>';
      html += '<ul class="home-sidebar__nav" data-category="' + esc(cat.key) + '">';
      items.forEach(function (l) {
        var activeClass = (cat.key === 'core') ? ' home-sidebar__link--active' : '';
        html += '<li><a class="home-sidebar__link' + activeClass + '" href="' + esc(l.path) +
                '" data-category="' + esc(cat.key) + '" data-lesson-id="' + esc(l.id) + '">' +
                esc(l.icon || '📚') + ' ' + esc(l.title) + '</a></li>';
      });
      html += '</ul>';
    });
    container.innerHTML = html;
    bindSidebarSearch();
  }

  /* ===== 渲染：精选推荐（右侧栏） ===== */
  function renderAside(container) {
    if (!container) return;
    var featured = getFeatured(LESSONS);
    if (!featured.length) { container.style.display = 'none'; return; }
    var html = '<div class="home-aside__title">⭐ 精选推荐</div>';
    featured.forEach(function (l) {
      html += '<a class="featured-item" href="' + esc(l.path) + '">' +
              '<span class="featured-item__icon">' + esc(l.icon || '📚') + '</span>' +
              '<div class="featured-item__body">' +
              '<span class="featured-item__grade">' + esc(l.grade || '') + '</span>' +
              '<span class="featured-item__title">' + esc(l.title) + '</span>' +
              '</div></a>';
    });
    container.innerHTML = html;
  }

  /* ===== 渲染：课程卡片网格（替换旧 inline IIFE） ===== */
  var currentFilter = 'all';

  function renderCards(container, filterCategory) {
    if (!container) return;
    container.innerHTML = '';
    var filtered = LESSONS.filter(function (l) {
      if (filterCategory === 'all') return true;
      if (filterCategory === 'coming') return l.status === 'coming';
      return l.category === filterCategory;
    });
    filtered.forEach(function (lesson) {
      container.insertAdjacentHTML('beforeend', buildCardHTML(lesson));
    });
    currentFilter = filterCategory;
  }

  /* ===== 搜索过滤 ===== */
  function bindSidebarSearch() {
    var input = document.getElementById('sidebar-search');
    if (!input) return;
    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();
      document.querySelectorAll('.home-sidebar__link').forEach(function (link) {
        var text = (link.textContent || '').toLowerCase();
        var li = link.closest('li');
        if (li) li.style.display = text.indexOf(q) !== -1 ? '' : 'none';
      });
      document.querySelectorAll('.home-sidebar__nav').forEach(function (nav) {
        var anyVisible = Array.from(nav.children).some(function (li) {
          return li.style.display !== 'none';
        });
        var title = nav.previousElementSibling;
        if (title && title.classList.contains('home-sidebar__category')) {
          title.style.display = anyVisible ? '' : 'none';
        }
      });
    });
  }

  /* ===== 侧栏点击（分类过滤） ===== */
  function bindSidebarClicks() {
    document.getElementById('sidebar-nav').addEventListener('click', function (e) {
      var link = e.target.closest('.home-sidebar__link');
      if (!link) return;
      e.preventDefault();
      var cat = link.getAttribute('data-category');
      // 更新 active 状态
      document.querySelectorAll('.home-sidebar__link').forEach(function (el) {
        el.classList.remove('home-sidebar__link--active');
      });
      link.classList.add('home-sidebar__link--active');
      // 过滤卡片
      renderCards(document.getElementById('lesson-cards'), cat);
    });
  }

  /* ===== 公开 API（挂载到 window） ===== */
  window.GUOXUE_HOMEPAGE = {
    init: function (opts) {
      opts = opts || {};
      renderSidebar(opts.sidebarContainer || document.getElementById('sidebar-nav'));
      renderAside(opts.asideContainer || document.getElementById('home-aside'));
      renderCards(opts.cardGridContainer || document.getElementById('lesson-cards'), 'all');
      bindSidebarClicks();
    },
    refreshCards: function (filter) {
      renderCards(document.getElementById('lesson-cards'), filter || currentFilter);
    }
  };

  /* ===== 自动初始化 ===== */
  function boot() {
    if (!LESSONS.length) {
      setTimeout(boot, 50);
      return;
    }
    window.GUOXUE_HOMEPAGE.init();
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
