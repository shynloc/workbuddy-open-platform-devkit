# Validation Ledger

| Asset | Type | Version | Local validation | Platform parse | Runtime | Review | Published | Record |
|---|---|---:|---|---|---|---|---|---|
| 微信公众号文章全流程发布 | Skill | 1.0.0 | ✅ Pass | ✅ Pass | — Not run | ⏳ Pending | — | [record](records/wechat-article-publishing-1.0.0.yaml) |

## Status semantics

- **Local validation**：WB-OPDK Validator / Schema / smoke test；
- **Platform parse**：WorkBuddy 开放平台当前解析器接受包/配置；
- **Runtime**：真实 WorkBuddy 客户端安装/召唤/连接并跑核心路径；
- **Review**：平台审核状态；
- **Published**：正式发布/市场可用。

这些状态必须分开记录。

> “Platform Parse Pass” 不等于审核通过；“审核通过”也不等于所有运行时行为已验证。
