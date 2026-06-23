/**
 * auth.js — 国学课堂 Casdoor OAuth2 PKCE 登录模块
 * 
 * 依赖: 无（纯原生 JS, 含内置 SHA-256 回退, 无需 HTTPS）
 * 用法：在页面中引入 <script src="assets/js/auth.js" defer></script>
 *       在导航栏中添加 <div id="auth-nav"></div> 作为登录按钮的挂载点
 */

const AUTH = (function() {
  "use strict";

  // ============ 配置 ============
  const CONFIG = {
    serverUrl: "https://guoxue.8023laozhanshi.cc",
    clientId: "16891ab8fba3b3416919",
    scope: "openid profile email",
    authorizeEndpoint: "/login/oauth/authorize",
    tokenEndpoint: "/api/login/oauth/access_token",
    userinfoEndpoint: "/api/userinfo",
    logoutEndpoint: "/logout",
  };

  // ============ PKCE 工具 ============

  // 生成随机字符串
  function randomString(len) {
    const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_";
    const array = new Uint8Array(len);
    crypto.getRandomValues(array);
    let result = "";
    for (let i = 0; i < len; i++) {
      result += chars[array[i] & 0x3f];
    }
    return result;
  }

  // Base64URL 编码
  function base64URLEncode(bytes) {
    let binary = "";
    for (let i = 0; i < bytes.byteLength; i++) {
      binary += String.fromCharCode(bytes[i]);
    }
    return btoa(binary)
      .replace(/\+/g, "-")
      .replace(/\//g, "_")
      .replace(/=+$/, "");
  }

  // SHA-256 (Web Crypto API, 需要 HTTPS/localhost)
  async function sha256WebCrypto(verifier) {
    const encoder = new TextEncoder();
    const data = encoder.encode(verifier);
    const digest = await crypto.subtle.digest("SHA-256", data);
    return new Uint8Array(digest);
  }

  // ============ 纯 JS SHA-256 回退 (兼容 HTTP) ============
  function sha256Fallback(str) {
    function rrot(v, b) { return (v >>> b) | (v << (32 - b)); }
    const K = [
      0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
      0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
      0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
      0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
      0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
      0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
      0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
      0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2,
    ];
    let H = [0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
    const enc = unescape(encodeURIComponent(str));
    const buf = [];
    for (let i = 0; i < enc.length; i++) buf.push(enc.charCodeAt(i));
    const bitLen = buf.length * 8;
    buf.push(0x80);
    while ((buf.length * 8) % 512 !== 448) buf.push(0);
    for (let i = 56; i >= 0; i -= 8) buf.push((bitLen >>> i) & 0xff);
    for (let i = 0; i < buf.length; i += 64) {
      const w = new Array(64);
      for (let j = 0; j < 16; j++)
        w[j] = (buf[i+j*4]<<24)|(buf[i+j*4+1]<<16)|(buf[i+j*4+2]<<8)|buf[i+j*4+3];
      for (let j = 16; j < 64; j++) {
        const s0 = rrot(w[j-15],7)^rrot(w[j-15],18)^(w[j-15]>>>3);
        const s1 = rrot(w[j-2],17)^rrot(w[j-2],19)^(w[j-2]>>>10);
        w[j] = (w[j-16] + s0 + w[j-7] + s1) >>> 0;
      }
      let [a,b,c,d,e,f,g,h] = H;
      for (let j = 0; j < 64; j++) {
        const S1 = rrot(e,6)^rrot(e,11)^rrot(e,25);
        const ch = (e&f)^((~e)&g);
        const t1 = (h + S1 + ch + K[j] + w[j]) >>> 0;
        const S0 = rrot(a,2)^rrot(a,13)^rrot(a,22);
        const maj = (a&b)^(a&c)^(b&c);
        const t2 = (S0 + maj) >>> 0;
        h=g; g=f; f=e; e=(d+t1)>>>0; d=c; c=b; b=a; a=(t1+t2)>>>0;
      }
      H = [(H[0]+a)>>>0,(H[1]+b)>>>0,(H[2]+c)>>>0,(H[3]+d)>>>0,
           (H[4]+e)>>>0,(H[5]+f)>>>0,(H[6]+g)>>>0,(H[7]+h)>>>0];
    }
    const out = new Uint8Array(32);
    for (let i = 0; i < 8; i++) {
      out[i*4] = (H[i] >>> 24) & 0xff;
      out[i*4+1] = (H[i] >>> 16) & 0xff;
      out[i*4+2] = (H[i] >>> 8) & 0xff;
      out[i*4+3] = H[i] & 0xff;
    }
    return out;
  }

  // ============ 生成 PKCE code_challenge (自动回退) ============
  async function generateCodeChallenge(verifier) {
    try {
      return base64URLEncode(await sha256WebCrypto(verifier));
    } catch (e) {
      console.warn("[Auth] Web Crypto 不可用, 使用 JS 回退 (HTTP 环境)", e.message);
      return base64URLEncode(sha256Fallback(verifier));
    }
  }

  // ============ 核心方法 ============

  /**
   * 登录：打开邮箱登录弹窗
   */
  function login() {
    try {
      localStorage.setItem("casdoor_redirect_back", window.location.href);
      if (typeof window.showLoginModal === 'function') {
        window.showLoginModal();
      } else {
        console.error("[Auth] auth-email.js 未加载");
      }
    } catch (e) {
      console.error("[Auth] 登录失败:", e);
    }
  }

  /**
   * 处理 OAuth 回调（在 callback.html 中调用）
   */
  async function handleCallback() {
    const params = new URLSearchParams(window.location.search);
    const code = params.get("code");
    const state = params.get("state");
    const error = params.get("error");

    if (error) {
      showError("登录失败：" + error);
      return { success: false, error };
    }

    if (!code) {
      showError("没有收到授权码");
      return { success: false, error: "no_code" };
    }

    // 验证 state（防止 CSRF）
    const savedState = localStorage.getItem("casdoor_state");
    if (state && savedState && state !== savedState) {
      showError("state 不匹配，可能存在 CSRF 攻击");
      return { success: false, error: "state_mismatch" };
    }
    localStorage.removeItem("casdoor_state");

    // 获取 PKCE verifier
    const verifier = localStorage.getItem("casdoor_code_verifier");
    if (!verifier) {
      showError("找不到 PKCE verifier，请重新登录");
      return { success: false, error: "no_verifier" };
    }
    localStorage.removeItem("casdoor_code_verifier");

    // 交换授权码获取 Token
    const redirectUri = getRedirectUri();
    const tokenUrl = CONFIG.serverUrl + CONFIG.tokenEndpoint;
    const body = new URLSearchParams({
      grant_type: "authorization_code",
      code: code,
      redirect_uri: redirectUri,
      client_id: CONFIG.clientId,
      code_verifier: verifier,
    });

    try {
      const resp = await fetch(tokenUrl, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: body.toString(),
      });

      if (!resp.ok) {
        const errText = await resp.text();
        showError("获取 Token 失败: HTTP " + resp.status + " - " + errText);
        return { success: false, error: errText };
      }

      const tokenData = await resp.json();

      // 校验：服务器正常响应但 access_token 为空（如账号被禁）
      if (!tokenData.access_token) {
        const serverMsg = tokenData.msg || tokenData.error || "服务器未返回 access_token";
        showError("Token 无效: " + serverMsg);
        return { success: false, error: serverMsg };
      }

      localStorage.setItem("casdoor_access_token", tokenData.access_token);
      localStorage.setItem("casdoor_id_token", tokenData.id_token || "");
      localStorage.setItem("casdoor_token_type", tokenData.token_type || "Bearer");
      if (tokenData.expires_in) {
        localStorage.setItem("casdoor_expires_at", String(Date.now() + tokenData.expires_in * 1000));
      } else {
        // 无过期信息时设默认 24 小时，避免 expiresAt=0 导致的 bug
        localStorage.setItem("casdoor_expires_at", String(Date.now() + 86400000));
      }
      if (tokenData.refresh_token) {
        localStorage.setItem("casdoor_refresh_token", tokenData.refresh_token);
      }

      // ===== 登录成功，同步用户到 Supabase（不阻塞返回） =====
      if (typeof window !== 'undefined' && window.SUPABASE && window.SUPABASE.syncUser) {
        setTimeout(function() {
          window.SUPABASE.syncUser().then(function() {
            console.log('[Auth] 用户已同步到 Supabase');
            window.dispatchEvent(new CustomEvent('auth:user-synced'));
          }).catch(function(err) {
            console.warn('[Auth] Supabase 同步失败（非致命）:', err);
          });
        }, 100);
      }

      return { success: true, tokenData };
    } catch (err) {
      showError("网络错误: " + err.message);
      return { success: false, error: err.message };
    }
  }

  /**
   * 获取用户信息
   */
  async function getUserInfo() {
    const token = getAccessToken();
    if (!token) return null;

    try {
      const resp = await fetch(CONFIG.serverUrl + CONFIG.userinfoEndpoint, {
        headers: {
          Authorization: "Bearer " + token,
        },
      });
      if (!resp.ok) return null;
      return await resp.json();
    } catch {
      return null;
    }
  }

  /**
   * 从 ID Token 中解析基本信息（无需网络请求）
   */
  function parseIdToken() {
    const idToken = localStorage.getItem("casdoor_id_token");
    if (!idToken) return null;
    try {
      const parts = idToken.split(".");
      if (parts.length !== 3) return null;
      const payload = JSON.parse(atob(parts[1].replace(/-/g, "+").replace(/_/g, "/")));
      return {
        sub: payload.sub,
        name: payload.name || payload.preferred_username || payload.sub,
        email: payload.email || "",
        avatar: payload.picture || "",
      };
    } catch {
      return null;
    }
  }

  /**
   * 内部：清除所有认证相关的 localStorage key
   * 包含 Casdoor OAuth、邮件登录、微信 OAuth 三条路径写入的全部 key。
   */
  function _clearTokens() {
    [
      // Casdoor / 邮件 JWT token
      "casdoor_access_token", "casdoor_id_token", "casdoor_token_type",
      "casdoor_expires_at",   "casdoor_refresh_token",
      // 邮件登录写入的用户信息
      "guoxue_token", "guoxue_username", "guoxue_email",
      // WeChat / Casdoor OAuth 写入的用户信息（callback.html 设置）
      "casdoor_user_name", "casdoor_user_avatar",
    ].forEach(k => localStorage.removeItem(k));
  }

  /**
   * 获取 access token
   *
   * 修复：原代码 expiresAt=0 时 Date.now()>0 永远为 true，
   * 导致每次调用都执行 logout() 清空刚保存的 token。
   * 现在：仅当 expiresAt>0 且已过期时才清除。
   */
  function getAccessToken() {
    const token = localStorage.getItem("casdoor_access_token");
    if (!token) return null;
    const expiresAt = parseInt(localStorage.getItem("casdoor_expires_at") || "0", 10);
    // expiresAt=0 表示无过期信息（邮件登录默认值），视为有效
    if (expiresAt > 0 && Date.now() > expiresAt) {
      _clearTokens();
      updateAuthUI();
      return null;
    }
    return token;
  }

  /**
   * 判断是否已登录
   *
   * 修复：原代码 expiresAt=0 时 Date.now()<0 永远为 false，
   * 导致登录成功后用户状态始终显示未登录。
   * 现在：expiresAt=0 表示无过期限制，只要有 token 即视为已登录。
   */
  function isLoggedIn() {
    const token = localStorage.getItem("casdoor_access_token");
    if (!token) return false;
    const expiresAt = parseInt(localStorage.getItem("casdoor_expires_at") || "0", 10);
    // expiresAt=0 → 无过期信息 → 视为有效
    if (expiresAt === 0) return true;
    return Date.now() < expiresAt;
  }

  /**
   * 退出登录：清除所有本地 token。
   * 邮件验证码登录使用无状态 JWT，无需服务端 session 失效，
   * 直接清除本地存储即可完成登录态注销。
   */
  function logout() {
    _clearTokens();
    updateAuthUI();
  }

  // ============ UI 相关 ============

  function getRedirectUri() {
    return window.location.origin + "/callback.html";
  }

  function showError(msg) {
    const el = document.getElementById("auth-error");
    if (el) {
      el.textContent = msg;
      el.style.display = "block";
    }
    console.error("[Auth]", msg);
  }

  /**
   * 更新导航栏中的登录/用户按钮
   */
  function updateAuthUI() {
    const container = document.getElementById("auth-nav");
    if (!container) return;

    if (isLoggedIn()) {
      const user = parseIdToken();
      const displayName = (user && user.name) ? user.name
        : localStorage.getItem("guoxue_username") || "用户";
      const initial = displayName.charAt(0).toUpperCase();
      // 对 displayName 做 HTML 转义，防止 XSS（名称含 < > " 等字符时）
      const safeName = displayName
        .replace(/&/g, "&amp;").replace(/</g, "&lt;")
        .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
      container.innerHTML = [
        '<div class="auth-user-dropdown">',
        '  <button class="ds-btn-nav auth-user-btn" id="auth-user-btn"',
        '    aria-haspopup="true" aria-expanded="false" title="' + safeName + '">',
        '    <span class="auth-avatar">' + initial + '</span>',
        '    <span class="auth-name">' + safeName + '</span>',
        '  </button>',
        '  <div class="auth-dropdown-menu" id="auth-dropdown-menu" hidden role="menu">',
        '    <a class="auth-dropdown-item" href="/dashboard.html" role="menuitem">📊 学习面板</a>',
        '    <a class="auth-dropdown-item" href="/notes.html" role="menuitem">📝 笔记书签</a>',
        '    <div class="auth-dropdown-divider"></div>',
        '    <a class="auth-dropdown-item auth-dropdown-item--danger" href="#"',
        '       id="auth-logout-btn" role="menuitem">退出登录</a>',
        '  </div>',
        '</div>',
      ].join("");

      const logoutBtn = document.getElementById("auth-logout-btn");
      if (logoutBtn) {
        logoutBtn.addEventListener("click", function(e) { e.preventDefault(); logout(); });
      }
      const userBtn = document.getElementById("auth-user-btn");
      const dropdown = document.getElementById("auth-dropdown-menu");
      if (userBtn && dropdown) {
        userBtn.addEventListener("click", function(e) {
          e.stopPropagation();
          const open = !dropdown.hidden;
          dropdown.hidden = open;
          userBtn.setAttribute("aria-expanded", String(!open));
        });
        document.addEventListener("click", function() {
          if (dropdown && !dropdown.hidden) {
            dropdown.hidden = true;
            userBtn && userBtn.setAttribute("aria-expanded", "false");
          }
        });
        dropdown.addEventListener("click", function(e) { e.stopPropagation(); });
        // ESC 关闭
        document.addEventListener("keydown", function(e) {
          if (e.key === "Escape" && !dropdown.hidden) {
            dropdown.hidden = true;
            userBtn && userBtn.setAttribute("aria-expanded", "false");
            userBtn && userBtn.focus();
          }
        });
      }
    } else {
      container.innerHTML = [
        '<div class="auth-login-container">',
        '  <button class="ds-btn-nav auth-login-btn" id="auth-login-btn">登录 / 注册</button>',
        '</div>',
      ].join("");
      const loginBtn = document.getElementById("auth-login-btn");
      if (loginBtn) {
        loginBtn.addEventListener("click", function(e) { e.preventDefault(); login(); });
      }
    }
  }

  /**
   * 初始化：更新 UI + 静默检查登录状态
   */
  function init() {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", () => {
        updateAuthUI();
      });
    } else {
      updateAuthUI();
    }
  }

  // ============ 导出公共 API ============
  return {
    init: init,
    login: login,
    logout: logout,
    handleCallback: handleCallback,
    getUserInfo: getUserInfo,
    isLoggedIn: isLoggedIn,
    getAccessToken: getAccessToken,
    parseIdToken: parseIdToken,
    updateAuthUI: updateAuthUI,
  };
})();

// 自动初始化
AUTH.init();
