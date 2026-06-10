# 国学课堂 - 登录问题诊断和修复指南

## 🔍 快速诊断（1分钟）

### 第一步：打开浏览器开发者工具

1. **打开开发者工具** (按 `F12` 或 `Ctrl+Shift+I`)
2. **查看 Console 标签** - 查看红色错误信息
3. **查看 Network 标签** - 查看网络请求状态

### 常见错误信息

```
❌ CORS 错误
→ Access to XMLHttpRequest at 'https://8023laozhanshi.cc/...' 
  from origin 'https://cgartlab.github.io' has been blocked by CORS policy

❌ 重定向 URI 不匹配
→ Redirect URI mismatch

❌ Token 获取失败
→ POST .../access_token 400 (Bad Request)

❌ 网络超时
→ Failed to fetch / Network error
```

---

## 🔧 逐步排查

### 1️⃣ 检查认证模块是否加载

在浏览器 Console 中运行：

```javascript
// 检查 AUTH 对象
console.log(AUTH)
// 应该返回对象：{login, logout, isLoggedIn, ...}

// 如果返回 undefined，说明 auth.js 未加载
```

**解决**：确保 `index.html` 中包含：
```html
<script src="assets/js/auth.js" defer></script>
```

### 2️⃣ 检查登录按钮是否存在

在 Console 中运行：

```javascript
document.getElementById('auth-nav')  // 应该返回元素
document.querySelectorAll('button').forEach(b => console.log(b.textContent))
```

**解决**：确保导航栏有 `<div id="auth-nav"></div>`

### 3️⃣ 测试 Casdoor 服务器连接

在 Console 中运行：

```javascript
// 测试服务器是否在线
fetch('https://8023laozhanshi.cc/', { 
  method: 'HEAD',
  mode: 'no-cors' 
})
  .then(() => console.log('✓ Casdoor 服务器在线'))
  .catch(err => console.log('✗ 无法连接:', err))
```

**如果失败**：
- Casdoor 服务可能离线
- 检查网络连接
- 尝试刷新页面

### 4️⃣ 测试 CORS 预检

在 Console 中运行：

```javascript
// 测试 CORS 预检请求
fetch('https://8023laozhanshi.cc/api/login/oauth/authorize', {
  method: 'OPTIONS',
  headers: {
    'Origin': window.location.origin,
    'Access-Control-Request-Method': 'POST',
    'Access-Control-Request-Headers': 'content-type'
  }
})
  .then(r => {
    console.log('CORS 头:', {
      'Allow-Origin': r.headers.get('access-control-allow-origin'),
      'Allow-Methods': r.headers.get('access-control-allow-methods')
    })
  })
  .catch(err => console.log('✗ CORS 预检失败:', err))
```

### 5️⃣ 查看完整的网络请求

打开 **Network** 标签：

1. 清空日志 (Ctrl+L)
2. 点击"登录/注册"按钮
3. 查看请求列表
4. 找到 `authorize` 请求
5. 检查：
   - **URL** 是否正确
   - **Status** 是否 200/302
   - **Response Headers** 中的 CORS 字段

---

## ❌ 常见错误及解决

### 错误 1: CORS 被阻止

**症状**：
```
Access to XMLHttpRequest at 'https://8023laozhanshi.cc/...' 
has been blocked by CORS policy
```

**原因**：
- Casdoor 未配置允许的域名
- 请求来自 GitHub Pages

**解决方案**：

**A. 联系 Casdoor 管理员**
- 在 Casdoor 中添加 CORS 允许列表：
  ```
  https://cgartlab.github.io
  https://guoxue.8023laozhanshi.cc
  ```

**B. 使用备用认证方式**
- 等待 Casdoor 配置完成
- 使用本地开发测试 (localhost)

### 错误 2: 重定向 URI 不匹配

**症状**：
```
Redirect URI mismatch
The redirect_uri parameter does not match...
```

**原因**：
- Casdoor 配置的回调 URL 与实际使用 URL 不一致

**解决方案**：

1. 检查当前 URL
   ```javascript
   console.log('Current URL:', window.location.href)
   console.log('Expected redirect:', window.location.origin + '/guoxue/callback.html')
   ```

2. 登录 Casdoor Dashboard 更新 **Redirect URIs**：
   ```
   https://cgartlab.github.io/guoxue/callback.html
   ```

### 错误 3: Token 获取失败 (400 错误)

**症状**：
```
POST .../api/login/oauth/access_token 400 (Bad Request)
```

**原因**：
- PKCE 验证失败
- code 已过期
- client_id 不正确

**解决方案**：

1. 清除 localStorage
   ```javascript
   localStorage.clear()
   sessionStorage.clear()
   ```

2. 重新登录

3. 如果仍失败，检查 Casdoor 日志

### 错误 4: 网络超时

**症状**：
```
Failed to fetch
Network error
Timeout
```

**原因**：
- Casdoor 服务离线
- 网络不稳定
- 请求超时

**解决方案**：

1. 刷新页面重试
2. 检查网络连接
3. 检查 Casdoor 服务状态：
   ```bash
   ping 8023laozhanshi.cc
   curl -I https://8023laozhanshi.cc/
   ```

### 错误 5: Callback 页面处理失败

**症状**：
- 登录后跳转到 callback.html
- 页面显示"❌ 登录处理失败"

