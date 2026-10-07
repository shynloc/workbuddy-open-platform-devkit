# MCP + OAuth Connector Template

适用于 MCP Server 自己实现标准 OAuth 的场景。

## 特点

- `auth_mode` 不需要设置为 token；
- WorkBuddy 内置 OAuth 管理器按 OAuth 2.1 + PKCE 连接；
- MCP Server 需要实现官方要求的 metadata / register / authorize / token 端点；
- mcp.json 不写真实 Bearer Token。

模板使用 `examples_zh/examples_en`，因此默认最低 WorkBuddy 版本为 4.24.0。

## 验证

```bash
python3 scripts/validate_connector.py path/to/connector
```

官方来源：https://open.workbuddy.cn/docs/connector
