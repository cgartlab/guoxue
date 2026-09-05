# 国学课堂 Supabase 集成补丁

本文档提供需要修改现有文件的具体补丁。

## 1. 修改 `assets/js/auth.js` - 添加 Supabase 同步

在 `auth.js` 中的 `handleCallback()` 函数的返回之前，添加 Supabase 用户同步。

### 查找位置：
搜索以下代码（大约在 line 165-175）：

```javascript
// auth.js 原代码
async function handleCallback() {
  // ... 上面的代码 ...
  
  try {
    const resp = await fetch(tokenUrl, {
      // ... Token 交换代码 ...
    })

    if (!resp.ok) {
      // ... 错误处理 ...
    }

    const tokenData = await resp.json()
    localStorage.setItem("casdoor_access_token", tokenData.access_token || "")
    localStorage.setItem("casdoor_id_token", tokenData.id_token || "")
    // ... 其他 Token 存储 ...

    return { success: true, tokenData }  // ← 在这一行之前添加下面的代码
  } catch (err) {
    // ...
  }
}
```

### 补丁：
在 `return { success: true, tokenData }` 之前添加：

```javascript
    // ===== 登录成功，同步用户到 Supabase =====
    // 异步调用，不阻塞主流程
    if (typeof window !== 'undefined' && window.SUPABASE && window.SUPABASE.syncUser) {
      setTimeout(() => {
        window.SUPABASE.syncUser()
          .then(() => {
            console.log('[Auth] 用户已同步到 Supabase')
            // 触发自定义事件（可选）
            window.dispatchEvent(new CustomEvent('supabase:user-synced'))
          })
          .catch(err => {
            console.warn('[Auth] Supabase 同步失败（非致命）:', err)
          })
      }, 100)
    }

    return { success: true, tokenData }
```

### 完整修改片段：

在 `auth.js` 的返回对象中，也可以添加 `updateAuthUI` 后的调用：

```javascript
/**
 * 初始化：更新 UI + 静默检查登录状态
 */
function init() {
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => {
      updateAuthUI()
      // 登录成功后同步用户到 Supabase
      if (isLoggedIn() && window.SUPABASE && window.SUPABASE.syncUser) {
        window.SUPABASE.syncUser().catch(err => {
          console.warn('[Auth] 初始化 Supabase 同步失败:', err)
        })
      }
    })
  } else {
    updateAuthUI()
    if (isLoggedIn() && window.SUPABASE && window.SUPABASE.syncUser) {
      window.SUPABASE.syncUser().catch(err => {
        console.warn('[Auth] 初始化 Supabase 同步失败:', err)
      })
    }
  }
}
```

---

## 2. 修改 `assets/js/slide-engine.js` - 云端进度保存

在 `slide-engine.js` 中修改 `saveProgress()` 函数以支持 Supabase 云端保存。

### 查找位置：
搜索 `function saveProgress()` 函数（大约在 line 82-96）：

```javascript
/* ========== localStorage 持久化 ========== */
var STORAGE_KEY = 'guoxue_progress_' + courseId;

function saveProgress() {
  try {
    var data = {
      currentPage: curPage,
      quizAnswered: Object.keys(quizAnswered),
      quizScore: quizScore,
      updatedAt: Date.now()
    };
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
  } catch(e) { /* ignore quota errors */ }
}
```

### 补丁：
替换为以下代码：

```javascript
/* ========== localStorage 持久化 + Supabase 云端保存 ========== */
var STORAGE_KEY = 'guoxue_progress_' + courseId;

function saveProgress() {
  try {
    var data = {
      currentPage: curPage,
      quizAnswered: Object.keys(quizAnswered),
      quizScore: quizScore,
      updatedAt: Date.now()
    };
    
    // 1. 本地存储（总是成功，立即返回）
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    
    // 2. 云端保存（如果登录且 Supabase 可用）
    if (typeof AUTH !== 'undefined' && AUTH.isLoggedIn && 
        typeof window !== 'undefined' && window.SUPABASE && window.SUPABASE.saveProgress) {
      
      if (AUTH.isLoggedIn()) {
        window.SUPABASE.saveProgress(courseId, {
          currentPage: curPage,
          totalPages: totalPages,
          quizAnswered: quizAnswered,
          quizScore: quizScore
        }).catch(function(err) {
          // 云端保存失败不影响本地使用
          console.warn('[Sync] 云端保存失败（本地进度已保存）:', err)
        })
      }
    }
  } catch(e) { /* ignore quota errors */ }
}
```

### 注意：
- 保留原有的 `loadProgress()` 和 `clearProgress()` 函数不变
- 也可修改 `loadProgress()` 以支持从 Supabase 恢复：

