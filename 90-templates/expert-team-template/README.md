# Expert Team Template

这是一个最小三角色 WorkBuddy Expert Team 起点。

## settings.json — 当前有效要求

WorkBuddy Expert Team 官方页面要求 Team 插件根目录提供：

```text
settings.json
```

2026-10-08 的真实开放平台解析进一步确认：

> 如果只提供 `setting.json`（单数），平台会报错：
>
> `settings.json 不存在或无法读取（Team 型专家必须在 plugin root 下提供 settings.json）`

因此本 Starter **只使用 `settings.json`（复数）**。

当前结构：

```json
{
  "agent": "your-expert-team-team-lead"
}
```

`agent` 必须与：

- `plugin.json.agentName`
- `plugin.json.teamInfo.leadAgent`

一致。

> 官方可下载的 `trading-team.zip` 曾使用 `setting.json`，已确认与当前平台解析器不一致。详见：
> - `30-expert-team/settings-json.md`
> - `sources/known-inconsistencies.md`

## 使用

1. 修改 `.codebuddy-plugin/plugin.json` 中的名称、职业、描述、分类、成员；
2. 主理人文件名建议保留“团队前缀 + team-lead”的结构；
3. 更新 `settings.json.agent`；
4. 为团队和每个成员准备头像：
   - PNG/JPG
   - 512×512
   - ≤500KB
5. tags 按当前字段表保持 3 条；
6. quickPrompts 保持 3 条，第一条等于 defaultInitPrompt；
7. 运行：

```bash
python3 scripts/validate_expert_team.py path/to/team
```

## 注意

本模板不包含二进制头像文件。发布当天仍需再次核对官方 Expert Team 页面和开放平台实际解析行为。

官方来源：https://open.workbuddy.cn/docs/expert-team
