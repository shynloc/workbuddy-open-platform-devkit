# Recipe: 把已有 MCP 产品化为 WorkBuddy Connector

## 1. 先做差距分析

已有 MCP != 可上架 Connector。

检查：

- 是否远程 HTTPS；
- SSE / streamableHttp 是否稳定；
- Tool 名称、描述、schema 是否适合 AI；
- 错误是否可读；
- 鉴权是 OAuth / Token / 无认证；
- 是否支持多用户隔离；
- 是否需要固定出口 IP / 白名单；
- 生产可用性和超时。

## 2. 选择 Auth

- MCP OAuth：按官方 OAuth 2.1 + PKCE 服务端要求；
- 用户 API Key/PAT：auth_mode=token + token-schema；
- 同一服务 OAuth/Token 双形态：官方要求不同 source、独立 Connector。

## 3. 包装

```text
connector/
├── connector-meta.json
├── mcp.json
├── icon.svg
└── skills/
```

## 4. AI 使用说明

工具多、参数复杂、高风险操作明显时，强烈建议配套 Skill。

## 5. QA

使用 `40-connector/qa-checklist.md`，尤其验证：

- auth 失效
- timeout
- 参数错误
- 多账号隔离
- WorkBuddy 重启
- 版本兼容