```javascript
function loadProgress() {
  // 先从本地加载（快速）
  try {
    var raw = localStorage.getItem(STORAGE_KEY);
    if (raw) return JSON.parse(raw);
  } catch(e) { }
  
  // 本地没有，则尝试从 Supabase 加载
  if (typeof AUTH !== 'undefined' && AUTH.isLoggedIn && 
      typeof window !== 'undefined' && window.SUPABASE && window.SUPABASE.getProgress) {
    
    if (AUTH.isLoggedIn()) {
      window.SUPABASE.getProgress(courseId)
        .then(function(progress) {
          if (progress) {
            console.log('[Sync] 从 Supabase 恢复进度:', progress)
            // 可选：存到本地缓存
            localStorage.setItem(STORAGE_KEY, JSON.stringify({
              currentPage: progress.current_page,
              quizAnswered: progress.quiz_answered,
              quizScore: progress.quiz_score,
              updatedAt: new Date(progress.updated_at).getTime()
            }))
          }
        })
        .catch(function(err) {
          console.warn('[Sync] Supabase 加载失败，使用本地或新建:', err)
        })
    }
  }
  
  return null
}
```

---

## 3. 修改 `index.html` 和课程页面

在所有 HTML 文件中，在 `</head>` 之前或 `</body>` 之前，添加以下引入顺序：

### 原有的引入（保持不变）：
```html
<script src="/assets/js/auth.js" defer></script>
```

### 新增的引入（在 auth.js 之后）：
```html
<!-- Supabase JS 库 -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2" defer></script>

<!-- Supabase 客户端 -->
<script src="/assets/js/supabase-client.js" defer></script>

<!-- 或保持原有的其他脚本 -->
<script src="/assets/js/slide-engine.js" defer></script>
```

### 完整示例（在 `<head>` 末尾）：
```html
  <!-- 认证和数据存储 -->
  <script src="/assets/js/auth.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2" defer></script>
  <script src="/assets/js/supabase-client.js" defer></script>
  
  <!-- 课程页面脚本 -->
  <script src="/assets/js/navbar.js" defer></script>
  <script src="/assets/js/slide-engine.js" defer></script>
  <script src="/assets/js/lessons-manifest.js" defer></script>
  
  <!-- 课程特定的 JS（如果有） -->
  <script defer>
    // 可选：自定义配置
    window.GUOXUE_COURSE_ID = '01-lunyu'
    // window.GUOXUE_QUIZ_OVERRIDE = [...]
  </script>
</head>
```

---

## 4. 可选：创建迁移脚本

如需将现有的 localStorage 数据迁移到 Supabase，可在任何页面中添加：

```html
<script>
// 仅在登录后调用一次
async function migrateStorageToSupabase() {
  if (!AUTH || !AUTH.isLoggedIn() || !window.SUPABASE) return
  
  const courseIds = [
    '01-lunyu', '01-lunyu-mixed', '02-sanzijing', '02-xueer', 
    '03-xueer-xiaoti', '04-zengzi-sansheng', '05-dao-qiancheng-guo',
    '06-dizi-ruze-xiao', '07-xianxian-yise', '08-junzi-bu-zhong'
  ]
  
  let migratedCount = 0
  
  for (const courseId of courseIds) {
    try {
      const stored = JSON.parse(localStorage.getItem('guoxue_progress_' + courseId) || '{}')
      
      if (stored && stored.currentPage > 0) {
        const success = await window.SUPABASE.saveProgress(courseId, {
          currentPage: stored.currentPage || 0,
          totalPages: stored.totalPages || 0,
          quizAnswered: stored.quizAnswered || {},
          quizScore: stored.quizScore || 0
        })
        
        if (success) {
          console.log(`✅ 已迁移: ${courseId}`)
          migratedCount++
        }
      }
    } catch (err) {
      console.warn(`⚠️ 迁移失败: ${courseId}`, err)
    }
  }
  
  console.log(`✅ 迁移完成: 共 ${migratedCount} 个课程`)
  return migratedCount
}

// 在登录 1-2 秒后调用
window.addEventListener('supabase:user-synced', () => {
  setTimeout(migrateStorageToSupabase, 500)
})
</script>
```

---

## 5. 打包和部署检查清单

在提交修改前，请检查：

- [ ] 已更新 `auth.js` - 添加 Supabase 同步
- [ ] 已更新 `slide-engine.js` - 云端进度保存
- [ ] 已在所有 HTML 中添加 Supabase 脚本引入
- [ ] 已创建 `supabase-client.js` 
- [ ] 已在 Supabase 中执行 `01-schema.sql` 和 `02-rls.sql`
- [ ] 已在 `supabase-client.js` 中正确配置 `SUPABASE_URL` 和 `SUPABASE_ANON_KEY`
- [ ] 本地测试：登录 → 做题 → 检查 Supabase Dashboard 中的数据
- [ ] 浏览器控制台无错误日志

---

## 验证集成

登录后，打开浏览器控制台（F12），运行：

```javascript
// 1. 检查 Supabase 客户端是否加载
console.log(window.SUPABASE)  // 应该返回对象

// 2. 获取当前用户
await window.SUPABASE.getUser()  // 应返回用户对象

// 3. 获取课程进度
await window.SUPABASE.getProgress('01-lunyu')  // 应返回进度或 null

// 4. 测试保存进度
await window.SUPABASE.saveProgress('01-lunyu', {
  currentPage: 2,
  totalPages: 10,
  quizAnswered: { '0': true },
  quizScore: 90
})  // 应返回 true
```

祝集成顺利！🎉
