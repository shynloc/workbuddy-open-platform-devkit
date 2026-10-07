# Minimal WorkBuddy OAuth 2.1 Reference

这是 **WB-OPDK 示例代码**，用于演示第三方应用后端完成：

```text
/login
→ WorkBuddy authorize
→ /callback
→ code exchange
→ server-side token store
→ /profile
→ /refresh
```

官方来源：

- https://open.workbuddy.cn/docs/openapi
- https://open.workbuddy.cn/docs/third-party-app

## 官方当前确认的 OAuth 关键点

- Authorization Endpoint：`GET https://www.workbuddy.cn/openapi/v2/authorize`
- Token Endpoint：`POST https://www.workbuddy.cn/openapi/v2/token`
- Token Content-Type：`application/x-www-form-urlencoded`
- Authorization Code 请求：`grant_type=authorization_code`
- 交换字段：`code / redirect_uri / client_id / client_secret`
- Refresh 请求：`grant_type=refresh_token`
- Refresh 字段：`refresh_token / client_id / client_secret`
- `redirect_uri` 必须与 authorize 阶段字节级一致
- `state` 应用于 CSRF 防护
- 授权码一次性使用，官方当前写有效期 10 分钟
- Access Token TTL 不应写死，应读取接口实际 `expires_in`

> 当前官方中英文示例中的 `expires_in` 数值存在差异，所以示例代码只使用响应值，不把固定时长编码进业务。

## 运行

```bash
cd examples/third-party-oauth-minimal
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export WORKBUDDY_CLIENT_ID="..."
export WORKBUDDY_CLIENT_SECRET="..."
export WORKBUDDY_REDIRECT_URI="http://127.0.0.1:5000/callback"
export WORKBUDDY_SCOPE="user.profile.readable"
export FLASK_SECRET_KEY="$(python3 -c 'import secrets;print(secrets.token_hex(32))')"

python app.py
```

在开放平台把 OAuth callback URL 配成与 `WORKBUDDY_REDIRECT_URI` **完全相同**的值。

## Production Checklist

这个 Demo **不是生产 Token Store**。

生产环境必须至少：

- 使用数据库/Secret Store 保存 token；
- token 静态加密；
- 不向浏览器返回 access/refresh token；
- 不记录完整 token 到日志；
- 使用 HTTPS；
- 管理 refresh token 轮换；
- 用户撤销授权后删除 token；
- Scope 最小化；
- 按实际 `expires_in` 调度刷新；
- 对 `invalid_grant` 重新走授权，而不是盲目重试。

参见：

- `60-open-api/oauth-2.1.md`
- `60-open-api/integration-checklist.md`
- `70-release-engineering/security-checklist.md`
