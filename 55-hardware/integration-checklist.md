# Hardware Integration Checklist

## Open Platform

- [ ] 创建的是 Hardware Access 应用
- [ ] 应用审核状态允许接入
- [ ] OAuth redirect URI 正确
- [ ] Scope 最小化

## Credentials

- [ ] client_secret 只在后端
- [ ] 设备端无长期平台 Secret
- [ ] Token 刷新由后端安全完成
- [ ] 设备解绑可撤销会话/映射

## Runtime

- [ ] Local Assistant online/offline
- [ ] Cloud Task create/query
- [ ] ACP reconnect
- [ ] Artifact recovery
- [ ] 网络中断
- [ ] Token 过期
- [ ] 重复事件

## Device lifecycle

- [ ] 首次绑定
- [ ] 换用户
- [ ] 退出账号
- [ ] 恢复出厂
- [ ] 丢失/远程解绑
- [ ] 二手转让
