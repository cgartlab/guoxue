/**
 * 修复 Issue #90: 移动端菜单覆盖内容问题
 * 在每个 lesson HTML 文件中添加内联 CSS 修复
 */

const fs = require('fs');
const path = require('path');

const lessonsDir = path.join(__dirname, 'lessons');
const cssFix = `
<style>
/* Mobile Menu Overlay Fix - Issue #90 */
@media (max-width: 767px) {
    .ds-navbar--global {
        position: relative;
        z-index: 100;
    }
    
    .ds-navbar__menu {
        max-height: calc(100vh - 120px);
        overflow-y: auto;
        -webkit-overflow-scrolling: touch;
        overscroll-behavior: contain;
    }
    
    /* 确保内容可滚动 */
    body.menu-open {
        overflow: hidden;
        position: fixed;
        width: 100%;
        height: 100%;
    }
    
    .ds-slide-container {
        position: relative;
        z-index: 1;
    }
}
</style>
`;

// 找到所有 lesson HTML 文件
const lessonDirs = fs.readdirSync(lessonsDir).filter(item => {
    const stat = fs.statSync(path.join(lessonsDir, item));
    return stat.isDirectory();
});

console.log(`找到 ${lessonDirs.length} 个课程目录`);

let modified = 0;
let errors = [];

for (const dir of lessonDirs) {
    const htmlPath = path.join(lessonsDir, dir, 'index.html');
    
    if (!fs.existsSync(htmlPath)) continue;
    
    try {
        let content = fs.readFileSync(htmlPath, 'utf8');
        
        // 检查是否已经包含此修复
        if (content.includes('Mobile Menu Overlay Fix - Issue #90')) {
            console.log(`跳过 ${dir} (已包含修复)`);
            continue;
        }
        
        // 在 </head> 前插入 CSS
        content = content.replace('</head>', cssFix + '\n</head>');
        
        fs.writeFileSync(htmlPath, content, 'utf8');
        console.log(`已修复: ${dir}`);
        modified++;
        
    } catch (err) {
        errors.push({ dir, error: err.message });
        console.error(`错误 ${dir}: ${err.message}`);
    }
}

console.log(`\n完成: 修改 ${modified} 个文件`);
if (errors.length > 0) {
    console.log(`失败: ${errors.length} 个`);
    errors.forEach(e => console.log(`  - ${e.dir}: ${e.error}`));
}
