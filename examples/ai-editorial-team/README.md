# AI Editorial Team — Real Validation Candidate

这是 WB-OPDK 为 v1.0 真实平台验证准备的 **Expert Team 候选资产**。

团队：

- 总编辑（Lead）
- 研究编辑
- 写作编辑
- 视觉总监
- 发布编辑

## 本次验证重点

1. Expert Team package 是否被 WorkBuddy 当前解析器接受；
2. 当前平台是否接受修正后的 `settings.json`；首次上传使用 `setting.json` 已被明确拒绝；
3. Lead 是否真正调度 Member；
4. Member 是否按角色边界工作；
5. quickPrompts 是否能触发不同团队协作路径；
6. 市场字段与头像是否正常；
7. 平台审核反馈。

## 本地检查

```bash
python3 scripts/validate_asset_schemas.py examples/ai-editorial-team
python3 scripts/validate_expert_team.py examples/ai-editorial-team
python3 scripts/release_check.py examples/ai-editorial-team --dist dist --side-effect-review not-applicable
```

## 真实平台测试建议

### Prompt 1 — 完整生产

“我有一组关于 AI Agent 工具链的笔记，请团队把它做成一篇完整文章，并给出视觉和发布方案。”

观察是否形成 Research → Writing → Design → Publishing。

### Prompt 2 — 已有草稿评审

“这是我的草稿，让整个编辑部评审并完善，但不要改变我的核心观点。”

观察 Lead 是否避免重复调用、Writer 是否保护作者声音。

### Prompt 3 — 研究型选题

“先研究 WorkBuddy Connector 的产品化要求，再决定这个题怎么写。”

观察 Research Editor 是否先介入。

## 记录

上传/运行后，新建：

```bash
python3 scripts/new_validation_record.py \
  --type expert-team \
  --name ai-editorial-team \
  --version 1.0.0
```

只记录真实发生的状态。

## 首次 Platform Parse 结果 — 2026-10-08

第一版候选包沿用了官方下载模板中的 `setting.json`（单数）。

WorkBuddy 开放平台解析失败：

```text
settings.json 不存在或无法读取（Team 型专家必须在 plugin root 下提供 settings.json）
```

已修正为：

```text
settings.json
```

内容：

```json
{
  "agent": "ai-editorial-team-team-lead"
}
```

下一次上传应使用修正版候选包；平台是否继续接受其 JSON 内容，以实际解析结果为准。
