# 《Ethics of Artificial Intelligence and Robotics》中英精读网页 —— 内容标注规范 v1

你负责把 SEP（斯坦福哲学百科）词条 *Ethics of Artificial Intelligence and Robotics*（作者 Vincent C. Müller，2026 夏季归档版）的**指定分片**加工成结构化中文学习内容。最终产物是一个 JSON 文件，供程序装配成交互网页。

## 0. 最高铁律（违反即返工）

1. **英文原文一字不可改**：你产出的中译必须完整对应分片里的每一个英文段落，**不得总结、删减、增补、改写、调换顺序、合并或拆分段落**。原文有几句就译几句，原文的限定语、让步、引用、举例、数字、人名、年份都要在中译里有着落。
2. **中译是翻译，不是导读**：不得加入原文没有的判断、例子、过渡句。你的解释只能放进 `logic / terms / background / vocab` 四个标注层，严禁混进 `zh` 译文。
3. **每个段落（kind 为 `p` 或 `quote`）都必须有 `zh`**，且通过 `pid` 与源文件一一对应，**pid 原样照抄，不得新造**。
4. **每个标题块（kind 为 `heading`）都必须有 `title_zh`**。
5. **不得编造**：背景知识、词汇例句、术语解释凡涉及事实（日期、著作、事件、数据），拿不准就不写；`vocab.ex` 必须是该段原文中逐字摘录的片段，严禁自造例句。
6. 全程使用**简体中文**（专有名词、英文术语除外），使用中文标点（，。；：“”（）？）。数字、年份、百分比保留阿拉伯数字。

## 1. 输入与输出

- 输入：`content-source/shard-<X>.source.json`（X = a/b/c/d），其中 `blocks` 按原文顺序排列，每个块有：
  - 标题块：`{kind:"heading", level:2|3|4, num:"2.1.1", id, title_en}`
  - 正文段：`{kind:"p", pid:"p007", text_en, html_en}`
  - 引文段：`{kind:"quote", pid, text_en, html_en}`
- 输出：在项目根目录创建 `content/` 文件夹，写入 `content/shard-<X>.json`，UTF-8 编码、合法 JSON（用 Python `json.dumps(..., ensure_ascii=False)` 校验）。
- 输出结构：

```json
{
  "shard": "a",
  "blocks": [
    {"kind":"heading","level":2,"num":"1","id":"Int","title_en":"Introduction","title_zh":"导论"},
    {"kind":"p","pid":"p002","zh":"……完整中译……",
     "logic":["……","……"],
     "terms":[{"en":"moral status","zh":"道德地位","def":"……"}],
     "background":[{"title":"伊曼努尔·康德（Immanuel Kant）","body":"……"}],
     "vocab":[{"en":"substantial","pos":"adj.","zh":"重大的；实质性的","ex":"substantial impact on the world"}]
    }
  ]
}
```

输出 `blocks` 的**数量、顺序、kind、pid/id 必须与输入完全一致**，只新增中文字段，不新增/删除/重排块。

## 2. 各字段写法

### 2.1 `zh`（段落中译，必填）
- 学术哲学文风：准确、严谨、通顺，优先保证概念准确与逻辑关系显豁（因果、转折、让步、指代要交代清楚）。
- 长句可按中文习惯拆句，但**信息不得增减**；代词（it/they/this）若指代关键，要把指代对象译明。
- 文内引用标记原样保留，如 “(Good 1965, 33)”“(Müller 2020)”“(EU 2016)”。
- 人名：公认译名直接用中文（康德、亚里士多德、图灵、阿西莫夫、波斯特洛姆等）；不常见者保留英文原文，**不要臆造音译**。
- 著作/文件/法案名：著名者用通行中译名并在首次出现处括注英文（例：《通用数据保护条例》（GDPR））；不著名者保留英文。
- 术语首次出现时用“中文（English）”格式，后续用中文；以第 4 节术语表为准。
- 原文斜体强调可用中文着重号式表达，必要时在词外加 `**强调词**`（少量、克制）。
- 引文段（quote）同样完整翻译，并在 zh 末尾保留出处标记。

