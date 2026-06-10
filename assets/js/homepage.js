/* =============================================================
 * 国学课堂 — 首页渲染引擎 v2.1 (homepage.js)
 * -------------------------------------------------------------
 * 依赖: lessons-manifest.js (window.GUOXUE_LESSONS),
 *       categories.js     (window.GUOXUE_CATEGORIES),
 *       ds-design-system.css
 * 提供: 侧栏抽屉导航、门类折叠、搜索过滤、系列封面、课程卡片
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

  /* ===== 渲染:系列封面 ===== */
  function renderSeriesCover(container) {
    if (!container) return;
    var readyCount  = LESSONS.filter(function (l) { return l.status === 'ready'; }).length;
    var comingCount = LESSONS.filter(function (l) { return l.status === 'coming'; }).length;
    var catCount    = CATEGORIES.length;

    var html = '<div class="series-cover__stats">' +
               '<div class="series-stat"><span class="series-stat__value">' + readyCount + '</span><span class="series-stat__label">已上线课程</span></div>' +
               '<div class="series-stat"><span class="series-stat__value">' + comingCount + '</span><span class="series-stat__label">筹备中</span></div>' +
               '<div class="series-stat"><span class="series-stat__value">' + catCount + '</span><span class="series-stat__label">学科门类</span></div>' +
               '</div>';
    container.innerHTML = html;
  }

  /* ===== 渲染:侧栏 ===== */
  function renderSidebar(container) {
    if (!container) return;
    var groups = buildSidebarGroups();
    var html = '';

    // L1: 品牌标识
    // L1: 品牌标识 + 折叠按钮（桌面端抽屉内的收起/展开控制）
    html += '<div class="home-sidebar__header">';
    html += '<div class="home-sidebar__brand">课程导航</div>';
    html += '<button class="ds-drawer-toggle-btn" id="drawer-close-btn" type="button" aria-label="收起侧栏">';
    html += '<span aria-hidden="true">◀</span>';
    html += '</button>';
    html += '</div>';

    // L2: 搜索框
    html += '<div class="search-box"><input class="search-box__input" id="sidebar-search" type="text" placeholder="搜索课程…" autocomplete="off"></div>';

    // L3: "全部课程" 重置链接
    html += '<ul class="home-sidebar__nav home-sidebar__nav--all" data-subject-group="all">';
    html += '<li><a class="home-sidebar__link home-sidebar__link--active" href="#" data-subject="all" data-action="filter">全部课程</a></li>';
    html += '</ul>';

    // 门类分组
    groups.forEach(function (g) {
      var cat = g.category;
      var isComing = cat.status === 'coming';
      var groupClass = 'home-sidebar__group' + (isComing ? ' home-sidebar__group--coming' : '');

      html += '<div class="' + groupClass + '">';
      // 门类标题行 — 可点击折叠/展开
      html += '<div class="home-sidebar__category-header" data-group-key="' + esc(cat.key) + '">';
      html += '<span class="home-sidebar__category-icon">' + esc(cat.icon) + '</span>';
      html += '<span class="home-sidebar__category-label">' + esc(cat.label) + '</span>';
      html += (isComing ? '<span class="home-sidebar__badge--coming">敬请期待</span>' : '');
      html += '<span class="home-sidebar__chevron" aria-hidden="true">›</span>';
      html += '</div>';

      // 子项容器(默认隐藏)
      html += '<ul class="home-sidebar__nav" data-subject-group="' + esc(cat.key) + '" hidden role="group">';

      // 门类描述行 — 点击过滤
      html += '<li><a class="home-sidebar__link home-sidebar__link--filter" href="#" data-subject="' + esc(cat.key) + '" data-action="filter">';
      html += esc(cat.description || '查看本门类课程');
      html += '</a></li>';

      // ready 课程
      g.readyLessons.forEach(function (l) {
        html += '<li><a class="home-sidebar__link home-sidebar__link--sub" href="' + esc(l.path) + '" data-subject="' + esc(cat.key) + '" data-action="navigate">';
        html += esc(l.icon || '📚') + ' ' + esc(l.title);
        html += '</a></li>';
      });

      // planned 课程
      g.plannedLessons.forEach(function (l) {
        html += '<li><a class="home-sidebar__link home-sidebar__link--sub home-sidebar__link--planned" href="#" data-subject="' + esc(cat.key) + '" data-action="navigate">';
        html += esc(l.icon || '📚') + ' ' + esc(l.title);
        html += '<span class="home-sidebar__badge--coming">⏳</span>';
        html += '</a></li>';
      });

      html += '</ul>';
      html += '</div>';
    });

    container.innerHTML = html;
    bindSidebarEvents();
  }

  /* ===== 侧栏事件绑定 ===== */
  function bindSidebarEvents() {
    var nav = document.getElementById('sidebar-nav');
    if (!nav) return;

    // 抽屉收起/展开按钮
    var drawerBtn = document.getElementById('drawer-close-btn');
    if (drawerBtn) {
      drawerBtn.addEventListener('click', function (e) {
        e.preventDefault();
        var wrapper = document.querySelector('.home-wrapper');
        var sidebar = document.getElementById('sidebar-nav');
        if (!sidebar) return;
        sidebar.classList.toggle('is-collapsed');
        if (wrapper) wrapper.classList.toggle('sidebar-collapsed');
      });
    }

    // 门类折叠/展开
    nav.addEventListener('click', function (e) {
      var header = e.target.closest('.home-sidebar__category-header');
      if (header) {
        e.preventDefault();
        var key = header.getAttribute('data-group-key');
        var group = header.closest('.home-sidebar__group');
        if (!group) return; // 空指针防护
        var subNav = group.querySelector('.home-sidebar__nav');
        if (subNav) {
          var isHidden = subNav.hasAttribute('hidden');
          if (isHidden) {
            subNav.removeAttribute('hidden');
            header.classList.add('is-expanded');
          } else {
            subNav.setAttribute('hidden', '');
            header.classList.remove('is-expanded');
          }
        }
        return;
      }

      var link = e.target.closest('.home-sidebar__link');
      if (!link) return;

      var action = link.getAttribute('data-action');
      if (action === 'navigate') {
        return; // 自然跳转
      }

      // action === 'filter'
      e.preventDefault();
      var subject = link.getAttribute('data-subject') || 'all';

      // 更新 active 状态
      nav.querySelectorAll('.home-sidebar__link').forEach(function (el) {
        el.classList.remove('home-sidebar__link--active');
      });
      link.classList.add('home-sidebar__link--active');

      // 如果是"全部课程",展开所有门类
      if (subject === 'all') {
        nav.querySelectorAll('.home-sidebar__category-header').forEach(function (h) {
          var sn = h.closest('.home-sidebar__group').querySelector('.home-sidebar__nav');
          if (sn) {
            sn.removeAttribute('hidden');
            h.classList.add('is-expanded');
          }
        });
      } else {
        // 只展开选中的门类
        nav.querySelectorAll('.home-sidebar__category-header').forEach(function (h) {
          var sn = h.closest('.home-sidebar__group').querySelector('.home-sidebar__nav');
          var hKey = h.getAttribute('data-group-key');
          if (hKey === subject) {
            if (sn) {
              sn.removeAttribute('hidden');
              h.classList.add('is-expanded');
            }
          } else if (sn) {
            sn.setAttribute('hidden', '');
            h.classList.remove('is-expanded');
          }
        });
      }

      renderCards(subject);

    });

    // ===== 移动端：在导航栏中添加侧栏开关按钮 =====
    (function addMobileToggle() {
      if (window.innerWidth >= 768) return;
      var existingToggle = document.getElementById('mobile-sidebar-toggle');
      if (existingToggle) return;
      var navbarInner = document.querySelector('.ds-navbar-inner');
      if (!navbarInner) return;
      var toggleBtn = document.createElement('button');
      toggleBtn.id = 'mobile-sidebar-toggle';
      toggleBtn.className = 'ds-btn-nav ds-btn-nav--icon';
      toggleBtn.setAttribute('type', 'button');
      toggleBtn.setAttribute('aria-label', '打开课程导航');
      toggleBtn.innerHTML = '<span class="ds-btn-nav__icon" aria-hidden="true">☰</span><span class="ds-btn-nav__text">目录</span>';
      function toggleMobileSidebar(open) {
        var sidebar = document.getElementById('sidebar-nav');
        if (!sidebar) return;
        var overlay = document.getElementById('sidebar-overlay');
        if (open === undefined) {
          sidebar.classList.toggle('is-open');
        } else {
          if (open) sidebar.classList.add('is-open');
          else sidebar.classList.remove('is-open');
        }
        var isOpen = sidebar.classList.contains('is-open');
        toggleBtn.setAttribute('aria-label', isOpen ? '关闭课程导航' : '打开课程导航');
        toggleBtn.innerHTML = isOpen
          ? '<span class="ds-btn-nav__icon" aria-hidden="true">✕</span><span class="ds-btn-nav__text">关闭</span>'
          : '<span class="ds-btn-nav__icon" aria-hidden="true">☰</span><span class="ds-btn-nav__text">目录</span>';
        // 遮罩
        if (!overlay) {
          overlay = document.createElement('div');
          overlay.id = 'sidebar-overlay';
          overlay.className = 'sidebar-overlay';
          overlay.addEventListener('click', function () { toggleMobileSidebar(false); });
          document.body.appendChild(overlay);
        }
        overlay.classList.toggle('is-visible', isOpen);
      }
      toggleBtn.addEventListener('click', function () { toggleMobileSidebar(); });
      // 插入到品牌链接后面
      var brand = navbarInner.querySelector('.ds-navbar-brand');
      if (brand && brand.nextSibling) {
        navbarInner.insertBefore(toggleBtn, brand.nextSibling);
      } else {
        navbarInner.appendChild(toggleBtn);
      }
    })();

    // 搜索过滤 (带防抖)
    var searchInput = document.getElementById('sidebar-search');
    if (searchInput) {
      var searchTimer = null;
      searchInput.addEventListener('input', function () {
        clearTimeout(searchTimer);
        searchTimer = setTimeout(function () {
          var q = searchInput.value.trim().toLowerCase();

          // 过滤所有链接
          nav.querySelectorAll('.home-sidebar__link').forEach(function (link) {
            var text = (link.textContent || '').toLowerCase();
            var li = link.closest('li');
            if (!li) return;
            if (q === '') {
              li.style.display = '';
            } else {
              li.style.display = text.indexOf(q) !== -1 ? '' : 'none';
            }
          });

          // 门类分组：组内任意一项可见则显示，否则隐藏
          nav.querySelectorAll('.home-sidebar__group').forEach(function (group) {
            var items = group.querySelectorAll('.home-sidebar__nav > li');
            var anyVisible = Array.from(items).some(function (li) { return li.style.display !== 'none'; });
            group.style.display = anyVisible ? '' : 'none';
          });
        }, 200); // 200ms 防抖
      });
    }
  }

  /* ===== 渲染:筛选标题 ===== */
  function renderFilterTitle(subjectKey) {
    var el = document.getElementById('filter-title');
    if (!el) return;
    if (!subjectKey || subjectKey === 'all') {
      el.textContent = '全部课程';
    } else {
      var cat = getCategoryByKey(subjectKey);
      el.textContent = cat ? (cat.icon + ' ' + cat.label) : '全部课程';
    }
  }

  /* ===== 渲染:课程卡片 ===== */
  var currentFilter = 'all';
  var expandedGroups = {}; // 记录用户展开的门类状态

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

    if (subject !== 'all' && cat && cat.status === 'coming' && !hasReady) {
      renderComingSoon(cat);
      gridEl.hidden = true;
      if (comingEl) comingEl.hidden = false;
    } else {
      if (comingEl) comingEl.hidden = true;
      gridEl.hidden = false;
      gridEl.innerHTML = '';
      var filtered = LESSONS.filter(function (l) {
        if (subject === 'all') return l.status === 'ready';
        return l.subject === subject && l.status === 'ready';
      });
      
      // 空课程列表友好提示
      if (filtered.length === 0) {
        gridEl.innerHTML = '<div class=\"ds-empty-state\" role=\"status\" style=\"text-align:center;padding:var(--ds-space-12);color:var(--ds-color-muted);\">' +
          '<div style=\"font-size:3rem;margin-bottom:var(--ds-space-4);\" aria-hidden=\"true\">📚</div>' +
          '<p>暂无课程</p>' +
          '<p style=\"font-size:0.875rem;margin-top:var(--ds-space-2);\">该门类课程正在筹备中，敬请期待。</p>' +
          '</div>';
      } else {
        filtered.forEach(function (lesson) {
          gridEl.insertAdjacentHTML('beforeend', buildCardHTML(lesson));
        });
      }
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

    var groups = buildSidebarGroups();
    var g = null;
    for (var i = 0; i < groups.length; i++) {
      if (groups[i].category.key === cat.key) { g = groups[i]; break; }
    }
    if (g && g.plannedLessons.length) {
      html += '<div class="ds-coming-soon__planned"><h4>规划中的课程</h4><div class="ds-card-grid">';
      g.plannedLessons.forEach(function (l) {
        html += buildComingSoonCardHTML(l);
      });
      html += '</div></div>';
    }

    html += '</div>';
    el.innerHTML = html;
  }

  /* ===== 公开 API ===== */
  window.GUOXUE_HOMEPAGE = {
    init: function (opts) {
      opts = opts || {};
      renderSeriesCover(document.getElementById('series-cover-stats'));
      renderSidebar(opts.sidebarContainer || document.getElementById('sidebar-nav'));
      renderCards('all');
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
