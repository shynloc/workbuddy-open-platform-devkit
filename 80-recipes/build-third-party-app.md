# Recipe: Third-party App 接入 WorkBuddy

先分清官方现在的两条路径：

- 产品要调用 WorkBuddy Open API：创建 OAuth 应用。当前类型表是硬件接入，或「其他 > 积分兑换」。
- 产品要把内容分享进 WorkBuddy 输入区：走分享应用，见 `60-open-api/share-to-workbuddy.md`。不要申请 OAuth Scope 来代替它。

## 调用 Open API

1. 明确外部产品场景；
2. 判断需要本地助理、云任务、ACP、会话产物、兑换码中的哪些能力；
3. 按场景创建硬件接入或积分兑换应用。积分兑换只开放积分与权益类 Scope；
4. 申请最小 Scope；
5. 配置 OAuth redirect URI；
6. 后端保存 client_secret。官方写它在应用创建成功后只明文展示一次；
7. 实现 authorize → code → token；
8. 实现 refresh token，TTL 读 `expires_in`；
9. 接入目标 Open API；
10. 处理 401/403/429/超时；
11. 提供用户撤销授权入口；
12. Runtime Test；
13. 准备审核说明与隐私/数据说明；
14. 上线后监控 API 错误与授权失效。

## 分享到 WorkBuddy

1. 确认主体已企业认证，客户端目标是 WorkBuddy 5.8.0 及以上的 Windows 或 macOS；
2. 在「第三方接入 → 分享功能接入」注册，而不是创建硬件/积分应用；
3. 登记应用官网、logo，以及对应端的签名身份；
4. 审核通过后在本地生成 RSA 密钥，私钥只留在服务端；
5. 用户点击分享时现签 `newTask` 包，打开 `https://workbuddy.cn/app/open-deeplink`；
6. 把预填成功和用户提交任务分开验收。
