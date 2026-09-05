#!/bin/bash
# 国学课堂 API 部署脚本
# 在服务器上运行：bash deploy.sh
set -e

echo "=== 国学课堂 API 部署 ==="

# 1. 检查 .env
if [ ! -f .env ]; then
  echo "❌ 缺少 .env 文件！请先创建 .env"
  echo "   参考 .env.example 填写配置"
  exit 1
fi

# 2. 创建 Docker 网络（如果不存在，让 Casdoor 也能连进来）
docker network inspect guoxue-net >/dev/null 2>&1 || \
  docker network create guoxue-net

# 3. 拉取镜像并启动
echo "🚀 启动服务..."
docker compose up -d

# 4. 等待健康检查
echo "⏳ 等待数据库就绪..."
sleep 3

# 5. 检查状态
echo ""
echo "=== 服务状态 ==="
docker compose ps

echo ""
echo "=== 查看日志 ==="
docker compose logs --tail=20

echo ""
echo "✅ 部署完成！API 服务在内部端口 3000 运行"
echo "   请配置 Nginx 反向代理:"
echo "     https://api.8023laozhanshi.cc → http://localhost:3000"
echo ""
echo "   记得在 .env 中设置正确的 CASDOOR_JWT_SECRET"
echo "   （Casdoor 后台 → 组织 → JWT Secret）"
