# -*- coding: utf-8 -*-
"""Build content/shard-b.json from content-source/shard-b.source.json.
Copies every source field verbatim; adds title_zh / zh / logic / terms / background / vocab.
"""
import json
from pathlib import Path

ROOT = Path(r"C:\Users\loong\Desktop\人工智能与机器人伦理学")
src = json.loads((ROOT / "content-source" / "shard-b.source.json").read_text(encoding="utf-8"))

title_zh = {
    "EpiIssOpaExp": "认识论问题：不透明性与可解释性",
    "GooDecFaiBia": "好的决定：公平与偏见",
    "sec-2-4-1": "决定",
    "sec-2-4-2": "偏见",
    "HumRobInt": "人—机器人互动",
    "sec-2-5-1": "例（一）护理机器人",
    "sec-2-5-2": "例（二）性爱机器人",
    "AutAISys": "自主人工智能系统",
    "sec-2-6-1": "自主性总论",
    "sec-2-6-2": "例（一）自动驾驶汽车",
    "sec-2-6-3": "例（二）自主武器",
}

ann = {}

ann["p030"] = {
"zh": "当一个人工智能系统作出一项决定时——例如“你被拒绝核发信用卡”——受影响的人往往无法知道该系统是如何得出这一输出的，也就是说，该系统对这个人而言是“不透明的”（opaque）或“黑箱”（black box）。此外，许多人工智能系统依赖于（模拟）神经网络中的机器学习（machine learning）技术，这些技术会从给定数据集中提取模式，无论是否提供了“正确”的解答，即监督学习、半监督学习或无监督学习。借助这些技术，“学习”过程捕捉数据中的模式，并以某种在系统所做决策上显得有用的方式加以标记，而程序员其实并不知道系统究竟使用了数据中的哪些模式。这意味着，结果对专家程序员而言同样是不透明的——这就是标准不透明性（standard opacity）（Durán and Jongsma 2021）。有时，甚至还可能存在原则上无法消除的“深层”或“本质”不透明性（Humphreys 2009; Müller 2025a; Beisbart 2026）。",
"logic": [
"以“信用卡被拒”为例界定不透明性与黑箱：受影响者无法获知系统如何得出其输出。",
"解释机器学习的工作机制——监督、半监督、无监督学习从数据中提取并标记模式，而程序员本身不知道系统用了哪些模式。",
"由此指出结果对专家程序员同样不透明，即“标准不透明性”；并进一步区分出原则上不可消除的“深层/本质不透明性”。",
],
"terms": [
{"en": "opacity", "zh": "不透明性", "def": "本文指 AI 系统的决策过程对受影响者乃至专家程序员都不可知的状态。"},
{"en": "black box", "zh": "黑箱", "def": "指其内部运作机制无法被观察者了解的系统；本文以之为不透明系统的另一称呼。"},
{"en": "machine learning", "zh": "机器学习", "def": "从数据中自动提取模式的技术，分监督、半监督、无监督等方式。"},
{"en": "neural network", "zh": "神经网络", "def": "本文指机器学习技术所依托的（模拟）神经网络计算结构。"},
{"en": "standard opacity", "zh": "标准不透明性", "def": "本文指结果对专家程序员同样不透明的不透明性（Durán and Jongsma 2021）；与之相对的是原则上不可消除的“深层/本质”不透明性。"},
],
"background": [],
"vocab": [
{"en": "affected", "pos": "adj.", "zh": "受影响的", "ex": "impossible for the affected person to know"},
{"en": "come to", "pos": "phr.", "zh": "得出；得出（输出）", "ex": "how the system came to this output"},
{"en": "rely on", "pos": "v.", "zh": "依赖于", "ex": "many AI systems rely on machine learning"},
{"en": "extract", "pos": "v.", "zh": "提取", "ex": "extract patterns from a given dataset"},
{"en": "capture", "pos": "v.", "zh": "捕捉；把握", "ex": "captures patterns in the data"},
{"en": "label", "pos": "v.", "zh": "标记", "ex": "these are labelled in a way that appears useful"},
{"en": "in principle", "pos": "phr.", "zh": "原则上", "ex": "cannot be removed, in principle"},
],
}

ann["p031"] = {
"zh": "众所周知，认识论条件会对规范性问题产生影响。就我们这里的情形而言，如果存在不透明性，那么决策中的任何偏见都将难以察觉。不透明性与偏见乃是如今有时被称为“数据伦理”（data ethics）、“大数据伦理”或“算法伦理”（ethics of algorithms）这一领域的核心问题（Floridi and Taddeo 2016; Mittelstadt et al. 2016）。用于自动化决策支持与“预测性分析”的人工智能系统引发了“对缺乏正当程序、问责、社区参与与审计的严重关切”（Danaher 2016b; Whittaker et al. 2018, 18ff）。《通用数据保护条例》（GDPR）中所体现的“获得人工决定或说明理由之权利”这一观念，是否真正为我们所需，并不明了；一些学者主张，我们所拥有的其实是获得“良好校准的机器决定”的权利（Huq 2020），或者我们需要避免一种“证词缺口”（testimony gap）（Robert Sparrow and Flenady 2025）。不透明性与操纵（manipulation）有时被置于“认识论技术”（epistemic technology）（Alvarado 2023）或“认识论风险”的名目下加以讨论，但传统认识论（关于真的、得到证成的信念之条件）的诸概念与问题，是否适合于人类知觉与知识受人工智能技术影响的众多方式，仍有待观察。",
"logic": [
"从一般认识论原理出发：认识论条件影响规范性问题，据此指出不透明性使决策中的偏见难以被发现。",
"将不透明性与偏见定位为“数据伦理/算法伦理”的核心问题，并列举自动化决策支持与预测性分析引发的正当程序、问责、审计等关切。",
"检视“获得人工决定或说明理由之权利”是否够用，引出“良好校准的机器决定”与“证词缺口”两种替代主张。",
"最后对“认识论技术/认识论风险”能否借用传统认识论概念表示存疑，认为其适用性仍待观察。",
],
"terms": [
{"en": "opacity", "zh": "不透明性", "def": "此处强调其规范后果：它使决策中的偏见难以被察觉。"},
{"en": "bias", "zh": "偏见", "def": "本文指决策中基于不相干标准而对个体或群体造成不利的倾向；与不透明性并列为数据伦理核心。"},
{"en": "due process", "zh": "正当程序", "def": "本文指自动化决策中个人应享有的程序性保障，被指在 AI 系统中缺失。"},
{"en": "accountability", "zh": "问责（性）", "def": "本文指对决策后果可被追究的要求，被指在自动化决策支持系统中缺失。"},
{"en": "testimony gap", "zh": "证词缺口", "def": "本文指机器决策无法像人那样提供可作证词之说明的缺口（Robert Sparrow and Flenady 2025）。"},
],
"background": [
{"title": "《通用数据保护条例》（GDPR）", "body": "欧盟 2016 年通过的个人数据保护立法，其中赋予个人在自动化决策情形下获得人工干预与说明理由的权利；本文用它来讨论“获得人工决定之权利”这一观念是否真正够用。"},
],
"vocab": [
{"en": "have an impact on", "pos": "phr.", "zh": "对……产生影响", "ex": "conditions have an impact on normative issues"},
{"en": "detect", "pos": "v.", "zh": "察觉；发现", "ex": "will be hard to detect"},
{"en": "raise concerns", "pos": "phr.", "zh": "引发关切", "ex": "raise significant concerns about lack of due process"},
{"en": "under the heading(s) of", "pos": "phr.", "zh": "在……名目下", "ex": "discussed under the headings of"},
{"en": "it remains to be seen", "pos": "phr.", "zh": "仍有待观察", "ex": "it remains to be seen whether notions"},
{"en": "impact", "pos": "v.", "zh": "影响", "ex": "knowledge are impacted by AI technologies"},
{"en": "well-calibrated", "pos": "adj.", "zh": "良好校准的", "ex": "a well-calibrated machine decision"},
],
}

