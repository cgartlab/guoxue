const API_BASE = 'https://guoxue.8023laozhanshi.cc/api';

function setAuthToken(token, username) {
  localStorage.setItem('guoxue_token', token);
  localStorage.setItem('guoxue_username', username);
  localStorage.setItem('casdoor_access_token', token);
  // 始终设置过期时间，避免 expiresAt=0 导致 isLoggedIn() 永远返回 false
  // 优先从 JWT payload.exp 取，否则默认 24 小时
  let expiresAt = Date.now() + 86400000; // fallback: 24h
  try {
    const parts = token.split('.');
    if (parts.length === 3) {
      const payload = JSON.parse(atob(parts[1].replace(/-/g, '+').replace(/_/g, '/')));
      if (payload.exp && payload.exp > 0) {
        expiresAt = payload.exp * 1000;
      }
    }
  } catch (e) { /* ignore, use fallback */ }
  localStorage.setItem('casdoor_expires_at', String(expiresAt));
}

const MODAL_HTML = `
<style>
.modal-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: oklch(0 0 0 / 0.4);
  z-index: 9999;
  align-items: center;
  justify-content: center;
  padding: var(--ds-space-4);
  font-family: var(--ds-font-body);
}
.modal-overlay.open {
  display: flex;
}
.modal-dialog {
  background: var(--ds-color-surface);
  border-radius: var(--ds-radius-xl);
  box-shadow: var(--ds-shadow-lg);
  width: 100%;
  max-width: 420px;
  padding: var(--ds-space-8);
  position: relative;
  animation: modal-in var(--ds-duration-300) var(--ds-ease-out);
}
@keyframes modal-in {
  from { opacity: 0; transform: scale(0.95) translateY(8px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}
.modal-close {
  position: absolute;
  top: var(--ds-space-4);
  right: var(--ds-space-4);
  background: none;
  border: none;
  cursor: pointer;
  color: var(--ds-color-muted);
  font-size: 20px;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--ds-radius-md);
  transition: background var(--ds-duration-150);
}
.modal-close:hover {
  background: var(--ds-color-bg-hover);
  color: var(--ds-color-fg);
}
.modal-title {
  text-align: center;
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--ds-color-fg-strong);
  margin-bottom: var(--ds-space-6);
}
.modal-tabs {
  display: flex;
  gap: 0;
  background: var(--ds-color-bg);
  border-radius: var(--ds-radius-lg);
  padding: 3px;
  margin-bottom: var(--ds-space-6);
}
.modal-tab {
  flex: 1;
  padding: var(--ds-space-2) var(--ds-space-4);
  border: none;
  background: transparent;
  cursor: pointer;
  border-radius: calc(var(--ds-radius-lg) - 2px);
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--ds-color-muted);
  transition: all var(--ds-duration-150);
  font-family: inherit;
}
.modal-tab.active {
  background: var(--ds-color-surface);
  color: var(--ds-color-fg-strong);
  box-shadow: var(--ds-shadow-sm);
}
.form-group {
  margin-bottom: var(--ds-space-4);
}
.form-label {
  display: block;
  font-size: 0.8125rem;
  font-weight: 500;
  color: var(--ds-color-fg);
  margin-bottom: var(--ds-space-2);
}
.form-input {
  width: 100%;
  padding: var(--ds-space-3) var(--ds-space-4);
  border: 1.5px solid var(--ds-color-border);
  border-radius: var(--ds-radius-lg);
  font-size: 0.9375rem;
  font-family: inherit;
  color: var(--ds-color-fg);
  background: var(--ds-color-surface);
  transition: border-color var(--ds-duration-150), box-shadow var(--ds-duration-150);
  outline: none;
}
.form-input:focus {
  border-color: var(--ds-accent);
  box-shadow: 0 0 0 3px var(--ds-accent-soft);
}
.form-input.error {
  border-color: var(--ds-color-error);
}
.form-row {
  display: flex;
  gap: var(--ds-space-3);
}
.form-row .form-group {
  flex: 1;
}
.btn-send {
  width: 100%;
  padding: var(--ds-space-3);
  background: var(--ds-accent-soft);
  color: var(--ds-accent);
  border: none;
  border-radius: var(--ds-radius-lg);
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  font-family: inherit;
  transition: all var(--ds-duration-150);
  white-space: nowrap;
}
.btn-send:hover:not(:disabled) {
  background: var(--ds-accent);
  color: var(--ds-color-on-accent);
}
.btn-send:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.btn-submit {
  width: 100%;
  padding: var(--ds-space-3) var(--ds-space-4);
  background: var(--ds-accent);
  color: var(--ds-color-on-accent);
  border: none;
  border-radius: var(--ds-radius-lg);
  font-size: 0.9375rem;
  font-weight: 600;
  cursor: pointer;
  font-family: inherit;
  transition: all var(--ds-duration-150);
}
.btn-submit:hover:not(:disabled) {
  background: var(--ds-accent-hover);
}
.btn-submit:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.error-msg {
  color: var(--ds-color-error);
  font-size: 0.8125rem;
  margin-top: var(--ds-space-2);
  display: none;
}
.error-msg.visible {
  display: block;
}
.form-section {
  display: none;
}
.form-section.active {
  display: block;
}
.success-msg {
  text-align: center;
  color: var(--ds-color-success);
  font-size: 0.875rem;
  margin-top: var(--ds-space-3);
  display: none;
}
.success-msg.visible {
  display: block;
}
</style>
<div class="modal-overlay" id="login-modal">
  <div class="modal-dialog" role="dialog" aria-modal="true" aria-labelledby="modal-title">
    <button class="modal-close" id="modal-close-btn" aria-label="关闭">×</button>
    <h2 class="modal-title" id="modal-title">登录 / 注册</h2>
    <div class="modal-tabs">
      <button class="modal-tab active" id="tab-login" type="button">登录</button>
      <button class="modal-tab" id="tab-register" type="button">注册</button>
    </div>
    <div class="form-section active" id="section-login">
      <div class="form-group">
        <label class="form-label" for="login-email">邮箱</label>
        <div class="form-row">
          <input class="form-input" id="login-email" type="email" placeholder="your@email.com" autocomplete="email" maxlength="100">
          <button class="btn-send" id="login-send-btn" type="button">发送验证码</button>
        </div>
        <div class="error-msg" id="login-email-error"></div>
      </div>
      <div class="form-group">
        <label class="form-label" for="login-code">验证码</label>
        <input class="form-input" id="login-code" type="text" placeholder="6位验证码" maxlength="6" autocomplete="one-time-code">
        <div class="error-msg" id="login-code-error"></div>
      </div>
      <button class="btn-submit" id="login-submit-btn" type="button">登录</button>
      <div class="success-msg" id="login-success"></div>
      <div class="error-msg" id="login-form-error"></div>
    </div>
    <div class="form-section" id="section-register">
      <div class="form-group">
        <label class="form-label" for="reg-email">邮箱</label>
        <div class="form-row">
          <input class="form-input" id="reg-email" type="email" placeholder="your@email.com" autocomplete="email" maxlength="100">
          <button class="btn-send" id="reg-send-btn" type="button">发送验证码</button>
        </div>
        <div class="error-msg" id="reg-email-error"></div>
      </div>
      <div class="form-group">
        <label class="form-label" for="reg-code">验证码</label>
        <input class="form-input" id="reg-code" type="text" placeholder="6位验证码" maxlength="6" autocomplete="one-time-code">
        <div class="error-msg" id="reg-code-error"></div>
      </div>
      <div class="form-group">
        <label class="form-label" for="reg-password">密码 <span style="font-weight:400;color:var(--ds-color-muted)">(至少6位)</span></label>
        <input class="form-input" id="reg-password" type="password" placeholder="设置密码" maxlength="50" autocomplete="new-password">
        <div class="error-msg" id="reg-password-error"></div>
      </div>
      <div class="form-group">
        <label class="form-label" for="reg-username">用户名 <span style="font-weight:400;color:var(--ds-color-muted)">(3-30位，字母数字下划线)</span></label>
        <input class="form-input" id="reg-username" type="text" placeholder="字母、数字、下划线" maxlength="30" autocomplete="username">
        <div class="error-msg" id="reg-username-error"></div>
      </div>
      <button class="btn-submit" id="reg-submit-btn" type="button">注册并登录</button>
      <div class="error-msg" id="reg-form-error"></div>
    </div>
  </div>
</div>
`;

