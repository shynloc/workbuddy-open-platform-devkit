# Third-party App / Open API Integration Checklist

## Application

- [ ] 应用已创建
- [ ] client_id 已记录
- [ ] client_secret 已安全保存且不进入前端
- [ ] redirect_uri 与平台登记一致
- [ ] Scope 最小化
- [ ] 审核状态允许当前调用

## OAuth

- [ ] state 随机且校验
- [ ] code 只由后端兑换
- [ ] access_token 不记录到客户端日志
- [ ] refresh_token 后端安全存储
- [ ] token 刷新和失效恢复完成

## API

- [ ] 请求头/错误码处理
- [ ] 429/超时重试策略
- [ ] 用户撤销授权路径
- [ ] 数据最小化
- [ ] 日志脱敏

## Runtime

- [ ] 本地助理/云任务能力按 Scope 验证
- [ ] ACP（如使用）有断线重连
- [ ] 会话产物解析兼容缺失字段
- [ ] 测试账号与生产账号隔离