ann["p032"] = {
"zh": "不透明性促成了人们尝试勾勒可解释人工智能（explainable AI, XAI）的约束条件（Zednik 2021）以及认知模型的作用（Budding and Zednik 2024）。“可解读的”（interpretable）究竟意味着什么仍在讨论之中，尤其是它与解释（explanation）（Sullivan 2022; Zerilli 2022）以及与信任（Baron 2025; Robertson 2025）的关系——典型的区分在于导致一项决定的诸原因与一个理性能动者（rational agent）本会给出的诸理由之间，其中后者才是与责任相关者。如今已有大量活动旨在通过“可解释人工智能”来消除或弥补不透明性，而 XAI 已是一个重要的技术领域（Schwalbe and Finzel 2024）。",
"logic": [
"指出不透明性催生了对可解释 AI（XAI）的约束条件研究以及认知模型之作用的研究。",
"聚焦“可解读性”含义之争，尤其它与解释、与信任之间的关系。",
"引入关键区分：导致决定的诸原因 vs 理性能动者本会给出的诸理由，并指出后者才与责任相关。",
"总结 XAI 作为旨在消除或弥补不透明性的技术活动，已发展为一个重要技术领域。",
],
"terms": [
{"en": "explainable AI (XAI)", "zh": "可解释人工智能", "def": "旨在使 AI 系统决策可被人类理解、以消除或弥补不透明性的技术与研究领域。"},
{"en": "interpretability", "zh": "可解读性", "def": "本文指系统决策可被人类理喻的程度；其与“解释”的关系仍在讨论之中。"},
{"en": "rational agent", "zh": "理性能动者", "def": "本文指能为其行动提供理由的行动者；“理由”与“原因”相对，前者才算与责任相关。"},
],
"background": [],
"vocab": [
{"en": "generate", "pos": "v.", "zh": "促成；引发", "ex": "has generated attempts to outline"},
{"en": "outline", "pos": "v.", "zh": "勾勒；概述", "ex": "to outline the constraints for"},
{"en": "under discussion", "pos": "phr.", "zh": "在讨论之中", "ex": "means is under discussion"},
{"en": "lead to", "pos": "v.", "zh": "导致", "ex": "the causes that lead to a decision"},
{"en": "count for", "pos": "phr.", "zh": "对……重要；有价值", "ex": "the latter is what counts for responsibility"},
{"en": "remedy", "pos": "v.", "zh": "补救；弥补", "ex": "remove or remedy opacity"},
{"en": "aim to", "pos": "v.", "zh": "旨在", "ex": "activities that aim to remove"},
],
}

ann["p033"] = {
"zh": "如上所述，把所有人工智能系统都视为决策系统，可能是有益的。何者构成一个“好的”决定，在理性选择理论（theory of rational choice）中仍争论激烈（Thoma 2019）。也有人主张，有些困难选择是“难分高下”（on a par）的（Chang 2002），但究竟选哪一个的确事关重大，因为我们由此把它在未来变成“我们自己的”选择（Chang 2020）。此外还值得考虑：人工智能的决定或建议是否应当建立在用户“偏好”（preferences）这一假定之上。这在信息技术中是一种常见术语，但专司预测人类行为的科学（即心理学）是否大量使用它，并不清楚。",
"logic": [
"承接前文，把 AI 系统统一视为决策系统，为本节讨论奠定框架。",
"引入理性选择理论中“何为好决定”的争论，并以“难分高下”说作为一例。",
"即使选项难分高下，仍强调选择本身事关重大，因为选择会把选项变成“我们的”未来。",
"最后质疑 AI 决策/建议所依赖的用户“偏好”假定：IT 常用此术语，心理学却并不怎么使用。",
],
"terms": [
{"en": "theory of rational choice", "zh": "理性选择理论", "def": "研究理性前提下如何作选择的理论；本文指“何为好决定”在其中争论激烈。"},
{"en": "on a par", "zh": "难分高下", "def": "Chang（2002）提出的选项关系：两选项既非一个更好、也非相等，而是“难分高下”。"},
{"en": "preferences", "zh": "偏好", "def": "IT 中用以指用户被假定具有的选择倾向；本文质疑心理学是否真正使用这一概念。"},
],
"background": [
{"title": "张美露（Ruth Chang）", "body": "当代哲学家，以提出选项之间“难分高下”（parity）关系著称；本文引用其 2002 与 2020 年著作，讨论困难选择中何者当选为何仍事关重大。"},
],
"vocab": [
{"en": "regard ... as", "pos": "phr.", "zh": "把……视为", "ex": "regard all AI systems as decision systems"},
{"en": "constitute", "pos": "v.", "zh": "构成", "ex": "What constitutes a good decision"},
{"en": "hotly debated", "pos": "phr.", "zh": "争论激烈", "ex": "is hotly debated in the theory"},
{"en": "be worth", "pos": "adj.", "zh": "值得", "ex": "It is worth considering whether"},
{"en": "be based on", "pos": "phr.", "zh": "建立在……基础上", "ex": "should be based on the assumption"},
{"en": "specialise on", "pos": "v.", "zh": "专司；专门研究", "ex": "the science that specialises on the prediction"},
{"en": "make use of", "pos": "phr.", "zh": "使用；利用", "ex": "makes much use of it"},
],
}

ann["p034"] = {
"zh": "自动化的人工智能决策支持系统与“预测性分析”以数据为运作对象，并把一项决定作为“输出”产出。这种输出可从相对琐碎的一直到高度重大的不等：“这家餐厅合你的口味”、“保释被拒”，或“目标已识别并已交火”。数据分析在商业、医疗及其他领域中常被用于“预测性分析”，以预见未来的事态发展——既然预测变得更容易，它也将成为一种更廉价的商品。预测的一种用途是“预测性警务”（predictive policing）（Meijer and Wessels 2019），它包含着对公共自由的威胁（Alikhademi et al. 2022），因为它可以剥夺被预测者的力量。然而，许多关于警务的担忧似乎依赖于这样一些未来主义场景：执法部门预见到并惩罚尚在计划中的行动，而不是等到罪行已经犯下（如 2002 年电影《少数派报告》（Minority Report）中的情形）。原则上，这一做法对所有利益相关者都可能有其可取之处（Asaro 2019）。",
"logic": [
"描述自动化决策支持与预测性分析的运作方式：以数据为输入、决定为输出，并举三个分量迥异的例子展示输出的跨度。",
"指出预测因变易而变廉，进而被广泛应用；以预测性警务为例，指出其对公共自由的威胁。",
"缓和上述担忧：指出许多担忧依赖于“预治未然之罪”的科幻式场景（《少数派报告》）。",
"最后原则上肯定该做法对所有利益相关者可能有可取之处。",
],
"terms": [
{"en": "predictive analytics", "zh": "预测性分析", "def": "以数据分析预见未来事态的做法，广泛用于商业、医疗等领域。"},
{"en": "predictive policing", "zh": "预测性警务", "def": "用预测手段指导警务的做法；本文指出其可剥夺被预测者的力量，威胁公共自由。"},
{"en": "bail", "zh": "保释", "def": "本文作为“高度重大”决定输出的一例（“保释被拒”）。"},
],
"background": [
{"title": "《少数派报告》（Minority Report）", "body": "2002 年斯皮尔伯格执导的科幻电影，设定在执法机构可在罪行发生前预见并“预治”犯罪的未来社会；本文用以类比预测性警务所引发担忧的极端场景。"},
],
"vocab": [
{"en": "operate on", "pos": "phr.", "zh": "以……为运作对象", "ex": "operate on data and produce"},
{"en": "trivial", "pos": "adj.", "zh": "琐碎的", "ex": "from the relatively trivial to"},
{"en": "range from ... to ...", "pos": "phr.", "zh": "从……到……不等", "ex": "may range from the relatively trivial"},
{"en": "foresee", "pos": "v.", "zh": "预见", "ex": "to foresee future developments"},
{"en": "commodity", "pos": "n.", "zh": "商品", "ex": "a cheaper commodity"},
{"en": "take away", "pos": "v.", "zh": "夺走；剥夺", "ex": "take away power from the people"},
{"en": "merit", "pos": "n.", "zh": "可取之处；优点", "ex": "there could be merits in the approach"},
],
}

ann["p035"] = {
"zh": "随着大语言模型（LLM）的出现，让人工智能系统本身就伦理事务提供建议，变得更加可以设想了。或许人工智能系统甚至能让我们按照我们自己的标准成为更好的人（O'Neill, Klincewicz, and Kemmer 2022）。看来，即便早期版本也表现得足够好，以至于在“人类生成的伦理建议与人工智能生成的伦理建议之间，所感知到的建议价值并无显著差异”这一点上已被观察到（Terwiesch, Meincke, and Nave 2023）。",
"logic": [
"指出大语言模型的出现使“AI 自身就伦理事务提供建议”这一设想变得可行。",
"提出更强主张：AI 或可帮人按自身标准成为更好的人。",
"援引实证观察：早期版本的 AI 伦理建议在被感知的价值上已与人类建议无显著差异。",
],
"terms": [
{"en": "LLM", "zh": "大语言模型", "def": "本文指使 AI 自身能够就伦理事务建言的新一代模型。"},
],
"background": [],
"vocab": [
{"en": "advent", "pos": "n.", "zh": "出现；来临", "ex": "With the advent of LLMs"},
{"en": "conceivable", "pos": "adj.", "zh": "可设想的", "ex": "became more conceivable to have"},
{"en": "advise on", "pos": "v.", "zh": "就……提供建议", "ex": "advising on ethical matters"},
{"en": "by our own standards", "pos": "phr.", "zh": "按我们自己的标准", "ex": "become better humans, by our own standards"},
{"en": "perceived", "pos": "adj.", "zh": "被感知到的", "ex": "the perceived value of the advice"},
{"en": "no significant difference", "pos": "phr.", "zh": "无显著差异", "ex": "no significant difference in the perceived value"},
],
}

