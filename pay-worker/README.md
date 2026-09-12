# pay-worker — 面包多订单验单解锁 Worker

国学课堂付费墙的后端验单服务。前端把用户在[面包多](https://mbd.pub/o/bread/YZaVlJ5rag==)付款后拿到的订单号 POST 给本 Worker,Worker 调用面包多商店开放接口验单,校验通过后为**每个订单**生成唯一的课程解锁码(幂等:同一订单号重复请求返回同一码),并写入 Cloudflare KV。

## 接口

### `POST /api/redeem`

请求体(JSON):

```json
{
  "order_id": "32位小写/大写hex订单号",
  "email": "用户邮箱(可选,第二版发信用,当前版本忽略)"
}
```

响应:

| 场景 | HTTP 状态 | 响应体 |
| --- | --- | --- |
| 校验通过 | 200 | `{ "ok": true, "code": "GX-XXXXXXXX" }` |
| 订单号格式不对 | 400 | `{ "ok": false, "reason": "invalid_order_id" }` |
| 已支付但金额不足 | 402 | `{ "ok": false, "reason": "amount_mismatch" }` |
| 面包多无此订单 | 404 | `{ "ok": false, "reason": "not_found" }` |
| 订单未支付/取消/无效 | 402 | `{ "ok": false, "reason": "not_paid" }` |
| 开发者密钥缺失或被拒(验签失败) | 502 | `{ "ok": false, "reason": "bad_key" }` |
| 上游接口异常/网络错误 | 502 | `{ "ok": false, "reason": "upstream_error" }` |

CORS:允许来源由 `ALLOWED_ORIGIN`(可逗号分隔多个)控制,默认 `https://guoxue.8023laozhanshi.cc`;同时始终允许任意端口的 `http://localhost:*` 便于本地调试。自动处理 `OPTIONS` 预检。

> 安全说明:Worker 只返回极简结果,**不会**向客户端透传面包多上游响应的任何敏感字段。

## 部署步骤

前置:已安装 [wrangler](https://developers.cloudflare.com/workers/wrangler/)(仅部署时需要,仓库根目录不需要安装 Cloudflare 依赖):

```bash
npm i -g wrangler
```

1. **登录 Cloudflare**(若未登录):

   ```bash
   wrangler login
   ```

2. **创建 KV 命名空间**(在 `pay-worker/` 目录下执行):

   ```bash
   wrangler kv:namespace create CODES
   ```

   把输出中的 `id = "xxxx..."` 填入 `wrangler.toml` 的 `[[kv_namespaces]] id`(当前为 `<在此填入 KV namespace id>` 占位)。

3. **注入密钥**(密钥绝不可写进代码或配置文件):

   ```bash
   wrangler secret put MBD_DEVELOPER_KEY
   ```

   按提示粘贴面包多开发者密钥(整串,形如 `<你的appid>:xxxx:yyyy`)。

4. **部署**:

   ```bash
   wrangler deploy
   ```

   部署成功后输出 Worker URL,例如 `https://guoxue-pay.<子域>.workers.dev`。

5. **前端替换占位项**:把 `assets/js/unlock.js` 中 `CONFIG.redeemApi` 的占位地址
   `https://YOUR-WORKER.workers.dev/api/redeem` 替换为真实 Worker URL
   (或在页面加载前设置 `window.GUOXUE_REDEEM_API = 'https://.../api/redeem'`)。

## 本地开发测试

复制示例密钥文件并填入真实密钥(仅本地使用,已被 .gitignore 忽略):

```bash
cp .dev.vars.example .dev.vars
# 编辑 .dev.vars 填入 MBD_DEVELOPER_KEY
```

启动本地 Worker:

```bash
wrangler dev
```

默认地址 `http://localhost:8787`,可用 curl 测试:

```bash
# 正常验单(替换为真实订单号)
curl -X POST http://localhost:8787/api/redeem \
  -H "Content-Type: application/json" \
  -d '{"order_id":"<32位hex>"}'

# 非法订单号
curl -X POST http://localhost:8787/api/redeem \
  -H "Content-Type: application/json" \
  -d '{"order_id":"abc"}'
# => {"ok":false,"reason":"invalid_order_id"}
```

> 本地调试会真实调用面包多接口,请勿用虚假订单号刷接口;仓库内 Playwright 测试(见 `tests/paywall.spec.js`)通过 `page.route()` 拦截验单请求,不会连真实接口。