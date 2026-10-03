export const site = {
  title: "我的博客",
  author: "我的名字",
  role: "内容创作者 / 独立开发者",
  description: "用杂志式视觉记录个人经历、项目、作品与数据。保持好奇，持续输出。",
  url: "https://personal-blog-gamma-six.vercel.app",
  location: "中国",
  email: "hello@example.com",
  navigation: [
    { label: "首页", href: "/" },
    { label: "个人介绍", href: "/about" },
    { label: "项目经历", href: "/experience" },
    { label: "作品展示", href: "/works" },
    { label: "数据图表", href: "/dashboard" },
  ],
  socials: [
    { label: "GitHub", href: "https://github.com/mingq776-blip" },
    { label: "邮箱", href: "mailto:hello@example.com" },
  ],
} as const;