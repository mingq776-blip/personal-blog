export const site = {
  title: "我的博客",
  author: "我的名字",
  role: "内容创作者 / 独立开发者",
  description: "记录技术、创作与长期主义的个人空间。这里既有文章，也存放正在生长的作品。",
  url: "https://personal-blog-gamma-six.vercel.app",
  location: "中国",
  email: "hello@example.com",
  navigation: [
    { label: "首页", href: "/" },
    { label: "博客", href: "/blog" },
    { label: "项目", href: "/projects" },
    { label: "归档", href: "/archive" },
    { label: "关于", href: "/about" },
  ],
  socials: [
    { label: "GitHub", href: "https://github.com/" },
    { label: "即刻", href: "https://web.okjike.com/" },
    { label: "邮箱", href: "mailto:hello@example.com" },
  ],
} as const;