document.addEventListener('DOMContentLoaded', function() {
  document.body.insertAdjacentHTML('beforeend', MODAL_HTML);

  let loginTab = document.getElementById('tab-login');
  let registerTab = document.getElementById('tab-register');
  let sectionLogin = document.getElementById('section-login');
  let sectionRegister = document.getElementById('section-register');
  let modalOverlay = document.getElementById('login-modal');
  let modalCloseBtn = document.getElementById('modal-close-btn');
  let loginSendBtn = document.getElementById('login-send-btn');
  let loginSubmitBtn = document.getElementById('login-submit-btn');
  let loginEmailInput = document.getElementById('login-email');
  let loginCodeInput = document.getElementById('login-code');
  let regSendBtn = document.getElementById('reg-send-btn');
  let regSubmitBtn = document.getElementById('reg-submit-btn');
  let regEmailInput = document.getElementById('reg-email');
  let regCodeInput = document.getElementById('reg-code');
  let regPasswordInput = document.getElementById('reg-password');
  let regUsernameInput = document.getElementById('reg-username');

  function switchTab(tab) {
    if (tab === 'login') {
      loginTab.classList.add('active');
      registerTab.classList.remove('active');
      sectionLogin.classList.add('active');
      sectionRegister.classList.remove('active');
      document.getElementById('modal-title').textContent = '登录';
    } else {
      loginTab.classList.remove('active');
      registerTab.classList.add('active');
      sectionLogin.classList.remove('active');
      sectionRegister.classList.add('active');
      document.getElementById('modal-title').textContent = '注册';
    }
    clearAllErrors();
  }

  function showError(id, msg) {
    let el = document.getElementById(id);
    if (el) { el.textContent = msg; el.classList.add('visible'); }
  }

  function showSuccess(id, msg) {
    let el = document.getElementById(id);
    if (el) { el.textContent = msg; el.classList.add('visible'); }
  }

  function clearError(id) {
    let el = document.getElementById(id);
    if (el) { el.textContent = ''; el.classList.remove('visible'); }
  }

  function clearAllErrors() {
    document.querySelectorAll('.error-msg').forEach(e => {
      e.textContent = ''; e.classList.remove('visible');
    });
    document.querySelectorAll('.success-msg').forEach(e => {
      e.textContent = ''; e.classList.remove('visible');
    });
  }

  function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  function validateUsername(username) {
    return /^[a-zA-Z0-9_]{3,30}$/.test(username);
  }

  function setSendBtnState(btn, countdown) {
    if (countdown > 0) {
      btn.disabled = true;
      btn.textContent = countdown + '秒后重发';
      let timer = setInterval(() => {
        countdown--;
        if (countdown <= 0) {
          clearInterval(timer);
          btn.disabled = false;
          btn.textContent = '发送验证码';
        } else {
          btn.textContent = countdown + '秒后重发';
        }
      }, 1000);
    } else {
      btn.disabled = false;
      btn.textContent = '发送验证码';
    }
  }

  async function handleSendCode(btn, email, purpose) {
    clearError(btn.id.replace('-send-btn', '') + '-email-error');
    if (!validateEmail(email)) {
      showError(btn.id.replace('-send-btn', '') + '-email-error', '请输入有效的邮箱地址');
      return;
    }
    btn.disabled = true;
    try {
      let res = await fetch(API_BASE + '/auth/email/send-code', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, purpose })
      });
      let data = await res.json();
      if (data.success) {
        setSendBtnState(btn, 60);
        showSuccess(btn.id.replace('-send-btn', '') + '-success', '验证码已发送');
      } else {
        showError(btn.id.replace('-send-btn', '') + '-email-error', data.error || '发送失败，请稍后重试');
        btn.disabled = false;
      }
    } catch (e) {
      showError(btn.id.replace('-send-btn', '') + '-email-error', '网络错误，请检查网络连接');
      btn.disabled = false;
    }
  }

  async function handleLogin() {
    clearAllErrors();
    let email = loginEmailInput.value.trim();
    let code = loginCodeInput.value.trim();
    if (!validateEmail(email)) { showError('login-email-error', '请输入有效的邮箱地址'); return; }
    if (!/^\d{6}$/.test(code)) { showError('login-code-error', '请输入6位验证码'); return; }
    loginSubmitBtn.disabled = true;
    try {
      let res = await fetch(API_BASE + '/auth/email/verify-login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, code })
      });
      let data = await res.json();
      if (data.token) {
        localStorage.setItem('guoxue_email', email);
        setAuthToken(data.token, data.username || email.split('@')[0]);
        showSuccess('login-success', '登录成功！正在跳转…');
        setTimeout(() => {
          hideLoginModal();
          let redirect = localStorage.getItem('casdoor_redirect_back') || localStorage.getItem('redirect_back') || document.location.origin;
          localStorage.removeItem('casdoor_redirect_back');
          localStorage.removeItem('redirect_back');
          document.location.href = redirect;
        }, 500);
      } else {
        showError('login-form-error', data.error || '验证码错误或已过期');
        loginSubmitBtn.disabled = false;
      }
    } catch (e) {
      showError('login-form-error', '网络错误，请检查网络连接');
      loginSubmitBtn.disabled = false;
    }
  }

  async function handleRegister() {
    clearAllErrors();
    let email = regEmailInput.value.trim();
    let code = regCodeInput.value.trim();
    let password = regPasswordInput.value;
    let username = regUsernameInput.value.trim();
    if (!validateEmail(email)) { showError('reg-email-error', '请输入有效的邮箱地址'); return; }
    if (!/^\d{6}$/.test(code)) { showError('reg-code-error', '请输入6位验证码'); return; }
    if (password.length < 6) { showError('reg-password-error', '密码至少6位'); return; }
    if (!validateUsername(username)) { showError('reg-username-error', '用户名3-30位，只能包含字母、数字、下划线'); return; }
    regSubmitBtn.disabled = true;
    try {
      let res = await fetch(API_BASE + '/auth/email/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, code, password, username })
      });
      let data = await res.json();
      if (data.token) {
        localStorage.setItem('guoxue_email', email);
        setAuthToken(data.token, username);
        showSuccess('login-success', '注册成功！正在跳转…');
        setTimeout(() => {
          hideLoginModal();
          let redirect = localStorage.getItem('casdoor_redirect_back') || localStorage.getItem('redirect_back') || document.location.origin;
          localStorage.removeItem('casdoor_redirect_back');
          localStorage.removeItem('redirect_back');
          document.location.href = redirect;
        }, 500);
      } else {
        showError('reg-form-error', data.error || '注册失败，请稍后重试');
        regSubmitBtn.disabled = false;
      }
    } catch (e) {
      showError('reg-form-error', '网络错误，请检查网络连接');
      regSubmitBtn.disabled = false;
    }
  }

  loginTab.addEventListener('click', () => switchTab('login'));
  registerTab.addEventListener('click', () => switchTab('register'));
  loginSendBtn.addEventListener('click', () => handleSendCode(loginSendBtn, loginEmailInput.value.trim(), 'login'));
  regSendBtn.addEventListener('click', () => handleSendCode(regSendBtn, regEmailInput.value.trim(), 'register'));
  loginSubmitBtn.addEventListener('click', handleLogin);
  regSubmitBtn.addEventListener('click', handleRegister);
  loginCodeInput.addEventListener('keydown', e => { if (e.key === 'Enter') handleLogin(); });
  regCodeInput.addEventListener('keydown', e => { if (e.key === 'Enter') handleRegister(); });
  regPasswordInput.addEventListener('keydown', e => { if (e.key === 'Enter') handleRegister(); });
  regUsernameInput.addEventListener('keydown', e => { if (e.key === 'Enter') handleRegister(); });
  modalCloseBtn.addEventListener('click', hideLoginModal);
  modalOverlay.addEventListener('click', e => { if (e.target === modalOverlay) hideLoginModal(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && modalOverlay.classList.contains('open')) hideLoginModal(); });

  function showLoginModal() {
    clearAllErrors();
    modalOverlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    loginEmailInput.focus();
  }

  function hideLoginModal() {
    modalOverlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  window.showLoginModal = showLoginModal;
  window.hideLoginModal = hideLoginModal;
});
