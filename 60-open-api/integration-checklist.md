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

## Share to WorkBuddy

这是另一条注册路径，不要复用上面的 client_secret 检查项。

- [ ] 开发者已完成企业认证
- [ ] 分享应用已审核为「已开通」，且客户端为 5.8.0 及以上
- [ ] Windows / macOS 身份按官方页登记，签名证书不是自签名
- [ ] RSA 私钥只在服务端，按 `kid` 轮换，不进安装包
- [ ] 签名在用户发起分享时生成，不长期复用链接
- [ ] PC 端不依赖 image/audio/resource 的内嵌 `data`
- [ ] 预填成功没有被当成用户已提交任务
- [ ] 填充方式冲突已按 `sources/known-inconsistencies.md` 处理，没有自行选边写成唯一算法
