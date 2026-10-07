# Examples

本目录放 **可运行或可提交验证的参考实现**，用来证明 WB-OPDK 的工程说明可以落地。

## 当前示例

### ai-content-editor

`examples/ai-content-editor/`

真实 Expert 候选：

- AI 内容主编
- 本地 Schema / Validator / Release Check 已通过
- 目标：WorkBuddy Platform Parse + Runtime + Review
- 当前未声称平台已接受

### ai-editorial-team

`examples/ai-editorial-team/`

真实 Expert Team 候选：

- AI 编辑部
- Lead + Research + Writer + Art Director + Publishing Editor
- 本地 Schema / Validator / Release Check 已通过
- 目标：验证 Team parser、角色调度与 `setting.json` 实际行为
- 当前未声称平台已接受

### third-party-oauth-minimal

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

## Candidate Build

Expert / Expert Team 候选由 GitHub Actions 自动构建：

https://github.com/shynloc/workbuddy-open-platform-devkit/actions/workflows/candidate-builds.yml

产物包括：

- release ZIP
- release manifest
- submission notes

## 原则

- 示例必须标明 Production Gap；
- 不写入真实 client_secret；
- 不把 Token 暴露到浏览器；
- 只使用当前官方已确认的 endpoint / 字段；
- 官方文档变化时，示例必须随 Source Watch 重新验证；
- “本地通过”与“WorkBuddy 平台通过”必须分开记录。
