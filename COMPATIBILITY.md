# Compatibility Policy

WB-OPDK 同时面对三种变化：

1. WorkBuddy 官方文档变化；
2. WorkBuddy 客户端/开放平台解析器变化；
3. 上游模板与 Runtime 行为变化。

## Compatibility classes

### Document-compatible

规则来自当前官方文档，但尚未经过真实 Runtime 验证。

### Parser-validated

真实 WorkBuddy 开放平台解析器已经接受对应结构。

### Runtime-validated

已在真实 WorkBuddy 客户端完成核心运行路径。

### Review-validated

已通过平台审核。

### Published-observed

已正式发布，并在真实用户环境观察。

## Version policy

涉及 WorkBuddy 最低版本的字段必须：

- 记录官方最低版本；
- 在 Connector 中正确声明 `minWorkbuddyVersion`；
- 不把新字段默认用于旧客户端。

全局知识文档使用 `last_verified` 记录上游核验日期。

## Breaking upstream change

发现以下任一情况：

- Source Watch hash 改变；
- Parser 返回未知/新错误；
- 官方模板改变；
- Runtime 行为与 KB 冲突；

应：

```text
Detect
→ Mark affected knowledge STALE
→ Review upstream
→ Update spec/template/schema/validator
→ CI
→ Real validation
→ VERIFIED
```

## Support target

WB-OPDK 不承诺支持所有历史 WorkBuddy 版本。

默认目标是：

> 当前公开开放平台规范 + 当前主流/最新可用 WorkBuddy Runtime。

需要支持旧版本时，必须明确记录对应版本范围和降级策略。
