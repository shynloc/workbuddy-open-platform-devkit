# Runtime Test Matrix

静态结构通过不代表产品可发布。至少按产品类型完成真实 WorkBuddy Runtime Test。

## Skill

- [ ] 明确触发词能自动命中
- [ ] 相似但不相关请求不会误触发
- [ ] @references 可读取
- [ ] scripts 能由 Bash 运行
- [ ] 无可选依赖时 fallback 正常
- [ ] 高风险步骤会停下来确认

## Expert

- [ ] 市场卡片字段正常展示
- [ ] 召唤后角色稳定
- [ ] defaultInitPrompt 与 quick prompt 行为一致
- [ ] Skills 成功预加载
- [ ] 无强依赖时不会强制连接外部服务

## Expert Team

- [ ] Lead 实际建立团队并调度成员
- [ ] Member 不越权承担 Lead 职责
- [ ] 并行/串行关系符合设计
- [ ] 成员失败时 Lead 能恢复
- [ ] 最终由 Lead 汇总与验收

## Connector

- [ ] 首次连接
- [ ] 已连接重复进入
- [ ] Token/OAuth 失效
- [ ] 错误参数
- [ ] MCP 超时
- [ ] WorkBuddy 重启后的状态恢复
- [ ] 高风险 Tool 确认
- [ ] 多用户凭据不串号

## Buddy App

- [ ] Preview 链接进入正确应用
- [ ] 3–5 个工作模式边界清晰
- [ ] 场景胶囊能真正启动高频任务
- [ ] 市场资产可发现/可用
- [ ] 默认模型与模型排序符合设计
- [ ] 内置 OAuth Connector 首次绑定体验正常
