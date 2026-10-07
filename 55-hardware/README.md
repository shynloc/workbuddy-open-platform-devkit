# Hardware Integration

WorkBuddy 当前把“硬件接入”作为第三方应用的一种正式应用类型，面向智能眼镜、车机等设备厂商/合作伙伴。

官方来源：

- https://open.workbuddy.cn/docs/third-party-app
- https://open.workbuddy.cn/docs/openapi

硬件取得用户 OAuth 2.1 授权后，可按业务需要申请并调用本地助理、云端任务、会话产物等 Open API。

## 已覆盖

- `architecture.md` — 硬件接入参考架构
- `oauth-and-scopes.md` — 授权与 Scope
- `runtime.md` — Local Assistant / Cloud Task / ACP / Artifacts
- `device-security.md` — 设备端安全
- `integration-checklist.md` — 发布/接入检查

硬件不是一个特殊“Connector ZIP”；它属于 Third-party App / Open API 接入路径。
