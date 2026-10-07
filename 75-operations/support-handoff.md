# Support Handoff

每个正式发布资产建议具备最小支持包。

## Support facts

- Asset name
- Version
- Publisher
- Repository/owner
- Official source verification date
- Supported WorkBuddy version
- External dependencies
- Auth mode

## Troubleshooting

至少准备：

- 安装/解析失败
- 认证失败
- 依赖不可用
- Tool 参数错误
- 超时
- 版本不兼容
- 高风险写操作失败

## Escalation bundle

升级给开发者时包含：

- 时间
- 版本
- WorkBuddy 版本
- OS
- request id
- sanitized error
- reproduction steps

禁止要求用户公开提交 Token/Secret。

## Handoff template

可复用：

`90-templates/release-handoff.md`