### 2.2 `logic`（逻辑拆解，必填，2–4 条）
- 用中文逐条说明**这一段在论证中做了什么**：提出论点 / 界定概念 / 区分立场 / 给出论据 / 援引案例 / 回应反驳 / 过渡到下一议题。
- 每条一个完整句子，按行文顺序排列，能串成该段的论证链。例：“先以技术史类比指出，对新技术的担忧有的被证明多余、有的成立，为后文甄别真问题确立标准。”
- 只描述该段实际的论证动作，不评价对错，不引入段外内容。

### 2.3 `terms`（名词解释，每段 1–5 条）
- 只收**哲学术语、伦理/法律/技术核心概念、或在本文有特定用法的词**；日常词汇不收（日常词汇进 vocab）。
- 字段：`en`（原文中的术语写法）、`zh`（与术语表一致的中文定名）、`def`（1–2 句中文，说明该术语**在本文语境中**的含义；若本文给了定义，忠实转述本文定义）。
- 同一术语可在不同段重复出现，但每条 def 要自足；定名为术语表中的同一中文。
- 短语优先（如 “responsibility gap”“value alignment”），不要拆成单词解释。

### 2.4 `background`（背景知识补充，每段 0–4 条）
- 仅当该段**点名了**具体人物、著作、案例、事件、组织、法案、思想实验、学派或技术时才写。
- 字段：`title`（“中文名（English Name）”或事件名）、`body`（1–3 句客观中文说明：是什么、与本文论点的关系）。
- 内容为学界常识性事实（如“康德是 18 世纪德国义务论代表人物”“COMPAS 是美国用于量刑风险评估的算法工具，2016 年 ProPublica 调查指其存在种族偏差”）。**严禁杜撰日期、数据与引文**；无把握的背景宁可不写。
- 同一背景在全文首次出现处写一次即可，后续段再提及时不重复。

### 2.5 `vocab`（英文词汇，每段 4–8 条；短段可 2–4 条）
- 服务中文学术英语学习：收该段中出现的**高频学术词、固定搭配、动词短语**（如 purport to、give rise to、in light of、salient、exacerbate、warrant、underdetermine）。
- 字段：`en`（词或短语原形）、`pos`（词性 n./v./adj./phr.）、`zh`（该语境中的释义）、`ex`（**逐字摘自该段**、包含该词的最短英文片段，3–12 个词为宜）。
- 不收：专有名词、术语表已收的专业概念（那些进 terms）、过于简单的基础词。
- 同一词在不同段可重复收（语境义不同时）。

## 3. 标题翻译

- `title_zh` 要简洁、学术，与术语表一致，例如：
  - 1 Introduction → 导论
  - 1.1 Scope: Ethics of AI & Robotics → 1.1 范围：人工智能与机器人伦理学
  - 2.2 Human Autonomy & Manipulation → 2.2 人的自主性与操纵
  - 2.7 Moral Status, Machine Ethics, Responsibility → 2.7 道德地位、机器伦理与责任
  - 2.8 Superintelligence & Existential Risk → 2.8 超级智能与存在性风险
- 编号（1、2.1.1）不要写进 title_zh（编号由 num 字段渲染）。

## 4. 统一术语表（必须沿用；遇到表中术语一律用此定名）

