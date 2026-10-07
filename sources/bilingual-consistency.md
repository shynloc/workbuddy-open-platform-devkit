# Official zh/en Consistency

WorkBuddy 官方开放平台同时存在中文和英文文档。

WB-OPDK 不做自动机器翻译，也不假设两边永远同步。

## 当前检查范围

`scripts/check_bilingual_docs.py` 检查：

- 两边页面是否可访问；
- 字段名 / 文件名 / endpoint / OAuth 参数等技术字面量是否同时存在；
- 页面可见文本体积是否出现极端差异。

它**不证明全文语义完全一致**。

## 为什么这样做

技术字段最容易直接影响：

- Schema
- Starter Template
- Validator
- Open API 集成
- WorkBuddy 最低版本
- 发布兼容性

如果中文页和英文页出现不一致，应：

1. 查看两边当前原文；
2. 判断是翻译延迟、文档更新延迟还是实际规范冲突；
3. 写入 `known-inconsistencies.md`；
4. 不擅自把其中一边当成唯一真相；
5. 以开放平台实际 Schema / Runtime 作为进一步验证依据。
