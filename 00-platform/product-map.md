---
title: WorkBuddy Ecosystem Product Map
knowledge_type: DERIVED
official_sources:
  - workbuddy-open-platform-overview
  - workbuddy-buddy-app
last_verified: 2026-10-08
status: VERIFIED
---

# 产品地图

```text
                     WorkBuddy Open Platform
                              │
        ┌─────────────────────┼──────────────────────┐
        │                     │                      │
     AI 方法层             专业角色层             外部能力层
        │                     │                      │
      Skill              Expert / Team           Connector
        └─────────────┬───────┴───────────┬──────────┘
                      │                   │
                 Buddy App          Third-party App
                行业 Harness          + Open API
                                          │
                              ┌───────────┴───────────┐
                           Hardware              Other Apps
```

## 价值位置

- Skill：把 know-how 变成可复用执行规则；
- Expert：把 know-how 人格化、职业化；
- Expert Team：把复杂工作拆成多角色协作；
- Connector：把 AI 接到真实系统；
- Buddy App：把前述资产编排成行业级工作台；
- Third-party App：让你自己的产品反向调用 WorkBuddy Runtime；
- Hardware：是 Third-party App 的正式应用类型之一，适用于智能眼镜、车机等设备接入。

开发时不要先问“我要做哪个包”，先问“用户价值主要发生在哪一层”。