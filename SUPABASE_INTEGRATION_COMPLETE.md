# 国学课堂 Supabase 集成 - 完整指南

**项目**: 国学课堂  
**集成**: Supabase + Casdoor OAuth2  
**创建日期**: 2026年6月  
**状态**: ✅ 完成

---

## 📋 目录

1. [快速开始](#快速开始)
2. [架构概览](#架构概览)
3. [数据库设计](#数据库设计)
4. [前端集成](#前端集成)
5. [API 文档](#api-文档)
6. [部署和测试](#部署和测试)
7. [常见问题](#常见问题)
8. [后续功能规划](#后续功能规划)

---

## 快速开始

### 第一步：在 Supabase 中创建数据库

你已经拥有项目：`https://zbjdpwkcnfnrrnlwifti.supabase.co`

#### 1.1 执行 Schema 脚本

1. 登录 [Supabase Dashboard](https://app.supabase.com)
2. 选择你的项目
3. 打开 **SQL Editor** → **New query**
4. 复制并执行 `/supabase/01-schema.sql` 中的所有代码

**预期结果**: 创建 13 个表和自动更新触发器

#### 1.2 配置行级安全策略

1. 在 SQL Editor 中 **New query**
2. 复制并执行 `/supabase/02-rls.sql` 中的所有代码

**预期结果**: 所有表启用 RLS，配置安全策略

#### 1.3 获取 API 密钥

1. 点击 **Settings** → **API**
2. 复制以下信息：
   - **Project URL**: 你的 Supabase URL
   - **anon public key**: 匿名密钥

在 `assets/js/supabase-client.js` 中更新这两个值（已预设）

### 第二步：集成前端代码

#### 2.1 添加脚本引入

在所有 HTML 文件（`index.html` 和各课程页面）中，在 `</head>` 前添加：

```html
<!-- 认证 -->
<script src="/assets/js/auth.js" defer></script>

<!-- Supabase -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2" defer></script>
<script src="/assets/js/supabase-client.js" defer></script>
<script src="/assets/js/auth-supabase-patch.js" defer></script>

<!-- 现有脚本 -->
<script src="/assets/js/navbar.js" defer></script>
<script src="/assets/js/slide-engine.js" defer></script>
<script src="/assets/js/lessons-manifest.js" defer></script>
```

#### 2.2 检查 slide-engine.js 集成

编辑 `assets/js/slide-engine.js`，找到 `saveProgress()` 函数（约 line 82-96），替换为：

```javascript
function saveProgress() {
  try {
    var data = {
      currentPage: curPage,
      quizAnswered: Object.keys(quizAnswered),
      quizScore: quizScore,
      updatedAt: Date.now()
    };
    
    // 本地存储
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    
    // 云端保存
    if (typeof AUTH !== 'undefined' && AUTH.isLoggedIn && 
        typeof window !== 'undefined' && window.SUPABASE) {
      
      if (AUTH.isLoggedIn()) {
        window.SUPABASE.saveProgress(courseId, {
          currentPage: curPage,
          totalPages: totalPages,
          quizAnswered: quizAnswered,
          quizScore: quizScore
        }).catch(function(err) {
          console.warn('[Sync] 云端保存失败:', err)
        })
      }
    }
  } catch(e) { }
}
```

### 第三步：访问新功能

集成完成后，用户可访问：

- **学习面板**: `/dashboard.html` - 查看学习统计、成绩、进度
- **笔记和书签**: `/notes.html` - 管理笔记和书签
- **测试工具**: `/supabase/test-integration.html` - 测试集成是否正常

---

## 架构概览

### 系统架构图

```
┌─────────────────────────────────────────────────────────┐
│                  国学课堂前端（静态 HTML）               │
│  - 课程页面（讲义、测验、答疑）                        │
│  - 学生面板（dashboard.html）                           │
│  - 笔记管理（notes.html）                               │
└────────────────┬────────────────────────────────────────┘
                 │ Casdoor OAuth2 Token
                 ↓
        ┌─────────────────────┐
        │   Casdoor 认证服务  │
        │ https://8023...     │
        └────────────┬────────┘
                     │ access_token
                     ↓
        ┌─────────────────────────────────────┐
        │    Supabase PostgreSQL 数据库       │
        ├─────────────────────────────────────┤
        │ ✓ 用户表 (users)                    │
        │ ✓ 学习进度 (study_progress)         │
        │ ✓ 笔记 (study_notes)                │
        │ ✓ 书签 (bookmarks)                  │
        │ ✓ 成绩 (quiz_scores)                │
        │ ✓ 订单 (orders)                     │
        │ ✓ 成就 (achievements)               │
        │ + 其他 7 张表                       │
        └─────────────────────────────────────┘
```

### 数据流

1. **登录**: 用户通过 Casdoor 登录 → 获取 Token
2. **同步**: Token 获取后，自动同步用户信息到 Supabase
3. **保存**: 用户学习时，进度同时保存到本地和云端
4. **恢复**: 用户重新访问时，从 Supabase 恢复进度
5. **管理**: 用户可在面板中查看所有数据

---

## 数据库设计

### 13 个核心表

#### 1. `users` - 用户表

| 字段 | 类型 | 说明 |
|------|------|------|
| id | UUID | 主键 |
| casdoor_id | TEXT | Casdoor 用户 ID（唯一） |
| username | TEXT | 用户名 |
| email | TEXT | 邮箱 |
| full_name | TEXT | 全名 |
| avatar_url | TEXT | 头像 URL |
| user_type | ENUM | 用户类型：student/parent/teacher/admin |
| bio | TEXT | 个人签名 |
| locale | TEXT | 语言设置（zh-CN）|
| created_at | TIMESTAMP | 创建时间 |
| updated_at | TIMESTAMP | 更新时间 |

#### 2. `study_progress` - 学习进度表

| 字段 | 类型 | 说明 |
|------|------|------|
| id | UUID | 主键 |
| user_id | UUID | 用户 ID（外键）|
| course_id | TEXT | 课程 ID（如 01-lunyu）|
| current_page | INT | 当前页码（0-indexed）|
| total_pages | INT | 总页数 |
| quiz_answered | JSONB | 已答题目（{"0": true, "1": false}）|
| quiz_score | FLOAT | 测验成绩（0-100）|
| completed | BOOLEAN | 是否完成 |
| completed_at | TIMESTAMP | 完成时间 |
| created_at | TIMESTAMP | 创建时间 |
| updated_at | TIMESTAMP | 更新时间 |

**索引**: (user_id, course_id) UNIQUE

#### 3. `study_notes` - 学习笔记表

支持颜色标签（yellow, green, blue, pink, red）和公开/私密分享

#### 4. `bookmarks` - 书签表

快速标记重要页面，支持备注

#### 5. `quiz_scores` - 测试成绩表

支持多次尝试，记录详细答题情况

#### 6. `orders` - 订单表

支持 VIP 订阅、内容付费、支付方式记录

#### 7-13. 其他表

- `study_lists` - 学习清单（收藏夹）
- `study_list_items` - 清单项目
- `achievements` - 成就徽章系统
- `study_logs` - 学习日志（用于分析）
- `parent_student_relations` - 家长-学生关系
- 等等

### 安全策略 (RLS)

所有表启用行级安全策略：

- **用户只能查看自己的数据**
- **用户只能修改自己的数据**
- **家长可以查看关联学生的数据**
- **教师可以查看所有学生的数据（如果配置）**

---

## 前端集成

### 文件结构

```
guoxue/
├── supabase/
│   ├── 01-schema.sql           # 数据库 schema
│   ├── 02-rls.sql              # RLS 安全策略
│   └── test-integration.html   # 测试工具
│
├── assets/js/
│   ├── auth.js                 # Casdoor 认证（原有）
│   ├── supabase-client.js      # Supabase 客户端
│   ├── auth-supabase-patch.js  # auth.js 集成补丁
│   ├── slide-engine.js         # 课程引擎（需修改）
│   ├── navbar.js               # 导航栏
│   └── lessons-manifest.js     # 课程清单
│
├── dashboard.html              # 📊 学生个人面板
├── notes.html                  # 📝 笔记和书签管理
│
├── index.html                  # 首页
├── callback.html               # OAuth 回调页面
└── lessons/
    ├── 01-lunyu/index.html
    ├── 02-sanzijing/index.html
    └── ... 其他课程
```

### 核心模块

#### `supabase-client.js` (950+ 行)

提供统一的 Supabase API 接口：

```javascript
// 用户
await window.SUPABASE.getUser()
await window.SUPABASE.syncUser()

// 学习进度
await window.SUPABASE.getProgress(courseId)
await window.SUPABASE.saveProgress(courseId, data)

// 笔记
await window.SUPABASE.getNotes(courseId)
await window.SUPABASE.createNote(courseId, page, data)
await window.SUPABASE.updateNote(noteId, updates)
await window.SUPABASE.deleteNote(noteId)

// 书签
await window.SUPABASE.getBookmarks(courseId)
await window.SUPABASE.addBookmark(courseId, page, note)
await window.SUPABASE.removeBookmark(courseId, page)

// 成绩
await window.SUPABASE.getQuizScores(courseId)
await window.SUPABASE.saveQuizScore(courseId, score, answers)
```

#### `auth-supabase-patch.js` (50 行)

自动 hook `auth.js`，在登录成功后同步用户到 Supabase

#### `dashboard.html`

学生个人面板，展示：
- 用户信息
- 学习统计（完成课程、平均成绩、笔记数、进度百分比）
- 学习进度列表
- 最近成绩（表格）
- 所有成绩详情

#### `notes.html`

笔记和书签管理：
- 标签页切换（笔记 / 书签）
- 课程过滤
- 笔记颜色标签
- 删除和编辑功能

---

## API 文档

### `window.SUPABASE` 对象

#### 用户相关

##### `getUser()`

获取当前用户信息（带 5 分钟缓存）

```javascript
const user = await window.SUPABASE.getUser()
// 返回：{ id, casdoor_id, username, email, avatar_url, ... }
```

##### `syncUser()`

从 Casdoor Token 同步用户到 Supabase

```javascript
const user = await window.SUPABASE.syncUser()
```

#### 学习进度

##### `getProgress(courseId)`

```javascript
const progress = await window.SUPABASE.getProgress('01-lunyu')
// 返回：{ id, user_id, course_id, current_page, total_pages, quiz_score, ... }
```

##### `saveProgress(courseId, data)`

保存学习进度（自动创建或更新）

```javascript
const success = await window.SUPABASE.saveProgress('01-lunyu', {
  currentPage: 5,
  totalPages: 20,
  quizAnswered: { '0': true, '1': false, '2': true },
  quizScore: 85.5
})
// 返回：true/false
```

##### `completeProgress(courseId)`

标记课程已完成

```javascript
await window.SUPABASE.completeProgress('01-lunyu')
```

#### 笔记管理

##### `getNotes(courseId)`

```javascript
const notes = await window.SUPABASE.getNotes('01-lunyu')
// 返回：[{ id, title, content, color_tag, is_pinned, created_at, ... }]
```

##### `createNote(courseId, page, noteData)`

```javascript
const note = await window.SUPABASE.createNote('01-lunyu', 5, {
  title: '我的笔记',
  content: '笔记内容\n支持多行',
  color_tag: 'yellow'  // yellow, green, blue, pink, red
})
```

##### `updateNote(noteId, updates)`

```javascript
await window.SUPABASE.updateNote('note-id', {
  title: '新标题',
  content: '新内容',
  is_pinned: true
})
```

##### `deleteNote(noteId)`

```javascript
await window.SUPABASE.deleteNote('note-id')
```

#### 书签管理

##### `getBookmarks(courseId)`

```javascript
const bookmarks = await window.SUPABASE.getBookmarks('01-lunyu')
```

##### `addBookmark(courseId, page, note)`

```javascript
const bookmark = await window.SUPABASE.addBookmark('01-lunyu', 5, '重要知识点')
```

##### `removeBookmark(courseId, page)`

```javascript
await window.SUPABASE.removeBookmark('01-lunyu', 5)
```

#### 成绩管理

##### `getQuizScores(courseId)`

```javascript
const scores = await window.SUPABASE.getQuizScores('01-lunyu')
// 返回：按日期排序的成绩列表
```

##### `getBestQuizScore(courseId)`

```javascript
const bestScore = await window.SUPABASE.getBestQuizScore('01-lunyu')
```

##### `saveQuizScore(courseId, score, answers)`

```javascript
const result = await window.SUPABASE.saveQuizScore('01-lunyu', 85, [
  { q_idx: 0, chosen: 1, correct: 1 },
  { q_idx: 1, chosen: 0, correct: 0 },
  { q_idx: 2, chosen: 1, correct: 1 }
])
```

#### 清单管理

##### `getStudyLists()`

```javascript
const lists = await window.SUPABASE.getStudyLists()
```

##### `createStudyList(title, description)`

```javascript
const list = await window.SUPABASE.createStudyList('我的高分课程', '暑假复习')
```

##### `getListItems(listId)`

```javascript
const items = await window.SUPABASE.getListItems('list-id')
```

##### `addItemToList(listId, courseId)`

```javascript
await window.SUPABASE.addItemToList('list-id', '01-lunyu')
```

#### 工具方法

##### `clearCache()`

清除用户信息缓存

```javascript
window.SUPABASE.clearCache()
```

---

## 部署和测试

### 本地测试

#### 第一步：执行 SQL 脚本

1. 打开 Supabase Dashboard
2. 执行 `/supabase/01-schema.sql` 和 `/supabase/02-rls.sql`

#### 第二步：启动本地服务

```bash
# 如果使用 Python
python -m http.server 8000

# 或使用 Node.js
npx http-server

# 或使用 Live Server（VS Code 扩展）
```

#### 第三步：打开浏览器

1. 访问 `http://localhost:8000`
2. 点击"登录 / 注册"
3. 使用 Casdoor 完成登录
4. 访问 `/dashboard.html` 查看个人面板
5. 访问 `/notes.html` 查看笔记

#### 第四步：测试集成

访问 `/supabase/test-integration.html`，按照页面指引进行测试

### GitHub Pages 部署

由于项目已使用 GitHub Pages，集成会自动部署。确保：

1. 所有文件已 commit 并 push 到 main 分支
2. `.gitignore` 中没有排除必要的文件
3. Supabase 密钥已在 `supabase-client.js` 中正确配置

```bash
git add .
git commit -m "feat: integrate Supabase user system with Casdoor"
git push origin main
```

### 生产环境检查清单

- [ ] 已在 Supabase 中执行所有 SQL 脚本
- [ ] 已更新所有 HTML 中的脚本引入
- [ ] 已修改 `slide-engine.js` 的 `saveProgress()` 函数
- [ ] 已验证 `supabase-client.js` 中的 URL 和密钥正确
- [ ] 已在浏览器控制台验证：
  - `window.AUTH` 可用
  - `window.SUPABASE` 可用
  - 登录后 Supabase 数据表中有用户记录
- [ ] 已测试页面翻页、做题、查看面板等功能
- [ ] 已验证离线时本地存储仍然有效

---

## 常见问题

### Q1: "Supabase 客户端未加载" 错误

**原因**: Supabase JS 库或 `supabase-client.js` 未成功加载

**解决**:
```javascript
// 在浏览器控制台检查
console.log(window.supabase)  // 应该返回对象
console.log(window.SUPABASE)  // 应该返回对象
```

如果返回 `undefined`，检查：
- HTML 中是否正确引入了脚本
- 网络连接是否正常
- 是否有 CORS 错误

### Q2: 登录后无法同步用户

**原因**: Casdoor Token 可能已过期或无效

**解决**:
```javascript
// 在控制台验证
AUTH.isLoggedIn()  // 应该返回 true
AUTH.getAccessToken()  // 应该返回有效的 token
AUTH.parseIdToken()  // 应该返回用户信息
```

### Q3: Supabase API 返回 401 错误

**原因**: Token 过期或 Supabase 密钥配置错误

**解决**:
1. 检查 `supabase-client.js` 中的 `SUPABASE_URL` 和 `SUPABASE_ANON_KEY`
2. 重新登录获取新的 Token
3. 查看 Supabase RLS 策略是否配置正确

### Q4: 学习进度保存失败，但本地仍有数据

**原因**: 这是预期行为！本地存储作为后备

**提示**: 保存进度时：
1. 首先保存到本地存储（总是成功）
2. 然后尝试保存到 Supabase（如果失败不影响使用）
3. 用户可以在任何设备继续学习（如果登录了）

### Q5: 如何迁移现有的 localStorage 数据？

**方法**: 在首次登录后运行迁移脚本

```javascript
async function migrateLocalStorage() {
  const courseIds = [
    '01-lunyu', '02-sanzijing', '02-xueer',
    // ... 其他课程
  ]
  
  for (const courseId of courseIds) {
    const stored = JSON.parse(
      localStorage.getItem('guoxue_progress_' + courseId) || '{}'
    )
    if (stored.currentPage > 0) {
      await window.SUPABASE.saveProgress(courseId, stored)
    }
  }
  
  alert('✅ 迁移完成')
}

// 在登录后调用
migrateLocalStorage()
```

### Q6: 如何处理多设备同步？

**工作原理**:
1. 用户 A 在设备 1 学习 → 数据保存到 Supabase
2. 用户 A 在设备 2 打开课程 → 自动从 Supabase 恢复进度
3. 不同用户的数据通过 RLS 隔离

**注意**: 当前实现是"最后保存优先"，不支持实时同步。如需实时同步，可使用 Supabase Realtime 功能。

### Q7: 如何备份数据？

**方法**:

1. **Supabase 自动备份**: Supabase 每天自动备份数据库
2. **导出数据**:
   ```sql
   -- 在 Supabase SQL Editor 中运行
   SELECT * FROM study_progress
   WHERE user_id = 'user-id' AND course_id = '01-lunyu'
   ```
3. **使用 pgdump**:
   ```bash
   pg_dump postgresql://user:password@host/db > backup.sql
   ```

---

## 后续功能规划

### 第二阶段（下月）

- [ ] 家长端应用（查看学生进度、设置目标）
- [ ] 教师端应用（班级管理、批量成绩查询）
- [ ] 推送通知（学习提醒、成绩推送）
- [ ] 学习数据分析（学习时长、知识掌握度）

### 第三阶段（下一个季度）

- [ ] VIP 订阅系统（支付宝/微信支付）
- [ ] 社交功能（分享笔记、互相关注）
- [ ] AI 学习助手（个性化推荐、自动总结）
- [ ] 移动应用（iOS/Android 小程序）

### 第四阶段（明年）

- [ ] 竞赛系统（排行榜、徽章、奖励）
- [ ] 个性化学习路径
- [ ] 成绩预测和诊断
- [ ] 教材扩展（更多经典著作）

---

## 支持和联系

如有问题，请：

1. 查看浏览器控制台的错误信息
2. 访问测试页面 `/supabase/test-integration.html`
3. 查阅本文档的常见问题部分
4. 检查 Supabase Dashboard 的日志

---

## 许可证

本集成遵循项目原有许可证。

---

## 更新日志

### v1.0.0 (2026-06-10)

✅ 初版发布

- 完整的 Supabase 数据库设计（13 个表）
- RLS 安全策略
- Supabase 客户端模块（950+ 行）
- 学生个人面板
- 笔记和书签管理
- 集成文档和测试工具

**下一个版本**: v1.1.0（家长端应用）

---

**🎉 恭喜！国学课堂已成功集成 Supabase。现在用户可以跨设备同步学习数据了！**
