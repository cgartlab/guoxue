# 新增第10课《君子不重则不威》- PR #48

## 任务
将"子曰：君子不重则不威，学则不固。主忠信，无友不如己者，过，则勿惮改。"制作成国学课堂课程并上线。

## 执行
1. 创建分支 feat/08-junzi-bu-zhong（基于 main，已含 01-07 全部课程）
2. 创建 lessons/08-junzi-bu-zhong/index.html（791行，28页幻灯片）
3. 更新 assets/js/lessons-manifest.js 注册新课程
4. 应用缓存版本化（deploy.yml 的 cache-bust 流程会在上传时重新版本化）
5. 提交、推送、创建 PR #48 到 cgartlab/guoxue

## 课程内容
- 讲义 8 页：原文注音 → 逐句四解（持重·忠信·择友·改过）→ 修身五要总结
- 测验 10 题
- 答疑解惑 3 页：FAQ → 生活应用 → 课程总结

## 文件
- lessons/08-junzi-bu-zhong/index.html
- assets/js/lessons-manifest.js（追加 08-junzi-bu-zhong 条目）
