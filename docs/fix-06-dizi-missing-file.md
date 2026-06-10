# 06-dizi-ruze-xiao 课程文件缺失修复记录

## 问题
用户反馈"弟子入则孝"课程（06-dizi-ruze-xiao）无法打开。

## 原因
manifest（assets/js/lessons-manifest.js）中注册了 `06-dizi-ruze-xiao` 课程条目，指向 `lessons/06-dizi-ruze-xiao/index.html`。
但该 HTML 文件仅在 `feat/06-dizi-ruze-xiao` 分支（PR #46）上存在，尚未合并到 main。
`feat/07-xianxian-yise` 分支在编辑 manifest 时一次添加了 06 和 07 两个条目，导致 manifest 引用了不存在的文件。

## 修复
从 `feat/06-dizi-ruze-xiao` 分支通过 `git show` 取回 `lessons/06-dizi-ruze-xiao/index.html` 文件，
应用到当前 `feat/07-xianxian-yise` 分支，并更新缓存版本号。

## 文件
- lessons/06-dizi-ruze-xiao/index.html（512行，来自 feat/06-dizi-ruze-xiao 分支）
- 已推送至 feat/07-xianxian-yise 分支
