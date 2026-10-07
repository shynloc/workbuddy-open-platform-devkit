# Source Policy

WB-OPDK 使用 Official-first 策略。

## 权威层级

1. WorkBuddy 当前官方开放平台文档
2. 开放平台实际 Schema / 后台行为
3. VERIFIED 本地知识
4. OBSERVED 实测
5. DERIVED 工程建议
6. EXPERIMENTAL 未充分验证方案

## 知识类型

- `OFFICIAL`：官方明确写出的规则、字段、限制、流程
- `DERIVED`：基于官方信息整理出的工程决策/SOP
- `OBSERVED`：真实调试、审核、运行中观察到的行为
- `EXPERIMENTAL`：尚未形成稳定证据的尝试
- `STALE`：对应上游发生变化，需重新核验
- `DEPRECATED`：官方已废弃

## 冲突处理

当官方文档与平台运行时行为冲突时：

1. 不静默“修正”官方文档；
2. 单独记录 `official_doc_says` 与 `runtime_observed`；
3. 将结论标为 `OBSERVED` / `STALE`；
4. 在影响发布/安全/权限时要求人工复核。

## 禁止事项

- 不把推断写成 OFFICIAL；
- 不把历史截图当成当前规则；
- 不提交 Secret、Token、AppSecret；
- 不把官网整页原文大段复制进本仓库；保存来源、结构化事实和工程化解释即可。
