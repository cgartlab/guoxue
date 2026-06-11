/**
 * Guoxue Supabase Schema
 * 为国学课堂项目创建完整的数据库表结构
 * 
 * 使用说明：
 * 1. 在 Supabase SQL 编辑器中打开此文件
 * 2. 点击"运行"执行所有 SQL 命令
 * 3. 按顺序执行 02-rls.sql、03-functions.sql（如果有）
 */

-- ============================================================
-- 1. 启用 UUID 扩展
-- ============================================================
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ============================================================
-- 2. 用户表（从 Casdoor 同步）
-- ============================================================
CREATE TABLE IF NOT EXISTS public.users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  casdoor_id TEXT UNIQUE NOT NULL,  -- 来自 Casdoor sub claim
  username TEXT,
  email TEXT UNIQUE,
  full_name TEXT,
  avatar_url TEXT,
  user_type TEXT CHECK (user_type IN ('student', 'parent', 'teacher', 'admin')) DEFAULT 'student',
  bio TEXT,  -- 个人签名
  locale TEXT DEFAULT 'zh-CN',  -- 语言设置
  
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 创建索引加速查询
CREATE INDEX idx_users_casdoor_id ON public.users(casdoor_id);
CREATE INDEX idx_users_email ON public.users(email);
CREATE INDEX idx_users_user_type ON public.users(user_type);

-- ============================================================
-- 3. 学习进度表
-- ============================================================
CREATE TABLE IF NOT EXISTS public.study_progress (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
  course_id TEXT NOT NULL,  -- 例如 '01-lunyu', '02-sanzijing'
  
  current_page INT DEFAULT 0,  -- 当前页数（0-indexed）
  total_pages INT DEFAULT 0,   -- 课程总页数
  
  quiz_answered JSONB DEFAULT '{}'::jsonb,  -- { "0": true, "1": false, "2": true, ... }
  quiz_score FLOAT DEFAULT 0,  -- 最终测试成绩（0-100）
  
  completed BOOLEAN DEFAULT FALSE,
  completed_at TIMESTAMP WITH TIME ZONE,
  
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  
  UNIQUE(user_id, course_id)
);

CREATE INDEX idx_study_progress_user_id ON public.study_progress(user_id);
CREATE INDEX idx_study_progress_course_id ON public.study_progress(course_id);
CREATE INDEX idx_study_progress_user_course ON public.study_progress(user_id, course_id);

-- ============================================================
-- 4. 学习笔记表
-- ============================================================
CREATE TABLE IF NOT EXISTS public.study_notes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
  course_id TEXT NOT NULL,
  page INT NOT NULL,  -- 第几页
  
  title TEXT,  -- 笔记标题
  content TEXT,  -- 笔记内容（支持 Markdown）
  color_tag TEXT DEFAULT 'yellow',  -- 标签颜色: yellow, green, blue, pink, red
  
  is_public BOOLEAN DEFAULT FALSE,  -- 是否与其他学生分享
  is_pinned BOOLEAN DEFAULT FALSE,  -- 是否置顶
  
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_study_notes_user_id ON public.study_notes(user_id);
CREATE INDEX idx_study_notes_course_id ON public.study_notes(course_id);
CREATE INDEX idx_study_notes_user_course ON public.study_notes(user_id, course_id);
CREATE INDEX idx_study_notes_is_public ON public.study_notes(is_public);

-- ============================================================
-- 5. 书签表
-- ============================================================
CREATE TABLE IF NOT EXISTS public.bookmarks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
  course_id TEXT NOT NULL,
  page INT NOT NULL,
  
  note TEXT,  -- 书签备注（可选）
  color TEXT DEFAULT 'bookmark-red',  -- bookmark-red, bookmark-orange, bookmark-yellow, bookmark-green, bookmark-blue
  
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  
  UNIQUE(user_id, course_id, page)
);

CREATE INDEX idx_bookmarks_user_id ON public.bookmarks(user_id);
CREATE INDEX idx_bookmarks_course_id ON public.bookmarks(course_id);

-- ============================================================
-- 6. 测试成绩表（支持多次尝试）
-- ============================================================
CREATE TABLE IF NOT EXISTS public.quiz_scores (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
  course_id TEXT NOT NULL,
  
  score FLOAT NOT NULL CHECK (score >= 0 AND score <= 100),  -- 0-100
  correct_count INT DEFAULT 0,  -- 答对数
  total_questions INT DEFAULT 0,  -- 总题数
  attempt INT DEFAULT 1,  -- 第 N 次尝试
  
  answers JSONB DEFAULT '[]'::jsonb,  -- [{ q_idx: 0, chosen: 1, correct: 1 }, ...]
  
  completed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  
  UNIQUE(user_id, course_id, attempt)
);

