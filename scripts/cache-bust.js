/**
 * 静态资源版本化脚本 - 解决缓存失效问题
 * 
 * 使用说明：
 *   node scripts/cache-bust.js
 * 
 * 功能：
 *   1. 扫描所有 HTML 文件中的静态资源引用（<link>, <script>）
 *   2. 添加/更新 ?v= 参数为 Git commit hash
 *   3. 开发模式下跳过版本化（NODE_ENV=development）
 */

const fs = require('fs');
const path = require('path');

// 获取版本号（Git commit hash 短版本）
function getVersion() {
    try {
        const childProcess = require('child_process');
        const version = childProcess
            .execSync('git rev-parse --short HEAD', { cwd: __dirname + '/..' })
            .toString().trim();
        return version || Date.now().toString(36);
    } catch (e) {
        return Date.now().toString(36);
    }
}

// 更新单个 HTML 文件中的版本参数
function updateVersionInHTML(filePath, version) {
    let html = fs.readFileSync(filePath, 'utf8');
    
    // 更新 href 属性（link, anchor 等）
    html = html.replace(
        /href="(assets\/[^"]+)(?:\?v=[^"]*)?"/g,
        `href="$1?v=${version}"`
    );
    
    // 更新 src 属性（script 等）
    html = html.replace(
        /src="(assets\/[^"]+)(?:\?v=[^"]*)?"/g,
        `src="$1?v=${version}"`
    );
    
    fs.writeFileSync(filePath, html);
    console.log('Updated:', filePath, '-> v=' + version);
}

// 遍历所有 HTML 文件
function processAllHTML(version) {
    const root = __dirname + '/..';
    const htmlFiles = [
        path.join(root, 'index.html'),
        path.join(root, 'about.html'),
        path.join(root, '404.html')
    ];
    
    // 扫描 lessons 目录
    const lessonsDir = path.join(root, 'lessons');
    if (fs.existsSync(lessonsDir)) {
        const lessonsHtml = getAllHTMLFiles(lessonsDir);
        htmlFiles.push(...lessonsHtml);
    }
    
    htmlFiles.forEach(file => {
        if (fs.existsSync(file)) {
            updateVersionInHTML(file, version);
        }
    });
}

// 递归获取所有 HTML 文件
function getAllHTMLFiles(dir) {
    const files = [];
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
        const fullPath = path.join(dir, entry.name);
        if (entry.isDirectory()) {
            files.push(...getAllHTMLFiles(fullPath));
        } else if (entry.name.endsWith('.html')) {
            files.push(fullPath);
        }
    }
    return files;
}

// 主入口
const version = getVersion();
const isDev = process.env.NODE_ENV === 'development';

if (isDev) {
    console.log('[cache-bust] 开发模式，跳过版本化');
} else {
    console.log('[cache-bust] 版本化静态资源，v=' + version);
    processAllHTML(version);
}