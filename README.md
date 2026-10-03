# 我的博客

Astro + React + Three.js 搭建的个人博客与作品集。

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

## 内容维护

- 文章：`src/content/posts`
- 项目：`src/content/projects`
- 网站名称与社交链接：`src/data/site.ts`
- 封面图片：`src/assets/covers`

完整图文说明见 `docs/个人博客使用与维护说明.docx`。
