/**
 * Supabase 客户端模块 - 国学课堂
 * 
 * 用途：与 Supabase 后端通信，实现用户数据持久化
 * 依赖：Supabase JS 库（通过 CDN 引入）
 * 使用：在 auth.js 之后引入本文件
 * 
 * 使用说明：
 * 1. 在 HTML 中引入：<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
 * 2. 然后引入本文件
 * 3. 在代码中使用 window.SUPABASE.* 调用
 */

(function() {
  'use strict'

  // ============================================================
  // 配置
  // ============================================================
  const SUPABASE_URL = 'https://zbjdpwkcnfnrrnlwifti.supabase.co'
  const SUPABASE_ANON_KEY = 'sb_publishable_oFnI4iU_vmua5AZnVPJtCg_yX5GvkJ9'

  // 缓存用户信息和 session
  let cachedUser = null
  let cacheExpiry = 0
  const CACHE_DURATION = 5 * 60 * 1000  // 5 分钟缓存

  // ============================================================
  // 工具函数
  // ============================================================

  /**
   * 使用 Casdoor Token 调用 Supabase REST API
   */
  async function fetchSupabaseAPI(endpoint, options = {}) {
    const url = new URL(`${SUPABASE_URL}/rest/v1${endpoint}`)
    const fetchOptions = {
      method: options.method || 'GET',
      headers: {
        'apikey': SUPABASE_ANON_KEY,
        'Content-Type': 'application/json',
        'Prefer': options.prefer || ''
      }
    }

    // 添加请求体
    if (options.data) {
      fetchOptions.body = JSON.stringify(options.data)
    }

    // 添加查询参数
    if (options.params) {
      for (const [key, value] of Object.entries(options.params)) {
        url.searchParams.append(key, value)
      }
    }

    try {
      const response = await fetch(url.toString(), fetchOptions)
      
      if (response.status === 401) {
        console.error('[Supabase] Token 已过期，需要重新登录')
        return { data: null, error: 'Token expired', status: 401 }
      }

      if (!response.ok) {
        let error = `HTTP ${response.status}`
        try {
          const errorData = await response.json()
          error = errorData.message || error
        } catch {
          error = await response.text() || error
        }
        return { data: null, error, status: response.status }
      }

      // 处理空响应（DELETE 等操作）
      const contentType = response.headers.get('content-type')
      let data = null
      if (contentType && contentType.includes('application/json')) {
        data = await response.json()
      }

      return { data, error: null, status: response.status }
    } catch (error) {
      console.error('[Supabase] 网络错误:', error)
      return { data: null, error: error.message, status: 0 }
    }
  }

  /**
   * 构建 Supabase 过滤字符串
   * 例如：buildFilter({ user_id: { eq: 'xxx' }, score: { gte: 80 } })
   */
  function buildFilter(filters) {
    const parts = []
    for (const [key, conditions] of Object.entries(filters)) {
      for (const [op, value] of Object.entries(conditions)) {
        if (typeof value === 'string') {
          parts.push(`${key}=${op}.${encodeURIComponent(value)}`)
        } else {
          parts.push(`${key}=${op}.${value}`)
        }
      }
    }
    return parts.join('&')
  }

  /**
   * 构建排序字符串
   * 例如：buildOrder([{ by: 'created_at', ascending: false }])
   */
  function buildOrder(orders) {
    if (!Array.isArray(orders)) orders = [orders]
    return orders.map(o => {
      const direction = o.ascending === true ? 'asc' : 'desc'
      return `${o.by}.${direction}`
    }).join(',')
  }

  /**
   * 获取当前用户信息（带缓存）
   */
  async function getCurrentUser() {
    if (!AUTH || !AUTH.isLoggedIn || !AUTH.isLoggedIn()) {
      return null
    }

    // 检查缓存
    if (cachedUser && Date.now() < cacheExpiry) {
      return cachedUser
    }

    try {
      const idToken = AUTH.parseIdToken()
      if (!idToken) return null

      // 从数据库查找用户
      const filter = buildFilter({
        casdoor_id: { eq: idToken.sub }
      })

      const { data, error } = await fetchSupabaseAPI(`/users?${filter}&select=*`)

      if (error || !data || data.length === 0) {
        console.warn('[Supabase] 用户不存在，自动创建...')
        return await syncUserToSupabase(idToken)
      }

      cachedUser = data[0]
      cacheExpiry = Date.now() + CACHE_DURATION
      return cachedUser
    } catch (err) {
      console.error('[Supabase] 获取用户失败:', err)
      return null
    }
  }

  /**
   * 同步用户信息到 Supabase（从 Casdoor Token）
   */
  async function syncUserToSupabase(idToken) {
    if (!idToken) {
      idToken = AUTH && AUTH.parseIdToken ? AUTH.parseIdToken() : null
      if (!idToken) return null
    }

    const userData = {
      casdoor_id: idToken.sub,
      username: idToken.name || idToken.preferred_username || idToken.sub,
      email: idToken.email || null,
      full_name: idToken.name || null,
      avatar_url: idToken.picture || null,
      user_type: 'student',  // 默认值
      locale: 'zh-CN',
      updated_at: new Date().toISOString()
    }

    // 移除 null 值
    Object.keys(userData).forEach(key => {
      if (userData[key] === null) delete userData[key]
    })

    const { data, error, status } = await fetchSupabaseAPI('/users', {
      method: 'POST',
      data: userData,
      prefer: 'resolution=merge-duplicates'
    })

    if (error) {
      console.error('[Supabase] 用户同步失败:', error)
      return null
    }

    cachedUser = data && Array.isArray(data) ? data[0] : data
    cacheExpiry = Date.now() + CACHE_DURATION
    return cachedUser
  }

  // ============================================================
  // 公共 API
  // ============================================================

  window.SUPABASE = {
    // ========== 用户相关 ==========

    /**
     * 获取当前登录用户
     */
    async getUser() {
      return await getCurrentUser()
    },

    /**
     * 同步用户信息
     */
    async syncUser() {
      return await syncUserToSupabase()
    },

    // ========== 学习进度 ==========

    /**
     * 获取课程学习进度
     * @param {string} courseId - 课程 ID，例如 '01-lunyu'
     * @returns {object} 进度对象或 null
     */
    async getProgress(courseId) {
      const user = await getCurrentUser()
      if (!user) return null

      const filter = buildFilter({
        user_id: { eq: user.id },
        course_id: { eq: courseId }
      })

      const { data, error } = await fetchSupabaseAPI(`/study_progress?${filter}&select=*`)
      return data && data.length > 0 ? data[0] : null
    },

    /**
     * 保存或更新学习进度
     * @param {string} courseId - 课程 ID
     * @param {object} progressData - 进度数据
     * @returns {boolean} 是否成功
     */
    async saveProgress(courseId, progressData) {
      const user = await getCurrentUser()
      if (!user) {
        console.warn('[Supabase] 用户未登录，无法保存进度')
        return false
      }

      const data = {
        user_id: user.id,
        course_id: courseId,
        current_page: progressData.currentPage || 0,
        total_pages: progressData.totalPages || 0,
        quiz_answered: progressData.quizAnswered || {},
        quiz_score: progressData.quizScore || 0,
        updated_at: new Date().toISOString()
      }

      // 使用 upsert（如果存在则更新，否则创建）
      const { error } = await fetchSupabaseAPI('/study_progress', {
        method: 'POST',
        data: data,
        prefer: 'resolution=merge-duplicates'
      })

      if (error) {
        console.error('[Supabase] 保存进度失败:', error)
        return false
      }

      return true
    },

    /**
     * 标记课程已完成
     */
    async completeProgress(courseId) {
      const user = await getCurrentUser()
      if (!user) return false

      const filter = buildFilter({
        user_id: { eq: user.id },
        course_id: { eq: courseId }
      })

      const { error } = await fetchSupabaseAPI(`/study_progress?${filter}`, {
        method: 'PATCH',
        data: {
          completed: true,
          completed_at: new Date().toISOString(),
          updated_at: new Date().toISOString()
        }
      })

      return !error
    },

    // ========== 学习笔记 ==========

    /**
     * 获取课程的所有笔记
     */
    async getNotes(courseId) {
      const user = await getCurrentUser()
      if (!user) return []

      const filter = buildFilter({
        user_id: { eq: user.id },
        course_id: { eq: courseId }
      })

      const order = buildOrder({ by: 'is_pinned', ascending: false })
      const order2 = buildOrder({ by: 'created_at', ascending: false })

      const { data, error } = await fetchSupabaseAPI(
        `/study_notes?${filter}&select=*&order=${order},${order2}`,
        { method: 'GET' }
      )

      return !error && data ? data : []
    },

    /**
     * 创建学习笔记
     */
    async createNote(courseId, page, noteData) {
      const user = await getCurrentUser()
      if (!user) return null

      const data = {
        user_id: user.id,
        course_id: courseId,
        page: page,
        title: noteData.title || '',
        content: noteData.content || '',
        color_tag: noteData.color_tag || 'yellow',
        is_public: false,
        is_pinned: false,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString()
      }

      const { data: result, error } = await fetchSupabaseAPI('/study_notes', {
        method: 'POST',
        data: data,
        prefer: 'return=representation'
      })

      if (error) {
        console.error('[Supabase] 创建笔记失败:', error)
        return null
      }

      return result && Array.isArray(result) ? result[0] : result
    },

    /**
     * 更新笔记
     */
    async updateNote(noteId, updates) {
      const user = await getCurrentUser()
      if (!user) return false

      const filter = buildFilter({
        id: { eq: noteId },
        user_id: { eq: user.id }
      })

      updates.updated_at = new Date().toISOString()

      const { error } = await fetchSupabaseAPI(`/study_notes?${filter}`, {
        method: 'PATCH',
        data: updates
      })

      return !error
    },

    /**
     * 删除笔记
     */
    async deleteNote(noteId) {
      const user = await getCurrentUser()
      if (!user) return false

      const filter = buildFilter({
        id: { eq: noteId },
        user_id: { eq: user.id }
      })

      const { error } = await fetchSupabaseAPI(`/study_notes?${filter}`, {
        method: 'DELETE'
      })

      return !error
    },

    // ========== 书签 ==========

    /**
     * 获取课程书签
     */
    async getBookmarks(courseId) {
      const user = await getCurrentUser()
      if (!user) return []

      const filter = buildFilter({
        user_id: { eq: user.id },
        course_id: { eq: courseId }
      })

      const order = buildOrder({ by: 'page', ascending: true })

      const { data, error } = await fetchSupabaseAPI(
        `/bookmarks?${filter}&select=*&order=${order}`
      )

      return !error && data ? data : []
    },

    /**
     * 添加书签
     */
    async addBookmark(courseId, page, note = '') {
      const user = await getCurrentUser()
      if (!user) return null

      const data = {
        user_id: user.id,
        course_id: courseId,
        page: page,
        note: note,
        color: 'bookmark-blue',
        created_at: new Date().toISOString()
      }

      const { data: result, error } = await fetchSupabaseAPI('/bookmarks', {
        method: 'POST',
        data: data,
        prefer: 'return=representation'
      })

      if (error) {
        console.error('[Supabase] 添加书签失败:', error)
        return null
      }

      return result && Array.isArray(result) ? result[0] : result
    },

    /**
     * 删除书签
     */
    async removeBookmark(courseId, page) {
      const user = await getCurrentUser()
      if (!user) return false

      const filter = buildFilter({
        user_id: { eq: user.id },
        course_id: { eq: courseId },
        page: { eq: page }
      })

      const { error } = await fetchSupabaseAPI(`/bookmarks?${filter}`, {
        method: 'DELETE'
      })

      return !error
    },

    // ========== 测试成绩 ==========

    /**
     * 获取课程测试成绩历史
     */
    async getQuizScores(courseId) {
      const user = await getCurrentUser()
      if (!user) return []

      const filter = buildFilter({
        user_id: { eq: user.id },
        course_id: { eq: courseId }
      })

      const order = buildOrder({ by: 'completed_at', ascending: false })

      const { data, error } = await fetchSupabaseAPI(
        `/quiz_scores?${filter}&select=*&order=${order}`
      )

      return !error && data ? data : []
    },

    /**
     * 获取最高成绩
     */
    async getBestQuizScore(courseId) {
      const scores = await window.SUPABASE.getQuizScores(courseId)
      if (scores.length === 0) return null
      return scores.reduce((best, current) => 
        current.score > best.score ? current : best
      )
    },

    /**
     * 保存测试成绩
     */
    async saveQuizScore(courseId, score, answers) {
      const user = await getCurrentUser()
      if (!user) return null

      const correctCount = answers.filter(a => a.correct === 1).length

      const data = {
        user_id: user.id,
        course_id: courseId,
        score: Math.round(score),
        correct_count: correctCount,
        total_questions: answers.length,
        answers: answers,
        attempt: 1,  // 简化版，后续可增加多次尝试处理
        completed_at: new Date().toISOString(),
        created_at: new Date().toISOString()
      }

      const { data: result, error } = await fetchSupabaseAPI('/quiz_scores', {
        method: 'POST',
        data: data,
        prefer: 'return=representation'
      })

      if (error) {
        console.error('[Supabase] 保存成绩失败:', error)
        return null
      }

      return result && Array.isArray(result) ? result[0] : result
    },

    // ========== 学习清单 ==========

    /**
     * 获取用户的所有学习清单
     */
    async getStudyLists() {
      const user = await getCurrentUser()
      if (!user) return []

      const filter = buildFilter({
        user_id: { eq: user.id }
      })

      const { data, error } = await fetchSupabaseAPI(`/study_lists?${filter}&select=*`)

      return !error && data ? data : []
    },

    /**
     * 创建学习清单
     */
    async createStudyList(title, description = '') {
      const user = await getCurrentUser()
      if (!user) return null

      const data = {
        user_id: user.id,
        title: title,
        description: description,
        icon: '📚',
        is_public: false,
        sort_order: 0,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString()
      }

      const { data: result, error } = await fetchSupabaseAPI('/study_lists', {
        method: 'POST',
        data: data,
        prefer: 'return=representation'
      })

      return !error && result ? (Array.isArray(result) ? result[0] : result) : null
    },

    /**
     * 获取学习清单的课程
     */
    async getListItems(listId) {
      const filter = buildFilter({
        list_id: { eq: listId }
      })

      const order = buildOrder({ by: 'sort_order', ascending: true })

      const { data, error } = await fetchSupabaseAPI(
        `/study_list_items?${filter}&select=*&order=${order}`
      )

      return !error && data ? data : []
    },

    /**
     * 向清单添加课程
     */
    async addItemToList(listId, courseId) {
      const data = {
        list_id: listId,
        course_id: courseId,
        sort_order: 0,
        added_at: new Date().toISOString()
      }

      const { data: result, error } = await fetchSupabaseAPI('/study_list_items', {
        method: 'POST',
        data: data,
        prefer: 'return=representation'
      })

      return !error && result ? (Array.isArray(result) ? result[0] : result) : null
    },

    // ========== 工具方法 ==========

    /**
     * 清除缓存
     */
    clearCache() {
      cachedUser = null
      cacheExpiry = 0
    },

    /**
     * 获取 Supabase 配置（用于调试）
     */
    getConfig() {
      return {
        url: SUPABASE_URL,
        hasKey: !!SUPABASE_ANON_KEY
      }
    }
  }

  console.log('[Supabase] 客户端已加载，可使用 window.SUPABASE 调用')
})()
