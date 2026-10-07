---
title: WorkBuddy Expert Specification
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-expert
last_verified: 2026-10-07
status: VERIFIED
---

# Expert 官方规范

官方来源：https://open.workbuddy.cn/docs/expert

## 1. 基础结构

```text
my-expert/
├── .codebuddy-plugin/
│   └── plugin.json
├── avatars/
│   └── expert.png
├── agents/
│   └── my-expert.md
└── README.md
```

如果携带 Skill，可在插件包增加 skills/；若存在运行时依赖，可按官方专家/专家团依赖机制声明。

## 2. plugin.json 核心字段

基础字段：

- `name`：唯一标识，小写字母+连字符
- `expertType`：单专家填 `agent`
- `version`：语义化版本
- `description`：英文简述
- `author: {name,email}`
- `agents`：Agent MD 路径列表
- `agentName`：主 Agent 名称
- 可选 `skills` / `homepage` / `license` / `keywords`

市场字段：

- `displayName: {en,zh}`
- `profession: {en,zh}`
- `displayDescription: {en,zh}`（官方要求中文 40–50 字）
- `avatar`
- `categoryId`
- `defaultInitPrompt: {en,zh}`
- `plugin`（与 name 一致）
- `tags`（固定 3 个）
- `quickPrompts`（固定 3 个）

`defaultInitPrompt` 必须与 `quickPrompts` 第一条一致。

## 3. Agent MD frontmatter

官方当前要求：

- `name`（与文件名一致，不含 .md）
- `description`（英文，供 AI 判断何时激活）
- `displayName: {en,zh}`
- `profession: {en,zh}`

可选：

- `maxTurns`（默认 50）
- `skills`（预加载技能名称）

开发者不可自行给专家添加 tools，工具权限由系统统一分配。

## 4. 头像

- PNG 推荐，也支持 JPG
- 512×512 px
- 单张 ≤ 500KB
- 专业自然的漫画/插画风格
- 与角色定位一致

## 5. categoryId

官方当前列出 15 个分类：

01-ProductDesign、02-Engineering、03-GameSpatial、04-DataAI、05-MarketingGrowth、06-ContentCreative、07-SalesCommerce、08-FinanceInvestment、09-OperationsHR、10-ProjectQuality、11-SecurityCompliance、12-IndustryConsultant、13-TencentZone、14-WorldWise、15-Education。
