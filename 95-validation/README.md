# Real-world Validation

WB-OPDK 的目标不是只做“看起来合理”的规范整理。

本目录记录真实 WorkBuddy 平台验证：

```text
Local Schema / Validator
→ WorkBuddy Platform Parse
→ Runtime Test
→ Platform Review
→ Published Observation
→ OBSERVED 反哺 KB
```

## 当前入口

- `methodology.md` — 验证方法
- `ledger.md` — 总账
- `v1-readiness.md` — v1.0 真实验证缺口
- `record-template.yaml` — 统一记录模板
- `records/` — machine-readable 验证记录
- `wechat-article-publishing-skill.md` — 首个真实 Skill 案例

## 记录原则

- 只记录实际发生的状态；
- “平台接受上传”不等于“审核通过”；
- “审核通过”不等于“所有 Runtime 情况都验证”；
- OBSERVED 不冒充 OFFICIAL；
- 案例必须脱敏，不记录 Secret / Token / 用户隐私。

## 新建记录

```bash
python3 scripts/new_validation_record.py \
  --type expert \
  --name my-expert \
  --version 1.0.0

python3 scripts/validate_validation_records.py
```

## v1.0 目标

见 `v1-readiness.md`。
