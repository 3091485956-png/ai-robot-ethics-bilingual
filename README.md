# 人工智能与机器人伦理学 · 中英精读

对人工智能与机器人伦理学主题文章的中英双语精读项目：保留英文原文，逐段配中文译文、逻辑拆解、术语解释、背景知识与词汇标注，最终构建为一个独立的单文件 HTML 页面。

**📖 在线阅读**：<https://3091485956-png.github.io/ai-robot-ethics-bilingual/>

线上版本由 GitHub Pages 从 `main` 分支的 `docs/index.html` 发布；本地构建时 `build.py` 会自动同步该发布副本。

最终成品：`docs/index.html`（无需服务器，浏览器直接打开即可；本地构建另会生成中文名副本）。

## 项目结构

```
ethics-ai-raw.html          原始抓取的页面（提取原文的来源）
parse_article.py            从原始 HTML 解析文章结构
extract.py                  抽取结构化原文 → article.json
slice.py                    将原文切分为 a/b/c/d 四个分片
content-source/             标注规范（ANNOTATION-SPEC.md）与分片源文件
content/                    各分片的中文标注（译文/逻辑/术语/背景/词汇）及构建脚本
build.py                    合并原文与标注，生成最终单文件 HTML
web/index.html              页面模板（数据注入占位符）
qc_check.py / qc_sample.py  标注质量抽检
smoke_test.py               构建结果冒烟测试
qa_shots.py / make_shot_build.py / make_probe.py   页面截图与人工核查辅助
```

## 构建方法

```bash
python build.py            # 正式构建（要求四个分片齐全；同时更新 docs/index.html）
python build.py --dev      # 开发预览（缺失标注用占位内容）
```

## 发布

- GitHub Pages：Settings → Pages → Source 选 `main` 分支 `/docs` 目录。
- 构建后提交 `docs/index.html` 的变更即可自动重新发布，线上地址见顶部链接。

## 说明

- 仓库内容（原文与译文）仅用于个人学习精读，请勿作为公开版本发布时直接转载原文。
- 分片标注可多人并行：按 `content-source/ANNOTATION-SPEC.md` 的规范各自完成 `shard-*.json`，再由 `build.py` 统一合并。
