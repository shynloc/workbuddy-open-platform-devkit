# Security & Privacy Checklist

## Secrets

- [ ] 包内无 client_secret
- [ ] 无 access_token / refresh_token / API Key / PAT
- [ ] 示例凭据明显为占位值
- [ ] 日志不输出完整凭据

## Auth

- [ ] 最小权限
- [ ] redirect_uri 精确匹配
- [ ] OAuth 使用 state
- [ ] Connector MCP OAuth 支持 PKCE S256
- [ ] token-schema 敏感字段使用 password

## External Side Effects

- [ ] 发布、删除、支付、发送、覆盖等操作有确认门槛
- [ ] 重试不会造成明显重复副作用
- [ ] 幂等性策略清楚

## User Data

- [ ] 只读取完成任务所需数据
- [ ] 不把用户私有数据写入公开日志/仓库
- [ ] 多用户凭据、缓存、会话严格隔离
- [ ] 用户断开连接/登出后授权可撤销或失效

## Public Repository

- [ ] .env 被 gitignore
- [ ] 示例使用 placeholder
- [ ] 截图/日志已脱敏
- [ ] 不上传真实生产配置备份

## Working-grade Security Gate

涉及外部账号、用户数据、Open API、Connector 或 Hardware 时，进一步执行：

- `65-security-governance/credential-handling.md`
- `65-security-governance/data-and-logging.md`
- `65-security-governance/side-effect-policy.md`
- `65-security-governance/release-security-gate.md`

本页是快速检查；`65-security-governance/` 是完整治理层。
