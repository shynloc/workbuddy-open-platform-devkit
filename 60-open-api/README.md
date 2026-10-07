# Third-party App / Open API

官方来源：

- https://open.workbuddy.cn/docs/third-party-app
- https://open.workbuddy.cn/docs/openapi

## 已覆盖

- `third-party-app.md` — 应用类型、Scope、OAuth 接入边界
- `oauth-2.1.md` — 授权码、Token 与安全基线
- `capability-map.md` — API 能力域总览
- `endpoints-quick-reference.md` — 当前 endpoint 快速索引
- `user-and-credits.md` — 用户资料 / 额度相关能力与当前 Scope 差异
- `local-assistant.md` — PC 本地助理状态、消息、历史
- `cloud-tasks.md` — 云端任务创建 / 查询 / ACP 凭据
- `acp-and-artifacts.md` — ACP 双通道与会话产物同步
- `integration-checklist.md` — 接入检查表

## 推荐阅读顺序

```text
third-party-app
→ oauth-2.1
→ capability-map
→ endpoints-quick-reference
→ 按业务选择 Local Assistant / Cloud Tasks / ACP & Artifacts
→ integration-checklist
```

Open API 变化较快，endpoint、Scope、Token TTL 和应用类型权限都应在集成当天回查官方页面。

已知官方文档内部差异见：

`sources/known-inconsistencies.md`
