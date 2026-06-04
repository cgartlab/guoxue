/* =============================================================
 * 国学课堂 — 首页渲染引擎 v2.0 (homepage.js)
 * -------------------------------------------------------------
 * 依赖: lessons-manifest.js (window.GUOXUE_LESSONS),
 *       categories.js     (window.GUOXUE_CATEGORIES),
 *       ds-design-system.css (.home-sidebar, .home-aside, .featured-item,
 *                             .home-sidebar__group--coming, .ds-coming-soon)
 * 提供: 侧栏导航、门类分组、搜索过滤、精选推荐面板、"敬请期待"占位
 * ============================================================= */
(function () {
  'use strict';

  var LESSONS    = window.GUOXUE_LESSONS    || [];
  var CATEGORIES = window.GUOXUE_CATEGORIES || [];

  /* ===== 工具函数 ===== */
  function esc(str) {
    if (str === undefined || str === null) return '';
    var d = document.createElement('div');
    d.textContent = String(str);
    return d.innerHTML;
  }

  function getCategoryByKey(key) {
    for (var i = 0; i < CATEGORIES.length; i++) {
      if (CATEGORIES[i].key === key) return CATEGORIES[i];
    }
    return null;
  }

  function sortCategories() {
    return CATEGORIES.slice().sort(function (a, b) {
      return (a.order || 0) - (b.order || 0);
    });
  }

  /* ===== 侧栏数据构建 ===== */
  function buildSidebarGroups() {
    var groups = [];
    var sorted = sortCategories();
    for (var i = 0; i < sorted.length; i++) {
      var cat = sorted[i];
      var readyLessons    = [];
      var plannedLessons  = [];
      for (var j = 0; j < LESSONS.length; j++) {
        var l = LESSONS[j];
        if (l.subject !== cat.key) continue;
        if (l.status === 'ready') readyLessons.push(l);
        else if (l.status === 'coming') plannedLessons.push(l);
      }
      groups.push({
        category: cat,
        readyLessons: readyLessons,
        plannedLessons: plannedLessons
      });
    }
    return groups;
  }

  function getFeatured(list) {
    return list.filter(function (l) { return l.featured === true; }).slice(0, 4);
  }

  /* ===== 课程卡片 HTML ===== */
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

  function buildComingSoonCardHTML(lesson) {
    return '<div class="ds-lesson-card" style="opacity:0.5;pointer-events:none;cursor:not-allowed;">' +
           '<div class="lesson-icon">' + esc(lesson.icon || '📚') + '</div>' +
           '<span class="lesson-grade">' + esc(lesson.grade || '') + '</span>' +
           '<h3 class="lesson-title">' + esc(lesson.title || '') + '</h3>' +
           '<p class="lesson-subtitle">' + esc(lesson.subtitle || '') + '</p>' +
           '<p class="lesson-desc" style="margin-bottom:var(--ds-space-5)">' + esc(lesson.description || '') + '</p>' +
           '<div class="lesson-cta"><span>敬请期待</span></div>' +
           '</div>';
  }

  /* ===== 渲染:侧栏 ===== */
  function renderSidebar(container) {
    if (!container) return;
    var groups = buildSidebarGroups();
    var html = '<div class="home-sidebar__brand">📜 课程导航</div>';
    html += '<div class="search-box"><input class="search-box__input" id="sidebar-search" type="text" placeholder="🔍 搜索课程…" autocomplete="off"></div>';

    // "全部"重置链接
    html += '<ul class="home-sidebar__nav" data-subject-group="all">';
    html += '<li><a class="home-sidebar__link home-sidebar__link--active" href="#" data-subject="all" data-action="filter">✨ 全部课程</a></li>';
    html += '</ul>';

    // 每个门类一组
    groups.forEach(function (g) {
      var cat = g.category;
      var isComing = cat.status === 'coming';
      var groupClass = 'home-sidebar__group' + (isComing ? ' home-sidebar__group--coming' : '');

      html += '<div class="' + groupClass + '">';
      html += '<div class="home-sidebar__category">' +
              esc(cat.icon) + ' ' + esc(cat.label) +
              (isComing ? '<span class="home-sidebar__badge--coming">⏳ 敬请期待</span>' : '') +
              '</div>';
      html += '<ul class="home-sidebar__nav" data-subject-group="' + esc(cat.key) + '">';

      // 门类本身作为筛选项
      html += '<li><a class="home-sidebar__link" href="#" data-subject="' + esc(cat.key) + '" data-action="filter">' +
              esc(cat.description || '查看本门类课程') + '</a></li>';

      // 该门类下的 ready 课程
      g.readyLessons.forEach(function (l) {
        html += '<li><a class="home-sidebar__link home-sidebar__link--sub" href="' + esc(l.path) + '" data-subject="' + esc(cat.key) + '" data-action="navigate">' +
                esc(l.icon || '📚') + ' ' + esc(l.title) + '</a></li>';
      });

      // 该门类下的 planned 课程(灰显)
      g.plannedLessons.forEach(function (l) {
        html += '<li><a class="home-sidebar__link home-sidebar__link--sub home-sidebar__link--planned" href="' + esc(l.path) + '" data-subject="' + esc(cat.key) + '" data-action="navigate">' +
                esc(l.icon || '📚') + ' ' + esc(l.title) + '<span class="home-sidebar__badge--coming">⏳</span></a></li>';
      });

      html += '</ul>';
      html += '</div>';
    });

    container.innerHTML = html;
    bindSidebarSearch();
  }

  /* ===== 渲染:精选推荐(右侧栏) ===== */
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

  /* ===== 渲染:筛选标题 ===== */
  function renderFilterTitle(subjectKey) {
    var el = document.getElementById('filter-title');
    if (!el) return;
    if (!subjectKey || subjectKey === 'all') {
      el.textContent = '✨ 全部课程';
    } else {
      var cat = getCategoryByKey(subjectKey);
      el.textContent = cat ? (cat.icon + ' ' + cat.label) : '✨ 全部课程';
    }
  }

  /* ===== 渲染:课程卡片网格 ===== */
  var currentFilter = 'all';

  function renderCards(filterSubject) {
    var gridEl = document.getElementById('lesson-cards');
    var comingEl = document.getElementById('coming-soon');
    if (!gridEl) return;

    var subject = filterSubject || 'all';
    currentFilter = subject;

    var cat = (subject === 'all') ? null : getCategoryByKey(subject);
    var hasReady = LESSONS.some(function (l) {
      return l.status === 'ready' && (subject === 'all' || l.subject === subject);
    });

    // 切换主区显示
    if (subject !== 'all' && cat && cat.status === 'coming' && !hasReady) {
      // 门类未上线:显示"敬请期待"占位
      renderComingSoon(cat);
      gridEl.hidden = true;
      if (comingEl) comingEl.hidden = false;
    } else {
      // 显示课程网格
      if (comingEl) comingEl.hidden = true;
      gridEl.hidden = false;
      gridEl.innerHTML = '';
      var filtered = LESSONS.filter(function (l) {
        if (subject === 'all') return l.status !== 'coming' || hasReady; // 全部视图隐藏纯 coming
        return l.subject === subject && l.status === 'ready';
      });
      // 全部视图:只显示 ready 课程,以及分散在不同门类的 coming
      if (subject === 'all') {
        filtered = LESSONS.filter(function (l) { return l.status === 'ready'; });
      }
      filtered.forEach(function (lesson) {
        gridEl.insertAdjacentHTML('beforeend', buildCardHTML(lesson));
      });
    }

    renderFilterTitle(subject);
  }

  /* ===== 渲染:"敬请期待"占位 ===== */
  function renderComingSoon(cat) {
    var el = document.getElementById('coming-soon');
    if (!el) return;
    var html = '<div class="ds-coming-soon" role="status">' +
               '<div class="ds-coming-soon__icon" aria-hidden="true">' + esc(cat.icon) + '</div>' +
               '<h3 class="ds-coming-soon__heading">' + esc(cat.label) + ' · 即将上线</h3>' +
               '<p class="ds-coming-soon__desc">' + esc(cat.description || '本门类课程正在筹备中,敬请期待。') + '</p>';

    // 列出本门类下 planned 课程(若有)
    var groups = buildSidebarGroups();
    var g = null;
    for (var i = 0; i < groups.length; i++) {
      if (groups[i].category.key === cat.key) { g = groups[i]; break; }
    }
    if (g && g.plannedLessons.length) {
      html += '<div class="ds-coming-soon__planned"><h4>📅 规划中的课程</h4><div class="ds-card-grid">';
      g.plannedLessons.forEach(function (l) {
        html += buildComingSoonCardHTML(l);
      });
      html += '</div></div>';
    }

    html += '</div>';
    el.innerHTML = html;
  }

  /* ===== 搜索过滤 ===== */
  function bindSidebarSearch() {
    var input = document.getElementById('sidebar-search');
    if (!input) return;
    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();

      // 同时过滤侧栏门类与课程链接
      document.querySelectorAll('.home-sidebar__link').forEach(function (link) {
        var text = (link.textContent || '').toLowerCase();
        var li = link.closest('li');
        if (!li) return;
        li.style.display = text.indexOf(q) !== -1 ? '' : 'none';
      });

      // 门类分组(整组)显示规则:组内任意一项可见则显示
      document.querySelectorAll('.home-sidebar__group').forEach(function (group) {
        var items = group.querySelectorAll('.home-sidebar__nav > li');
        var anyVisible = Array.from(items).some(function (li) { return li.style.display !== 'none'; });
        group.style.display = anyVisible ? '' : 'none';
      });
    });
  }

  /* ===== 侧栏点击(门类过滤) ===== */
  function bindSidebarClicks() {
    var nav = document.getElementById('sidebar-nav');
    if (!nav) return;
    nav.addEventListener('click', function (e) {
      var link = e.target.closest('.home-sidebar__link');
      if (!link) return;
      var action = link.getAttribute('data-action');
      if (action === 'navigate') {
        // 让链接自然跳转
        return;
      }
      // action === 'filter'
      e.preventDefault();
      var subject = link.getAttribute('data-subject') || 'all';

      // 更新 active 状态
      nav.querySelectorAll('.home-sidebar__link').forEach(function (el) {
        el.classList.remove('home-sidebar__link--active');
      });
      link.classList.add('home-sidebar__link--active');

      // 过滤主区
      renderCards(subject);

      // 滚动到主区(移动端体验)
      var main = document.querySelector('.home-content');
      if (main && window.innerWidth < 768) {
        main.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  }

  /* ===== 公开 API(挂载到 window) ===== */
  window.GUOXUE_HOMEPAGE = {
    init: function (opts) {
      opts = opts || {};
      renderSidebar(opts.sidebarContainer || document.getElementById('sidebar-nav'));
      renderAside(opts.asideContainer || document.getElementById('home-aside'));
      renderCards('all');
      bindSidebarClicks();
    },
    refreshCards: function (subject) {
      renderCards(subject || currentFilter);
    }
  };

  /* ===== 自动初始化 ===== */
  function boot() {
    if (!CATEGORIES.length) {
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
