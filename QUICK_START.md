# 国学课堂 Supabase 集成 - 快速开始指南

⏱️ **预计时间**: 15 分钟

---

## 🚀 5 分钟快速部署

### 步骤 1️⃣：执行数据库脚本（5 分钟）

```bash
# 1. 登录 Supabase Dashboard
# https://app.supabase.com

# 2. 选择你的项目: https://zbjdpwkcnfnrrnlwifti.supabase.co

# 3. 打开 SQL Editor → New query

# 4. 复制并执行这个文件的全部内容：
# /supabase/01-schema.sql

# 5. 再执行这个文件的全部内容：
# /supabase/02-rls.sql

# 完成！✅
```

### 步骤 2️⃣：部署代码（5 分钟）

```bash
# 如果还没有 clone 项目
git clone https://github.com/cgartlab/guoxue.git
cd guoxue

# 1. 检查这些文件是否存在：
ls assets/js/supabase-client.js       # ✅ 应该存在
ls assets/js/auth-supabase-patch.js   # ✅ 应该存在
ls dashboard.html                     # ✅ 应该存在
ls notes.html                         # ✅ 应该存在

# 2. 提交并推送
git add -A
git commit -m "feat: integrate Supabase user system"
git push origin main

# 完成！✅ 代码已自动部署到 GitHub Pages
```

### 步骤 3️⃣：测试（5 分钟）

```bash
# 1. 打开你的项目网站
# https://cgartlab.github.io/guoxue/

# 2. 点击"登录 / 注册"
# 使用 Casdoor 完成登录

# 3. 打开一个课程，翻页、做题

# 4. 访问学习面板
# https://cgartlab.github.io/guoxue/dashboard.html
# ✅ 应该看到学习统计和成绩

# 5. 访问笔记管理
# https://cgartlab.github.io/guoxue/notes.html
# ✅ 应该能看到笔记列表（可能是空的）

# 完成！✅
```

---

## 📊 验证集成

### 在浏览器控制台中运行：

```javascript
// 1. 检查认证
AUTH.isLoggedIn()  // 应该返回 true

// 2. 检查 Supabase 客户端
window.SUPABASE  // 应该返回对象

// 3. 获取当前用户
await window.SUPABASE.getUser()
// 输出示例: { id: "uuid", casdoor_id: "xxx", username: "张三", ... }

// 4. 获取学习进度
await window.SUPABASE.getProgress('01-lunyu')
// 输出示例: { id: "uuid", user_id: "uuid", course_id: "01-lunyu", current_page: 5, ... }
```

---

## 🧪 完整测试

访问测试页面：

```
https://cgartlab.github.io/guoxue/supabase/test-integration.html
```

这个页面会指导你：
1. ✅ 检查登录状态
2. ✅ 测试用户同步
3. ✅ 测试进度保存
4. ✅ 测试笔记和书签
5. ✅ 测试成绩保存

---

## 📁 重要文件

### 数据库脚本
- `supabase/01-schema.sql` - 创建表和索引
- `supabase/02-rls.sql` - 配置安全策略

### 前端代码
- `assets/js/supabase-client.js` - Supabase API 客户端（950+ 行）
- `assets/js/auth-supabase-patch.js` - 自动同步用户
- `dashboard.html` - 学生个人面板
- `notes.html` - 笔记和书签管理
- `supabase/test-integration.html` - 测试工具

### 文档
- `SUPABASE_INTEGRATION_COMPLETE.md` - 完整文档
- `SUPABASE_SETUP.md` - 详细设置指南
- `INTEGRATION_PATCHES.md` - 代码补丁说明

---

## 🎯 主要功能

### 1️⃣ 学习进度同步

```javascript
// 自动保存（在 slide-engine.js 中）
// 用户翻页、做题时自动保存进度到 Supabase
```

### 2️⃣ 学生面板

```
/dashboard.html
- 显示已完成课程数
- 显示平均成绩
- 显示学习笔记数
- 显示总体进度百分比
- 列出所有课程的学习进度
- 列出最近的测验成绩
```

### 3️⃣ 笔记管理

```
/notes.html
- 浏览所有学习笔记（可按课程过滤）
- 笔记按颜色标签分类
- 删除笔记功能
- 浏览所有书签（可按课程过滤）
- 删除书签功能
```

### 4️⃣ 多设备同步

```
设备 A: 学习课程 → 保存到 Supabase
设备 B: 打开课程 → 自动恢复进度
```

---

## ⚡ 常见问题

### Q: 登录后无法看到数据？

A: 
```javascript
// 检查登录状态
if (!AUTH.isLoggedIn()) {
  alert('请先登录')
  return
}

// 检查 Supabase 是否加载
if (!window.SUPABASE) {
  alert('Supabase 未加载')
  return
}

// 检查是否有数据
const user = await window.SUPABASE.getUser()
console.log('用户:', user)
```

### Q: 为什么有些操作失败了？

A: 这是正常的！系统设计为：
- ✅ 本地操作总是成功（使用 localStorage）
- ⚠️ 云端操作可能失败（网络问题）
- 当云端恢复时，数据会自动同步

### Q: 如何清除数据？

A:
```javascript
// 清除本地缓存
localStorage.clear()

// 在 Supabase 中删除（需要管理员权限）
// Dashboard → Table Editor → 选择表 → 删除行
```

### Q: 支持离线使用吗？

A: 是的！
- ✅ 登录后可以离线学习（进度保存到本地）
- ✅ 在线时自动同步到 Supabase
- ❌ 如果从未登录过，无法离线访问

---

## 🔧 开发者命令

### 本地测试

```bash
# 启动本地服务（Python）
python -m http.server 8000

# 访问
# http://localhost:8000

# 查看日志
# F12 打开开发者工具 → Console
```

### 数据库操作

```sql
-- 查看所有用户
SELECT id, username, email, created_at FROM users;

-- 查看某个用户的学习进度
SELECT * FROM study_progress 
WHERE user_id = 'user-uuid' 
ORDER BY updated_at DESC;

-- 查看总学习笔记数
SELECT COUNT(*) FROM study_notes;

-- 查看平均成绩
SELECT AVG(score) FROM quiz_scores;
```

### 调试日志

```javascript
// 在 supabase-client.js 中启用详细日志
// 搜索 console.log 并取消注释

// 或在控制台中：
localStorage.setItem('supabase_debug', 'true')
```

---

## 📞 获取帮助

### 1. 查看完整文档
```
SUPABASE_INTEGRATION_COMPLETE.md
```

### 2. 运行测试工具
```
/supabase/test-integration.html
```

### 3. 检查浏览器控制台
```
F12 → Console → 查看错误信息
```

### 4. 查看 Supabase 日志
```
Supabase Dashboard → SQL Editor → 查看错误
```

---

## ✨ 下一步

### 推荐的后续工作

1. **推送通知** - 提醒用户学习
2. **家长端** - 家长查看学生进度
3. **VIP 系统** - 付费课程和订阅
4. **成就徽章** - 激励系统
5. **数据分析** - 学习报告

### 如何贡献

1. Fork 项目
2. 创建特性分支：`git checkout -b feature/xxx`
3. 提交更改：`git commit -m "feat: xxx"`
4. 推送分支：`git push origin feature/xxx`
5. 创建 Pull Request

---

**🎉 恭喜！你已经成功集成 Supabase！**

现在用户可以：
- ✅ 跨设备同步学习进度
- ✅ 管理学习笔记和书签
- ✅ 查看学习统计和成绩
- ✅ 离线学习（本地存储后备）

**祝学习愉快！** 📚✨
