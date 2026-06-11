-- 国学课堂数据库表结构
-- 独立的数据库，与 Casdoor 的用户数据分开存储
-- 用户身份通过 Casdoor JWT 的 sub claim 关联

CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ============================================================
-- 用户表（从 Casdoor JWT 同步）
-- ============================================================
CREATE TABLE IF NOT EXISTS public.users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  casdoor_sub TEXT UNIQUE NOT NULL,   -- Casdoor JWT 的 sub claim
  username TEXT,
  full_name TEXT,
  email TEXT,
  avatar_url TEXT,
  user_type TEXT DEFAULT 'student',
  locale TEXT DEFAULT 'zh-CN',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_users_casdoor_sub ON public.users(casdoor_sub);

-- ============================================================
-- 学习进度
-- ============================================================
CREATE TABLE IF NOT EXISTS public.study_progress (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
  course_id TEXT NOT NULL,
  current_page INT DEFAULT 0,
  total_pages INT DEFAULT 0,
  quiz_answered JSONB DEFAULT '{}',
  quiz_score FLOAT DEFAULT 0,
  completed BOOLEAN DEFAULT FALSE,
  completed_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(user_id, course_id)
);

CREATE INDEX idx_progress_user ON public.study_progress(user_id);
CREATE INDEX idx_progress_course ON public.study_progress(course_id);

-- ============================================================
-- 学习笔记
-- ============================================================
CREATE TABLE IF NOT EXISTS public.study_notes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
  course_id TEXT NOT NULL,
  page INT NOT NULL,
  title TEXT DEFAULT '',
  content TEXT DEFAULT '',
  color_tag TEXT DEFAULT 'yellow',
  is_public BOOLEAN DEFAULT FALSE,
  is_pinned BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_notes_user ON public.study_notes(user_id);
CREATE INDEX idx_notes_course ON public.study_notes(course_id);

-- ============================================================
-- 书签
-- ============================================================
CREATE TABLE IF NOT EXISTS public.bookmarks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
  course_id TEXT NOT NULL,
  page INT NOT NULL,
  note TEXT DEFAULT '',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(user_id, course_id, page)
);

CREATE INDEX idx_bookmarks_user ON public.bookmarks(user_id);

-- ============================================================
-- 测验成绩
-- ============================================================
CREATE TABLE IF NOT EXISTS public.quiz_scores (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
  course_id TEXT NOT NULL,
  score FLOAT NOT NULL CHECK (score >= 0 AND score <= 100),
  correct_count INT DEFAULT 0,
  total_questions INT DEFAULT 0,
  attempt INT DEFAULT 1,
  answers JSONB DEFAULT '[]',
  completed_at TIMESTAMPTZ DEFAULT NOW(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(user_id, course_id, attempt)
);

CREATE INDEX idx_scores_user ON public.quiz_scores(user_id);
CREATE INDEX idx_scores_course ON public.quiz_scores(course_id);

-- ============================================================
-- 自动更新 updated_at
-- ============================================================
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_users_updated_at
  BEFORE UPDATE ON public.users
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER trg_progress_updated_at
  BEFORE UPDATE ON public.study_progress
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER trg_notes_updated_at
  BEFORE UPDATE ON public.study_notes
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();

-- ============================================================
-- 创建时自动同步用户函数（当 JWT sub 不存在时自动创建用户记录）
-- ============================================================
CREATE OR REPLACE FUNCTION sync_or_get_user(p_casdoor_sub TEXT, p_username TEXT DEFAULT NULL, p_full_name TEXT DEFAULT NULL, p_email TEXT DEFAULT NULL)
RETURNS UUID AS $$
DECLARE
  v_user_id UUID;
BEGIN
  INSERT INTO public.users (casdoor_sub, username, full_name, email)
  VALUES (p_casdoor_sub, p_username, p_full_name, p_email)
  ON CONFLICT (casdoor_sub)
  DO UPDATE SET
    username = COALESCE(p_username, users.username),
    full_name = COALESCE(p_full_name, users.full_name),
    email = COALESCE(p_email, users.email),
    updated_at = NOW()
  RETURNING id INTO v_user_id;
  
  RETURN v_user_id;
END;
$$ LANGUAGE plpgsql;
