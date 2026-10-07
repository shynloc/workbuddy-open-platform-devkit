# Security Policy

## Scope

This policy covers WB-OPDK's own scripts, templates, schemas, documentation tooling and example code.

It does **not** make WB-OPDK the security contact for WorkBuddy itself.

For WorkBuddy platform/account/API security issues, use WorkBuddy's current official contact/support channel:

https://open.workbuddy.cn/docs/contact

## Never post secrets publicly

Do not open a public Issue or PR containing:

- client_secret
- access_token / refresh_token
- API Key / PAT
- OAuth code
- ACP ticket
- cookie/session
- private key
- real user private data
- production credentials

If a log is needed, redact these values first.

## Reporting a WB-OPDK issue

For non-sensitive security bugs in this repository, open a GitHub Issue with reproduction steps and affected version/commit.

For a vulnerability that would expose secrets or user data if described publicly:

1. do not include exploit details in a public issue;
2. contact the repository owner through an available private GitHub/contact channel;
3. provide the smallest reproducible evidence;
4. rotate any credential that may already be compromised.

## Supported security posture

WB-OPDK examples are reference implementations unless explicitly stated otherwise.

A sample passing CI means:

> it passes the repository's current static checks.

It does not automatically mean:

- production hardening is complete;
- the external service is secure;
- WorkBuddy has reviewed/approved it;
- every runtime path has been tested.

Use `65-security-governance/` and `70-release-engineering/security-checklist.md` before production release.