CREATE INDEX idx_quiz_scores_user_id ON public.quiz_scores(user_id);
CREATE INDEX idx_quiz_scores_course_id ON public.quiz_scores(course_id);
CREATE INDEX idx_quiz_scores_best_score ON public.quiz_scores(user_id, course_id, score DESC);

-- ============================================================
-- 7. 订单表（支持 VIP/内容付费）
-- ============================================================
CREATE TABLE IF NOT EXISTS public.orders (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
  
  product_id TEXT NOT NULL,  -- 'course_bundle_1', 'vip_monthly', 'course_01-lunyu'
  product_name TEXT,
  amount_cents INT NOT NULL CHECK (amount_cents >= 0),  -- 价格（分为单位）
  
  status TEXT CHECK (status IN ('pending', 'paid', 'failed', 'cancelled')) DEFAULT 'pending',
  payment_method TEXT,  -- 'alipay', 'wechat', 'card', 'manual'
  transaction_id TEXT UNIQUE,
  
  expires_at TIMESTAMP WITH TIME ZONE,  -- 订阅过期时间（用于 VIP）
  notes TEXT,
  
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_orders_user_id ON public.orders(user_id);
CREATE INDEX idx_orders_status ON public.orders(status);
CREATE INDEX idx_orders_product_id ON public.orders(product_id);

-- ============================================================
-- 8. 学习清单（收藏夹）
-- ============================================================
CREATE TABLE IF NOT EXISTS public.study_lists (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
  
  title TEXT NOT NULL,  -- "我的高分课程", "暑假必学"
  description TEXT,
  icon TEXT DEFAULT '📚',  -- Emoji 图标
  
  is_public BOOLEAN DEFAULT FALSE,  -- 是否公开分享
  sort_order INT DEFAULT 0,  -- 排序
  
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_study_lists_user_id ON public.study_lists(user_id);

-- ============================================================
-- 9. 学习清单项目
-- ============================================================
CREATE TABLE IF NOT EXISTS public.study_list_items (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  list_id UUID NOT NULL REFERENCES public.study_lists(id) ON DELETE CASCADE,
  course_id TEXT NOT NULL,
  
  sort_order INT DEFAULT 0,
  added_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_study_list_items_list_id ON public.study_list_items(list_id);

-- ============================================================
-- 10. 学习成就徽章（后续功能）
-- ============================================================
CREATE TABLE IF NOT EXISTS public.achievements (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
  
  badge_id TEXT NOT NULL,  -- 'first_lesson', 'all_perfect', 'share_master'
  badge_name TEXT,
  badge_icon TEXT,  -- Emoji 或 URL
  badge_description TEXT,
  
  unlocked_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  
  UNIQUE(user_id, badge_id)
);

CREATE INDEX idx_achievements_user_id ON public.achievements(user_id);

-- ============================================================
-- 11. 学习日志表（用于分析用户行为）
-- ============================================================
CREATE TABLE IF NOT EXISTS public.study_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
  course_id TEXT,
  
  action TEXT NOT NULL,  -- 'open_course', 'complete_page', 'submit_quiz', 'leave_note'
  metadata JSONB DEFAULT '{}'::jsonb,  -- 额外数据
  
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_study_logs_user_id ON public.study_logs(user_id);
CREATE INDEX idx_study_logs_created_at ON public.study_logs(created_at);

-- ============================================================
-- 12. 家长-学生关系表（用于家长端）
-- ============================================================
CREATE TABLE IF NOT EXISTS public.parent_student_relations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  parent_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
  student_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
  
  relationship TEXT,  -- '父亲', '母亲', '爷爷', '奶奶', '其他'
  verified BOOLEAN DEFAULT FALSE,
  verification_code TEXT,  -- 家长验证码
  
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  
  UNIQUE(parent_id, student_id)
);

CREATE INDEX idx_parent_student_relations_parent ON public.parent_student_relations(parent_id);
CREATE INDEX idx_parent_student_relations_student ON public.parent_student_relations(student_id);

-- ============================================================
-- 13. 更新时间触发器（自动更新 updated_at）
-- ============================================================
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 为所有需要的表创建触发器
CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON public.users
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_study_progress_updated_at BEFORE UPDATE ON public.study_progress
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_study_notes_updated_at BEFORE UPDATE ON public.study_notes
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_study_lists_updated_at BEFORE UPDATE ON public.study_lists
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_orders_updated_at BEFORE UPDATE ON public.orders
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_parent_student_relations_updated_at BEFORE UPDATE ON public.parent_student_relations
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- ============================================================
-- 完成！现在请执行下一个脚本：02-rls.sql
-- ============================================================
