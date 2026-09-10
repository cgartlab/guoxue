/* =============================================================
 * 国学课堂 — 学科门类清单 (Subject Catalog)
 * -------------------------------------------------------------
 * 用途:首页 index.html 读取此文件渲染侧栏分类导航
 *
 * 字段说明:
 *   key         唯一标识(小写字母 + 数字 + 连字符)
 *   label       显示名称(纯文本,不含图标)
 *   num         门类序号
 *   description 一句话介绍(可空)
 *   status      'ready' = 门类下已有上线课程 / 'coming' = 门类暂未上线
 *   order       排序权重(数字越小越靠前)
 * ============================================================= */
window.GUOXUE_CATEGORIES = [
    {
        key: 'daolun',
        label: '导论',
        num: '01',
        description: '《论语》总述 · 走近孔子',
        status: 'ready',
        order: 1
    },
    {
        key: 'xueer',
        label: '学而',
        num: '02',
        description: '《论语·学而篇》各章精讲',
        status: 'ready',
        order: 2
    },
    {
        key: 'weizheng',
        label: '为政',
        num: '03',
        description: '《论语·为政篇》各章精讲',
        status: 'ready',
        order: 3
    },
    {
        key: 'bayi',
        label: '八佾',
        num: '04',
        description: '《论语·八佾篇》各章精讲',
        status: 'ready',
        order: 4
    },
    {
        key: 'mengxue',
        label: '蒙学',
        num: '05',
        description: '蒙学经典 · 三字经 · 百家姓 · 千字文',
        status: 'ready',
        order: 5
    }
];
