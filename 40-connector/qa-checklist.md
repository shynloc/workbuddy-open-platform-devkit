# Connector QA Checklist

## Product

- [ ] 已明确 MCP 或 CLI，未混用
- [ ] source 为全局唯一 kebab-case
- [ ] 名称、描述、中英文示例完整
- [ ] version 语义化

## MCP

- [ ] 仅一个 Server
- [ ] 远程地址 HTTPS
- [ ] 工具 schema 清晰稳定
- [ ] 典型请求 30 秒内
- [ ] 覆盖超时/参数错误/授权失效
- [ ] 无真实 Token/密钥
- [ ] 使用新字段时 minWorkbuddyVersion 正确

## CLI

- [ ] macOS/Linux 可用
- [ ] Windows（如承诺）可用
- [ ] init 非交互
- [ ] status 幂等无副作用
- [ ] unAuth 能清理授权
- [ ] 登录态跨 WorkBuddy 重启
- [ ] auth 不依赖 TTY
- [ ] 超时符合官方约束

## Auth

- [ ] OAuth 元数据、动态注册、PKCE 可用（如采用）
- [ ] Token schema key 与 mcp.json 占位符精确一致
- [ ] 密钥字段 password
- [ ] 最小权限

## Skill / UX

- [ ] AI 能知道核心工具/命令如何用
- [ ] 高风险操作有确认
- [ ] icon 小尺寸清晰
