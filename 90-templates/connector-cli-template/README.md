# CLI Connector Template

适用于已经存在成熟、稳定、跨平台 CLI 的服务。

模板使用：

- Node runtime
- init / auth / unAuth / status
- statusMatch
- authUrlDomain
- examples_zh/examples_en

因此默认 `minWorkbuddyVersion` 设为 4.24.0。

## 重要

WorkBuddy 提取到认证 URL 后，默认会终止 auth 子进程。不要让 auth 子进程本身承担必须持续存活的 OAuth 回调服务器。

如果服务支持 OAuth 2.0 Device Flow，可另按 WorkBuddy 5.0.0+ 的 `authDeviceFlow` 方案实现。

## 验证

```bash
python3 scripts/validate_connector.py path/to/connector
```

官方来源：https://open.workbuddy.cn/docs/connector
