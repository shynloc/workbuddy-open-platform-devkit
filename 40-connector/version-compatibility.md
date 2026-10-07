# Connector Version Compatibility

官方来源：https://open.workbuddy.cn/docs/connector

使用新字段时按最高最低版本声明 `minWorkbuddyVersion`。

| 能力 | 最低版本 |
|---|---|
| skill-only / server-side / CLI unAuth,statusMatch,authUrlDomain | 基础 |
| CLI runtime/npmRegistry/env/authWaitForExit/authQrModal；gateway | 4.22.0 |
| authSuppressBrowser | 4.22.8 |
| min/maxWorkbuddyVersion | 4.22.12 |
| MCP cwd/disabledTools | 4.22.15 |
| token auth + token-schema | 4.23.0 |
| name_zh/en、examples_zh/en、statusMatchJson、versionCheck、npmRegistries、多步 auth | 4.24.0 |
| CLI Device Flow/Python runtime；MCP preAuth/runtime/staticEnv/staticHeaders | 5.0.0 |
| name_map / description_map | 5.2.0 |

低于声明版本的客户端：未启用过时不展示；已启用/曾连接则置灰并提示升级。
