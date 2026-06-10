# [紧急修复] 恢复被误删的课程工具栏

## 问题
导航栏 EDIC 改造后，点击课件页只显示导航栏，课件内容消失。

## 根因
前次 Powershell 脚本（navbar-component 替换）使用了双重 `</nav>` 匹配逻辑：
```
$endIdx  = <nav 的 </nav>    # 全局导航栏的结束标签
$endIdx2 = 第二个 </nav>      # 课程工具栏的结束标签
```
如果两者间距 < 1500 字符，脚本会误认为这是一个"大的导航区域"，把全局导航栏 **和课程工具栏一起** 替换掉。

## 修复
在 10 个课件页的 navbar placeholder 后重新插入 `ds-toolbar`，确保：
- `<nav data-navbar="global">` (导航栏组件)
- `<nav class="ds-toolbar">` (课程工具栏：返回目录/讲义测验标签/翻页按钮/全屏)
- `<div class="slide-viewport">` (幻灯片容器)

## 验证
全部 10 个课件页均已恢复:
01-lunyu, 01-lunyu-mixed, 02-sanzijing, 02-xueer,
03-xueer-xiaoti, 04-zengzi-sansheng, 05-dao-qiancheng-guo,
06-dizi-ruze-xiao, 07-xianxian-yise, 08-junzi-bu-zhong

## 教训
- 批量替换 HTML 时使用纯 ASCII 标记匹配，避免依赖中文（编码问题）
- 修改前确认页面结构，标注**不会被替换的边界**
- 替换范围检查：只替换目标元素，不吞掉相邻元素
