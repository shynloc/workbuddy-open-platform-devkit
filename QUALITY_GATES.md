# WB-OPDK Quality Gates

WB-OPDK 区分两个目标：

1. **Working-grade DevKit**：可以被真实开发团队用于需求、开发、校验、发布和维护；
2. **v1.0 Runtime-complete**：主要 WorkBuddy 产品类型都完成真实平台/Runtime 验证。

前者不应被后者拖住，但两者不能混为一谈。

## Gate A — Source Governance

- [x] Official-first Source of Truth
- [x] 官方来源注册表
- [x] visible-text / heading hash baseline
- [x] source → downstream impact map
- [x] 官方模板 ZIP 审计
- [x] 官方内部冲突记录
- [x] Source Watch CI
- [x] Source Registry Validator

## Gate B — Product Coverage

- [x] Platform / onboarding
- [x] Qualification & service categories
- [x] Skill
- [x] Expert
- [x] Expert Team
- [x] Connector
- [x] Buddy App
- [x] Hardware
- [x] Third-party App / Open API
- [x] Security & governance
- [x] Release engineering
- [x] Post-release operations

## Gate C — Executable DevKit

- [x] Starter templates
- [x] Scaffold tool
- [x] JSON Schemas
- [x] Product validators
- [x] Release ZIP packer
- [x] Release manifest
- [x] Submission notes generator
- [x] Runtime/Security/Submission checklists
- [x] MkDocs HTML build
- [x] CI smoke tests

## Gate D — Governance / Distribution

- [x] MIT License for WB-OPDK original work
- [x] NOTICE / upstream attribution
- [x] Compatibility policy
- [x] Security reporting policy
- [x] Contribution policy
- [x] Changelog / Roadmap

## Gate E — Real WorkBuddy Evidence

Current:

- Skill: Platform Parse ✅ / Review Approved ✅ / Published ✅
- Expert: Platform Parse ✅ / Review pending
- Expert Team: Platform Parse ✅ after `settings.json` correction / Review pending
- Connector: pending real platform/runtime validation
- Buddy App: pending real preview/review validation
- Third-party App/Open API: pending real OAuth/API validation

See:

`95-validation/v1-readiness.md`

## Working-grade definition

WB-OPDK reaches **Working-grade DevKit** when Gates A–D are green and CI/source monitoring are healthy.

It reaches **v1.0 Runtime-complete** only when Gate E satisfies the v1.0 release criteria.

This distinction prevents two bad outcomes:

- declaring production confidence from documentation alone;
- delaying a useful development kit until every ecosystem product has completed market review.