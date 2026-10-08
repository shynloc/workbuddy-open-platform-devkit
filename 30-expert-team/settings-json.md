---
title: Expert Team Lead Settings File
knowledge_type: OBSERVED
last_verified: 2026-10-08
status: VERIFIED
official_sources:
  - workbuddy-expert-team
---

# Expert Team Lead Settings File

## Current effective rule

**Team 型专家必须在 plugin root 下提供 `settings.json`（复数）。**

当前推荐结构：

```text
my-team/
├── .codebuddy-plugin/
│   └── plugin.json
├── agents/
├── avatars/
├── settings.json
└── README.md
```

当前 WB-OPDK 使用：

```json
{
  "agent": "my-team-team-lead"
}
```

其中 `agent` 必须与：

- `plugin.json.agentName`
- `plugin.json.teamInfo.leadAgent`

保持一致。

## Evidence

### Official page

WorkBuddy Expert Team 官方页面基础结构明确写：

```text
settings.json    # 设置主理人（必须）
```

官方来源：

https://open.workbuddy.cn/docs/expert-team

### Official downloadable template inconsistency

同页提供的 `trading-team.zip` 曾实际包含：

```text
setting.json
```

内容：

```json
{
  "agent": "trading-team-lead"
}
```

### Real platform parser — 2026-10-08

WB-OPDK 的真实候选 `ai-editorial-team-v1.0.0.zip` 使用 `setting.json` 上传 WorkBuddy 开放平台后，解析器返回：

```text
settings.json 不存在或无法读取（Team 型专家必须在 plugin root 下提供 settings.json）
```

这条真实平台证据明确裁决了文件名：

> 当前平台解析器要求 `settings.json`，不接受仅提供 `setting.json` 的 Team 包。

## WB-OPDK rule

1. Starter 使用 `settings.json`；
2. Validator 强制要求 `settings.json`；
3. 如果发现 `setting.json`，Validator 报错；
4. 当前 `settings.json` 内容沿用官方模板中已知的 `agent` 字段；
5. 如果平台下一步对 JSON schema 给出新的错误，再继续基于真实证据修订。

详见：`sources/known-inconsistencies.md`。

## Review / publication evidence — 2026-10-08

修正为 `settings.json` 后，AI 编辑部 Expert Team 已完成：

```text
Local Validation
→ Platform Parse
→ Platform Review
→ Published
```

全部通过。

因此当前 WB-OPDK 对 Team 主理人设置文件的执行结论是：

> **plugin root 必须提供 `settings.json`；当前 `{"agent":"<lead>"}` 结构已经随真实 Team 包通过平台审核并发布。**

这仍然不意味着官方旧版 `trading-team.zip` 中的 `setting.json` 应被覆盖或删除；它继续作为上游模板与当前 Runtime 不一致的历史证据保留在 Template Audit 中。
