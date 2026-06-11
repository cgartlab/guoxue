# 国学课堂 Supabase 集成指南

这份文档将一步步指导你如何为国学课堂项目集成 Supabase 用户系统。

## 📋 目录

1. [前置条件](#前置条件)
2. [第一步：创建数据库表](#第一步创建数据库表)
3. [第二步：配置 RLS 安全策略](#第二步配置-rls-安全策略)
4. [第三步：获取 API 密钥](#第三步获取-api-密钥)
5. [第四步：前端集成](#第四步前端集成)
6. [第五步：测试](#第五步测试)
7. [常见问题](#常见问题)

---

## 前置条件

- ✅ 已创建 Supabase 项目：https://zbjdpwkcnfnrrnlwifti.supabase.co
- ✅ Casdoor 认证系统已配置
- ✅ 项目包含 `auth.js`（已有）

---

## 第一步：创建数据库表

### 步骤 1.1：打开 Supabase SQL 编辑器

1. 登录 [Supabase Dashboard](https://app.supabase.com)
2. 选择你的项目
3. 左侧菜单 → **SQL Editor**
4. 点击 **New query**

### 步骤 1.2：执行 Schema 脚本

1. 打开文件 `/supabase/01-schema.sql`
2. 复制所有 SQL 内容
3. 粘贴到 Supabase SQL 编辑器
4. 点击 **Run** 执行

✅ **结果：** 会看到以下 13 个表被创建
- `users` — 用户信息
- `study_progress` — 学习进度
- `study_notes` — 学习笔记
- `bookmarks` — 书签
- `quiz_scores` — 测试成绩
- `orders` — 订单
- `study_lists` — 学习清单
- `study_list_items` — 清单项目
- `achievements` — 成就徽章
- `study_logs` — 学习日志
- `parent_student_relations` — 家长-学生关系

### 步骤 1.3：验证表结构

1. 左侧菜单 → **Table Editor**
2. 检查所有表都已显示在列表中

---

## 第二步：配置 RLS 安全策略

### 步骤 2.1：执行 RLS 脚本

1. 打开 Supabase SQL 编辑器（New query）
2. 打开文件 `/supabase/02-rls.sql`
3. 复制所有内容并执行

✅ **结果：** 启用了行级安全策略，保护用户隐私

### 步骤 2.2：验证 RLS 已启用

1. 左侧菜单 → **Authentication → Policies**
2. 选择任意表，应该看到多个 Policy 规则

---

## 第三步：获取 API 密钥

### 步骤 3.1：查找你的项目 URL 和密钥

1. 在 Supabase Dashboard，点击 **Settings** → **API**
2. 找到以下信息：
   - **Project URL**：例如 `https://zbjdpwkcnfnrrnlwifti.supabase.co`
   - **anon public key**：一个很长的字符串，以 `eyJhbGc...` 开头

### 步骤 3.2：保存到项目文件

创建文件 `.kiro/supabase.env`（项目级配置，不提交到 Git）：

```bash
# Supabase 配置
SUPABASE_URL=https://zbjdpwkcnfnrrnlwifti.supabase.co
SUPABASE_ANON_KEY=你的匿名密钥
```

或者在 `assets/js/supabase-client.js` 中直接配置（见下一步）。

---

## 第四步：前端集成

### 步骤 4.1：创建 Supabase 客户端模块

创建文件 `assets/js/supabase-client.js`：

```javascript
/**
 * Supabase 客户端初始化
 * 在 auth.js 之后引入
 */

// 配置（替换为你的实际值）
const SUPABASE_URL = 'https://zbjdpwkcnfnrrnlwifti.supabase.co'
const SUPABASE_ANON_KEY = '你的 anon key'

// 创建 Supabase 客户端
const supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
  auth: {
    autoRefreshToken: false,  // 使用 Casdoor Token，不用 Supabase 的
    persistSession: false     // 不持久化（用 Casdoor 的 localStorage）
  }
})

/**
 * 使用 Casdoor Token 调用 Supabase API
 */
async function supabaseQuery(method, table, options = {}) {
  const token = AUTH.getAccessToken()
  if (!token) {
    console.warn('[Supabase] 未登录，无法调用 API')
    return { data: null, error: 'Not authenticated' }
  }

  // 构建请求 URL
  const url = new URL(`${SUPABASE_URL}/rest/v1/${table}`)
  
  // 添加查询参数
  if (options.select) {
    url.searchParams.append('select', options.select)
  }
  if (options.filter) {
    // 简单过滤器：{ eq: { user_id: 'xxx' } }
    for (const [key, value] of Object.entries(options.filter)) {
      if (typeof value === 'object') {
        const op = Object.keys(value)[0]
        const val = value[op]
        url.searchParams.append(`${key}=${op}.${val}`)
      }
    }
  }
  if (options.order) {
    // 排序：{ by: 'created_at', ascending: false }
    const dir = options.order.ascending ? 'asc' : 'desc'
    url.searchParams.append('order', `${options.order.by}.${dir}`)
  }
  if (options.limit) {
    url.searchParams.append('limit', options.limit)
  }

  try {
    const response = await fetch(url.toString(), {
      method: method,
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
        'apikey': SUPABASE_ANON_KEY
      },
      body: options.data ? JSON.stringify(options.data) : undefined
    })

    if (!response.ok) {
      const error = await response.text()
      return { data: null, error }
    }

    const data = await response.json()
    return { data, error: null }
  } catch (error) {
    console.error('[Supabase] 请求失败:', error)
    return { data: null, error: error.message }
  }
}

// 导出常用的 CRUD 操作
window.SUPABASE = {
  // 查询用户
  async getUser() {
    if (!AUTH.isLoggedIn()) return null
    const user = AUTH.parseIdToken()
    const { data, error } = await supabaseQuery('GET', 'users', {
      select: '*',
      filter: { casdoor_id: { eq: user.sub } }
    })
    return data?.[0] || null
  },

  // 同步/创建用户（从 Casdoor Token 获取信息）
  async syncUser() {
    if (!AUTH.isLoggedIn()) return null
    const user = AUTH.parseIdToken()
    const { data, error } = await supabaseQuery('POST', 'users', {
      data: {
        casdoor_id: user.sub,
        username: user.name,
        email: user.email,
        avatar_url: user.avatar,
        full_name: user.name,
        updated_at: new Date().toISOString()
      }
    })
    return data?.[0] || null
  },

  // 获取学习进度
  async getProgress(courseId) {
    const user = await SUPABASE.getUser()
    if (!user) return null
    const { data, error } = await supabaseQuery('GET', 'study_progress', {
      select: '*',
      filter: { 
        user_id: { eq: user.id },
        course_id: { eq: courseId }
      }
    })
    return data?.[0] || null
  },

  // 保存学习进度
  async saveProgress(courseId, progressData) {
    const user = await SUPABASE.getUser()
    if (!user) {
      console.warn('[Supabase] 用户未登录，无法保存进度')
      return false
    }
    const { data, error } = await supabaseQuery('POST', 'study_progress', {
      data: {
        user_id: user.id,
        course_id: courseId,
        current_page: progressData.currentPage,
        total_pages: progressData.totalPages,
        quiz_answered: progressData.quizAnswered,
        quiz_score: progressData.quizScore,
        updated_at: new Date().toISOString()
      }
    })
    if (error) {
      console.error('[Supabase] 保存进度失败:', error)
      return false
    }
    return true
  },

  // 获取学习笔记列表
  async getNotes(courseId) {
    const user = await SUPABASE.getUser()
    if (!user) return []
    const { data, error } = await supabaseQuery('GET', 'study_notes', {
      select: '*',
      filter: {
        user_id: { eq: user.id },
        course_id: { eq: courseId }
      },
      order: { by: 'created_at', ascending: false }
    })
    return data || []
  },

  // 创建笔记
  async createNote(courseId, page, note) {
    const user = await SUPABASE.getUser()
    if (!user) return false
    const { data, error } = await supabaseQuery('POST', 'study_notes', {
      data: {
        user_id: user.id,
        course_id: courseId,
        page: page,
        title: note.title || '',
        content: note.content,
        color_tag: note.color_tag || 'yellow',
        is_public: false,
        created_at: new Date().toISOString()
      }
    })
    return !error
  },

  // 获取测试成绩
  async getQuizScores(courseId) {
    const user = await SUPABASE.getUser()
    if (!user) return []
    const { data, error } = await supabaseQuery('GET', 'quiz_scores', {
      select: '*',
      filter: {
        user_id: { eq: user.id },
        course_id: { eq: courseId }
      },
      order: { by: 'created_at', ascending: false }
    })
    return data || []
  },

  // 保存测试成绩
  async saveQuizScore(courseId, score, answers) {
    const user = await SUPABASE.getUser()
    if (!user) return false
    const { data, error } = await supabaseQuery('POST', 'quiz_scores', {
      data: {
        user_id: user.id,
        course_id: courseId,
        score: score,
        correct_count: answers.filter(a => a.correct).length,
        total_questions: answers.length,
        answers: answers,
        completed_at: new Date().toISOString()
      }
    })
    return !error
  }
}
```

### 步骤 4.2：在 HTML 中引入 Supabase

编辑 `index.html` 和各个课程页面的 `index.html`，在 `auth.js` 之后添加：

```html
<!-- Supabase JS 库（只需引入一次） -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>

<!-- 你的 Supabase 客户端 -->
<script src="/assets/js/supabase-client.js" defer></script>

<!-- 然后是其他脚本 -->
<script src="/assets/js/slide-engine.js" defer></script>
```

### 步骤 4.3：修改 auth.js 添加 Supabase 同步

在 `auth.js` 的 `handleCallback()` 函数成功后调用 Supabase 同步：

```javascript
// 在 auth.js 中，handleCallback() 函数的最后添加：
if (result.success) {
  // 登录成功后同步用户到 Supabase
  setTimeout(() => {
    if (window.SUPABASE && SUPABASE.syncUser) {
      SUPABASE.syncUser().catch(err => {
        console.warn('[Auth] Supabase 同步失败（非致命错误）:', err)
      })
    }
  }, 100)
}
```

### 步骤 4.4：修改 slide-engine.js 实现云端保存

在 `slide-engine.js` 中，找到 `saveProgress()` 函数，改为：

```javascript
function saveProgress() {
  try {
    var data = {
      currentPage: curPage,
      quizAnswered: Object.keys(quizAnswered),
      quizScore: quizScore,
      updatedAt: Date.now()
    };
    
    // 1. 本地保存（快速，离线可用）
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    
    // 2. 云端保存（如果登录）
    if (AUTH && AUTH.isLoggedIn() && window.SUPABASE) {
      SUPABASE.saveProgress(courseId, {
        currentPage: curPage,
        totalPages: totalPages,
        quizAnswered: quizAnswered,
        quizScore: quizScore
      }).catch(err => {
        console.warn('[Sync] 云端保存失败（本地仍有效）:', err)
      })
    }
  } catch(e) { /* ignore quota errors */ }
}
```

---

## 第五步：测试

### 测试 5.1：验证用户同步

1. 打开任意课程页面
2. 点击"登录 / 注册"
3. 使用 Casdoor 完成登录
4. 登录后，打开 Supabase Dashboard
5. 进入 **Table Editor** → **users** 表
6. 应该看到刚才登录的用户已被创建

### 测试 5.2：验证进度保存

1. 登录后，打开一个课程
2. 翻到第 3 页
3. 做一道测验题
4. 打开 Supabase Dashboard
5. 进入 **Table Editor** → **study_progress** 表
6. 应该看到一条记录，`current_page: 2`（0-indexed），`quiz_score` > 0

### 测试 5.3：验证离线回退

1. 打开浏览器开发者工具 → Network
2. 在课程页面，设置 Network 为 Offline
3. 翻页、做题
4. 应该仍然能翻页和做题（因为有本地存储作为后备）

---

## 常见问题

### Q1: 为什么某些 API 调用返回 401？

**A:** 说明 Casdoor Token 已过期或无效。检查：
- `AUTH.isLoggedIn()` 是否返回 `true`
- `AUTH.getAccessToken()` 是否返回有效的 Token

### Q2: 如何处理 Token 刷新？

**A:** 当前使用 Casdoor 的 Token。如需自动刷新，在 `auth.js` 中添加：

```javascript
// 定期检查 Token 是否即将过期
setInterval(() => {
  const expiresAt = parseInt(localStorage.getItem("casdoor_expires_at") || "0", 10)
  if (Date.now() > expiresAt - 60000) {  // 提前 1 分钟刷新
    // 调用 refresh_token 端点
  }
}, 30000)  // 每 30 秒检查一次
```

### Q3: 如何批量迁移现有的 localStorage 数据？

**A:** 创建迁移脚本：

```javascript
async function migrateLocalStorageToSupabase() {
  if (!AUTH.isLoggedIn()) return
  
  const courseIds = [
    '01-lunyu', '02-sanzijing', '02-xueer', 
    '03-xueer-xiaoti', '04-zengzi-sansheng', 
    '05-dao-qiancheng-guo', '06-dizi-ruze-xiao', 
    '07-xianxian-yise', '08-junzi-bu-zhong'
  ]
  
  for (const courseId of courseIds) {
    const stored = JSON.parse(localStorage.getItem('guoxue_progress_' + courseId) || '{}')
    if (stored.currentPage > 0) {
      await SUPABASE.saveProgress(courseId, stored)
    }
  }
  
  console.log('✅ 迁移完成')
}

// 在首次登录成功后调用
migrateLocalStorageToSupabase()
```

### Q4: 如何在生产环境安全地存储 API 密钥？

**A:** 不要在客户端代码中硬编码密钥。使用以下方法之一：
- **方法 1（推荐）**：使用环境变量 + 构建流程
- **方法 2**：由服务器端端点代理 API 请求
- **方法 3**：使用 Supabase Realtime 限制 anon key 权限

---

## 📚 后续步骤

完成集成后，你可以实现：

1. **学生个人面板**（学习统计、成绩查询）
2. **笔记和书签管理**
3. **家长端**（查看学生进度）
4. **教师端**（班级管理）
5. **VIP/订阅系统**（支付集成）
6. **学习数据分析**

---

**最后一步**：将此文档和 SQL 脚本提交到 GitHub，团队其他成员可以快速复现集成。

```bash
git add supabase/ SUPABASE_SETUP.md
git commit -m "feat: integrate Supabase user system with Casdoor auth"
git push origin main
```

祝好！🎉
