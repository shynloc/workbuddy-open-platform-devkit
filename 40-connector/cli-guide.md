---
title: CLI Connector Guide
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-connector
last_verified: 2026-10-07
status: VERIFIED
---

# CLI Connector

## 适用条件

只有已有成熟、稳定、跨平台 CLI 时优先考虑。

官方要求：

- 至少支持 macOS 和 Linux，建议 Windows；
- 提供非交互安装；
- auth / status / unAuth 清晰；
- status 幂等、无副作用；
- 业务结果优先 JSON；
- 不依赖用户预装 Node/Python；需要时声明 runtime；
- 凭据与安装目录分离。

## 认证节奏

WorkBuddy 会：

1. 检查安装，必要时 init；
2. 执行 status；
3. 未登录则 auth；
4. 从输出提取认证 URL；
5. 每 3 秒轮询 status；
6. 最长等待 5 分钟。

官方特别指出：提取到认证 URL 后会立即终止 auth 子进程，因此 auth 子进程不能作为 OAuth 回调接收方。

推荐可选方案：

- 后台 Daemon
- Device Code Flow（官方标注推荐）
- 服务端 Token 存储

## 超时

- init：5 分钟
- auth：10 秒
- status：10 秒
- unAuth：30 秒
- 认证轮询：5 分钟

WorkBuddy 重启后只会自动执行 status 恢复连接，不会重新 auth，因此登录态必须跨重启持久化。
