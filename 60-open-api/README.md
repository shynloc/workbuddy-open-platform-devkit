# Third-party App / Open API

官方来源：

- https://open.workbuddy.cn/docs/third-party-app
- https://open.workbuddy.cn/docs/openapi

## 已覆盖

- `third-party-app.md` — 第三方应用与 Scope
- `oauth-2.1.md` — 授权码、Token、安全基线
- `capability-map.md` — API 能力域
- `local-assistant.md` — PC 本地助理
- `cloud-task.md` — 云端任务
- `acp.md` — ACP SSE + JSON-RPC 通道
- `artifacts.md` — 会话产物 REST + SSE 同步
- `integration-checklist.md` — 接入检查表

## 推荐阅读顺序

```text
third-party-app
→ oauth-2.1
→ capability-map
→ 按业务选择 local-assistant / cloud-task / acp / artifacts
→ integration-checklist
```

Open API 变化较快，endpoint、Scope 和 TTL 都应在集成当天回查官方页面。
