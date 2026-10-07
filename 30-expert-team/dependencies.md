# Expert / Expert Team Dependencies

官方来源：https://open.workbuddy.cn/docs/expert-team

## 依赖类型

### WorkBuddy 已上架 Connector

```json
{
  "dependencies": {
    "connectors": ["tencent-docs"]
  }
}
```

WorkBuddy 在召唤前引导用户完成连接。

### 自带 MCP

推荐：

```json
{
  "dependencies": {
    "mcpServers": "./.mcp.json"
  }
}
```

如果 plugin.json 未声明，根目录 `.mcp.json` 可作为 fallback。

## x-workbuddy

用于依赖引导卡片的展示与认证元信息：

- displayName
- description
- icon
- auth.type = oauth | token | none
- auth.tokenSchema

`x-workbuddy` 是 WorkBuddy 私有元信息，官方说明在写入用户最终自定义连接器配置时会被剥离。

## 安全

- Token 输入后由用户本地保存；
- 专家包禁止硬编码真实 Token/密钥；
- 已连接过的同名依赖不会重复引导；
- 只有核心任务必须依赖外部能力时才声明强依赖。