ann["p036"] = {
"zh": "人工智能系统可用于支持或取代人的决定，而在这些情形中，决定可能带有“偏见”（bias），也就是说，它可能依据不相干的标准作出决定，并或许由此对某些个体或群体作出不利歧视（另参 Friedman 1996）。偏见通常在以下情形显露出来：人们作出不公平的判断，因为作判断者受到了某种与手头事务实际上不相干的特征的影响——通常是对某一群体成员的歧视性成见。怀有偏见的人可能并未意识到自己怀有这种偏见——他们甚至可能真诚而明确地反对自己被发现所怀有的那种偏见（例如通过启动效应（priming）被发现，参 Graham and Lowery 2004）。关于机器学习中的公平与偏见，见 Binns 2018；关于更为一般的偏见概念，见 Johnson 2024。",
"logic": [
"先界定 AI 决策中“偏见”的含义：基于不相干标准作出决定，从而对个体或群体作出不利歧视。",
"进一步刻画偏见显露的机制：判断者被与手头事务不相干的特征（通常是群体成见）所影响。",
"指出偏见可以是无意识的：怀有者甚至可能真诚反对自己被测出的偏见。",
"末尾给出机器学习中公平与偏见问题以及一般偏见概念的文献指引。",
],
"terms": [
{"en": "bias", "zh": "偏见", "def": "本文指决策依据不相干标准、从而对个体或群体造成不利歧视的倾向。"},
{"en": "discrimination", "zh": "歧视", "def": "偏见在行为上的结果：对某些个体或群体作出不利对待。"},
{"en": "priming", "zh": "启动（效应）", "def": "心理学实验方法；本文用以说明人可在无觉察情形下表现出隐含偏见。"},
{"en": "fairness", "zh": "公平", "def": "机器学习研究中与偏见相对立的评价目标。"},
],
"background": [],
"vocab": [
{"en": "replacement", "pos": "n.", "zh": "取代；替换", "ex": "support or replacement of human decisions"},
{"en": "on the basis of", "pos": "phr.", "zh": "依据；在……基础上", "ex": "on the basis of criteria that are irrelevant"},
{"en": "irrelevant", "pos": "adj.", "zh": "不相干的", "ex": "criteria that are irrelevant"},
{"en": "surface", "pos": "v.", "zh": "显露；显现", "ex": "Bias typically surfaces when"},
{"en": "matter at hand", "pos": "phr.", "zh": "手头事务", "ex": "irrelevant to the matter at hand"},
{"en": "preconception", "pos": "n.", "zh": "成见", "ex": "a discriminatory preconception about members"},
{"en": "be aware of", "pos": "phr.", "zh": "意识到", "ex": "may not be aware of having that bias"},
],
}

ann["p037"] = {
"zh": "除了习得性偏见这一社会现象之外，人类认知系统一般还倾向于具有各种“认知偏见”（cognitive biases），例如“证实偏见”（confirmation bias）：人类倾向于把信息解释成在证实自己已有的信念。尽管这些偏见形式常被说成妨碍了理性判断中的表现（Kahnemann 2011），但它们其实只是认知系统应付如下事实的一种方式：用于某一既定决定的可用资源（时间、数据）总是有限的。这在计算机科学中被称为“有界最优性”（bounded optimality）（S. Russell 2016），在心理学中被称为“资源理性分析”（resource-rational analysis）（Lieder and Griffiths 2020）。",
"logic": [
"区分出第二种偏见：除社会习得偏见外，人类认知系统普遍具有的“认知偏见”，以证实偏见为例。",
"转述常见批评：认知偏见妨碍理性判断表现。",
"提出本文的重新评价：这些偏见实为认知系统应对有限资源（时间、数据）的方式。",
"给出两个跨学科定名：计算机科学的“有界最优性”与心理学的“资源理性分析”。",
],
"terms": [
{"en": "cognitive bias", "zh": "认知偏见", "def": "本文指人类认知系统普遍具有的系统性偏向，如证实偏见。"},
{"en": "confirmation bias", "zh": "证实偏见", "def": "倾向于把信息解释为证实自己已有信念的认知偏见。"},
{"en": "bounded optimality", "zh": "有界最优性", "def": "计算机科学中对有限资源下决策方式的刻画（S. Russell 2016）。"},
{"en": "resource-rational analysis", "zh": "资源理性分析", "def": "心理学对有限资源下认知行为的分析框架（Lieder and Griffiths 2020）。"},
],
"background": [
{"title": "丹尼尔·卡尼曼（Daniel Kahnemann）", "body": "心理学家，以系统揭示人类判断中的认知偏见与启发式著称，著有《思考，快与慢》；本文引用其 2011 年著作作为“认知偏见妨碍理性判断”这一常见说法的依据。"},
],
"vocab": [
{"en": "apart from", "pos": "phr.", "zh": "除了……之外", "ex": "Apart from the social phenomenon"},
{"en": "be prone to", "pos": "phr.", "zh": "倾向于", "ex": "is generally prone to have"},
{"en": "tend to", "pos": "v.", "zh": "倾向于", "ex": "humans tend to interpret information"},
{"en": "impede", "pos": "v.", "zh": "妨碍", "ex": "impede performance in rational judgment"},
{"en": "deal with", "pos": "v.", "zh": "应付；处理", "ex": "a way for cognitive systems to deal with"},
{"en": "available", "pos": "adj.", "zh": "可用的", "ex": "resources available for a given decision"},
{"en": "be known as", "pos": "phr.", "zh": "被称为", "ex": "is known as bounded optimality"},
],
}

ann["p038"] = {
"zh": "第三种偏见形式存在于数据之中，即数据表现出系统性误差之时，例如各种“统计偏见”（statistical bias）中的一种。严格而言，任何一个给定数据集只对单一一类问题才是无偏见的；因此，数据集的单纯创造本身就包含这样一种危险：它可能被用于另一类问题，结果对那类问题而言却是有偏见的。建立在这种数据之上的机器学习，届时不仅无法识别偏见，反而会把“历史偏见”（historical bias）编纂下来并自动化。因此，这类系统的问题在于偏见加上人类对系统过度的信任。这类自动化系统在政治上的影响可能相当重大（Eubanks 2018）。此外，程序的质量在很大程度上取决于所提供数据的质量，正应了那句老话“垃圾进，垃圾出”（garbage in, garbage out）。所以，如果数据本身已经带有偏见（例如关于嫌疑人肤色的警方数据），那么程序就会再生产这种偏见。有人主张，当今的伦理问题乃是人工智能所走的技术性“捷径”（shortcuts）的结果（Marcus 2018 [Other Internet Resources]; Cristianini 2023）——这就把偏见问题与一般的技术哲学联系了起来（见下文）。",
"logic": [
"引出第三种偏见：数据中表现为系统性误差的“统计偏见”。",
"指出关键事实：数据集只对单一类问题无偏见，移用于别类问题即变为有偏见，从而埋下危险。",
"说明机器学习在此情形下会把“历史偏见”编纂并自动化，问题在于偏见叠加人类过度信任。",
"援引“垃圾进，垃圾出”与警方肤色数据的例子说明偏见被程序再生产；最后把问题联系到技术“捷径”与一般技术哲学。",
],
"terms": [
{"en": "statistical bias", "zh": "统计偏见", "def": "数据表现出的系统性误差；本文指出任何数据集只对单一类问题无偏见。"},
{"en": "historical bias", "zh": "历史偏见", "def": "历史数据中已有的偏见；机器学习会将其编纂并自动化再生产。"},
{"en": "garbage in, garbage out", "zh": "垃圾进，垃圾出", "def": "计算机科学谚语：程序输出质量取决于输入数据质量。"},
{"en": "philosophy of technology", "zh": "技术哲学", "def": "本文指把偏见问题与 AI 所走技术“捷径”联系起来的一般技术哲学讨论。"},
],
"background": [
{"title": "维吉妮亚·尤班克斯（Virginia Eubanks）", "body": "著有《自动化不平等》（Automating Inequality, 2018），研究自动化公共福利系统对贫困人口的影响；本文引用其 2018 年著作，用以说明这类自动化系统在政治上的影响可能相当重大。"},
],
"vocab": [
{"en": "exhibit", "pos": "v.", "zh": "表现出；呈现", "ex": "when it exhibits systematic error"},
{"en": "danger", "pos": "n.", "zh": "危险", "ex": "involves the danger that may it"},
{"en": "turn out", "pos": "v.", "zh": "结果是；证明为", "ex": "turn out to be biased for"},
{"en": "codify", "pos": "v.", "zh": "编纂；成文化", "ex": "codify and automate the historical bias"},
{"en": "excessive trust", "pos": "n.", "zh": "过度信任", "ex": "placing excessive trust in the systems"},
{"en": "repercussion", "pos": "n.", "zh": "影响；后果", "ex": "The political repercussions of such"},
{"en": "depend on", "pos": "v.", "zh": "取决于", "ex": "depends heavily on the quality"},
{"en": "reproduce", "pos": "v.", "zh": "再生产；复制", "ex": "the program will reproduce that bias"},
],
}

