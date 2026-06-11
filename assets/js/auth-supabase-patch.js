/**
 * auth.js Supabase 集成补丁
 * 
 * 使用说明：
 * 1. 这是一个独立的补丁文件，不要直接修改 auth.js
 * 2. 在 HTML 中按顺序引入：auth.js → auth-supabase-patch.js → supabase-client.js
 * 3. 补丁会自动 hook auth.js 的回调函数
 * 
 * 或者，直接复制这里的代码到 auth.js 中
 */

(function() {
  'use strict'

  // 保存原有的 updateAuthUI 函数
  const originalUpdateAuthUI = AUTH.updateAuthUI

  /**
   * 登录成功后同步用户到 Supabase
   */
  async function syncUserAfterLogin() {
    // 等待 Supabase 客户端加载
    if (typeof window === 'undefined' || !window.SUPABASE) {
      console.warn('[Auth Patch] Supabase 客户端未加载，跳过用户同步')
      return
    }

    try {
      if (window.SUPABASE.syncUser) {
        const user = await window.SUPABASE.syncUser()
        console.log('[Auth Patch] 用户已同步到 Supabase:', user)
        
        // 触发自定义事件，通知其他模块用户已登录
        window.dispatchEvent(new CustomEvent('auth:user-synced', { 
          detail: { user } 
        }))
      }
    } catch (err) {
      console.warn('[Auth Patch] Supabase 同步失败（非致命）:', err)
    }
  }

  /**
   * 覆盖 AUTH.updateAuthUI，在登录/退出时触发同步
   */
  AUTH.updateAuthUI = function() {
    // 调用原有的 updateAuthUI
    originalUpdateAuthUI.call(AUTH)

    // 如果已登录，则同步到 Supabase
    if (AUTH.isLoggedIn && AUTH.isLoggedIn()) {
      setTimeout(() => {
        syncUserAfterLogin()
      }, 100)
    }
  }

  /**
   * 也在初始化时检查
   */
  const originalInit = AUTH.init

  AUTH.init = function() {
    // 调用原有的 init
    originalInit.call(AUTH)

    // 如果已登录，则同步到 Supabase
    if (AUTH.isLoggedIn && AUTH.isLoggedIn()) {
      setTimeout(() => {
        syncUserAfterLogin()
      }, 500)
    }
  }

  console.log('[Auth Patch] Supabase 集成补丁已加载')

  // 暴露同步函数供外部调用
  window.AUTH_SUPABASE = {
    syncUser: syncUserAfterLogin
  }
})()
