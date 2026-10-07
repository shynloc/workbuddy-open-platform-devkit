# Deprecation

资产不应无限期累积。

## Deprecation triggers

- 官方平台移除能力
- 上游 API 关闭
- 安全架构无法继续维护
- 被新资产完全替代
- 长期无人维护

## Process

```text
Announce
→ stop new adoption
→ migration guide
→ maintenance window
→ disable risky writes
→ retire
```

## Knowledge state

对应 WB-OPDK 页面改为：

```yaml
status: DEPRECATED
```

并写：

- replacement
- migration steps
- last supported version
- retirement date

不要直接删除历史文档，否则 Agent 无法解释旧包/旧配置。