ann["p039"] = {
"zh": "看来，针对偏见问题的技术性修复有着内在的局限，因为它们需要一种关于公平（fairness）的数学概念，而这种概念难得一见（Whittaker et al. 2018, 24ff; Selbst et al. 2019）；同样难得一见的，还有诸如“种族”（race）（见 Benthall and Haynes 2019）或“女性”（woman）（Mason 2022）之类关键术语的形式化概念。",
"logic": [
"对偏见的“技术性修复”主张提出内在限制：修复需要公平的数学概念，而这难以获得。",
"把困难进一步推广：关键术语（如“种族”“女性”）的形式化概念同样难以获得。",
],
"terms": [
{"en": "fairness", "zh": "公平", "def": "本文指可供技术修复偏见之用的、可数学化的公平概念；作者指出这种概念难以获得。"},
],
"background": [],
"vocab": [
{"en": "fix", "pos": "n.", "zh": "修复；补救办法", "ex": "technological fixes for the problem"},
{"en": "inherent limit", "pos": "n.", "zh": "内在局限", "ex": "have inherent limits in that"},
{"en": "in that", "pos": "conj.", "zh": "在于；因为", "ex": "in that they need a mathematical"},
{"en": "come by", "pos": "v.", "zh": "获得；得到", "ex": "which is hard to come by"},
{"en": "formal notion", "pos": "n.", "zh": "形式化概念", "ex": "a formal notion of key terms"},
],
}

ann["p040"] = {
"zh": "人—机器人互动（human-robot interaction, HRI）本身就是一个独立的学术领域，如今它对伦理事务、双方知觉的动态过程，以及社会语境中存在的各种不同利益与社会语境的复杂错综（包括协同工作）都给予了高度关注（例如 Arnold and Scheutz 2017）。",
"logic": [
"界定人—机器人互动（HRI）作为独立学术领域的地位。",
"列举该领域当前关注的对象：伦理事务、双方知觉动态、多元利益与复杂社会语境（含协同工作）。",
],
"terms": [
{"en": "human-robot interaction (HRI)", "zh": "人—机器人互动", "def": "研究人与机器人之间互动的独立学术领域，如今关注伦理、双方知觉动态与复杂社会语境。"},
],
"background": [],
"vocab": [
{"en": "in its own right", "pos": "phr.", "zh": "凭自身资格；本身", "ex": "an academic fields in its own right"},
{"en": "pay attention to", "pos": "phr.", "zh": "关注", "ex": "pays significant attention to"},
{"en": "dynamics", "pos": "n.", "zh": "动态过程；动力学", "ex": "the dynamics of perception from"},
{"en": "intricacy", "pos": "n.", "zh": "错综；复杂", "ex": "the intricacy of the social context"},
{"en": "context", "pos": "n.", "zh": "语境；情境", "ex": "the social context, including co-working"},
],
}

ann["p041"] = {
"zh": "人工智能也可用于驱动机器人；而如果这些机器人的运作过程或外观涉及欺骗、威胁人的尊严，或违反康德主义（Kantian）关于“对人性的尊重”（respect for humanity）的要求，它们就是成问题的。看来，人类极容易把心理属性归诸对象，并对它们产生共情，尤其是当这些对象的外观与有生命之物相似之时。这一点可以被用来欺骗人类（或动物），使其把超出机器人或人工智能系统所应得的理智乃至情感意义归诸它们。人形机器人学与动物机器人学中的某些部分在这一方面是成问题的。",
"logic": [
"指出 AI 驱动的机器人在三种情形下成问题：涉及欺骗、威胁人的尊严、违反康德式“尊重人性”要求。",
"给出心理机制解释：人极易把心理属性归诸外观类似生命的对象并产生共情。",
"指出这一机制可被利用，使人高估机器人的理智与情感意义。",
"据此点出人形与动物机器人学的某些方面在该问题上尤为成问题。",
],
"terms": [
{"en": "human dignity", "zh": "人的尊严", "def": "本文指康德意义上须受尊重的人性地位；机器人若威胁之即成问题。"},
{"en": "Kantian", "zh": "康德主义（者）（的）", "def": "本文指源自康德伦理学的立场，其要求“对人性的尊重”。"},
{"en": "humanoid robot", "zh": "人形机器人", "def": "外观类似人的机器人；本文指出其在引发人对机器的误归因方面成问题。"},
],
"background": [],
"vocab": [
{"en": "drive", "pos": "v.", "zh": "驱动", "ex": "used to drive robots"},
{"en": "involve", "pos": "v.", "zh": "涉及", "ex": "involve deception, threaten human dignity"},
{"en": "attribute ... to", "pos": "v.", "zh": "把……归诸", "ex": "attribute mental properties to objects"},
{"en": "empathise with", "pos": "v.", "zh": "对……共情", "ex": "empathise with them, especially when"},
{"en": "deceive into", "pos": "v.", "zh": "欺骗……使之", "ex": "deceive humans into attributing more"},
{"en": "in this regard", "pos": "phr.", "zh": "在这一方面", "ex": "problematic in this regard"},
],
}

ann["p042"] = {
"zh": "商业伦理与法律的基本约束同样适用于机器人：产品安全与法律责任（liability），或广告中不得欺骗。看来，这些既有的约束已经照料到了被提出的许多关切。然而，也存在一些情形：人与人的互动中有些方面看起来特别地属于人，或许无法由机器人替代——照护、爱与性。",
"logic": [
"指出商业伦理与法律的既有约束（产品安全、责任、广告真实性）同样适用于机器人。",
"认为这些既有约束已能应对多数被提出的关切。",
"转折指出例外：人际互动中照护、爱与性等“特别属人”的方面或不可被机器人替代。",
],
"terms": [
{"en": "liability", "zh": "法律责任；赔偿责任", "def": "此处指产品责任等商业法律约束，同样适用于机器人。"},
{"en": "care", "zh": "照护；关怀", "def": "本文指人际互动中特有的、机器人或许无法替代的方面之一（与爱、性并列）。"},
],
"background": [],
"vocab": [
{"en": "apply to", "pos": "v.", "zh": "适用于", "ex": "ethics and law apply to robots"},
{"en": "constraint", "pos": "n.", "zh": "约束", "ex": "Basic constraints of business ethics"},
{"en": "take care of", "pos": "phr.", "zh": "照料；处理", "ex": "take care of many concerns"},
{"en": "concern", "pos": "n.", "zh": "关切", "ex": "many concerns that are raised"},
{"en": "replace", "pos": "v.", "zh": "替代", "ex": "not be replaced by robots"},
],
}

ann["p043"] = {
"zh": "这些问题很快就会变得更加紧迫：届时机器人将在人工智能的帮助下真正离开工业“黄色笼子”（yellow cages），出现在更多日常生活情境之中。",
"logic": [
"指出问题将随机器人走出工业隔离、进入日常场景而变得更紧迫。",
"用“黄色笼子”的比喻标示机器人目前所处的工业隔离状态。",
],
"terms": [
{"en": "yellow cages", "zh": "黄色笼子", "def": "本文喻指机器人目前被隔离其中的工业作业区；离开它意味着进入日常生活。"},
],
"background": [],
"vocab": [
{"en": "urgent", "pos": "adj.", "zh": "紧迫的", "ex": "be more urgent soon"},
{"en": "with the help of", "pos": "phr.", "zh": "在……帮助下", "ex": "with the help of AI"},
{"en": "appear in", "pos": "v.", "zh": "出现在", "ex": "appear in more everyday life"},
{"en": "circumstance", "pos": "n.", "zh": "情境；情形", "ex": "everyday life circumstances"},
],
}

