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
    serverUrl: "https://casdoor.8023laozhanshi.cc",
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
    const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~";
    const array = new Uint8Array(len);
    crypto.getRandomValues(array);
    let result = "";
    for (let i = 0; i < len; i++) {
      result += chars[array[i] % chars.length];
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
   * 登录：重定向到 Casdoor 授权页面（PKCE 流）
   */
  async function login() {
    try {
      const verifier = randomString(64);
      const challenge = await generateCodeChallenge(verifier);
      const state = randomString(32);
      const redirectUri = getRedirectUri();

      localStorage.setItem("casdoor_code_verifier", verifier);
      localStorage.setItem("casdoor_state", state);
      localStorage.setItem("casdoor_redirect_back", window.location.href);

      const params = new URLSearchParams({
        client_id: CONFIG.clientId,
        response_type: "code",
        redirect_uri: redirectUri,
        scope: CONFIG.scope,
        state: state,
        code_challenge: challenge,
        code_challenge_method: "S256",
      });

      window.location.href = CONFIG.serverUrl + "/login/oauth/authorize?" + params.toString();
    } catch (e) {
      console.error("[Auth] 登录失败:", e);
      alert("登录失败: " + (e.message || "未知错误") + "\n请检查浏览器控制台获取详细信息。");
    }
  }

  /**
   * 使用指定 Provider 登录（微信等第三方 OAuth）
   */
  async function loginWithProvider(provider) {
    try {
      const verifier = randomString(64);
      const challenge = await generateCodeChallenge(verifier);
      const state = randomString(32);
      const redirectUri = getRedirectUri();

      localStorage.setItem("casdoor_code_verifier", verifier);
      localStorage.setItem("casdoor_state", state);
      localStorage.setItem("casdoor_redirect_back", window.location.href);

      const params = new URLSearchParams({
        client_id: CONFIG.clientId,
        response_type: "code",
        redirect_uri: redirectUri,
        scope: CONFIG.scope,
        state: state,
        code_challenge: challenge,
        code_challenge_method: "S256",
        provider: provider,
      });

      window.location.href = CONFIG.serverUrl + "/login/oauth/authorize?" + params.toString();
    } catch (e) {
      console.error("[Auth] " + provider + " 登录失败:", e);
      alert(provider + " 登录失败: " + (e.message || "未知错误") + "\n请检查浏览器控制台获取详细信息。");
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
      localStorage.setItem("casdoor_access_token", tokenData.access_token || "");
      localStorage.setItem("casdoor_id_token", tokenData.id_token || "");
      localStorage.setItem("casdoor_token_type", tokenData.token_type || "Bearer");
      if (tokenData.expires_in) {
        localStorage.setItem("casdoor_expires_at", String(Date.now() + tokenData.expires_in * 1000));
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
   * 获取 access token
   */
  function getAccessToken() {
    const expiresAt = parseInt(localStorage.getItem("casdoor_expires_at") || "0", 10);
    if (Date.now() > expiresAt) {
      logout();
      return null;
    }
    return localStorage.getItem("casdoor_access_token");
  }

  /**
   * 判断是否已登录
   */
  function isLoggedIn() {
    const token = localStorage.getItem("casdoor_access_token");
    const expiresAt = parseInt(localStorage.getItem("casdoor_expires_at") || "0", 10);
    return !!token && Date.now() < expiresAt;
  }

  /**
   * 退出登录
   */
  function logout() {
    const keys = [
      "casdoor_access_token", "casdoor_id_token", "casdoor_token_type",
      "casdoor_expires_at", "casdoor_refresh_token",
    ];
    keys.forEach(k => localStorage.removeItem(k));
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
      const displayName = user && user.name ? user.name : "用户";
      container.innerHTML = [
        '<div class="auth-user-dropdown">',
        '  <button class="ds-btn-nav auth-user-btn" id="auth-user-btn" title="用户菜单">',
        '    <span class="auth-avatar">', displayName.charAt(0), '</span>',
        '    <span class="auth-name">', displayName, '</span>',
        '  </button>',
        '  <div class="auth-dropdown-menu" id="auth-dropdown-menu" hidden>',
        '    <a class="auth-dropdown-item" href="#" id="auth-logout-btn">退出登录</a>',
        '  </div>',
        '</div>',
      ].join("");
      const logoutBtn = document.getElementById("auth-logout-btn");
      if (logoutBtn) {
        logoutBtn.addEventListener("click", function(e) {
          e.preventDefault();
          logout();
        });
      }
      const userBtn = document.getElementById("auth-user-btn");
      const dropdown = document.getElementById("auth-dropdown-menu");
      if (userBtn && dropdown) {
        userBtn.addEventListener("click", function(e) {
          e.stopPropagation();
          dropdown.hidden = !dropdown.hidden;
        });
        document.addEventListener("click", function() {
          if (dropdown) dropdown.hidden = true;
        });
        dropdown.addEventListener("click", function(e) {
          e.stopPropagation();
        });
      }
    } else {
      container.innerHTML = [
        '<div class="auth-login-container">',
        '  <button class="ds-btn-nav auth-login-btn" id="auth-login-btn">登录 / 注册</button>',
        '  <button class="ds-btn-nav auth-wechat-btn" id="auth-wechat-btn" title="微信登录">',
        '    <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M8.691 2.188C3.891 2.188 0 5.476 0 9.219c0 2.093 1.164 3.75 2.578 4.889 1.395 1.116 3.031 1.946 3.031 1.946l-.703-.422s-.766.469-1.447.703C2.164 14.906 1.5 16.375 1.5 17.938 1.5 21.687 4.57 24 8.691 24c4.121 0 7.191-2.313 7.191-6.062 0-3.75-3.094-6.062-7.191-6.062-4.121 0-6.978 2.625-6.978 6.062h2.859c0-1.664.984-2.869 2.578-2.869 1.595 0 2.578 1.204 2.578 2.869 0 1.664-.984 2.869-2.578 2.869-1.594 0-2.891-1.205-2.891-2.869h-2.86c0 3.426 2.578 6.062 5.75 6.062s5.75-2.636 5.75-6.062c0-3.563-2.578-6.062-5.75-6.062-.648 0-1.223.094-1.723.238l-1.305-2.098z"/></svg>',
        '  </button>',
        '</div>',
      ].join("");
      const loginBtn = document.getElementById("auth-login-btn");
      if (loginBtn) {
        loginBtn.addEventListener("click", function(e) {
          e.preventDefault();
          login();
        });
      }
      const wechatBtn = document.getElementById("auth-wechat-btn");
      if (wechatBtn) {
        wechatBtn.addEventListener("click", function(e) {
          e.preventDefault();
          localStorage.setItem("casdoor_redirect_back", window.location.href);
          window.location.href = "/api/auth/wechat/login";
        });
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
    loginWithProvider: loginWithProvider,
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
