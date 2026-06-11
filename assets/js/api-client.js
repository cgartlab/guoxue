/**
 * 国学课堂 API 客户端
 * 
 * 替代原来的 supabase-client.js。
 * 直接调用自建 API，不再依赖 Supabase。
 * 保持 window.SUPABASE 接口不变，现有页面无需修改。
 * 
 * 依赖：auth.js（提供 AUTH.parseIdToken()）
 * 用法：在 auth.js 之后引入本文件
 */

(function() {
  'use strict'

  const API_BASE = 'https://api.8023laozhanshi.cc'
  let cachedUser = null
  let cacheExpiry = 0
  const CACHE_DURATION = 5 * 60 * 1000

  // ─── 工具：从 localStorage 获取 JWT ──────────────────
  function getBearerToken() {
    return localStorage.getItem('casdoor_access_token')
  }

  // ─── 核心请求函数 ─────────────────────────────────────
  async function api(endpoint, options = {}) {
    const token = getBearerToken()
    if (!token) {
      return { data: null, error: 'Not logged in', status: 401 }
    }

    const url = options.params
      ? `${API_BASE}${endpoint}?${new URLSearchParams(options.params)}`
      : `${API_BASE}${endpoint}`

    try {
      const res = await fetch(url, {
        method: options.method || 'GET',
        headers: {
          'Authorization': 'Bearer ' + token,
          'Content-Type': 'application/json',
        },
        body: options.data ? JSON.stringify(options.data) : undefined,
      })

      if (res.status === 401) {
        console.warn('[API] Token 无效或已过期')
        return { data: null, error: 'Token expired', status: 401 }
      }

      if (!res.ok) {
        const err = await res.json().catch(() => ({ error: res.statusText }))
        return { data: null, error: err.error || `HTTP ${res.status}`, status: res.status }
      }

      // 204 No Content（DELETE）
      if (res.status === 204) {
        return { data: null, error: null, status: 204 }
      }

      const data = await res.json()
      return { data, error: null, status: res.status }
    } catch (err) {
      console.error('[API] 网络错误:', err)
      return { data: null, error: err.message, status: 0 }
    }
  }

  // ─── 用户同步（JWT sub → 本地数据库） ────────────────
  async function syncUser() {
    const token = getBearerToken()
    if (!token) return null

    const { data, error } = await api('/api/users/sync', { method: 'POST' })
    if (error) {
      console.error('[API] 用户同步失败:', error)
      return null
    }
    cachedUser = data
    cacheExpiry = Date.now() + CACHE_DURATION
    return data
  }

  // ─── 获取当前用户 ─────────────────────────────────────
  async function getCurrentUser() {
    if (cachedUser && Date.now() < cacheExpiry) return cachedUser

    const { data, error } = await api('/api/users/me')
    if (error) {
      if (error === 'Token expired') return null
      // 用户不存在 → 自动同步
      if (error.includes('not found')) return await syncUser()
      return null
    }
    cachedUser = data
    cacheExpiry = Date.now() + CACHE_DURATION
    return data
  }

  // ─── 暴露 window.SUPABASE ────────────────────────────
  window.SUPABASE = {
    // 用户
    async getUser() { return await getCurrentUser() },
    async syncUser() { return await syncUser() },
    clearCache() { cachedUser = null; cacheExpiry = 0 },

    // 进度
    async getProgress(courseId) {
      const { data } = await api('/api/progress/' + encodeURIComponent(courseId))
      return data
    },
    async saveProgress(courseId, progressData) {
      const { error } = await api('/api/progress', {
        method: 'POST',
        data: {
          courseId,
          currentPage: progressData.currentPage,
          totalPages: progressData.totalPages,
          quizAnswered: progressData.quizAnswered,
          quizScore: progressData.quizScore,
          completed: progressData.completed,
        },
      })
      return !error
    },
    async completeProgress(courseId) {
      const { error } = await api('/api/progress', {
        method: 'POST',
        data: { courseId, completed: true },
      })
      return !error
    },

    // 笔记
    async getNotes(courseId) {
      const { data } = await api('/api/notes')
      return courseId ? (data || []).filter(n => n.course_id === courseId) : (data || [])
    },
    async createNote(courseId, page, noteData) {
      const { data, error } = await api('/api/notes', {
        method: 'POST',
        data: { courseId, page, title: noteData.title, content: noteData.content, colorTag: noteData.color_tag },
      })
      return error ? null : data
    },
    async updateNote(noteId, updates) {
      // 简单实现：DELETE + re-INSERT
      // 完整实现需要 PATCH 路由，后续可加
      console.warn('[API] updateNote 暂未实现')
      return false
    },
    async deleteNote(noteId) {
      const { error } = await api('/api/notes/' + noteId, { method: 'DELETE' })
      return !error
    },

    // 书签
    async getBookmarks(courseId) {
      const { data } = await api('/api/bookmarks')
      return courseId ? (data || []).filter(b => b.course_id === courseId) : (data || [])
    },
    async addBookmark(courseId, page, note = '') {
      const { data, error } = await api('/api/bookmarks', {
        method: 'POST',
        data: { courseId, page, note },
      })
      return error ? null : data
    },
    async removeBookmark(courseId, page) {
      // 需要先获取 bookmark id
      const bs = await this.getBookmarks(courseId)
      const b = bs.find(x => x.page === page)
      if (!b) return false
      const { error } = await api('/api/bookmarks/' + b.id, { method: 'DELETE' })
      return !error
    },

    // 测验成绩
    async getQuizScores(courseId) {
      const { data } = await api('/api/quiz-scores')
      return courseId ? (data || []).filter(s => s.course_id === courseId) : (data || [])
    },
    async getBestQuizScore(courseId) {
      const scores = await this.getQuizScores(courseId)
      if (!scores.length) return null
      return scores.reduce((b, c) => c.score > b.score ? c : b)
    },
    async saveQuizScore(courseId, score, answers) {
      const correctCount = answers.filter(a => a.correct === 1).length
      const { error } = await api('/api/quiz-scores', {
        method: 'POST',
        data: { courseId, score, correctCount, totalQuestions: answers.length, answers },
      })
      return error ? null : { score }
    },

    // 工具
    getConfig() {
      return { url: API_BASE, mode: 'self-hosted' }
    },
  }

  console.log('[API] 客户端已加载，API:', API_BASE)
})()
