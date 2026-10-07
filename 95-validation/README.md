# Real-world Validation

WB-OPDK 的目标不是只做“看起来合理”的规范整理。

本目录记录真实 WorkBuddy 平台验证：

```text
本地规则 / Template / Validator
→ WorkBuddy 实际解析
→ Runtime / Review
→ OBSERVED 记录
→ 必要时反哺 KB
```

## 记录原则

- 只记录实际发生的状态；
- “平台接受上传”不等于“审核通过”；
- “审核通过”不等于“所有 Runtime 情况都验证”；
- OBSERVED 不冒充 OFFICIAL；
- 案例必须脱敏，不记录 Secret / Token / 用户隐私。

## v1.0 目标

至少各有一个真实验证案例：

- [x] Skill — 已提交平台并成功进入审核流程，审核结果待更新
- [ ] Expert
- [ ] Expert Team
- [ ] Connector
- [ ] Buddy App

Open API / Third-party App 另按独立集成测试记录。
