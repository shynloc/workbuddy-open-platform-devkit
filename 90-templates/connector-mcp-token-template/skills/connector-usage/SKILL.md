---
name: connector-usage
display_name: 连接器使用指南
display_name_en: Connector Usage Guide
description: 指导 AI 正确使用当前连接器、处理认证错误并在高风险操作前获得用户确认
description_zh: 指导 AI 正确使用连接器核心能力、参数、错误恢复和确认规则
description_en: Guides the AI to use connector capabilities, parameters, error recovery and confirmation rules correctly.
version: 1.0.0
author: Your Name
---

# Connector Usage

## Authentication

连接器由 WorkBuddy 收集用户凭据并注入 MCP 配置。不要要求用户把 Token 发进聊天。

## Core tools

在这里按真实 MCP Tool 描述：用途、参数、返回、错误恢复。

## Confirmation

任何会产生不可逆或明显外部副作用的操作，执行前必须得到用户明确确认。
