---
title: WorkBuddy Ecosystem Product Map
knowledge_type: DERIVED
official_sources:
  - workbuddy-open-platform-overview
  - workbuddy-buddy-app
  - workbuddy-third-party-app
last_verified: 2026-10-20
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
                 ┌────────────────────────┼────────────────────────┐
              Hardware                 积分兑换                 分享到 WorkBuddy
           OAuth 应用类型            OAuth 应用类型            独立注册，不是 OAuth Scope
```

## 价值位置

- Skill：把 know-how 变成可复用执行规则；
- Expert：把 know-how 人格化、职业化；
- Expert Team：把复杂工作拆成多角色协作；
- Connector：把 AI 接到真实系统；
- Buddy App：把前述资产编排成行业级工作台；
- Third-party App：让外部产品调用 WorkBuddy，或把内容分享进 WorkBuddy；
- Hardware：第三方应用页当前两类 OAuth 应用之一，适用于智能眼镜、车机等设备接入；
- 积分兑换：另一类 OAuth 应用，用卡券或兑换码兑换 credits，只开放积分与权益类 Scope；
- 分享到 WorkBuddy：企业认证开发者的 PC deeplink，不是上面两类应用的 Scope。

开发时不要先问“我要做哪个包”，先问“用户价值主要发生在哪一层”。