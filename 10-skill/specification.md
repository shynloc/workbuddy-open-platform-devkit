---
title: WorkBuddy Skill Specification
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-skill
last_verified: 2026-10-27
status: VERIFIED
---

# Skill 官方规范

官方来源：https://open.workbuddy.cn/docs/skill

## 1. 基础结构

```text
{skill-name}/
├── SKILL.md              # 必须
├── references/           # 可选
├── scripts/              # 可选
└── templates/            # 可选
```

`SKILL.md` 使用 YAML frontmatter + Markdown 正文。

## 2. Frontmatter

官方字段表当前必填：

- `name`
- `display_name`
- `display_name_en`
- `description`
- `description_zh`
- `description_en`
- `version`
- `author`

可选：

- `allowed-tools`
- `examples_zh`
- `examples_en`

`description_zh` / `description_en` 写明展示在技能详情页。`examples_zh` / `examples_en` 展示在详情页「试试这样用」。

2026-10-27 的字段表和示例都不再包含 `category`、`disable-model-invocation`、`user-invocable`。中英文页面一致。本仓库不把这三项从历史包里判为非法，也未观察到运行时拒绝它们。字段表以当前官方页为准。

官方示例把 `display_name_en` 写成 `切英文版展示名称`（冒号后没有空格），并把 `example` 写成 `exmaple`。示例缺陷见 `sources/known-inconsistencies.md`。模板使用可提交的英文展示名，不复制这两处笔误。

### 语义

- `description`：应明确用途和触发词，AI 用来判断何时激活；
- `allowed-tools`：工具白名单，逗号分隔；
- `examples_zh` / `examples_en`：详情页上的使用案例，不是字段表里的必填项。

## 3. 子资源

### references/

存放补充知识。官方指定在 SKILL.md 中用：

```text
@references/xxx.md
```

引用。

### scripts/

可执行脚本。AI 通过 Bash 执行，应在 SKILL.md 明确命令与参数。

### templates/

标准模板、报告/工作流模板等可复用资产。

## 4. 市场行为

Skill 可在 WorkBuddy 技能市场安装，安装后可在对话中调用。开放平台 ZIP 解析失败时，优先检查基础结构与子资源目录。
