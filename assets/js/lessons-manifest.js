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
    },
    {
        id: '04-zengzi-sansheng',
        title: '曾子三省',
        subtitle: '吾日三省吾身',
        path: 'lessons/04-zengzi-sansheng/index.html',
        icon: '🔄',
        grade: '小学中高年级',
        description: '《论语·学而》第四章精讲：吾日三省吾身——为人谋而不忠乎？与朋友交而不信乎？传不习乎？配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'mengxue',
        tier: 'core',
        featured: false
    },
    {
        id: '05-dao-qiancheng-guo',
        title: '道千乘之国',
        subtitle: '敬事信 · 节用爱',
        path: 'lessons/05-dao-qiancheng-guo/index.html',
        icon: '🏛️',
        grade: '小学中高年级',
        description: '《论语·学而》第五章精讲：孔子论治国五要——敬事而信、节用而爱人、使民以时。配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'mengxue',
        tier: 'core',
        featured: false
    },
    {
        id: '06-dizi-ruze-xiao',
        title: '弟子入则孝',
        subtitle: '先做人 · 后学文',
        path: 'lessons/06-dizi-ruze-xiao/index.html',
        icon: '🎓',
        grade: '小学中高年级',
        description: '《论语·学而》第六章精讲：先孝悌谨信爱众亲仁，行有余力则以学文——儒家教育思想的核心纲领。配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'mengxue',
        tier: 'core',
        featured: false
    },
    {
        id: '07-xianxian-yise',
        title: '贤贤易色',
        subtitle: '实践出真知',
        path: 'lessons/07-xianxian-yise/index.html',
        icon: '🤝',
        grade: '小学中高年级',
        description: '子夏论真学问——贤贤易色、事父母竭其力、事君致其身、与朋友交言而有信。配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'mengxue',
        tier: 'core',
        featured: false
    },
    {
        id: '08-junzi-bu-zhong',
        title: '君子不重则不威',
        subtitle: '自重威·信交友·勇改过',
        path: 'lessons/08-junzi-bu-zhong/index.html',
        icon: '⚖️',
        grade: '小学中高年级',
        description: '《论语·学而》第八章精讲：君子不重则不威——持重自威、主忠信、无友不如己者、过则勿惮改。配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'mengxue',
        tier: 'core',
        featured: false
    },
    {
        id: '09-wen-liang-gong-jian-rang',
        title: '温良恭俭让',
        subtitle: '夫子五德 · 以德服人',
        path: 'lessons/09-wen-liang-gong-jian-rang/index.html',
        icon: '🌟',
        grade: '小学中高年级',
        description: '《论语·学而》第十章精讲：子贡论孔子五德——温良恭俭让。子禽问于子贡，夫子至邦必闻其政，求之与抑与之与？配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'mengxue',
        tier: 'core',
        featured: false
    },
    {
        id: '10-fu-zai-guan-qi-zhi',
        title: '父在观其志',
        subtitle: '孝道 · 志行 · 传承',
        path: 'lessons/10-fu-zai-guan-qi-zhi/index.html',
        icon: '👨‍👦',
        grade: '小学中高年级',
        description: '《论语·学而》第十一章精讲：子曰：父在观其志，父没观其行，三年无改于父之道，可谓孝矣。配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'mengxue',
        tier: 'core',
        featured: false
    },
    {
        id: '11-li-zhi-yong-he-wei-gui',
        title: '礼之用和为贵',
        subtitle: '礼乐 · 和谐 · 节制',
        path: 'lessons/11-li-zhi-yong-he-wei-gui/index.html',
        icon: '⚖️',
        grade: '小学中高年级',
        description: '《论语·学而》第十二章精讲：有子论礼与和——礼之用和为贵，小大由之。知和而和，不以礼节之，亦不可行也。配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'mengxue',
        tier: 'core',
        featured: false
    },
    {
        id: '36-lin-fang-wen-li-zhi-ben',
        title: '林放问礼之本',
        subtitle: '宁俭宁戚 · 礼之本',
        path: 'lessons/36-lin-fang-wen-li-zhi-ben/index.html',
        icon: '🙏',
        grade: '小学高年级·初中',
        description: '《论语·八佾》第四章精讲：林放问礼之本，子曰"大哉问！礼与其奢也宁俭，丧与其易也宁戚"——孔子论礼之本在内心真诚，不在外在形式。配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'lunyu',
        tier: 'core',
        featured: false
    },
    {
        id: '37-yi-di-zhi-you-jun',
        title: '夷狄之有君',
        subtitle: '文明高于政权',
        path: 'lessons/37-yi-di-zhi-you-jun/index.html',
        icon: '🏛️',
        grade: '小学高年级·初中',
        description: '《论语·八佾》第五章精讲：子曰"夷狄之有君，不如诸夏之亡也"——孔子论礼乐文明高于政治形式，文化传承重于权力更替。配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'lunyu',
        tier: 'core',
        featured: false
    },
    {
        id: '38-ji-shi-lu-yu-tai-shan',
        title: '季氏旅于泰山',
        subtitle: '神不享非礼，礼不容乱序',
        path: 'lessons/38-ji-shi-lu-yu-tai-shan/index.html',
        icon: '📖',
        grade: '小学高年级·初中',
        description: '《论语·八佾》第六章精讲：季氏旅于泰山，孔子叹道"曾谓泰山不如林放乎"——借泰山之神，批评大夫僭礼，责备弟子失职，揭示"神不享非礼，礼不容乱序"的道理。配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'lunyu',
        tier: 'core',
        featured: false
    },
    {
        id: '39-jun-zi-wu-suo-zheng',
        title: '君子无所争',
        subtitle: '射以礼成，君子不争',
        path: 'lessons/39-jun-zi-wu-suo-zheng/index.html',
        icon: '🏹',
        grade: '小学高年级·初中',
        description: '《论语·八佾》第七章精讲：子曰"君子无所争，必也射乎！揖让而升，下而饮，其争也君子"——儒家射礼：把竞争的武器引入礼仪，以礼乐制约武力，培养彬彬有礼的君子风度。配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'lunyu',
        tier: 'core',
        featured: false
    },
    {
        id: '40-hui-shi-hou-su',
        title: '绘事后素',
        subtitle: '礼本于仁',
        path: 'lessons/40-hui-shi-hou-su/index.html',
        icon: '🎨',
        grade: '小学高年级·初中',
        description: '《论语·八佾》第八章精讲：子夏问诗，孔子答以"绘事后素"，子夏悟"礼后乎"——孔子赞"起予者商也"！白底先于图画，仁心先于礼节，礼本于仁。配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'lunyu',
        tier: 'core',
        featured: false
    }
    {
        id: '41-xia-li-wu-neng-yan-zhi',
        title: '夏礼吾能言之',
        subtitle: '言必有据',
        path: 'lessons/41-xia-li-wu-neng-yan-zhi/index.html',
        icon: '📜',
        grade: '小学高年级·初中',
        description: '《论语·八佾》第九章精讲：夏礼吾能言之，杞不足征也——孔子言必有据、实事求是的治学态度，对文献传承的深刻思考。配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'lunyu',
        tier: 'core',
        featured: false
    },
    {
        id: '42-di-zi-ji-guan-er-wang',
        title: '禘自既灌而往',
        subtitle: '礼贵诚敬',
        path: 'lessons/42-di-zi-ji-guan-er-wang/index.html',
        icon: '🏛️',
        grade: '小学高年级·初中',
        description: '《论语·八佾》第十章精讲：禘自既灌而往者，吾不欲观之矣——孔子叹息行礼者诚敬流失，揭示礼贵诚敬、善始善终的真谛。配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'lunyu',
        tier: 'core',
        featured: false
    },
    {
        id: '43-huo-wen-di-zhi-shuo',
        title: '或问禘之说',
        subtitle: '不言之教',
        path: 'lessons/43-huo-wen-di-zhi-shuo/index.html',
        icon: '🏛️',
        grade: '小学高年级·初中',
        description: '《论语·八佾》第十一章精讲：或问禘之说，子曰不知也——孔子不妄言、不僭言，以「指其掌」点破真理如示诸斯。配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'lunyu',
        tier: 'core',
        featured: false
    },
    {
        id: '44-ji-ru-zai',
        title: '祭如在',
        subtitle: '亲祭为贵',
        path: 'lessons/44-ji-ru-zai/index.html',
        icon: '🏛️',
        grade: '小学高年级·初中',
        description: '《论语·八佾》第十二章精讲：祭如在，祭神如神在——孔子论祭祀之诚：心存如在之敬，亲历亲为，不可假手他人。配套十道互动测验。',
        status: 'ready',
        duration: '约 12 分钟',
        subject: 'lunyu',
        tier: 'core',
        featured: false
    },
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
