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

后续变更应记录：

- source id
- detected_at
- previous hash / current hash
- 变化摘要
- 受影响 KB 文件
- 更新负责人/Agent
- 验证状态
