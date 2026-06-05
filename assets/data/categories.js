/* =============================================================
 * 国学课堂 — 学科门类清单 (Subject Catalog)
 * -------------------------------------------------------------
 * 用途:首页 index.html 读取此文件渲染侧栏分类导航
 *
 * 字段说明:
 *   key         唯一标识(小写字母 + 数字 + 连字符)
 *   label       显示名称(含 emoji)
 *   icon        emoji 字符
 *   description 一句话介绍(可空)
 *   status      'ready' = 门类下已有上线课程 / 'coming' = 门类暂未上线
 *   order       排序权重(数字越小越靠前)
 * ============================================================= */
window.GUOXUE_CATEGORIES = [
    {
        key: 'jing',
        label: '经部',
        icon: '📜',
        description: '儒家经典 · 诗书礼易春秋',
        status: 'coming',
        order: 1
    },
    {
        key: 'shi',
        label: '史部',
        icon: '📚',
        description: '史学经典 · 资治通鉴',
        status: 'coming',
        order: 2
    },
    {
        key: 'zi',
        label: '子部',
        icon: '💭',
        description: '诸子百家 · 儒道法墨',
        status: 'coming',
        order: 3
    },
    {
        key: 'ji',
        label: '集部',
        icon: '✒️',
        description: '诗词文集 · 楚辞汉赋',
        status: 'coming',
        order: 4
    },
    {
        key: 'mengxue',
        label: '蒙学',
        icon: '🌱',
        description: '三字经 · 百家姓 · 千字文 · 论语',
        status: 'ready',
        order: 5
    },
    {
        key: 'shufa',
        label: '书法',
        icon: '🖌️',
        description: '笔墨纸砚 · 楷行隶篆',
        status: 'coming',
        order: 6
    },
    {
        key: 'guohua',
        label: '国画',
        icon: '🎨',
        description: '山水花鸟 · 写意工笔',
        status: 'coming',
        order: 7
    },
    {
        key: 'zhongyi',
        label: '中医',
        icon: '🌿',
        description: '岐黄之道 · 阴阳五行',
        status: 'coming',
        order: 8
    },
    {
        key: 'wushu',
        label: '武术',
        icon: '🥋',
        description: '中华武学 · 内外兼修',
        status: 'coming',
        order: 9
    },
    {
        key: 'mingsu',
        label: '民俗',
        icon: '🏮',
        description: '节气节日 · 民间工艺',
        status: 'coming',
        order: 10
    },
    {
        key: 'guqin',
        label: '古琴',
        icon: '🎵',
        description: '琴棋书画 · 高山流水',
        status: 'coming',
        order: 11
    },
    {
        key: 'qilei',
        label: '棋类',
        icon: '♟️',
        description: '围棋象棋 · 博弈智慧',
        status: 'coming',
        order: 12
    }
];
