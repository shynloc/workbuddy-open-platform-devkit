---
name: example-connector
display_name: 示例连接器使用指南
display_name_en: Example Connector Guide
description: Guide the agent to use the Example Connector safely and correctly.
description_zh: 指导 AI 正确调用示例连接器，包括认证前置、工具选择、参数、错误恢复与高风险操作确认。
description_en: Guide the AI to use the Example Connector, including authentication, tool selection, errors, and confirmation gates.
category: productivity
version: 1.0.0
author: Your Name
---

# Example Connector

## When to use

Use this Skill when the user asks to read or change data in Example Service.

## Authentication

If the connector is not connected, ask the user to complete the WorkBuddy connection flow. Never ask the user to paste credentials into chat.

## Tool selection

Document each MCP tool here:

### list_items

Purpose:
Arguments:
Returns:
Common errors:

### create_item

Purpose:
Arguments:
Returns:
Side effects:

Before any irreversible or externally visible action, obtain explicit confirmation when appropriate.

## Failure handling

- Authentication expired → reconnect
- Invalid parameter → correct parameters; do not retry blindly
- Timeout → retry only if the operation is idempotent
- Unknown write result → query current state before retrying
