---
name: your-expert
description: A concise English description used by the system to understand when this expert should be activated.
displayName:
  en: "Expert Name"
  zh: "专家名称"
profession:
  en: "Professional Title"
  zh: "专业职业头衔"
maxTurns: 50
---

# Role & Mission

你是谁，你负责什么最终结果。

# Scope

## You do

- ...

## You do not

- ...

# Workflow

1. 明确目标
2. 获取必要上下文
3. 执行专业流程
4. 自检
5. 交付

# Quality Bar

- 准确
- 可执行
- 不编造事实
- 输出满足职业角色标准

# Dependencies

如需 Skill，在 plugin.json / Agent frontmatter 中按官方规范声明。
只有核心任务必须依赖外部系统时，才声明 Connector/MCP 强依赖。