ann["p044"] = {
"zh": "机器人在人类医疗保健中的使用，目前还处在真实环境中的概念研究阶段，但它可能在几年内成为一种可用技术，并已引发人们对一个照护被去人化的敌托邦（dystopia）未来的若干担忧（A. Sharkey and Sharkey 2011; Rob Sparrow 2016）。当前的系统包括：支持人类照护者的机器人（例如为病人翻身抬床或运送物品）、使病人能够独立完成某些事情的机器人（例如用机械臂进食），还有作为陪伴与安慰交给病人的机器人（例如“Paro”机器海豹）。综述见 van Wynsberghe 2016; Nørskov 2017; Fosch-Villaronga and Albo-Canals 2019；用户调查见 Draper et al. 2014。",
"logic": [
"定位护理机器人的发展阶段：尚处真实环境中的概念研究阶段，但数年内或可实用。",
"指出其已引发“照护被去人化”之敌托邦未来的担忧。",
"列举当前三类系统：辅助照护者、辅助病人自立、提供陪伴安慰（Paro 机器海豹）。",
"给出综述与用户调查的文献指引。",
],
"terms": [
{"en": "care robot", "zh": "护理机器人", "def": "本文指用于医疗照护场景的机器人；本段区分辅助照护者、辅助病人自立与陪伴安慰三类。"},
{"en": "dystopia", "zh": "敌托邦；反面乌托邦", "def": "本文指人们担忧的“照护被去人化”的未来图景。"},
],
"background": [
{"title": "Paro 机器海豹（Paro robot seal）", "body": "一种外形为海豹幼崽的社交陪伴型机器人，常用于康复与老年人照护场景，作为陪伴与安慰物提供给患者。"},
],
"vocab": [
{"en": "at the level of", "pos": "phr.", "zh": "处于……阶段/水平", "ex": "at the level of concept studies"},
{"en": "raise concerns", "pos": "phr.", "zh": "引发担忧", "ex": "raised a number of concerns"},
{"en": "enable", "pos": "v.", "zh": "使能够", "ex": "enable patients to do certain things"},
{"en": "company", "pos": "n.", "zh": "陪伴", "ex": "given to patients as company"},
{"en": "comfort", "pos": "n.", "zh": "安慰；慰藉", "ex": "as company and comfort"},
{"en": "overview", "pos": "n.", "zh": "综述；概述", "ex": "For an overview, see"},
],
}

ann["p045"] = {
"zh": "照护问题之所以走到前台，一个原因是有人主张，在老龄化社会中我们将需要机器人。但这里是否真的成其为一个问题，并不很清楚，因为讨论大多聚焦于机器人使照护去人化的担忧，而现实中以及可预见的照护机器人，其实是作为辅助机器人（assistive robot）对技术性任务做经典的自动化。因此，它们只是在“在照护环境中执行任务”这一行为意义上是“护理机器人”，而不是在人“关怀”病人那种意义上。要说有什么风险，照护机器人的风险恰恰在于这种有意关怀的**缺席**——因为所需要的人类照护者可能更少。有趣的是，照护某物——哪怕是一个虚拟能动者——对照护者本人可能是有益的（Lee et al. 2019）。一个假装关怀的系统将是欺骗性的，因而成问题——除非这种欺骗被足够大的效用增益（utility gain）所抵消（Coeckelbergh 2016）。或许，在某些情形中，被一台机器所关怀的感觉，在某种程度上竟可以是一种进步？",
"logic": [
"陈述照护问题凸显的常见理由：老龄化社会需要机器人。",
"对此提出质疑：现有与可预见的照护机器人只是辅助型自动化，“护理机器人”仅在行为意义上成立。",
"指出真正风险在于有意关怀的缺席，而非机器取代关怀；并补充“照护他物对照护者有益”的观察。",
"讨论“假装关怀”的欺骗性，提出唯有足够大的效用增益可作抵消，并以反问留待商榷。",
],
"terms": [
{"en": "assistive robot", "zh": "辅助机器人", "def": "本文指在照护环境中承担技术性任务自动化的机器人，而非有意关怀病人者。"},
{"en": "care", "zh": "关怀；照护", "def": "本文区分两层：行为上的执行照护任务 vs 人对病人有意的关怀；风险恰在后者缺席。"},
{"en": "utility gain", "zh": "效用增益", "def": "本文指可用来抵消“假装关怀”之欺骗性的功利主义考量（Coeckelbergh 2016）。"},
],
"background": [],
"vocab": [
{"en": "come to the fore", "pos": "phr.", "zh": "走到前台；凸显", "ex": "issue of care has come to the fore"},
{"en": "ageing society", "pos": "n.", "zh": "老龄化社会", "ex": "need robots in ageing societies"},
{"en": "focus on", "pos": "v.", "zh": "聚焦于", "ex": "discussion mostly focuses on the fear"},
{"en": "de-humanise", "pos": "v.", "zh": "使去人化", "ex": "robots de-humanising care"},
{"en": "absence", "pos": "n.", "zh": "缺席；缺失", "ex": "the absence of such intentional care"},
{"en": "counter", "pos": "v.", "zh": "抵消；对抗", "ex": "deception is countered by sufficiently"},
{"en": "to some extent", "pos": "phr.", "zh": "在某种程度上", "ex": "by a machine, to some extent"},
],
}

ann["p046"] = {
"zh": "几位技术乐观主义者主张，人类很可能会对与机器人发生性关系与结伴相处感兴趣，并对这一想法感到自在（Levy 2007）。鉴于人类性偏好的多样性——包括性玩具与性爱娃娃——这一点看来非常可能：问题在于，这类装置是否应当被制造和推广，以及在这一暧昧地带是否应当对使用加以限制。近来，它似乎已进入“机器人哲学”（robot philosophy）的主流（Sullins 2012; Danaher and McArthur 2017; N. Sharkey et al. 2017; Bendel 2018; Devlin 2018）。",
"logic": [
"转述技术乐观主义者的预测：人类会对与机器人的性与陪伴感兴趣并安之若素。",
"以人类性偏好的既有多样性（性玩具、性爱娃娃）佐证该预测的可信度。",
"把问题从“是否可能”转为“是否应当制造推广、是否应对使用设限”。",
"指出该议题近年已进入机器人哲学的主流。",
],
"terms": [
{"en": "sex robot", "zh": "性爱机器人", "def": "本段讨论对象：用于性与陪伴的机器人装置。"},
{"en": "robot philosophy", "zh": "机器人哲学", "def": "本文指近年将性爱机器人议题纳入主流的哲学研究领域。"},
],
"background": [],
"vocab": [
{"en": "be interested in", "pos": "phr.", "zh": "对……感兴趣", "ex": "be interested in sex and"},
{"en": "companionship", "pos": "n.", "zh": "结伴；陪伴关系", "ex": "sex and companionship with robots"},
{"en": "be comfortable with", "pos": "phr.", "zh": "对……感到自在", "ex": "be comfortable with the idea"},
{"en": "given", "pos": "prep.", "zh": "鉴于", "ex": "Given the variation of human"},
{"en": "murky", "pos": "adj.", "zh": "暧昧的；浑浊的", "ex": "use in this murky area"},
{"en": "mainstream", "pos": "n.", "zh": "主流", "ex": "the mainstream of robot philosophy"},
],
}

ann["p047"] = {
"zh": "人类长期以来就对对象怀有深厚的情感依恋，因此，与一个可预测的人形机器人（android）结伴乃至相爱，或许是有吸引力的——尤其对那些与真实人相处困难、而已经更喜欢狗、猫、一只鸟、一台电脑或一个拓麻歌子（tamagotchi）的人而言。一些学者（Nyholm, Danaher, and Earp 2022）主张，这可以是真正的友谊，因而是一个有价值的目标。这种友谊即便在深度与功能上有所欠缺，看起来也确实可能增进总体效用（Miyahara and Shimizu 2025）。在这整个领域中，存在一个欺骗（deception）问题，因为机器人（目前）无法言其所意，也无法对人类怀有感情。众所周知，人类很容易把情感与思想归诸那些行为得仿佛具有感知能力（sentience）的实体，甚至归诸那些根本不表现任何行为的、明确无生命的对象。此外，为欺骗付费似乎也是传统性产业的一个基本组成部分。",
"logic": [
"以人对物的深厚情感依恋为据，说明与可预测人形机器人相伴乃至相爱何以有吸引力。",
"转述 Nyholm 等人的主张：这种关系可以是真正的友谊，因而是有价值的目标；并以效用论视角补充。",
"转入核心问题：欺骗——机器人目前无法言其所意、亦无真情。",
"以人易向无生命物归因情感的心理事实、以及性产业本就含“为欺骗付费”的传统，缓和欺骗问题的尖锐性。",
],
"terms": [
{"en": "android", "zh": "人形机器人", "def": "本文指可与之结伴或相爱的可预测人形装置。"},
{"en": "sentience", "zh": "感知能力；感受苦乐的能力", "def": "本文指人倾向于归诸机器人的、仿佛可感受苦乐的能力。"},
{"en": "deception", "zh": "欺骗", "def": "本段核心问题：机器人目前无法言其所意或对人有真情，却可能被当作有。"},
],
"background": [
{"title": "拓麻歌子（Tamagotchi）", "body": "万代 1996 年推出的电子宠物玩具，玩家需要随时照料屏幕中的虚拟宠物；本文用以举例说明人会对虚拟对象产生依恋。"},
],
"vocab": [
{"en": "attachment", "pos": "n.", "zh": "依恋；依附", "ex": "emotional attachments to objects"},
{"en": "struggle with", "pos": "v.", "zh": "与……相处困难；苦苦应付", "ex": "people who struggle with actual humans"},
{"en": "attractive", "pos": "adj.", "zh": "有吸引力的", "ex": "is attractive, especially to people"},
{"en": "overall utility", "pos": "n.", "zh": "总体效用", "ex": "increase overall utility, even if"},
{"en": "mean what one says", "pos": "phr.", "zh": "言其所意；言行合一", "ex": "cannot mean what it says"},
{"en": "be prone to", "pos": "phr.", "zh": "倾向于", "ex": "humans are prone to attribute feelings"},
{"en": "attribute ... to", "pos": "v.", "zh": "把……归诸", "ex": "attribute feelings and thoughts to entities"},
],
}

