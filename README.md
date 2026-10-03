# 我的博客与作品档案

Astro 静态网站，采用杂志式视觉、轻量 Canvas 动画和数据图表。

## 页面结构

- 首页：封面主视觉、精选内容与数据概览
- 个人介绍：个人定位、关注方向与做事原则
- 项目经历：按时间线整理的实践阶段
- 作品展示：项目卡片与作品详情
- 数据图表：推进趋势、能力分布与时间分配

## 本地运行

项目内置便携版 Node.js，直接双击：

- `start-dev.cmd`：启动开发服务器
- `build-site.cmd`：构建网站与搜索索引
- `preview-site.cmd`：预览生产构建

## 手动命令

```bash
corepack pnpm install --frozen-lockfile
corepack pnpm check
corepack pnpm build
corepack pnpm preview
```

## 性能策略

- 不加载 React 或 Three.js，首页使用轻量 Canvas 2D 动画
- JavaScript 按需执行，动画支持减少动态效果
- 图片使用 WebP，并限制设备像素比和粒子数量
- `content-visibility` 已移除以避免滚动布局跳动

完整说明见 `docs/个人博客使用与维护说明.docx`。