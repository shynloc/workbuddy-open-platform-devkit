---
title: MCP Connector Guide
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-connector
last_verified: 2026-10-07
status: VERIFIED
---

# MCP Connector

## MCP Server 基线

官方要求/建议：

- 遵循 MCP 稳定协议；
- 远程 HTTPS；
- 支持 SSE 或 streamableHttp；
- 工具名称、描述、参数、返回清晰稳定；
- 返回可读错误；
- 单次请求建议 30 秒内响应；
- 服务建议可用性不低于 99.9%；
- 用户数据遵循最小权限；
- 一个连接器一个 MCP Server。

## mcp.json 常用字段

- `mcpServers`
- `type`
- `url`
- `command`
- `args`
- `headers` / `env`
- `timeout`
- `cwd`（>=4.22.15）
- `disabledTools`（>=4.22.15）
- `runtime`（>=5.0.0）
- `npmRegistry / npmRegistries`
- `staticEnv / staticHeaders`（>=5.0.0）
- `preAuth`（>=5.0.0）

### 变量引用

凭据使用 `${VAR_NAME}`，真实凭据不得写进 mcp.json。

### 远程示意

```json
{
  "mcpServers": {
    "service": {
      "type": "streamableHttp",
      "url": "https://example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${SERVICE_TOKEN}"
      },
      "timeout": 30000
    }
  }
}
```

这只是结构示意；具体认证方式必须与 connector-meta 的 auth_mode 配套。
