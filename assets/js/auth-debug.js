/**
 * 认证调试工具
 * 用于诊断登录问题
 * 
 * 使用方法：在浏览器 Console 中运行以下命令
 * 或在 HTML 中引入此文件
 */

window.AUTH_DEBUG = {
  /**
   * 运行完整诊断
   */
  runDiagnostics() {
    console.clear();
    console.log('%c=== 国学课堂认证诊断报告 ===', 'font-size: 16px; font-weight: bold; color: #667eea;');
    console.log('诊断时间:', new Date().toLocaleString('zh-CN'));
    
    // 1. 环境检查
    this.checkEnvironment();
    
    // 2. 连接检查
    this.checkConnectivity();
    
    // 3. 存储检查
    this.checkStorage();
    
    // 4. 认证状态检查
    this.checkAuthStatus();
    
    // 5. 详细信息
    this.showDetailedInfo();
    
    console.log('%c诊断完成 ✓', 'color: #52c41a; font-weight: bold;');
    return this.getSummary();
  },
  
  /**
   * 检查浏览器环境
   */
  checkEnvironment() {
    console.log('\n%c1️⃣ 环境检查', 'font-weight: bold; color: #1890ff;');
    
    const checks = {
      '浏览器': navigator.userAgent.split(' ').slice(-2).join(' '),
      '当前 URL': window.location.href,
      'HTTPS': window.location.protocol === 'https:' ? '✓' : '⚠️ HTTP (某些功能可能受限)',
      'localStorage': typeof localStorage !== 'undefined' ? '✓' : '✗',
      'sessionStorage': typeof sessionStorage !== 'undefined' ? '✓' : '✗',
      'crypto.getRandomValues': typeof crypto !== 'undefined' && typeof crypto.getRandomValues === 'function' ? '✓' : '✗'
    };
    
    for (const [key, value] of Object.entries(checks)) {
      console.log(`  ${key}: ${value}`);
    }
  },
  
  /**
   * 检查网络连接
   */
  async checkConnectivity() {
    console.log('\n%c2️⃣ 连接性检查', 'font-weight: bold; color: #1890ff;');
    
    const casdoorUrl = 'https://8023laozhanshi.cc';
    
    try {
      const response = await fetch(casdoorUrl + '/', {
        method: 'HEAD',
        mode: 'no-cors'
      });
      console.log(`  Casdoor 服务器: ✓ 在线`);
    } catch (err) {
      console.log(`  Casdoor 服务器: ✗ 离线或无法连接`);
      console.log(`    原因: ${err.message}`);
    }
    
    // 测试 CORS
    try {
      await fetch(casdoorUrl + '/api/login/oauth/authorize', {
        method: 'OPTIONS',
        mode: 'cors'
      });
      console.log(`  CORS 支持: ✓ 可用`);
    } catch (err) {
      console.log(`  CORS 支持: ⚠️ 受限 - ${err.message}`);
    }
  },
  
  /**
   * 检查本地存储
   */
  checkStorage() {
    console.log('\n%c3️⃣ 存储检查', 'font-weight: bold; color: #1890ff;');
    
    const storageKeys = [
      'casdoor_access_token',
      'casdoor_id_token',
      'casdoor_token_type',
      'casdoor_expires_at',
      'casdoor_refresh_token'
    ];
    
    const sessionKeys = [
      'casdoor_state',
      'casdoor_code_verifier',
      'casdoor_redirect_back'
    ];
    
    console.log('  localStorage:');
    storageKeys.forEach(key => {
      const value = localStorage.getItem(key);
      if (value) {
        const preview = value.substring(0, 30) + (value.length > 30 ? '...' : '');
        console.log(`    ${key}: ${preview}`);
      } else {
        console.log(`    ${key}: (空)`);
      }
    });
    
    console.log('  sessionStorage:');
    sessionKeys.forEach(key => {
      const value = sessionStorage.getItem(key);
      if (value) {
        const preview = value.substring(0, 30) + (value.length > 30 ? '...' : '');
        console.log(`    ${key}: ${preview}`);
      } else {
        console.log(`    ${key}: (空)`);
      }
    });
  },
  
  /**
   * 检查认证状态
   */
  checkAuthStatus() {
    console.log('\n%c4️⃣ 认证状态检查', 'font-weight: bold; color: #1890ff;');
    
    if (!window.AUTH) {
      console.log('  ✗ AUTH 模块未加载');
      return;
    }
    
    console.log('  AUTH 模块: ✓ 已加载');
    
    if (typeof AUTH.isLoggedIn === 'function') {
      const isLoggedIn = AUTH.isLoggedIn();
      console.log(`  登录状态: ${isLoggedIn ? '✓ 已登录' : '⚠️ 未登录'}`);
      
      if (isLoggedIn && typeof AUTH.parseIdToken === 'function') {
        try {
          const user = AUTH.parseIdToken();
          console.log(`  当前用户:`);
          console.log(`    名字: ${user.name || '(未知)'}`);
          console.log(`    邮箱: ${user.email || '(未知)'}`);
          console.log(`    ID: ${user.sub || '(未知)'}`);
        } catch (err) {
          console.log(`  ✗ 无法解析用户信息: ${err.message}`);
        }
      }
    }
    
    // 检查 Token 过期时间
    const expiresAt = localStorage.getItem('casdoor_expires_at');
    if (expiresAt) {
      const date = new Date(parseInt(expiresAt));
      const now = new Date();
      const expired = now > date;
      console.log(`  Token 过期时间: ${date.toLocaleString('zh-CN')}`);
      console.log(`  Token 状态: ${expired ? '✗ 已过期' : '✓ 有效'}`);
    }
  },
  
  /**
   * 显示详细信息
   */
  showDetailedInfo() {
    console.log('\n%c5️⃣ 详细信息', 'font-weight: bold; color: #1890ff;');
    
    if (window.AUTH && window.AUTH.CONFIG) {
      console.log('  Casdoor 配置:');
      console.log('    服务器:', window.AUTH.CONFIG.serverUrl || '(未设置)');
      console.log('    客户端 ID:', window.AUTH.CONFIG.clientId || '(未设置)');
    }
    
    // 显示最近的网络请求
    console.log('\n  💡 网络请求调试:');
    console.log('    1. 打开 Network 标签');
    console.log('    2. 清空日志 (Ctrl+L)');
    console.log('    3. 点击登录按钮');
    console.log('    4. 查看 authorize 请求的状态和响应头');
  },
  
  /**
   * 获取诊断摘要
   */
  getSummary() {
    const token = localStorage.getItem('casdoor_access_token');
    const isLoggedIn = window.AUTH && window.AUTH.isLoggedIn && window.AUTH.isLoggedIn();
    
    return {
      timestamp: new Date().toISOString(),
      url: window.location.href,
      isLoggedIn,
      hasToken: !!token,
      authModuleLoaded: typeof window.AUTH === 'object'
    };
  },
  
  /**
   * 清空所有认证数据
   */
  clearAuth() {
    const keys = [
      'casdoor_access_token',
      'casdoor_id_token',
      'casdoor_token_type',
      'casdoor_expires_at',
      'casdoor_refresh_token'
    ];
    
    keys.forEach(key => localStorage.removeItem(key));
    ['casdoor_state', 'casdoor_code_verifier', 'casdoor_redirect_back'].forEach(
      key => sessionStorage.removeItem(key)
    );
    
    console.log('✓ 已清空认证数据。请刷新页面重新登录。');
    
    if (window.AUTH && typeof AUTH.updateAuthUI === 'function') {
      AUTH.updateAuthUI();
    }
  },
  
  /**
   * 测试登录流程
   */
  async testLoginFlow() {
    console.log('%c开始测试登录流程...', 'color: #1890ff; font-weight: bold;');
    
    if (!window.AUTH || typeof AUTH.login !== 'function') {
      console.error('✗ AUTH 模块未加载或不可用');
      return;
    }
    
    console.log('1️⃣ 保存当前页面 URL');
    console.log('2️⃣ 将启动登录流程...');
    console.log('3️⃣ 您将被重定向到 Casdoor');
    console.log('4️⃣ 登录后将返回 callback.html');
    console.log('5️⃣ 然后自动跳转回首页');
    
    console.log('\n开始登录...');
    AUTH.login();
  },
  
  /**
   * 获取完整的诊断报告（文本格式）
   */
  getFullReport() {
    const report = [];
    report.push('=== 国学课堂认证诊断报告 ===');
    report.push('生成时间: ' + new Date().toLocaleString('zh-CN'));
    report.push('');
    report.push('环境信息:');
    report.push('  URL: ' + window.location.href);
    report.push('  浏览器: ' + navigator.userAgent);
    report.push('');
    report.push('认证状态:');
    report.push('  已登录: ' + (window.AUTH && window.AUTH.isLoggedIn ? window.AUTH.isLoggedIn() : 'unknown'));
    report.push('  Token: ' + (localStorage.getItem('casdoor_access_token') ? '已保存' : '未保存'));
    report.push('');
    report.push('更多帮助: 查看 LOGIN_TROUBLESHOOTING.md');
    
    return report.join('\n');
  }
};

// 自动在页面加载时注册快捷命令
if (window.console && typeof window.console.log === 'function') {
  console.log('%c💡 提示：在 Console 中运行以下命令进行诊断', 'color: #faad14; font-weight: bold;');
  console.log('%cAUTH_DEBUG.runDiagnostics()  %c// 运行完整诊断', 'color: #1890ff; font-weight: bold;', 'color: #999;');
  console.log('%cAUTH_DEBUG.clearAuth()      %c// 清空认证数据', 'color: #1890ff; font-weight: bold;', 'color: #999;');
  console.log('%cAUTH_DEBUG.testLoginFlow()  %c// 测试登录流程', 'color: #1890ff; font-weight: bold;', 'color: #999;');
}
