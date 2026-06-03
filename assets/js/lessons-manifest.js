/* =============================================================
 * 国学课堂 — 课程目录清单 (Course Catalog Manifest)
 * -------------------------------------------------------------
 * 用途:首页 index.html 读取此文件渲染课程卡片
 * 添加新课只需:1) 复制 lessons/_template.html  2) 填写内容
 *              3) 在下面的 GUOXUE_LESSONS 数组里追加一项
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
        status: 'ready'
    },
    {
        id: '01-lunyu-mixed',
        title: '《论语》问答课件 · 混合版',
        subtitle: '拓展版 · 内容更详尽',
        path: 'lessons/01-lunyu-mixed/index.html',
        icon: '📚',
        grade: '小学高年级 / 初中',
        description: '在标准版基础上拓展内容深度,适合学有余力的学生深入研读。',
        status: 'ready'
    }
    // ----- 在此下方添加新课程 -----
    // {
    //     id: '02-shijing',
    //     title: '《诗经》精选诵读',
    //     subtitle: '风雅颂 · 三百篇',
    //     path: 'lessons/02-shijing/index.html',
    //     icon: '🌿',
    //     grade: '小学高年级',
    //     description: '从《关雎》到《蒹葭》,在千年诗篇中感受古人最真挚的情感。',
    //     status: 'ready'
    // },
];
