---
title: WorkBuddy Expert Team Specification
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-expert-team
last_verified: 2026-10-07
status: VERIFIED
---

# Expert Team 官方规范

官方来源：https://open.workbuddy.cn/docs/expert-team

## 1. 基础结构

```text
my-team/
├── .codebuddy-plugin/
│   └── plugin.json
├── avatars/
│   ├── team.png
│   ├── team-lead.png
│   └── member-a.png
├── agents/
│   ├── {team}-team-lead.md
│   ├── member-a.md
│   └── member-b.md
├── skills/            # 可选
├── .mcp.json          # 可选
├── bin/               # 可选
├── settings.json      # 必须
└── README.md
```

主理人 Agent 文件名应带专家团前缀，不应使用通用 `team-lead.md`。

## 2. plugin.json

必须包含：

- `name`
- `expertType = "team"`
- `version`
- `description`
- `author`
- `agents`
- `agentName`
- `teamInfo`
- 市场展示字段
- `members`

`teamInfo`：

```json
{
  "leadAgent": "my-team-team-lead",
  "memberAgents": ["member-a", "member-b"]
}
```

`members` 必须包含主理人和所有成员，每项：

- id
- name {en,zh}
- profession {en,zh}
- avatar
- role = lead | member

官方字段表当前要求：

- tags：固定 3 个
- quickPrompts：固定 3 个
- defaultInitPrompt 与第一条 quickPrompt 一致
- displayDescription 中文 40–50 字

> 官方 trading-team 示例当前展示了 4 个 tags，但同页字段表写“固定 3 个”。本仓库把该差异记录在 `sources/known-inconsistencies.md`，发布前应再次看当前平台解析规则。

## 3. Agent MD

主理人和成员都使用 YAML frontmatter + Markdown。

至少包含：

- name
- description
- displayName {en,zh}
- profession {en,zh}

## 4. settings.json

官方目录规范明确要求 `settings.json`，用于设置主理人。

但当前公开页面正文没有给出该文件的完整字段 schema；官方同时提供 `trading-team.zip` 模板作为下载样例。

因此：

- 不凭经验伪造 settings.json 字段；
- 开发时以当前官方模板 ZIP / 平台解析行为为准；
- 字段被官方页面明确公开或官方模板内容被验证后，再固化 schema。

详见：`30-expert-team/settings-json.md`。

## 5. MCP / Connector dependencies

专家/专家团可声明：

- 自带 MCP：`dependencies.mcpServers`
- 已上架连接器：`dependencies.connectors`

如果 plugin.json 未声明 mcpServers，根目录 `.mcp.json` 可作为 fallback。

自带 MCP 可通过 `x-workbuddy` 提供展示名、描述、icon 与 auth（oauth/token/none）元信息。真实 Token/密钥严禁硬编码。