**原因**：
- URL 参数缺失（没有 `code` 和 `state`）
- Token 交换失败
- 回调处理出错

**解决方案**：

1. 检查 URL 中的参数
   ```javascript
   const params = new URLSearchParams(window.location.search)
   console.log('code:', params.get('code'))
   console.log('state:', params.get('state'))
   console.log('error:', params.get('error'))
   ```

2. 检查浏览器 Console 中的详细错误

3. 查看 localStorage 中是否保存了 state
   ```javascript
   console.log('saved state:', sessionStorage.getItem('casdoor_state'))
   console.log('verifier:', sessionStorage.getItem('casdoor_code_verifier'))
   ```

---

## 🧪 完整测试流程

### 在 Console 中逐项测试

```javascript
// === 诊断脚本 ===

// 1. 检查环境
console.log('=== 环境检查 ===')
console.log('URL:', window.location.href)
console.log('Auth 模块:', typeof AUTH)
console.log('localStorage 可用:', typeof localStorage !== 'undefined')

// 2. 检查配置
console.log('\n=== 配置检查 ===')
console.log('Casdoor 连接测试...')
fetch('https://8023laozhanshi.cc/', { mode: 'no-cors' })
  .then(() => console.log('✓ Casdoor 在线'))
  .catch(e => console.log('✗ Casdoor 离线:', e.message))

// 3. 检查 Token
console.log('\n=== Token 检查 ===')
console.log('Token:', localStorage.getItem('casdoor_access_token') ? '已保存' : '未保存')
console.log('ID Token:', localStorage.getItem('casdoor_id_token') ? '已保存' : '未保存')
console.log('已登录:', AUTH.isLoggedIn && AUTH.isLoggedIn())

// 4. 获取用户信息
if (AUTH.isLoggedIn && AUTH.isLoggedIn()) {
  console.log('\n=== 用户信息 ===')
  const user = AUTH.parseIdToken()
  console.log('用户:', user)
}
```

### 手动测试登录流程

```javascript
// 1. 点击"登录/注册"按钮
// 或在 Console 运行: AUTH.login()

// 2. 应该看到重定向到 Casdoor
// URL 应该变为: https://8023laozhanshi.cc/login/oauth/authorize?...

// 3. 在 Casdoor 页面登录

// 4. 应该重定向回 callback.html

// 5. 验证是否成功
console.log('已登录:', AUTH.isLoggedIn())
```

---

## 🔐 临时解决方案（开发测试）

### 模拟登录 (仅用于开发)

创建 `assets/js/auth-mock.js`:

```javascript
// 模拟登录（开发测试用）
window.AUTH_MOCK = {
  mockLogin() {
    const idToken = btoa(JSON.stringify({
      sub: 'test-user-' + Date.now(),
      name: '测试用户',
      email: 'test@example.com',
      picture: 'https://via.placeholder.com/40'
    })) + '.mock.mock';
    
    localStorage.setItem('casdoor_id_token', idToken);
    localStorage.setItem('casdoor_access_token', 'mock_token_' + Date.now());
    localStorage.setItem('casdoor_expires_at', String(Date.now() + 24*3600000));
    
    AUTH.updateAuthUI();
    alert('✓ 模拟登录成功（仅用于测试）');
  }
};
```

在 `index.html` 中添加：
```html
<script src="assets/js/auth-mock.js"></script>
<!-- 在页面某处添加测试按钮 -->
<button onclick="AUTH_MOCK.mockLogin()" style="display:none" id="test-login">
  测试登录（开发用）
</button>
```

然后在 Console 中运行：
```javascript
AUTH_MOCK.mockLogin()
```

---

## 📊 收集日志用于反馈

如果问题未解决，收集以下信息：

```javascript
// 在 Console 运行这段代码
const diagnostics = {
  url: window.location.href,
  userAgent: navigator.userAgent,
  timestamp: new Date().toISOString(),
  authStatus: AUTH.isLoggedIn ? AUTH.isLoggedIn() : 'unknown',
  localStorage: {
    hasToken: !!localStorage.getItem('casdoor_access_token'),
    hasIdToken: !!localStorage.getItem('casdoor_id_token')
  },
  sessionStorage: {
    hasState: !!sessionStorage.getItem('casdoor_state'),
    hasVerifier: !!sessionStorage.getItem('casdoor_code_verifier')
  }
};

console.log(JSON.stringify(diagnostics, null, 2));
// 复制这个输出到 GitHub Issues
```

---

## 📞 获取帮助

### 第 1 步：检查清单

- [ ] 打开 Console 查看错误
- [ ] 测试 Casdoor 服务连接
- [ ] 清除 localStorage 并重试
- [ ] 在不同浏览器中测试

### 第 2 步：收集信息

- 截图错误信息
- 浏览器和版本
- 操作系统
- 诊断日志

### 第 3 步：提交问题

提交到：https://github.com/cgartlab/guoxue/issues

包含：
- 错误信息（文本或截图）
- 诊断日志
- 重现步骤

---

## ✅ 验证修复

修复后验证：

- [ ] 登录按钮可点击
- [ ] 能打开 Casdoor 登录页面
- [ ] 能输入用户名密码
- [ ] 点击授权后回跳
- [ ] 显示"✅ 登录成功"
- [ ] 能看到用户名在导航栏
- [ ] 能访问 /dashboard.html

---

**🎓 如有问题，请按照上述步骤诊断。** 
