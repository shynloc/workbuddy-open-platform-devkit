---
name: cli-usage
display_name: CLI 连接器使用指南
display_name_en: CLI Connector Usage Guide
description: 指导 AI 正确调用当前 CLI 的业务命令、解析输出、恢复错误并确认高风险动作
description_zh: 指导 AI 正确使用 CLI 连接器的命令、参数、JSON 输出、错误恢复和确认边界
description_en: Guides the AI to use CLI commands, parameters, structured outputs, recovery paths and confirmation boundaries.
version: 1.0.0
author: Your Name
---

# CLI Usage

## Commands

按实际 CLI 描述每个业务命令：

- command
- parameters
- output
- exit code
- retry/recovery

优先让业务结果输出 JSON。

## Authentication

认证由 cli.json 的 auth/status/unAuth 处理。Skill 不要求用户在聊天里发送凭据。

## Confirmation

对删除、发布、发送、覆盖等有外部副作用的命令，执行前必须获得用户确认。
