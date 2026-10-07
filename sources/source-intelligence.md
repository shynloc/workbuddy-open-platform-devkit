# Source Intelligence

WB-OPDK 的 Source Intelligence 目标是：

```text
官方来源变化
→ 检测
→ 影响映射
→ STALE 候选
→ Review Artifact
→ 人/Agent 复核
→ 更新 KB / Schema / Template / Validator
→ 更新 Baseline
```

## 组成

- `official-sources.yaml` — 官方来源注册表
- `source-baseline.json` — 已审核页面 hash 基线
- `source-impact-map.json` — 上游来源 → 下游资产映射
- `check_official_sources.py` — URL / visible text hash 变化检测
- `build_source_change_report.py` — 影响分析和 Review Markdown
- `.github/workflows/source-watch.yml` — 定时执行

## 重要边界

Source Intelligence **不会自动修改知识库**。

原因：

- 页面样式变化不一定等于规则变化；
- 官方内部可能存在互相矛盾的描述；
- Schema / Validator 变化可能影响发布兼容；
- 自动同步容易把上游错误放大。

因此任何 upstream change 都先进入 Review。