ann["p048"] = {
"zh": "最后，还有一些常常伴随性事务而来的关切，即知情同意（consent）（L. Frank and Nyholm 2017）、审美方面的关切，以及担忧人类可能被某些经验所“腐蚀”。尽管这看起来可能有些老派，但人类的行为确受经验影响；而且，色情内容或性爱机器人很可能助长如下看法：把他人仅仅视为欲望的对象，甚至视为受虐待的承受者，从而毁掉更深层的性体验与情色体验。“反对性爱机器人运动”（Campaign Against Sex Robots）主张，这类装置是奴隶制与卖淫的延续（Richardson 2016）。",
"logic": [
"列举伴随性事务而来的三类传统关切：同意、审美、经验对人的“腐蚀”。",
"即便“腐蚀”说看似老派，仍以行为受经验影响为据论证：色情与性爱机器人可能助长把他人物化的感知，毁掉深层性体验。",
"援引“反对性爱机器人运动”的激进主张：此类装置是奴隶制与卖淫的延续。",
],
"terms": [
{"en": "consent", "zh": "知情同意", "def": "本文指伴随性事务的伦理关切之一，适用于性爱机器人使用的讨论。"},
{"en": "Campaign Against Sex Robots", "zh": "反对性爱机器人运动", "def": "本文引用的倡议组织，主张性爱机器人是奴隶制与卖淫的延续。"},
],
"background": [],
"vocab": [
{"en": "accompany", "pos": "v.", "zh": "伴随；与……俱来", "ex": "concerns that have often accompanied"},
{"en": "namely", "pos": "adv.", "zh": "即；也就是", "ex": "namely consent (L. Frank"},
{"en": "corrupt", "pos": "v.", "zh": "腐蚀；使堕落", "ex": "humans may be corrupted by certain"},
{"en": "be influenced by", "pos": "phr.", "zh": "受……影响", "ex": "behaviour is influenced by experience"},
{"en": "support", "pos": "v.", "zh": "助长；支持", "ex": "support the perception of other humans"},
{"en": "object of desire", "pos": "n.", "zh": "欲望对象", "ex": "mere objects of desire"},
{"en": "ruin", "pos": "v.", "zh": "毁掉；破坏", "ex": "and thus ruin a deeper sexual"},
],
}

ann["p049"] = {
"zh": "在关于自主系统的讨论中，存在着若干种自主性（autonomy）概念。在哲学争论中涉及一种较强的概念，那里自主性是责任（responsibility）与人格（personhood）的基础（Christman 2018）。在这一语境中，责任蕴含自主性，但反过来并不成立，因此可以存在这样的系统：它具有一定程度的技术自主性，却并不引发责任问题。机器人学中较弱、更偏技术性的自主性概念则是相对的、渐进的：一个系统相对于人的控制被说成在某一程度上是自主的（Müller 2012）。这里与人工智能中偏见和不透明性的问题存在一种平行关系，因为自主性也涉及一种权力关系：谁在控制，谁在负责？更高的自主性意味着更高的风险，但更高的自主性同时也是更高生产率收益的一个条件，因此发展方向是朝向更高风险的。所以，这一问题主要是一个风险与误用的问题，而不是严重的自主性问题。",
"logic": [
"先指出自主系统讨论中存在多种自主性概念。",
"区分两种概念：哲学上的强概念（自主性为责任与人格之基础）与机器人学上的弱技术概念（相对、渐进）。",
"指出“责任蕴含自主性但反之不然”，故技术自主性未必引发责任问题。",
"将自主性与偏见/不透明性问题类比：都涉及“谁控制、谁负责”的权力关系；并指出发展朝向更高风险，故主要问题是风险与误用。",
],
"terms": [
{"en": "autonomy", "zh": "自主性", "def": "本文区分强哲学义（责任与人格之基础）与弱技术义（相对于人控的程度性、渐进）。"},
{"en": "personhood", "zh": "人格（地位）", "def": "本文指哲学上自主性作为其基础的地位。"},
{"en": "responsibility", "zh": "责任", "def": "本段指出责任蕴含自主性；自主性问题与“谁负责”的权力关系相关。"},
],
"background": [],
"vocab": [
{"en": "notion", "pos": "n.", "zh": "概念；观念", "ex": "several notions of autonomy"},
{"en": "imply", "pos": "v.", "zh": "蕴含；意味着", "ex": "responsibility implies autonomy"},
{"en": "inversely", "pos": "adv.", "zh": "反过来地", "ex": "autonomy, but not inversely"},
{"en": "with respect to", "pos": "phr.", "zh": "相对于；关于", "ex": "autonomous with respect to human control"},
{"en": "to a certain degree", "pos": "phr.", "zh": "在某一程度上", "ex": "to a certain degree (Müller"},
{"en": "parallel", "pos": "n.", "zh": "平行；相似处", "ex": "There is a parallel here to"},
{"en": "productivity gain", "pos": "n.", "zh": "生产率收益", "ex": "higher productivity gains, so"},
],
}

ann["p050"] = {
"zh": "在大多数司法辖区中，已有一套精细的民事与刑事法律体系用以解决法律责任（liability）问题。技术标准——例如医疗环境中机械安全使用的标准——很可能需要加以调整。针对这类安全攸关的系统以及“安全应用”，已经存在一个“可验证人工智能”（verifiable AI）领域。技术标准乃是此类监管（regulation）与自我监管的一个重要组成部分。",
"logic": [
"指出多数辖区已有精细的民刑事法律体系处理责任问题。",
"认为既有技术标准（如医疗机械安全标准）需要调整。",
"指出“可验证 AI”领域已为安全攸关系统而存在。",
"总结技术标准在监管与自我监管中的重要地位。",
],
"terms": [
{"en": "liability", "zh": "法律责任；赔偿责任", "def": "本文指由民刑事法律体系处理的归责问题。"},
{"en": "verifiable AI", "zh": "可验证人工智能", "def": "本文指面向安全攸关系统与安全应用、可被验证的 AI 领域。"},
{"en": "regulation", "zh": "监管；规制", "def": "本文指由技术标准等构成的治理框架，含自我监管。"},
],
"background": [],
"vocab": [
{"en": "jurisdiction", "pos": "n.", "zh": "司法辖区", "ex": "In most jurisdictions, there is"},
{"en": "sophisticated", "pos": "adj.", "zh": "精细的；成熟的", "ex": "a sophisticated system of civil"},
{"en": "resolve", "pos": "v.", "zh": "解决", "ex": "to resolve issues of liability"},
{"en": "adjust", "pos": "v.", "zh": "调整", "ex": "likely need to be adjusted"},
{"en": "safety-critical", "pos": "adj.", "zh": "安全攸关的", "ex": "such safety-critical systems"},
{"en": "self-regulation", "pos": "n.", "zh": "自我监管", "ex": "such regulation and self-regulation"},
],
}

ann["p051"] = {
"zh": "在陆地上、水上、水下、空中或太空中的众多自主系统之中，我们讨论两个样本：自动驾驶汽车（autonomous vehicles）与自主武器（autonomous weapons）。如今还有一种朝向人工智能个人助理的发展，无论是否具有机器人形态。看来，这些助理将面临重大障碍是合理的推测，因为助理行为的伦理与法律责任将不得不予以澄清（Milano and Nyholm 2024）。",
"logic": [
"列举各空间域中的自主系统，引出本段将讨论的两个样本：自动驾驶汽车与自主武器。",
"提及 AI 个人助理的新发展（无论是否机器人形态）。",
"指出个人助理将面临重大障碍，理由是其行为的伦理与法律责任须予澄清。",
],
"terms": [
{"en": "autonomous vehicle (AV)", "zh": "自动驾驶汽车", "def": "本文讨论的两类自主系统之一。"},
{"en": "autonomous weapons", "zh": "自主武器", "def": "本文讨论的两类自主系统之一。"},
],
"background": [],
"vocab": [
{"en": "sample", "pos": "n.", "zh": "样本；示例", "ex": "we discuss two samples"},
{"en": "personal assistant", "pos": "n.", "zh": "个人助理", "ex": "towards AI personal assistants"},
{"en": "plausible", "pos": "adj.", "zh": "合理的；似可信的", "ex": "It seems plausible that"},
{"en": "hurdle", "pos": "n.", "zh": "障碍", "ex": "face significant hurdles, since"},
{"en": "clarify", "pos": "v.", "zh": "澄清；阐明", "ex": "would have to be clarified"},
],
}

