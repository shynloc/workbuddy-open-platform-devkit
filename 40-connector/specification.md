---
title: WorkBuddy Connector Specification
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-connector
last_verified: 2026-10-07
status: VERIFIED
---

# Connector 官方规范

官方来源：https://open.workbuddy.cn/docs/connector

## 1. 先选接入方式

官方支持两种方式：

| 方案 | 适用场景 |
|---|---|
| MCP + Skill（推荐） | 已有 API 服务，或可以开发 MCP Server |
| CLI + Skill | 已有成熟、稳定、跨平台 CLI |

如果服务可以通过网络 API 提供能力，官方建议优先 MCP + Skill。一个连接器只能选择一种方案，MCP 与 CLI 不可混用。

## 2. MCP 结构

```text
your-connector/
├── connector-meta.json
├── mcp.json
├── icon.svg
└── skills/
    └── {skill-name}/
        └── SKILL.md
```

远程 MCP 使用 HTTPS，支持 SSE 或 streamableHttp；本地可使用 stdio。一个连接器只配置一个 MCP Server。

## 3. CLI 结构

```text
your-cli-connector/
├── connector-meta.json
├── cli.json
├── icon.svg
└── skills/
    └── {skill-name}/
        └── SKILL.md
```

CLI 方案强烈推荐提供 Skill，因为 CLI 本身没有标准工具描述协议。

## 4. connector-meta.json

重点字段：

- name / name_zh / name_en
- description / description_zh / description_en
- source（全局唯一，仅小写字母、数字、连字符）
- type：mcp / cli / skill-only
- version
- examples_zh / examples_en
- auth_mode
- minWorkbuddyVersion / maxWorkbuddyVersion
- name_map / description_map

使用新版本字段时，必须按官方版本兼容表声明 `minWorkbuddyVersion`。

## 5. Skill

MCP 工具描述已经足够时 Skill 可选；CLI 强烈推荐。

Skill 应说明：

- Tool/命令用途
- 参数、类型、是否必填、默认值
- 调用示例与返回格式
- 认证前置条件
- 错误场景与恢复
- 高风险操作确认

## 6. Icon

- SVG 推荐，亦支持 PNG/JPG
- 文件名 icon.svg / icon.png / icon.jpg
- PNG/JPG 官方建议 64×64
- 建议透明背景
- 小尺寸可辨识
