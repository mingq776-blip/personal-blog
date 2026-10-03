from docx import Document
path = r'E:\codex\个人博客\docs\个人博客使用与维护说明.docx'
doc = Document(path)
updates = {
    '静态构建': '32 个页面构建成功',
    '搜索索引': '9 个文章与项目详情页，689 个词',
    '首页 Lighthouse': '性能 99 / 无障碍 100 / 最佳实践 100 / SEO 100',
    '文章页 Lighthouse': '数据页 Lighthouse 100 / 100 / 100 / 100',
}
for table in doc.tables:
    for row in table.rows:
        if row.cells[0].text in updates:
            row.cells[1].text = updates[row.cells[0].text]
doc.save(path)
print(path)
