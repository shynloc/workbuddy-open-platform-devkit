---
name: connector-usage
display_name: 连接器使用指南
display_name_en: Connector Usage Guide
description: 指导 AI 正确使用 OAuth MCP 连接器的核心工具、错误恢复和确认边界
description_zh: 指导 AI 正确调用 OAuth MCP 连接器并处理授权失效与高风险操作
description_en: Guides the AI to use the OAuth MCP connector, recover from authorization failures, and confirm high-risk actions.
version: 1.0.0
author: Your Name
---

# Connector Usage

## Authentication

OAuth 由 WorkBuddy 与 MCP Server 按标准流程完成。若工具返回授权失效，应引导用户重新连接，不要要求用户在聊天中发送 Token。

## Core tools

在这里按真实 MCP Tool 列出用途、参数、返回和错误恢复。

## Confirmation

产生不可逆或明显外部副作用的 Tool，在执行前取得用户明确确认。
