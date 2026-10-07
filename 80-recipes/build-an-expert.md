# Recipe: 从职业角色到 Expert

1. 定义目标用户与“现实职业角色”；
2. 定义独立交付结果与边界；
3. 决定是否内置 Skills；
4. 只有核心任务不可缺少外部系统时才声明 Connector/MCP 依赖；
5. 创建 plugin.json；
6. 创建 Agent MD；
7. 设计 512×512、≤500KB avatar；
8. 写 40–50 字中文 displayDescription；
9. 设计 3 个 tags + 3 个 quickPrompts；
10. 保证 defaultInitPrompt = quickPrompts[0]；
11. 按 categoryId 选最匹配行业；
12. 跑 Expert QA；
13. 实测“召唤专家”后的首轮体验。

核心判断：用户是在“调用一个方法”，还是“找一个专业的人”。前者优先 Skill，后者才是 Expert。
