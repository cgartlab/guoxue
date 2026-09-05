# ─── 构建阶段 ───
FROM node:20-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci --only=production && npm cache clean --force

# ─── 运行阶段 ───
FROM node:20-alpine
WORKDIR /app
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY --from=builder /app/node_modules ./node_modules
COPY src ./src
COPY package.json ./

USER appuser
EXPOSE 3000
CMD ["node", "src/index.js"]
