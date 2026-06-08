/* =============================================================
 * 国学课堂 — 课程目录清单 (Course Catalog Manifest)
 * -------------------------------------------------------------
 * 用途:首页 index.html 读取此文件渲染课程卡片
 * 添加新课只需:1) 复制 lessons/_template.html  2) 填写内容
 *              3) 在下面的 GUOXUE_LESSONS 数组里追加一项
 *              4) 若属新门类,在 assets/data/categories.js 同步登记
 *
 * 字段说明:
 *   id          唯一标识(数字 + kebab-case)
 *   title       课程标题(显示在卡片)
 *   subtitle    副标题(2-6 字)
 *   path        课程入口 HTML 的相对路径(相对于 index.html)
 *   icon        卡片左上角 emoji
 *   grade       适用年级
 *   description 课程简介(1-2 句话)
 *   status      'ready' = 已发布 / 'coming' = 即将上线
 *   subject     所属门类 key(对应 GUOXUE_CATEGORIES 中的 key)
 *   tier        难度分层: 'core' = 核心课 / 'advanced' = 进阶拓展 / 'supplement' = 补充材料(可选,默认: 'core')
 *   featured    true = 展示在右侧"精选推荐"面板 (可选,默认: false)
 * ============================================================= */
window.GUOXUE_LESSONS = [
    {
        id: '01-lunyu',
        title: '《论语》国学问答',
        subtitle: '传承经典 · 启迪智慧',
        path: 'lessons/01-lunyu/index.html',
        icon: '📖',
        grade: '小学中高年级',
        description: '走近孔子,理解仁、学、孝、礼四大核心思想,精读六句千古名言,配套十道互动测验。',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'mengxue',
        tier: 'core',
        featured: true
    },
    {
        id: '01-lunyu-mixed',
        title: '《论语》问答课件 · 混合版',
        subtitle: '拓展版 · 内容更详尽',
        path: 'lessons/01-lunyu-mixed/index.html',
        icon: '📚',
        grade: '小学高年级 / 初中',
        description: '在标准版基础上拓展内容深度,适合学有余力的学生深入研读。',
        status: 'ready',
        subject: 'mengxue',
        tier: 'advanced',
        featured: false
    },
    {
        id: '02-sanzijing',
        title: '《三字经》国学启蒙',
        subtitle: '人之初 · 性本善',
        path: 'lessons/02-sanzijing/index.html',
        icon: '📜',
        grade: '小学低中年级',
        description: '走进"三百千"之首,从开篇哲学到教育之道,从孝悌故事到历史长河,在朗朗书声中收获成长。',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'mengxue',
        tier: 'core',
        featured: true
    },
    {
        id: '02-xueer',
        title: '《学而》三问',
        subtitle: '学而时习 · 君子之道',
        path: 'lessons/02-xueer/index.html',
        icon: '🌱',
        grade: '小学中高年级',
        description: '深入解读《论语·学而》开篇三问：学而时习、有朋远来、人不知愠，理解君子修养的三重境界。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'mengxue',
        tier: 'core',
        featured: false
    },
    {
        id: '03-xueer-xiaoti',
        title: '孝悌为仁之本',
        subtitle: '学而第二章 · 有子曰',
        path: 'lessons/03-xueer-xiaoti/index.html',
        icon: '🌿',
        grade: '小学中高年级',
        description: '《论语·学而》第二章名句解读：孝悌是仁的根本，君子务本，本立而道生。配套十道互动测验。',
        status: 'ready',
        duration: '约 10 分钟',
        subject: 'mengxue',
        tier: 'core',
        featured: false
    }
    // ----- 在此下方添加新课程 -----
    // {
    //     id: '03-shijing',
    //     title: '《诗经》精选诵读',
    //     subtitle: '风雅颂 · 三百篇',
    //     path: 'lessons/03-shijing/index.html',
    //     icon: '🌿',
    //     grade: '小学高年级',
    //     description: '从《关雎》到《蒹葭》,在千年诗篇中感受古人最真挚的情感。',
    //     status: 'ready',
    //     subject: 'jing',
    //     tier: 'core',
    //     featured: false
    // },
];