ann["p052"] = {
"zh": "自动驾驶汽车怀有这样的希望：减少人类驾驶当前所造成的极为重大的损害——每年约有 100 万人丧生，更多人受伤，环境受到污染，大地被混凝土与沥青封死，城市中满是未使用（停放着）的汽车，等等。然而，关于自动驾驶汽车应如何行为、以及责任与风险应在其运作于其中的复杂系统中如何分配，似乎存在一些问题。（对于完全自主——即“5 级”汽车（SAE 2015）——的开发究竟还要多久，抑或是否已经实现，也存在重大分歧。）",
"logic": [
"先立自动驾驶汽车的正面许诺：大幅降低人类驾驶造成的伤亡与环境损害，并列举数据。",
"转折指出仍有规范性问题：车辆应如何行为、责任与风险如何在复杂系统中分配。",
"附带提及：对 L5 全自动驾驶何时实现（或是否已实现）存在重大分歧。",
],
"terms": [
{"en": "autonomous vehicle (AV)", "zh": "自动驾驶汽车", "def": "本文以其为自主系统的讨论样本之一。"},
{"en": "level 5", "zh": "5 级", "def": "SAE 2015 标准中完全自主的汽车等级。"},
],
"background": [
{"title": "SAE J3016 自动驾驶分级", "body": "SAE International 于 2015 年发布的自动驾驶分级标准，将驾驶自动化分为 0 至 5 级，其中“5 级”为完全自动驾驶；本文用其指称全自动驾驶汽车。"},
],
"vocab": [
{"en": "hold the promise", "pos": "phr.", "zh": "怀有……希望；有望", "ex": "hold the promise to reduce"},
{"en": "approximately", "pos": "adv.", "zh": "大约", "ex": "approximately 1 million humans"},
{"en": "distribute", "pos": "v.", "zh": "分配", "ex": "responsibility and risk should be distributed"},
{"en": "complicated", "pos": "adj.", "zh": "复杂的", "ex": "the complicated system the vehicles"},
{"en": "disagreement", "pos": "n.", "zh": "分歧", "ex": "significant disagreement over how long"},
{"en": "fully autonomous", "pos": "adj.", "zh": "完全自主的", "ex": "development of fully autonomous, or"},
],
}

ann["p053"] = {
"zh": "在这一语境中，围绕“电车难题”（trolley problems）有着大量讨论。在经典的“电车难题”中（Thomson 1976；另见 SEP 词条 Woollard and Howard-Snyder 2021），呈现了各种两难困境。最简单的版本是：一辆有轨电车行驶在轨道上，正朝五个人驶去并将碾死他们，除非把电车转轨到一条侧轨上；但那条侧轨上有一个人，如果电车走那条侧轨，这个人将被碾死。这个例子可追溯到 Foot（1967, 6）中的一处论述，她讨论了若干两难情形，其中一个行动的被容忍的后果不同于被意图的后果。“电车难题”并不意在描述现实的伦理问题，也不是要以一个“正确”选择来解决。毋宁说，它们是一些思想实验（thought experiment）：在其中，选择被人为地限制为数目有限、彼此分明、一次性的少量选项，而且能动者拥有完备的知识。这些问题被用作一种理论工具，以探究伦理直觉与伦理理论（Kamm and Rakowski 2016）。这类问题使许多人联想到现实驾驶以及自动驾驶中遇到的问题（Lin 2015）。然而，一个真实的司机或一辆自动驾驶汽车是否真会需要去解电车难题，是可疑的；而这一问题是否与自动驾驶汽车的伦理学真正相关，也存在争议（Awad et al. 2018; Paulo 2023）。",
"logic": [
"指出电车难题在自动驾驶语境中被大量讨论。",
"复述经典电车难题的最简版本，并追溯其起源于 Foot（1967）对“被容忍 vs 被意图后果”的讨论。",
"澄清电车难题的方法论定位：它们不是现实问题，而是人为限制条件、假定能动者有完备知识的思想实验，用作探究伦理直觉与理论的工具。",
"指出其之所以被联想到自动驾驶，同时质疑现实中司机/车是否真需面对它、以及它与 AV 伦理是否真正相关。",
],
"terms": [
{"en": "trolley problem", "zh": "电车难题", "def": "本文指一类关于是否转向撞一人以救五人的思想实验，用作探究伦理直觉的理论工具。"},
{"en": "thought experiment", "zh": "思想实验", "def": "本文指电车难题的方法论性质：人为约束选项为有限少数、假定能动者有完备知识。"},
{"en": "principle of double effect", "zh": "双重效应原则", "def": "Foot（1967）讨论中区分被意图后果与被容忍后果；这正是双重效应原则的核心区分。"},
],
"background": [
{"title": "菲利帕·福特（Philippa Foot）", "body": "20 世纪英国哲学家；现代电车难题讨论始于她 1967 年关于安乐死与双重效应原则的论述。"},
{"title": "朱迪思·贾维斯·汤姆森（Judith Jarvis Thomson）", "body": "美国哲学家；1976 年的论文使“电车难题”成为当代伦理学讨论的经典范式。"},
],
"vocab": [
{"en": "divert", "pos": "v.", "zh": "使转向", "ex": "unless the train is diverted"},
{"en": "go back to", "pos": "phr.", "zh": "可追溯到", "ex": "The example goes back to a remark"},
{"en": "tolerate", "pos": "v.", "zh": "容忍；容许", "ex": "where tolerated differ from intended"},
{"en": "intended", "pos": "adj.", "zh": "被意图的；有意的", "ex": "from intended consequences of an action"},
{"en": "be supposed to", "pos": "phr.", "zh": "意在；本应", "ex": "are not supposed to describe actual"},
{"en": "constrain", "pos": "v.", "zh": "约束；限制", "ex": "choice is artificially constrained to"},
{"en": "one-off", "pos": "adj.", "zh": "一次性的", "ex": "distinct one-off options"},
{"en": "relevance", "pos": "n.", "zh": "相关性", "ex": "has relevance to the ethics"},
],
}

ann["p054"] = {
"zh": "自动化武器这一观念由来已久：“例如，我们可以不部署简单的制导导弹或遥控飞行器，而是发射完全自主的陆、海、空航行器，使其能够执行复杂、远程的侦察与攻击任务。”（DARPA 1983, 1）。这一提议在当时被讥为“幻想”（Dreyfus, Dreyfus, and Athanasiou 1986, ix），但如今它已成现实，至少对于较容易识别的目标（导弹、车辆、飞机、舰船、建筑物等）是如此。反对（致命性）自主武器系统（AWS 或 LAWS）的主要论证是：它们支持法外杀戮（extrajudicial killing）、把责任从人身上移开、并使战争或杀戮更易发生——问题的详细清单见 Lin, Bekey, and Abney 2008, 73–86；Taddeo 2024。",
"logic": [
"以 DARPA 1983 年的引文表明“自动化武器”观念由来已久，并经历了从被讥为“幻想”到成为现实的过程。",
"限定当前现实的范围：至少对易识别目标已可实现。",
"列举反对（致命性）自主武器系统的三大主要论证：支持法外杀戮、抽走人对责任的承担、使战争/杀戮更易发生。",
],
"terms": [
{"en": "autonomous weapons / LAWS", "zh": "自主武器 / 致命性自主武器系统", "def": "本段讨论对象；指可自主执行侦察与攻击任务的武器系统。"},
{"en": "extrajudicial killing", "zh": "法外杀戮", "def": "本文指自主武器系统被指支持的未经司法程序的杀戮。"},
],
"background": [
{"title": "DARPA（美国国防高级研究计划局）", "body": "美国国防部下属研究机构；其 1983 年文件中已提出完全自主陆、海、空航行器的设想。本文用以说明自动化武器观念的历史之久。"},
],
"vocab": [
{"en": "field", "pos": "v.", "zh": "部署；投入战场", "ex": "instead of fielding simple guided"},
{"en": "launch", "pos": "v.", "zh": "发射；发起", "ex": "we might launch completely autonomous"},
{"en": "reconnaissance", "pos": "n.", "zh": "侦察", "ex": "far-ranging reconnaissance and attack"},
{"en": "ridicule", "pos": "v.", "zh": "讥讽；嘲笑", "ex": "This proposal was ridiculed as"},
{"en": "fantasy", "pos": "n.", "zh": "幻想", "ex": "as “fantasy” at the time"},
{"en": "identifiable", "pos": "adj.", "zh": "可识别的", "ex": "more easily identifiable targets"},
{"en": "take away", "pos": "v.", "zh": "移开；夺走", "ex": "take responsibility away from humans"},
],
}

