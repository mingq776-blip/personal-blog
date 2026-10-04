import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "zod";

const posts = defineCollection({
  loader: glob({ base: "./src/content/posts", pattern: "**/*.{md,mdx}" }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      description: z.string(),
      pubDate: z.coerce.date(),
      updatedDate: z.coerce.date().optional(),
      category: z.string(),
      tags: z.array(z.string()).default([]),
      cover: image(),
      coverAlt: z.string().default("文章封面"),
      featured: z.boolean().default(false),
      draft: z.boolean().default(false),
    }),
});

const projects = defineCollection({
  loader: glob({ base: "./src/content/projects", pattern: "**/*.{md,mdx}" }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      summary: z.string(),
      metric: z.string().default(""),
      evidence: z.string().default(""),
      year: z.number(),
      order: z.number().default(99),
      role: z.string(),
      stack: z.array(z.string()).default([]),
      cover: image(),
      coverAlt: z.string().default("项目封面"),
      liveUrl: z.string().default(""),
      repoUrl: z.string().default(""),
      featured: z.boolean().default(false),
      demo: z.boolean().default(true),
      draft: z.boolean().default(false),
    }),
});

export const collections = { posts, projects };

