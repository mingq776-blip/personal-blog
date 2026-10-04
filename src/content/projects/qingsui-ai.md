---
title: "青穗 AI 财务教练"
summary: "搭建集财务健康评分、异常预警、用户分层和目标预测于一体的 AI 产品原型，并完成前后端演示链路。"
metric: "4 个模型 · 9 个 API · 3000 条模拟样本"
evidence: "模型指标来自模拟数据，只能证明技术链路可运行，不能表述为真实用户效果。"
year: 2026
order: 1
role: "AI 产品原型 / 模型与接口"
stack: ["Python", "Flask", "scikit-learn", "Qwen"]
cover: "../../assets/covers/qingsui-ai.webp"
coverAlt: "绿色科技感 AI 金融教练项目封面"
liveUrl: ""
repoUrl: ""
featured: true
demo: false
draft: false
---

## 项目目标

用机器学习负责可计算的金融指标，用大模型负责解释和对话，形成可解释、可演示的财务教练原型。

## 技术与模型

- 使用 Python、Flask、scikit-learn 和 Qwen 搭建双引擎原型。
- 训练财务健康分、异常检测、用户分层和目标预测 4 类模型。
- 形成 9 个 API 端点，覆盖评分、预警、分层、预测、对话和看板。
- 使用 3000 条模拟样本进行留出集评估。

## 可展示证据

- MLP 健康分模型：MAE=0.23，R²=1.0，等级判定准确率 99.5%。
- Autoencoder 异常检测：召回率 100%，误报率 6%。
- KMeans 用户分层：4 类人群，轮廓系数 0.465。
- Ridge 目标预测：MAE=0.36 个月，R²=0.999。

## 展示边界

所有指标均来自 3000 条模拟数据；正式投递时统一表述为“模拟数据上的技术验证”，不写成真实用户或商业验证。