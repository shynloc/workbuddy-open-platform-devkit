# Security Release Gate

发布 Connector / Third-party App / Hardware / 高权限 Buddy App 前执行。

## Authorization

- [ ] Scope 最小化
- [ ] 权限用途可向用户解释
- [ ] 用户撤销/解绑路径存在
- [ ] client_secret 仅服务端
- [ ] refresh token 不进入客户端

## Data

- [ ] 已建立数据字段清单
- [ ] 已定义保留期限
- [ ] 已定义删除/匿名化触发条件
- [ ] 日志默认脱敏

## Side effects

- [ ] 所有写 Tool 已标风险等级
- [ ] R2/R3 有确认策略
- [ ] 非幂等超时不会盲目重试
- [ ] 服务端做最终权限校验

## Multi-user

- [ ] 凭据按用户隔离
- [ ] 缓存/数据库查询有租户边界
- [ ] 测试过用户 A 不会读到用户 B 数据

## Incident

- [ ] 有 Secret 轮换方法
- [ ] 有撤销会话方法
- [ ] 有故障联系人/升级路径
- [ ] 能定位受影响版本
