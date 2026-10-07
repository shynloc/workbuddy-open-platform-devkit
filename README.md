# WB-OPDK — WorkBuddy Open Platform Development Kit

> **一个面向 AI Agent 与开发者的 WorkBuddy 开放平台工程知识库与开发工具包。**  
> 基于 **WorkBuddy 开放平台官方文档** 进行整理、工程化和持续校验；官方文档始终是平台规则的最高可信上游。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Source](https://img.shields.io/badge/Upstream-WorkBuddy%20Official-19c37d)](https://open.workbuddy.cn/docs/what-is-open-platform)

## 这是什么？

WB-OPDK（WorkBuddy Open Platform Development Kit）不是 WorkBuddy 官方文档的镜像，也不是官方项目。

它的目标是把分散在开放平台中的规范，整理为 **Agent 可快速读取、开发者可直接执行、可以持续追溯和更新** 的工程知识库，覆盖从需求判断到开发、测试、打包、审核、发布与版本维护的完整过程。

你可以把它理解成：

```text
WorkBuddy 官方文档
        ↓
   Official Facts
        ↓
工程化解释与决策树
        ↓
SOP / Checklist / Template
        ↓
Skill / Expert / Expert Team / Connector / Buddy App / Open API
        ↓
测试 → 打包 → 审核 → 发布 → 维护
```

## Source of Truth

本项目采用 **Official-first** 原则：

1. **WorkBuddy 当前官方开放平台文档** — 最高可信来源；
2. **开放平台实际 Schema / 后台行为** — 用于发现文档与运行时差异；
3. **本仓库已验证知识** — 对官方规则的工程化整理；
4. **实测记录** — 明确标记为 Observed，不冒充官方规则；
5. **工程建议** — 明确标记为 Derived / Experimental。

如果本仓库内容与官方最新文档发生冲突，请以官方文档为准，并提交 Issue / PR 更新本仓库。

### 官方入口

- 开放平台概述：https://open.workbuddy.cn/docs/what-is-open-platform
- Skill：https://open.workbuddy.cn/docs/skill
- 专家：https://open.workbuddy.cn/docs/expert
- 专家团：https://open.workbuddy.cn/docs/expert-team
- 连接器：https://open.workbuddy.cn/docs/connector
- Buddy 应用：https://open.workbuddy.cn/docs/buddy-app
- 第三方应用：https://open.workbuddy.cn/docs/third-party-app
- Open API：https://open.workbuddy.cn/docs/openapi

完整来源注册表见 [`sources/official-sources.yaml`](sources/official-sources.yaml)。

## 适合谁？

- 想开发 WorkBuddy Skill 的个人开发者
- 想把专业方法论封装为 Expert / Expert Team 的创作者
- 已有 MCP / API，希望产品化为 WorkBuddy Connector 的团队
- 想做垂直行业 Buddy App 的产品团队
- 想让网站、App、硬件接入 WorkBuddy Open API 的开发者
- 需要一个本地 AI Agent 快速获得 WorkBuddy 开发上下文的人

## 先判断你该做什么

```text
只是告诉 AI「怎么完成一类任务」
        ↓
      Skill

希望用户召唤一个固定专业角色
        ↓
      Expert

需要多个独立专业角色协作
        ↓
   Expert Team

需要连接外部 API / SaaS / MCP
        ↓
    Connector

要构建完整垂直行业 AI 工作台
        ↓
    Buddy App

要让自己的 App / 网站 / 硬件调用 WorkBuddy
        ↓
 Third-party App / Open API
```

更完整的判断逻辑见 [`00-platform/capability-decision-tree.md`](00-platform/capability-decision-tree.md)。

## 给 AI Agent：从这里开始

如果你是 AI Agent，请先读：

**[`START_HERE.md`](START_HERE.md)**

不要一次性加载整个仓库。先确定产品类型与当前开发阶段，再按需读取对应目录。

示例：

```text
用户：我有一个微信公众号 MCP，想把它上架 WorkBuddy。

Agent：
1. 读取 START_HERE.md
2. 读取 00-platform/capability-decision-tree.md
3. 判定为 Connector
4. 读取 40-connector/
5. 读取 70-release-engineering/
6. 按官方来源核验当前规则
7. 输出需求分析 → 架构 → 开发包 → QA → 发布资料
```

## 知识分类

仓库中的知识应明确区分：

| 状态 | 含义 |
|---|---|
| `OFFICIAL` | 官方文档明确规定 |
| `DERIVED` | 基于官方规则整理出的工程流程或建议 |
| `OBSERVED` | 实际开发、调试或审核中观察到的行为 |
| `EXPERIMENTAL` | 尚未充分验证的方案 |
| `STALE` | 对应官方来源发生变化，等待重新验证 |
| `DEPRECATED` | 官方已经废弃或不再推荐 |

## 从需求到发布的统一流程

```text
01 Requirement Intake
        ↓
02 Product Type Decision
        ↓
03 Product Brief / PRD
        ↓
04 Architecture
        ↓
05 Build
        ↓
06 Local Validation
        ↓
07 Runtime Test
        ↓
08 Marketplace / Release Materials
        ↓
09 Packaging
        ↓
10 Submission QA
        ↓
11 Platform Review
        ↓
12 Review Fix
        ↓
13 Publish
        ↓
14 Version & Operations
```

开放平台官方概述同样将开发流程概括为：入驻与认证、创建业务类型、完善配置、测试验证、提交审核、上线与持续维护。本仓库在此基础上进一步拆成可执行的工程阶段。

## 目录结构

```text
workbuddy-open-platform-devkit/
├── START_HERE.md
├── README.md
├── LICENSE
├── CONTRIBUTING.md
│
├── 00-platform/              # 平台概念、产品地图、能力决策树
├── 10-skill/                 # Skill 开发
├── 20-expert/                # Expert 开发
├── 30-expert-team/           # Expert Team 开发
├── 40-connector/             # Connector / MCP / Auth
├── 50-buddy-app/             # Buddy App 产品与配置
├── 60-open-api/              # 第三方应用 / OAuth / Open API
├── 70-release-engineering/   # QA、打包、审核、发布、版本维护
├── 80-recipes/               # 端到端实战配方
├── 90-templates/             # 可复用模板
└── sources/                  # 官方来源注册表与更新状态
```

当前仓库先建立骨架与治理规则，后续按官方文档逐模块补全。

## 更新策略

本项目不会自动把官网内容覆盖进知识库。

推荐更新流程：

```text
定期检查官方 Sources
        ↓
正文 hash / 结构发生变化
        ↓
标记受影响文档为 STALE
        ↓
比较官方变化
        ↓
更新知识库 / 模板 / 校验器
        ↓
运行验证
        ↓
重新标记 VERIFIED
        ↓
记录 CHANGELOG
```

目标是做到：**可追溯、可复核、可更新**，而不是维护一份很快过期的静态快照。

## 项目边界与声明

- 本项目是非官方、社区性质的开发知识库。
- 本项目基于公开的 WorkBuddy 开放平台官方文档进行归纳、解释与工程化整理。
- 本项目不隶属于、也不代表腾讯或 WorkBuddy 官方。
- WorkBuddy、腾讯及相关名称、商标和产品归其各自权利人所有。
- 涉及平台字段、审核要求、权限、接口或发布规则时，请以官方最新文档与开放平台实际状态为准。

## Contributing

欢迎：

- 修正文档过期信息
- 提交官方文档更新差异
- 补充模板、校验器和发布 SOP
- 提交真实但已脱敏的审核 / 兼容性经验
- 报告“官方文档 vs 平台实际行为”的差异

请先阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## License

MIT License。详见 [`LICENSE`](LICENSE)。
