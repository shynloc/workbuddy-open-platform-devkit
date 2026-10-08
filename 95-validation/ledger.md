# Validation Ledger

| Asset | Type | Version | Local validation | Platform parse | Runtime | Review | Published | Record |
|---|---|---:|---|---|---|---|---|---|
| 微信公众号文章全流程发布 | Skill | 1.0.0 | ✅ Pass | ✅ Pass | — Not run | ✅ Approved | ✅ Published | [record](records/wechat-article-publishing-1.0.0.yaml) |
| AI 内容主编 | Expert | 1.0.0 | ✅ Pass | ✅ Pass | — Not run | ✅ Approved | ✅ Published | [record](records/ai-content-editor-1.0.0.yaml) |
| AI 编辑部 | Expert Team | 1.0.0 | ✅ Pass | ✅ Pass after settings.json fix | — Not run | ✅ Approved | ✅ Published | [record](records/ai-editorial-team-1.0.0.yaml) |

## Candidate Build Evidence

Expert + Expert Team candidate packages were built by:

https://github.com/shynloc/workbuddy-open-platform-devkit/actions/runs/37669725863

Artifact:

- name: `workbuddy-v1-candidates`
- artifact id: `11504640834`
- digest: `sha256:98b7c2cf2417a0eb7a5f93c7f5f7edf67b79e2255d36060c2f4726d3c1f36cd3`

## Status semantics

- **Local validation**：WB-OPDK Validator / Schema / Release Check；
- **Platform parse**：WorkBuddy 开放平台当前解析器接受包/配置；
- **Runtime**：真实 WorkBuddy 客户端安装/召唤/连接并跑核心路径；
- **Review**：平台审核状态；
- **Published**：正式发布/市场可用。

这些状态必须分开记录。

> “Platform Parse Pass” 不等于审核通过；“审核通过”也不等于所有运行时行为已验证。