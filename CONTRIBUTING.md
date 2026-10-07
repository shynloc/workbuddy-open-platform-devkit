# Contributing

感谢帮助维护 WB-OPDK。

## 基本原则

1. 官方规则必须提供对应 WorkBuddy 官方来源 URL。
2. 官方未明确规定的内容必须标记为 `DERIVED`、`OBSERVED` 或 `EXPERIMENTAL`。
3. 当官方文档变化时，不直接自动覆盖；先比较、确认影响范围，再更新相关知识和模板。
4. 不提交任何真实 Token、Secret、AppSecret、用户数据或内部凭据。
5. 实战案例请脱敏。

## 建议提交格式

每个知识文档建议包含：

```yaml
---
title: ...
knowledge_type: OFFICIAL | DERIVED | OBSERVED | EXPERIMENTAL
last_verified: YYYY-MM-DD
status: VERIFIED | STALE | DEPRECATED
official_sources:
  - source-id
---
```

如果发现“官方文档”和“平台实际行为”不一致，请同时记录二者，不要静默选择一个结论。

## Source IDs and impact mapping

新增 OFFICIAL / DERIVED 知识页时：

1. 优先引用 `sources/official-sources.yaml` 中已有 source id；
2. 如果新增官方来源，必须同时更新：
   - `sources/official-sources.yaml`
   - `sources/source-impact-map.json`
   - 人工核验后的 `sources/source-baseline.json`
3. 运行：

```bash
python3 scripts/validate_source_registry.py
```

## License / upstream boundary

MIT 只覆盖本项目自身原创代码、模板与工程化文档。官方 WorkBuddy 文档、商标、图片、ZIP 模板等上游材料不因被引用而转为 MIT。

见：`NOTICE.md`
