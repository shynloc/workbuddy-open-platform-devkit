# Expert Team Template

这是一个最小三角色 WorkBuddy Expert Team 起点。

## 官方文件名差异

截至 2026-10-07：

- 官方 Expert Team 页面基础结构写 `settings.json`；
- 同页官方 `trading-team.zip` 实际使用 `setting.json`；
- 官方模板内容为 `{"agent":"trading-team-lead"}`。

因此本 starter 跟随**当前官方可下载模板**，使用：

```text
setting.json
```

WB-OPDK Validator 同时接受单数/复数两种官方来源，但禁止同时放两个文件。

详见：

- `30-expert-team/settings-json.md`
- `sources/known-inconsistencies.md`

## 使用

1. 修改 `.codebuddy-plugin/plugin.json` 中的名称、职业、描述、分类、成员；
2. 主理人文件名建议保留“团队前缀 + team-lead”的结构；
3. 更新 `setting.json.agent`，必须与 `agentName/teamInfo.leadAgent` 一致；
4. 为团队和每个成员准备头像：
   - PNG/JPG
   - 512×512
   - ≤500KB
5. tags 先按当前字段表保持 3 条；
6. quickPrompts 保持 3 条，第一条等于 defaultInitPrompt；
7. 运行：

```bash
python3 scripts/validate_expert_team.py path/to/team
```

## 注意

本模板不包含二进制头像文件。发布当天仍需再次核对官方 Expert Team 页面和开放平台实际解析行为。

官方来源：https://open.workbuddy.cn/docs/expert-team
