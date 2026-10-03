export const formatDate = (date: Date) =>
  new Intl.DateTimeFormat("zh-CN", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).format(date);

export const readingTime = (body = "") => {
  const chineseCharacters = (body.match(/[\u3400-\u9fff]/g) ?? []).length;
  const latinWords = (body.replace(/[\u3400-\u9fff]/g, " ").match(/\b[\w'-]+\b/g) ?? []).length;
  const minutes = Math.max(1, Math.ceil(chineseCharacters / 420 + latinWords / 220));
  return `${minutes} 分钟阅读`;
};
