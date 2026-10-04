---
title: "Pixel2Motion"
summary: "将位图标识重建为可无限缩放的矢量资产，并生成可用于品牌展示的确定性与动效文件。"
metric: "IoU=0.9937 · 102 条 SVG 路径 · 32 帧 GIF"
evidence: "15 个关键帧、2100ms 动效；最终动效帧与静态渲染差异为 0。"
year: 2026
order: 6
role: "视觉技术 / 矢量重建 / 动效"
stack: ["Python", "Pillow", "NumPy", "SVG"]
cover: "../../assets/covers/pixel2motion.webp"
coverAlt: "绿色矢量路径与动效项目封面"
liveUrl: ""
repoUrl: ""
featured: true
demo: false
draft: false
---

## 项目目标

解决位图标识放大失真、动效不稳定和交付格式不统一的问题。

## 实现内容

- 完成校徽矢量重建，矢量拟合 IoU=0.9937。
- 输出 102 条 SVG 路径、15 个关键帧和 32 帧 GIF。
- 制作 2100ms 品牌动效，最终动效帧与静态渲染差异为 0。
- 交付可无限缩放 SVG、单文件 HTML 动效和 QA 规范。