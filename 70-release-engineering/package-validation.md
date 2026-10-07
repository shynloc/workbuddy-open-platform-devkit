# Package Validation

## 通用

- [ ] 根目录结构符合对应官方类型
- [ ] JSON/YAML 可解析
- [ ] 所有相对路径存在
- [ ] 文件名大小写一致
- [ ] 不包含 .DS_Store、临时文件、缓存、明文 Secret
- [ ] version 使用语义化版本
- [ ] README/说明中的字段与实际配置一致

## Skill

读取 `10-skill/qa-checklist.md`

## Expert

读取 `20-expert/qa-checklist.md`

## Expert Team

检查 plugin.json、settings.json、所有 agent/avatar/skills 路径、teamInfo/members 一致性。

## Connector

读取 `40-connector/qa-checklist.md`

## Buddy App

不是单纯 ZIP 资产；应按开放平台当前配置项逐模块完成，并在提交审核前使用预览链接调试。

## 凭据

任何类型都不得打包：

- client_secret
- access_token
- refresh_token
- API Key
- PAT
- 私有证书/真实 cookie
