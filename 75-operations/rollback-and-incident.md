# Rollback & Incident Response

## Incident classes

### P0 — Security / cross-user exposure

立即：

- 停止受影响能力
- 撤销/轮换凭据
- 阻断错误数据路径
- 保存必要审计证据
- 评估受影响用户

### P1 — destructive or widespread failure

例如：

- 批量错误写入
- 发布/删除 Tool 行为异常
- 大范围认证失败

优先关闭写能力或回退稳定版本。

### P2 — degraded UX

例如：

- 部分 Tool 超时
- 模型/依赖降级
- 个别场景失败

可以降级并持续服务。

## Rollback

发布前应知道：

- 上一个稳定版本
- 如何恢复
- 配置是否向后兼容
- 数据 migration 是否可逆

如果 schema migration 不可逆，“代码回滚”不等于真正恢复。

## Post-incident

记录：

- timeline
- root cause
- blast radius
- mitigation
- permanent fix
- KB/Validator 是否需要更新
