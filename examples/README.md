# Examples

本目录放 **可运行但非生产级** 的参考实现，用来证明 WB-OPDK 的工程说明可以落地。

## 当前示例

### third-party-oauth-minimal

位置：

`examples/third-party-oauth-minimal/`

演示：

```text
第三方应用
→ OAuth 2.1 authorize
→ callback
→ code 换 token
→ server-side token storage
→ Open API profile
→ refresh token
```

该示例遵循当前 WorkBuddy Open API 官方 OAuth 流程，但 Token Store 仅为进程内内存，生产环境必须替换。

## 原则

- 示例必须标明 Production Gap；
- 不写入真实 client_secret；
- 不把 Token 暴露到浏览器；
- 只使用当前官方已确认的 endpoint / 字段；
- 官方文档变化时，示例必须随 Source Watch 重新验证。
