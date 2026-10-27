# Source Update Log

记录官方来源的核验与变化。

## 2026-10-07

- 建立首版官方来源注册表。
- 核验：开放平台概述、入驻、Skill、Expert、Expert Team、Connector、Buddy App、Third-party App、Open API。
- 建立 OFFICIAL / DERIVED / OBSERVED / EXPERIMENTAL / STALE / DEPRECATED 分类规则。

## 2026-10-20

复核 GitHub Actions run `39225894385`（2026-10-19 定时 Official Source Watch）。失败步骤是「Fail when registered official content changed」，属于内容漂移信号。proposed baseline 与 2026-10-20 重新抓取的文本 hash 一致。

| source | 结论 | 仓库动作 |
|---|---|---|
| workbuddy-connector | 标题未变。相对 2026-10-10 Wayback（与旧 baseline 文本 hash 相同）去掉全部空白后文本一致，增加的 113 字节是 JSON 示例里 `:` / `,` 前的空格 | 只更新 baseline |
| workbuddy-openapi | 标题未变。把两段 token JSON 示例恢复成紧凑空格后，文本 hash 回到旧 baseline。endpoint 与 Scope 未增删 | 只更新 baseline。TTL 与 Buddy 应用措辞冲突记入 known-inconsistencies |
| workbuddy-service-categories-individual | 去掉新增导航文字「 收入变现」后文本 hash 回到旧 baseline。类目表未变 | 不改类目 KB |
| workbuddy-service-categories-enterprise | 与 2026-09-29 页面相比，正文只多了导航项「收入变现」，且该差异正好等于相对旧 baseline 的 13 字节 | 不改类目 KB |
| workbuddy-third-party-app | 可见文本 7355 → 29245 字节。移除标题「积分应用」，新增「积分兑换」以及分享能力、PC 端开发手册整段 | 更新应用类型、Scope 上限和 `60-open-api/share-to-workbuddy.md` |

未纳入本次注册表的页面：https://open.workbuddy.cn/docs/monetization 。它是类目页导航新增项的目标，内容是技能/专家付费与微信签约，不是类目表变更。下次要跟踪运营页时再单独登记。

## 2026-10-27

复核 GitHub Actions run `40295652584`（2026-10-26 定时 Official Source Watch）。失败步骤仍是「Fail when registered official content changed」。proposed baseline 的文本 hash 与 2026-10-27 重新抓取一致。2026-10-09 Common Crawl 存档与本次提交前的 baseline 文本 hash 一致的页面，用可见文本 diff 核对了语义。

| source | 结论 | 仓库动作 |
|---|---|---|
| workbuddy-open-platform-overview | 快速开始删除「在测试环境中进行调试和验证」（39 字节）。平台简介「WorkBuddy」改为「Workbuddy」并去掉前面的空格。合计 −42 字节 | 概述按当前七步改写。QA 仍是仓库 SOP |
| workbuddy-onboarding | 可见文本 4411 → 8191。企业认证收窄为营业执照主体，新增其他组织机构认证（上传组织信息、完成组织验证） | 更新入驻、主体决策和资质 Gate |
| workbuddy-skill | 字段表把 name / display_name / display_name_en 改为必填，用 examples_zh / examples_en 换下 disable-model-invocation 与 user-invocable。示例去掉 category，并带有 `切英文版展示名称` 与 `exmaple` | 更新规范、字段表、校验器和模板必填项 |
| workbuddy-expert | 只删除「，或扫描开放平台首页下方的二维码，加入开发者群聊沟通」，−79 字节。其余文本与 2026-10-09 存档一致 | 记下邮箱支持和「创建技能」笔误 |
| workbuddy-buddy-app | 背景图改为 792×240、纯色加右侧插图。场景数量改为 Top 3–5。最佳实践增加「iframe 或」。引号和「从 模型池」空格无配置含义 | 更新设计资产和产品设计。工作模式 3–5 / 2–4 仍并列 |
| workbuddy-third-party-app | 标题「权限配置列表及关联 API」改为「权限配置」。权限申请指南写明硬件接入与积分兑换的 Scope 上限。Scope 行未增删 | 第三方应用笔记改标题和这句上限 |
| workbuddy-contact | 去掉标题「官方社群」。正文只剩咨询邮箱。330 → 225 字节 | README 改为只指向邮箱 |
| workbuddy-service-categories-individual | 去掉导航文字「WorkBuddy 开放平台开发者公约（试行）」后，文本 hash 回到旧 baseline。类目表未变 | 不改类目 KB |
| workbuddy-service-categories-enterprise | 与个人类目页相同，整段差异就是这条导航，+50 字节 | 不改类目 KB |

未纳入本次注册表的页面：

- https://open.workbuddy.cn/docs/developer-agreement 。类目页导航新增项，公约版本 1.0，日期 2026年10月22日，内容是开发者行为规范和违规处理，不是类目表。
- https://open.workbuddy.cn/docs/developer-profile 。入驻页导航新增项。组织机构认证要求发布前到「设置 → 开发者信息」写昵称，字段约束记在入驻笔记里。下次要跟踪主页资料变更时再单独登记。
- https://open.workbuddy.cn/docs/monetization 仍保持 2026-10-20 的未登记状态。

后续变更应记录：

- source id
- detected_at
- previous hash / current hash
- 变化摘要
- 受影响 KB 文件
- 更新负责人/Agent
- 验证状态
