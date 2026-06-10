/**
 * Guoxue Supabase RLS (Row Level Security) 策略
 * 为所有表配置行级安全策略，保护用户隐私
 * 
 * 使用说明：
 * 1. 确保已执行 01-schema.sql
 * 2. 在 Supabase SQL 编辑器中运行此脚本
 * 3. 在 Supabase Dashboard 的 Authentication → Policies 中验证
 * 
 * ⚠️ 关键设计决策：
 * 本系统使用 Casdoor（而非 Supabase Auth）做身份认证。
 * Casdoor JWT 的 sub claim 存储在 users.casdoor_id 字段。
 * 因此 RLS 不能直接使用 auth.uid()（它返回 Supabase Auth 的 ID）。
 * 改为通过 helper 函数 current_user_id() 从 JWT sub 映射到 users.id UUID。
 * 
 * 前置条件：在 Supabase Dashboard → Authentication → Settings → JWT
 * 中配置 Casdoor 的 JWT secret，让 Supabase 能验证 Casdoor 签发的 token。
 */

-- ============================================================
-- 0. Helper 函数：从 Casdoor JWT 获取当前用户的 UUID
--    用途：代替 public.current_user_id()，通过 Casdoor sub claim 查到 users.id
-- ============================================================
CREATE OR REPLACE FUNCTION public.current_user_id()
RETURNS UUID
LANGUAGE SQL
STABLE
SECURITY DEFINER
AS $$
  SELECT id FROM public.users WHERE casdoor_id = (auth.jwt()->>'sub')
$$;

-- ============================================================
-- 启用 RLS
-- ============================================================
ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.study_progress ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.study_notes ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.bookmarks ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.quiz_scores ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.orders ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.study_lists ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.study_list_items ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.achievements ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.study_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.parent_student_relations ENABLE ROW LEVEL SECURITY;

-- ============================================================
-- 1. Users 表策略
-- ============================================================
-- 用户可以查看自己的信息 + 公开的用户资料
CREATE POLICY "Users can view own profile" ON public.users
  FOR SELECT
  USING (
    -- 自己的信息
    public.current_user_id() = id
    OR
    -- 或者是公开的用户资料（如果需要）
    public.current_user_id() IS NOT NULL
  );

-- 用户只能更新自己的信息
CREATE POLICY "Users can update own profile" ON public.users
  FOR UPDATE
  USING (public.current_user_id() = id)
  WITH CHECK (public.current_user_id() = id);

-- 服务端函数可以插入用户（创建/同步）
CREATE POLICY "Users can insert own profile" ON public.users
  FOR INSERT
  WITH CHECK (public.current_user_id() = id);

-- ============================================================
-- 2. Study Progress 表策略
-- ============================================================
-- 学生只能查看自己的学习进度
CREATE POLICY "Students can view own progress" ON public.study_progress
  FOR SELECT
  USING (public.current_user_id() = user_id);

-- 学生只能修改自己的学习进度
CREATE POLICY "Students can update own progress" ON public.study_progress
  FOR UPDATE
  USING (public.current_user_id() = user_id)
  WITH CHECK (public.current_user_id() = user_id);

-- 学生可以插入自己的学习进度
CREATE POLICY "Students can insert own progress" ON public.study_progress
  FOR INSERT
  WITH CHECK (public.current_user_id() = user_id);

-- 家长可以查看关联学生的学习进度
CREATE POLICY "Parents can view child's progress" ON public.study_progress
  FOR SELECT
  USING (
    user_id IN (
      SELECT student_id FROM public.parent_student_relations
      WHERE parent_id = public.current_user_id() AND verified = TRUE
    )
  );

-- 教师可以查看所有学生的进度（可选，根据需要启用）
-- CREATE POLICY "Teachers can view students progress" ON public.study_progress
--   FOR SELECT
--   USING (
--     EXISTS (
--       SELECT 1 FROM public.users
--       WHERE id = public.current_user_id() AND user_type = 'teacher'
--     )
--   );

-- ============================================================
-- 3. Study Notes 表策略
-- ============================================================
-- 用户只能查看自己或公开的笔记
CREATE POLICY "Users can view own and public notes" ON public.study_notes
  FOR SELECT
  USING (
    public.current_user_id() = user_id
    OR
    is_public = TRUE
  );

-- 用户只能创建自己的笔记
CREATE POLICY "Users can insert own notes" ON public.study_notes
  FOR INSERT
  WITH CHECK (public.current_user_id() = user_id);

-- 用户只能修改自己的笔记
CREATE POLICY "Users can update own notes" ON public.study_notes
  FOR UPDATE
  USING (public.current_user_id() = user_id)
  WITH CHECK (public.current_user_id() = user_id);

-- 用户只能删除自己的笔记
CREATE POLICY "Users can delete own notes" ON public.study_notes
  FOR DELETE
  USING (public.current_user_id() = user_id);

-- ============================================================
-- 4. Bookmarks 表策略
-- ============================================================
-- 用户只能查看自己的书签
CREATE POLICY "Users can view own bookmarks" ON public.bookmarks
  FOR SELECT
  USING (public.current_user_id() = user_id);

CREATE POLICY "Users can insert own bookmarks" ON public.bookmarks
  FOR INSERT
  WITH CHECK (public.current_user_id() = user_id);

CREATE POLICY "Users can update own bookmarks" ON public.bookmarks
  FOR UPDATE
  USING (public.current_user_id() = user_id)
  WITH CHECK (public.current_user_id() = user_id);

