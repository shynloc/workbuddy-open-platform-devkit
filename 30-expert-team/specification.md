---
title: WorkBuddy Expert Team Specification
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-expert-team
last_verified: 2026-10-08
status: VERIFIED
---

# Expert Team 官方规范

官方来源：https://open.workbuddy.cn/docs/expert-team

## 1. 基础结构

官方页面当前展示：

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
├── settings.json      # 页面结构写法
└── README.md
```

但同页官方可下载 `trading-team.zip` 当前实际使用 `setting.json`（单数）。这是官方文档内部差异，不应静默消解。详见：

`sources/known-inconsistencies.md`

WB-OPDK starter template 当前跟随官方可下载模板使用 `setting.json`。

## 2. plugin.json

必填基础字段：

- `name`
- `expertType = "team"`
- `version`
- `description`
- `author`
- `agents`
- `agentName`
- `teamInfo`

市场字段：

- displayName
- profession
- displayDescription
- avatar
- categoryId
- defaultInitPrompt
- plugin
- tags
- quickPrompts

WB-OPDK Validator 还要求 `members` 与团队成员定义保持一致，因为当前官方示例/团队结构使用该字段承载成员市场信息。

`teamInfo`：

```json
{
  "leadAgent": "my-team-team-lead",
  "memberAgents": ["member-a", "member-b"]
}
```

当前官方字段表要求：

- tags：固定 3 个
- quickPrompts：固定 3 个
- defaultInitPrompt 与第一条 quickPrompt 一致
- displayDescription 中文 40–50 字

> 官方 trading-team 示例当前 tags 数量与字段表存在差异，见 `sources/known-inconsistencies.md`。

## 3. Agent MD

主理人和成员都使用 YAML frontmatter + Markdown。

至少包含：

- name
- description
- displayName {en,zh}
- profession {en,zh}

主理人文件名建议带团队前缀，避免多个 Team 安装后出现通用名称冲突。

## 4. Lead 设置文件

当前有效规则：

```text
plugin root/
└── settings.json    # 必须
```

当前采用的内容结构来自官方 Team 模板中的已知字段：

```json
{
  "agent": "my-team-team-lead"
}
```

要求：

1. 文件名必须是 `settings.json`（复数）；
2. 必须位于 Team 插件根目录；
3. JSON 必须可读取；
4. `agent` 必须与 `plugin.json.agentName`、`teamInfo.leadAgent` 一致；
5. 不再打包 `setting.json`。

证据来源同时包括官方页面与 2026-10-08 的真实平台解析结果。

## 5. MCP / Connector dependencies

专家团可声明：

- 自带 MCP：`dependencies.mcpServers`
- 已上架连接器：`dependencies.connectors`

如果 plugin.json 未声明 mcpServers，根目录 `.mcp.json` 可作为 fallback。

自带 MCP 可通过 `x-workbuddy` 提供展示名、描述、icon 与 auth（oauth/token/none）元信息。真实 Token/密钥严禁硬编码。