/**
 * 静态资源缓存失效脚本 (Cache Busting)
 * 在部署前自动更新所有静态资源的版本参数
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// 获取 Git commit hash 作为版本号
function getVersion() {
  try {
    return execSync('git rev-parse --short HEAD').toString().trim();
  } catch (e) {
    return Date.now().toString();
  }
}

// 需要处理的 HTML 文件
const htmlFiles = ['index.html', 'about.html'];

// 更新 HTML 文件中的静态资源引用
function updateVersionInHTML(filePath, version) {
  if (!fs.existsSync(filePath)) {
    console.log('Skipped (not found):', filePath);
    return;
  }

  let html = fs.readFileSync(filePath, 'utf8');
  let updated = false;

  // 更新已带有 v= 参数的引用
  html = html.replace(/href="(assets\/[^"]+)\?v=[^"]*"/g, (match, asset) => {
    updated = true;
    return `href="${asset}?v=${version}"`;
  });
  html = html.replace(/src="(assets\/[^"]+)\?v=[^"]*"/g, (match, asset) => {
    updated = true;
    return `src="${asset}?v=${version}"`;
  });

  // 处理无 v 参数的引用（首次添加）
  html = html.replace(/href="(assets\/[^"]+)"/g, (match, asset) => {
    updated = true;
    return `href="${asset}?v=${version}"`;
  });
  html = html.replace(/src="(assets\/[^"]+)"/g, (match, asset) => {
    updated = true;
    return `src="${asset}?v=${version}"`;
  });

  if (updated) {
    fs.writeFileSync(filePath, html);
    console.log('Updated:', filePath, '-> v=' + version);
  } else {
    console.log('No changes:', filePath);
  }
}

// 主函数
const version = getVersion();
console.log('Cache busting with version:', version);

htmlFiles.forEach(file => {
  updateVersionInHTML(path.join(__dirname, '..', file), version);
});

console.log('Cache busting complete!');
