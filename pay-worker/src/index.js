/**
 * 国学课堂 — 面包多订单验单解锁 Worker
 * ------------------------------------------------------------
 * 用途: 校验用户在面包多平台的订单,验证通过后为每个订单生成/返回
 *       唯一的课程解锁码(每人独立),写入 Cloudflare KV。
 *
 * 鉴权: 调用面包多商店开放接口 https://x.mbd.pub/api/order-detail
 *       需携带 Header `x-token`,密钥从环境变量 MBD_DEVELOPER_KEY 读取
 *       (部署用 `wrangler secret put MBD_DEVELOPER_KEY` 注入),严禁硬编码。
 *
 * 幂等: 同一订单号(order_id)重复请求返回同一解锁码。
 *
 * 接口:
 *   POST /api/redeem   body: { "order_id": "32位hex", "email": "可选" }
 *   成功: { ok: true,  code: "GX-XXXXXXXX" }
 *   失败: { ok: false, reason: "invalid_order_id | not_found | not_paid | amount_mismatch | bad_key | upstream_error" }
 *
 * 注意: 本 Worker 不向客户端泄露面包多上游响应的任何敏感字段,
 *       只返回上面定义的极简结果。
 */

const DEFAULT_PRICE = 9.9;                                 // 默认验收价格(元)
const DEFAULT_ORIGIN = 'https://guoxue.8023laozhanshi.cc'; // 默认允许来源
const ORDER_DETAIL_URL = 'https://x.mbd.pub/api/order-detail';
const CODE_PREFIX = 'GX-';
// 生成解锁码用字符集: 去掉易混淆的 0/O/1/I/L
const CODE_ALPHABET = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789';

function json(body, status, extraHeaders) {
    const headers = { 'Content-Type': 'application/json; charset=utf-8' };
    if (extraHeaders) Object.assign(headers, extraHeaders);
    return new Response(JSON.stringify(body), {
        status: status || 200,
        headers: headers
    });
}

/** 判断来源是否允许(CORS) */
function isAllowedOrigin(origin, allowedList) {
    if (!origin) return false;
    // 本地调试: 允许任意端口的 http://localhost
    if (/^http:\/\/localhost(?::\d+)?$/.test(origin)) return true;
    return allowedList.indexOf(origin) !== -1;
}

/** 计算 CORS 响应头 */
function corsHeaders(request, env) {
    const origin = request.headers.get('Origin') || '';
    const allowedRaw = (env.ALLOWED_ORIGIN || DEFAULT_ORIGIN)
        .split(',')
        .map(function (s) { return s.trim(); })
        .filter(Boolean);
    const headers = {
        'Access-Control-Allow-Methods': 'GET,POST,OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '86400'
    };
    if (isAllowedOrigin(origin, allowedRaw)) {
        headers['Access-Control-Allow-Origin'] = origin;
        headers['Vary'] = 'Origin';
    }
    return headers;
}

/** 生成 8~10 位大写字母数字解锁码(形如 GX-AB23CDEF) */
function generateCode() {
    const len = 8 + Math.floor(Math.random() * 3);
    let s = '';
    for (let i = 0; i < len; i++) {
        s += CODE_ALPHABET[Math.floor(Math.random() * CODE_ALPHABET.length)];
    }
    return CODE_PREFIX + s;
}

export default {
    async fetch(request, env) {
        const url = new URL(request.url);
        const headers = corsHeaders(request, env);

        // CORS 预检
        if (request.method === 'OPTIONS') {
            if (url.pathname !== '/api/redeem') {
                return new Response(null, { status: 404 });
            }
            return new Response(null, { status: 204, headers: headers });
        }

        // 仅支持 POST /api/redeem
        if (url.pathname !== '/api/redeem' || request.method !== 'POST') {
            return json({ ok: false, reason: 'not_found' }, 404, headers);
        }

        // 解析请求体(非 JSON 视为无效请求)
        let body = null;
        try {
            body = await request.json();
        } catch (e) {
            return json({ ok: false, reason: 'invalid_request' }, 400, headers);
        }

        // 校验 order_id: 32 位 hex(不区分大小写,归一化小写)
        const rawOrderId = body && body.order_id ? String(body.order_id).trim() : '';
        if (!/^[0-9a-f]{32}$/i.test(rawOrderId)) {
            return json({ ok: false, reason: 'invalid_order_id' }, 400, headers);
        }
        const orderId = rawOrderId.toLowerCase();

        // 金额阈值: env.PRICE_YUAN 可覆盖(单位:元)
        const price = Number(env.PRICE_YUAN) > 0 ? Number(env.PRICE_YUAN) : DEFAULT_PRICE;

        // 幂等: 同一订单号已发放过解锁码,直接返回原码
        if (env.CODES) {
            const existing = await env.CODES.get('order:' + orderId);
            if (existing) {
                return json({ ok: true, code: existing }, 200, headers);
            }
        }

        // 调用面包多商店开放接口验单
        const developerKey = env.MBD_DEVELOPER_KEY || '';
        if (!developerKey) {
            return json({ ok: false, reason: 'bad_key' }, 502, headers);
        }
        let resp;
        try {
            resp = await fetch(ORDER_DETAIL_URL + '?order_id=' + encodeURIComponent(orderId), {
                headers: { 'x-token': developerKey }
            });
        } catch (e) {
            return json({ ok: false, reason: 'upstream_error' }, 502, headers);
        }
        let data;
        try {
            data = await resp.json();
        } catch (e) {
            return json({ ok: false, reason: 'upstream_error' }, 502, headers);
        }

        // 面包多开放接口 code: 200 正常 / 400 无此订单 / 403 验签失败
        if (data.code === 400) {
            return json({ ok: false, reason: 'not_found' }, 404, headers);
        }
        if (data.code === 403) {
            return json({ ok: false, reason: 'bad_key' }, 502, headers);
        }
        if (data.code !== 200 || !data.result || typeof data.result !== 'object') {
            return json({ ok: false, reason: 'upstream_error' }, 502, headers);
        }
        // 未支付 / 取消 / 无效
        if (data.result.state !== 'success') {
            return json({ ok: false, reason: 'not_paid' }, 402, headers);
        }
        // 金额不足(单位:元,如 9.9)
        if (Number(data.result.orderamount) < price) {
            return json({ ok: false, reason: 'amount_mismatch' }, 402, headers);
        }

        // 生成解锁码并写入 KV(order:<id> 用于幂等, code:<code> 用于查重)
        const code = generateCode();
        await env.CODES.put('order:' + orderId, code);
        await env.CODES.put('code:' + code, '1');
        return json({ ok: true, code: code }, 200, headers);
    }
};