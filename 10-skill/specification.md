---
title: WorkBuddy Skill Specification
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-skill
last_verified: 2026-10-07
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

官方当前必填：

- `description`
- `description_zh`
- `description_en`
- `version`
- `author`

可选：

- `name`
- `allowed-tools`
- `disable-model-invocation`
- `user-invocable`

官方示例还包含 `display_name`、`display_name_en`、`category`。

### 语义

- `description`：应明确用途和触发词，AI 用来判断何时激活；
- `allowed-tools`：工具白名单，逗号分隔；
- `disable-model-invocation: true`：模型不能自动触发，只能用户手动调用；
- `user-invocable: false`：隐藏菜单，仅供 AI 内部使用。

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
