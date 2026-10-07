---
title: Expert Team Lead Settings File
knowledge_type: OFFICIAL
last_verified: 2026-10-07
status: VERIFIED
official_sources:
  - workbuddy-expert-team
---

# Expert Team Lead Settings File

WorkBuddy 当前两个**官方来源彼此不一致**：

## 官方页面

Expert Team 基础结构写：

```text
settings.json    # 设置主理人（必须）
```

页面正文当前没有给出这个文件的字段 schema。

## 官方可下载模板

同页提供的 `trading-team.zip`，经 WB-OPDK 官方模板审计于 2026-10-07 实际验证：

```text
trading-team/
└── setting.json
```

注意文件名是 **`setting.json`（单数）**。

内容为：

```json
{
  "agent": "trading-team-lead"
}
```

审计哈希：

- ZIP SHA256：`4935e7b86b7d32c47d03bb7c70c24adc29a41dc7d74fb9a97596e6d5a3e04345`
- setting.json SHA256：`168767b04cffdc12b5c9f6b61d6a110208d58c3e0a1699dffa6e61a8091ca23b`

## WB-OPDK 执行规则

当前采用“兼容但不掩盖冲突”的策略：

1. Validator 接受 `setting.json` 或 `settings.json`；
2. 两者同时出现视为歧义并报错；
3. 当前 starter template 跟随官方可下载模板，使用 `setting.json`；
4. `setting.json.agent` 必须与 `plugin.json.agentName`、`teamInfo.leadAgent` 一致；
5. 如果未来官方文档或模板统一命名，应更新本文件并重新生成 starter。

详见：`sources/known-inconsistencies.md`。

> 不要把 CodeBuddy CLI 的其他项目级 settings 文件拿来类比此处字段。
