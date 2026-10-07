# Recipe: Third-party App 接入 WorkBuddy

1. 明确外部产品场景；
2. 判断需要本地助理、云任务、ACP、会话产物中的哪些能力；
3. 创建第三方应用；
4. 申请最小 Scope；
5. 配置 OAuth redirect URI；
6. 后端保存 client_secret；
7. 实现 authorize → code → token；
8. 实现 refresh token；
9. 接入目标 Open API；
10. 处理 401/403/429/超时；
11. 提供用户撤销授权入口；
12. Runtime Test；
13. 准备审核说明与隐私/数据说明；
14. 上线后监控 API 错误与授权失效。