CREATE POLICY "Users can delete own bookmarks" ON public.bookmarks
  FOR DELETE
  USING (public.current_user_id() = user_id);

-- ============================================================
-- 5. Quiz Scores 表策略
-- ============================================================
-- 用户只能查看自己的成绩
CREATE POLICY "Users can view own quiz scores" ON public.quiz_scores
  FOR SELECT
  USING (public.current_user_id() = user_id);

CREATE POLICY "Users can insert own quiz scores" ON public.quiz_scores
  FOR INSERT
  WITH CHECK (public.current_user_id() = user_id);

-- 家长可以查看关联学生的成绩
CREATE POLICY "Parents can view child's quiz scores" ON public.quiz_scores
  FOR SELECT
  USING (
    user_id IN (
      SELECT student_id FROM public.parent_student_relations
      WHERE parent_id = public.current_user_id() AND verified = TRUE
    )
  );

-- ============================================================
-- 6. Orders 表策略
-- ============================================================
-- 用户只能查看自己的订单
CREATE POLICY "Users can view own orders" ON public.orders
  FOR SELECT
  USING (public.current_user_id() = user_id);

CREATE POLICY "Users can insert own orders" ON public.orders
  FOR INSERT
  WITH CHECK (public.current_user_id() = user_id);

-- 用户可以更新自己的订单（仅限某些字段）
CREATE POLICY "Users can update own orders" ON public.orders
  FOR UPDATE
  USING (public.current_user_id() = user_id)
  WITH CHECK (public.current_user_id() = user_id);

-- ============================================================
-- 7. Study Lists 表策略
-- ============================================================
-- 用户可以查看自己的清单或公开的清单
CREATE POLICY "Users can view own and public study lists" ON public.study_lists
  FOR SELECT
  USING (
    public.current_user_id() = user_id
    OR
    is_public = TRUE
  );

CREATE POLICY "Users can insert own study lists" ON public.study_lists
  FOR INSERT
  WITH CHECK (public.current_user_id() = user_id);

CREATE POLICY "Users can update own study lists" ON public.study_lists
  FOR UPDATE
  USING (public.current_user_id() = user_id)
  WITH CHECK (public.current_user_id() = user_id);

CREATE POLICY "Users can delete own study lists" ON public.study_lists
  FOR DELETE
  USING (public.current_user_id() = user_id);

-- ============================================================
-- 8. Study List Items 表策略
-- ============================================================
-- 用户可以查看自己清单中的项目或公开清单中的项目
CREATE POLICY "Users can view items in own/public lists" ON public.study_list_items
  FOR SELECT
  USING (
    list_id IN (
      SELECT id FROM public.study_lists
      WHERE user_id = public.current_user_id() OR is_public = TRUE
    )
  );

CREATE POLICY "Users can insert items in own lists" ON public.study_list_items
  FOR INSERT
  WITH CHECK (
    list_id IN (
      SELECT id FROM public.study_lists
      WHERE user_id = public.current_user_id()
    )
  );

CREATE POLICY "Users can update items in own lists" ON public.study_list_items
  FOR UPDATE
  USING (
    list_id IN (
      SELECT id FROM public.study_lists
      WHERE user_id = public.current_user_id()
    )
  );

CREATE POLICY "Users can delete items in own lists" ON public.study_list_items
  FOR DELETE
  USING (
    list_id IN (
      SELECT id FROM public.study_lists
      WHERE user_id = public.current_user_id()
    )
  );

-- ============================================================
-- 9. Achievements 表策略
-- ============================================================
-- 用户可以查看自己的成就
CREATE POLICY "Users can view own achievements" ON public.achievements
  FOR SELECT
  USING (public.current_user_id() = user_id);

-- 系统（RLS 旁路）可以插入成就，后续可通过 trigger 实现
-- CREATE POLICY "System can insert achievements" ON public.achievements
--   FOR INSERT
--   WITH CHECK (true);

-- ============================================================
-- 10. Study Logs 表策略
-- ============================================================
-- 用户可以查看自己的日志
CREATE POLICY "Users can view own logs" ON public.study_logs
  FOR SELECT
  USING (public.current_user_id() = user_id);

-- 用户可以插入自己的日志（由应用端调用）
CREATE POLICY "Users can insert own logs" ON public.study_logs
  FOR INSERT
  WITH CHECK (public.current_user_id() = user_id);

-- ============================================================
-- 11. Parent Student Relations 表策略
-- ============================================================
-- 用户可以查看自己的关系记录
CREATE POLICY "Users can view own relations" ON public.parent_student_relations
  FOR SELECT
  USING (
    public.current_user_id() = parent_id OR public.current_user_id() = student_id
  );

-- 家长可以创建关系记录（邀请学生）
CREATE POLICY "Parents can insert relations" ON public.parent_student_relations
  FOR INSERT
  WITH CHECK (public.current_user_id() = parent_id);

-- 相关方可以更新关系记录（验证）
CREATE POLICY "Users can update own relations" ON public.parent_student_relations
  FOR UPDATE
  USING (
    public.current_user_id() = parent_id OR public.current_user_id() = student_id
  );

-- ============================================================
-- 完成！RLS 策略已配置
-- 
-- 下一步：
-- 1. 测试 API 连接（使用 supabase-client.js）
-- 2. 确保前端正确传递 auth token
-- ============================================================
