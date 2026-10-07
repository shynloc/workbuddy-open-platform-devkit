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
├── .codebuddy-plugin/plugin.json
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

核心字段与 Expert 类似，但：

- `expertType = "team"`
- `teamInfo` 必填
- `teamInfo.leadAgent` 指定主理人
- `teamInfo.memberAgents` 列出成员
- `members` 包含全部团队成员（含主理人），每项提供 id/name/profession/avatar/role。

市场字段同样要求 displayName、profession、displayDescription、avatar、categoryId、defaultInitPrompt、plugin、tags、quickPrompts。

官方当前写明 tags 固定 3 个、quickPrompts 固定 3 个；defaultInitPrompt 必须与第一条 quickPrompt 一致。

## 3. settings.json

专家团必须提供 settings.json 设置主理人。具体字段应以官方模板/当前开放平台解析结果为准，生成包时不要凭历史记忆猜字段。

## 4. MCP / Connector dependencies

专家/专家团可声明：

- 自带 MCP：`dependencies.mcpServers`
- 已上架连接器：`dependencies.connectors`

如果 plugin.json 未声明 mcpServers，根目录 `.mcp.json` 可作为兜底。

自带 MCP 可通过 `x-workbuddy` 提供展示名、描述、icon 与 auth（oauth/token/none）元信息。真实 Token/密钥严禁硬编码。