ann["p055"] = {
"zh": "自主武器系统会使战争更可能发生吗？看来，增加自主武器系统的可获得性、并降低被追究问责的概率，将会提高其被使用的概率。然而，有罪不罚（impunity）的这一关键不对称性，在使用远距离武器（例如遥控武器）的常规战争中就已经存在。这些正是“制止杀人机器人运动”（Campaign to Stop Killer Robots）及其他行动主义团体所提出的那类事例。其中有些看来无异于说：自主武器的确是武器……而武器是杀人的，但我们仍在以巨大数量制造它们。就问责（accountability）问题而言，自主武器也许会使对负责能动者的指认与起诉变得更为困难——但这一点并不确定，因为至少在常规战争中人们可以保存数字记录。分配惩罚的困难有时被称为“报复缺口”（retribution gap）（Danaher 2016a）。过去 5 年的发展看来朝向人工智能在战争中的被接受，但许多伦理问题依然存在，而且——至少在官方口径上——始终仍有“人在环中”（humans in the loop），即便人工智能的使用——例如用于目标识别——减少了人的介入，尤其在速度至关重要之时。就监管而言，全面禁令如今看来已不可能。",
"logic": [
"回答“自主武器是否使战争更可能”：指出可获得性上升、问责概率下降会提高其使用概率。",
"缓和该论证：有罪不罚的不对称性在常规远距离战争中早已存在；“武器即杀人之物却仍被大量制造”的反类比也被提出。",
"讨论问责维度：自主武器或使指认与起诉更难，但数字记录的留存又使之不明；引出“报复缺口”概念。",
"总览近五年趋势：AI 日益被战争接受，官方仍称“人在环中”，但实际人的介入减少；监管上全面禁令已无可能。",
],
"terms": [
{"en": "accountability", "zh": "问责（性）", "def": "本段指自主武器被使用后被追究责任的概率；降低之会提高使用概率。"},
{"en": "impunity", "zh": "有罪不罚", "def": "本文指行动者不受追究的不对称处境；在常规远距离武器战争中早已存在。"},
{"en": "retribution gap", "zh": "报复缺口", "def": "本文指分配惩罚的困难（Danaher 2016a）。"},
{"en": "humans in the loop", "zh": "人在环中", "def": "本文指官方口径中自主武器使用仍有人参与决策的状态。"},
],
"background": [
{"title": "制止杀人机器人运动（Campaign to Stop Killer Robots）", "body": "国际非政府倡议联盟，倡导禁止致命性自主武器系统；本文用以指其提出的那类反对案例。"},
],
"vocab": [
{"en": "availability", "pos": "n.", "zh": "可获得性", "ex": "increasing the availability of autonomous"},
{"en": "hold accountable", "pos": "phr.", "zh": "追究问责", "ex": "probability of being held accountable"},
{"en": "asymmetry", "pos": "n.", "zh": "不对称性", "ex": "crucial asymmetry of impunity"},
{"en": "bring forward", "pos": "v.", "zh": "提出", "ex": "cases brought forward by the Campaign"},
{"en": "equivalent to", "pos": "adj.", "zh": "等同于", "ex": "equivalent to saying that autonomous"},
{"en": "identification", "pos": "n.", "zh": "指认；识别", "ex": "identification and prosecution of"},
{"en": "off the cards", "pos": "phr.", "zh": "不可能；无望", "ex": "now seems off the cards"},
],
}

ann["p056"] = {
"zh": "另一个问题似乎是：在战争中使用自主武器，会使战争更糟，还是也许会使战争不那么糟？如果机器人能减少伤亡、战争罪（war crime）与战争中的罪行，答案很可能是肯定的；这一点既被用作支持这些武器的论证（Arkin 2009; Müller 2016a），也被用作反对它们的论证（Amoroso and Tamburrini 2018）。可以说，主要威胁并不在于在常规战争中使用这类武器，而在于在不对称冲突（asymmetric conflict）中被使用，或被非国家能动者——包括罪犯——所使用。",
"logic": [
"提出第二问：自主武器会使战争更糟还是不那么糟。",
"指出若机器人减少伤亡与战争罪，答案可能为肯定；该事实同时被正反两方援引。",
"引出作者判断：主要威胁不在常规战争，而在不对称冲突与非国家能动者（含罪犯）手中的使用。",
],
"terms": [
{"en": "war crime", "zh": "战争罪", "def": "本文指自主武器若能减少的罪行之一；也是正反论证共同援引的事实。"},
{"en": "asymmetric conflict", "zh": "不对称冲突", "def": "本文作者认为自主武器的主要威胁所在，区别于常规战争。"},
{"en": "non-state agent", "zh": "非国家能动者", "def": "本文指包括罪犯在内的非国家行动者，被视为主要威胁来源。"},
],
"background": [],
"vocab": [
{"en": "casualty", "pos": "n.", "zh": "伤亡（人员）", "ex": "reduce casualties, war crimes"},
{"en": "in favour of", "pos": "phr.", "zh": "支持；赞成", "ex": "an argument in favour of these"},
{"en": "arguably", "pos": "adv.", "zh": "可以说；按说", "ex": "Arguably the main threat is"},
{"en": "conventional", "pos": "adj.", "zh": "常规的", "ex": "in conventional warfare, but"},
{"en": "threat", "pos": "n.", "zh": "威胁", "ex": "the main threat is not the"},
],
}

ann["p057"] = {
"zh": "也有人说，自主武器无法符合国际人道法（International Humanitarian Law）；后者要求在军事冲突中遵守区分原则（principle of distinction，战斗员与平民之间）、比例原则（principle of proportionality，武力的）与军事必要原则（military necessity，武力的）（A. Sharkey 2019）。如今，这看来更像是一个技术问题，即武器必须被构造和使用得不违反人道法。有充分迹象表明，人权是人工智能伦理学的一个有用框架，但这一框架尚未被大量使用，仅有一些例外（Smuha 2021a）——反过来，在人权研究中，人工智能对该领域有重大影响这一点则被广泛承认。在这一语境中，有时也会提出人的尊严（human dignity）概念（A. Sharkey 2019；参 Rueda et al. 2025）。",
"logic": [
"转述“自主武器无法符合国际人道法”的主张，并列出人道法三原则：区分、比例、军事必要。",
"将该问题重新定性为技术问题：武器须被构造与使用得不违反人道法。",
"讨论人权框架与 AI 伦理的关系：人权框架有用却少被采用，反之 AI 对人权领域的影响已被广泛承认。",
"提及人的尊严概念在本语境中被提出。",
],
"terms": [
{"en": "International Humanitarian Law", "zh": "国际人道法", "def": "本文要求军事冲突中遵守区分、比例、军事必要三原则的法律体系。"},
{"en": "principle of distinction", "zh": "区分原则", "def": "国际人道法原则之一：区分战斗员与平民。"},
{"en": "principle of proportionality", "zh": "比例原则", "def": "国际人道法原则之一：使用武力须与军事目标成比例。"},
{"en": "military necessity", "zh": "军事必要", "def": "国际人道法原则之一：使用武力须为军事必要。"},
{"en": "human dignity", "zh": "人的尊严", "def": "本文在自主武器语境中被提出的伦理理念。"},
],
"background": [],
"vocab": [
{"en": "conform to", "pos": "v.", "zh": "符合；遵从", "ex": "cannot conform to International"},
{"en": "observance", "pos": "n.", "zh": "遵守", "ex": "requires observance of the principles"},
{"en": "violate", "pos": "v.", "zh": "违反", "ex": "do not violate Humanitarian Law"},
{"en": "framework", "pos": "n.", "zh": "框架", "ex": "a useful framework for AI ethics"},
{"en": "exception", "pos": "n.", "zh": "例外", "ex": "with some exceptions (Smuha"},
{"en": "inversely", "pos": "adv.", "zh": "反过来", "ex": "inversely, it is widely recognised"},
{"en": "raise", "pos": "v.", "zh": "提出", "ex": "has been raised in this context"},
],
}

blocks = []
for b in src["blocks"]:
    o = dict(b)
    if b["kind"] == "heading":
        o["title_zh"] = title_zh[b["id"]]
    else:
        a = ann[b["pid"]]
        o["zh"] = a["zh"]
        o["logic"] = a["logic"]
        o["terms"] = a["terms"]
        o["background"] = a["background"]
        o["vocab"] = a["vocab"]
    blocks.append(o)

out = {"shard": "b", "blocks": blocks}
(ROOT / "content").mkdir(exist_ok=True)
(ROOT / "content" / "shard-b.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", len(blocks), "blocks")