| English | 中文 |
|---|---|
| ethics of AI and robotics | 人工智能与机器人伦理学 |
| artificial intelligence (AI) | 人工智能（AI） |
| robotics | 机器人学；机器人技术（据语境） |
| agency | 能动作用；能动性 |
| moral agency | 道德能动性 |
| (moral) agent | （道德）能动者；（道德）主体 |
| moral patiency / patient | 道德承受者身份 / 道德承受者 |
| autonomy | 自主性 |
| self-determination | 自我决定 |
| autonomy (of systems) | 自主性（系统的） |
| privacy | 隐私 |
| data protection | 数据保护 |
| personal data | 个人数据 |
| informed consent | 知情同意 |
| surveillance | 监控 |
| surveillance capitalism | 监控资本主义 |
| manipulation | 操纵 |
| nudging / nudge | 助推 / 轻推（“助推”优先） |
| paternalism | 家长主义 |
| opacity | 不透明性 |
| black box | 黑箱 |
| explainability / XAI | 可解释性 / 可解释人工智能 |
| interpretability | 可解读性 |
| epistemic | 认识论的；认知的（据语境） |
| fairness | 公平 |
| bias | 偏见 |
| discrimination | 歧视 |
| algorithmic decision-making | 算法决策 |
| machine learning | 机器学习 |
| deep learning | 深度学习 |
| neural network | 神经网络 |
| training data | 训练数据 |
| human-robot interaction (HRI) | 人—机器人互动 |
| care robot | 护理机器人 |
| sex robot | 性爱机器人 |
| humanoid robot | 人形机器人 |
| autonomous vehicle (AV) | 自动驾驶汽车 |
| autonomous weapons / LAWS | 自主武器 / 致命性自主武器系统 |
| moral status | 道德地位 |
| consciousness | 意识 |
| sentience | 感知能力；感受苦乐的能力 |
| personhood | 人格（地位） |
| machine ethics | 机器伦理 |
| artificial moral agent (AMA) | 人工道德能动者 |
| Asimov's Three Laws of Robotics | 阿西莫夫“机器人三定律” |
| responsibility | 责任 |
| accountability | 问责（性） |
| liability | 法律责任；赔偿责任 |
| responsibility gap | 责任缺口 |
| many hands problem | “多手”问题 |
| superintelligence | 超级智能 |
| singularity | 奇点 |
| intelligence explosion | 智能爆炸 |
| artificial general intelligence (AGI) | 通用人工智能（AGI） |
| existential risk (x-risk) | 存在性风险 |
| value alignment / alignment problem | 价值对齐 / 对齐问题 |
| friendly AI | 友好人工智能 |
| instrumental convergence | 工具性趋同 |
| effective altruism | 有效利他主义 |
| longtermism | 长期主义 |
| philosophy of technology | 技术哲学 |
| technological unemployment | 技术性失业 |
| future of work | 工作的未来 |
| governance | 治理 |
| regulation | 监管；规制 |
| policy | 政策 |
| trolley problem | 电车难题 |
| utilitarianism | 功利主义 |
| consequentialism | 后果论 |
| deontology | 义务论 |
| virtue ethics | 美德伦理学 |
| Kantian | 康德主义（者）（的） |
| Turing test | 图灵测试 |
| Chinese Room (argument) | “中文屋”论证 |
| functionalism | 功能主义 |
| principle of double effect | 双重效应原则 |
| just war theory | 正义战争理论 |

## 5. 自检清单（写文件前逐项确认）

- [ ] 输出块数 = 输入块数；顺序一致；每个 p/quote 块都有非空 `zh`；每个 heading 都有 `title_zh`。
- [ ] 所有 pid、id、num、level、kind 原样照抄。
- [ ] 随机抽 5 段，逐句核对中译无漏译、无句义改变；数字、年份、人名齐全。
- [ ] logic 每段 2–4 条且确实在描述论证结构。
- [ ] terms 用了术语表定名；def 与本文语境相符。
- [ ] background 不含无把握的“事实”；同一背景未重复写。
- [ ] vocab 的 ex 全部能在该段 text_en 中逐字找到。
- [ ] JSON 可被 `json.load` 正常解析，ensure_ascii=False，无注释、无尾逗号。
- [ ] 文件路径：`content/shard-<X>.json`。
