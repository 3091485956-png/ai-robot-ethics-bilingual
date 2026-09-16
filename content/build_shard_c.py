# -*- coding: utf-8 -*-
"""Build content/shard-c.json from content-source/shard-c.source.json.
Copies every source field verbatim; adds title_zh / zh / logic / terms / background / vocab.
"""
import json
from pathlib import Path

ROOT = Path(r"C:\Users\loong\Desktop\人工智能与机器人伦理学")
src = json.loads((ROOT / "content-source" / "shard-c.source.json").read_text(encoding="utf-8"))

HEADINGS = {
    "MorStaMacEthRes": "道德地位、机器伦理与责任",
    "sec-2-7-1": "道德地位",
    "sec-2-7-2": "能动作用",
    "sec-2-7-3": "机器伦理",
    "sec-2-7-4": "责任",
    "SupExiRis": "超级智能与存在性风险",
    "sec-2-8-1": "奇点与超级智能",
    "sec-2-8-2": "存在性风险",
}

ANN = {}

# ---------------- 2.7.1 Moral Status ----------------
ANN["p058"] = {
    "zh": "在初步近似的意义上，人工智能与机器人系统的道德地位（moral status）问题关乎这样一个问题：它们是否负有义务，以及我们是否对它们负有义务——这一问题通常以能动作用（agency）的语言来表述：一个实体是道德能动者（moral agent），当且仅当它负有义务；它是道德承受者（moral patient），当且仅当道德能动者（例如人类）对它负有义务。人类是道德能动者的典型范例，有感知能力的动物则是道德承受者的典型范例。标准观点认为，人工智能与机器人系统不具有任何种类的道德地位……但这一观点已受到压力，相关讨论也使人们对道德地位的本性获得了新的洞见（Misselhorn 2020; Powers and Ganascia 2020）。",
    "logic": [
        "先以“初步近似”界定道德地位问题的两面：系统是否对他者负有义务，以及我们是否对系统负有义务。",
        "进而用能动作用的语言把该问题转写为道德能动者与道德承受者的定义，并以人类与有感知动物分别作为典型范例。",
        "指出标准观点认为人工智能与机器人系统毫无道德地位，但该观点已受到压力，讨论本身深化了对道德地位本性的理解。",
    ],
    "terms": [
        {"en": "moral status", "zh": "道德地位", "def": "一个实体是否负有义务、以及他者是否对其负有义务这一规范身份；本段以此界定人工智能与机器人系统的伦理地位问题。"},
        {"en": "moral agent", "zh": "道德能动者", "def": "负有义务的实体，即能够承担指责与赞扬的主体；本段以人类为其典型范例。"},
        {"en": "moral patient", "zh": "道德承受者", "def": "道德能动者对其负有义务的实体；本段以有感知能力的动物为其典型范例。"},
        {"en": "sentience", "zh": "感知能力；感受苦乐的能力", "def": "本文语境中指体验苦乐状态的能力；本段以有感知动物作为道德承受者的典型范例。"},
    ],
    "background": [],
    "vocab": [
        {"en": "approximation", "pos": "n.", "zh": "近似；粗略说法", "ex": "In a first approximation, the issue of moral status"},
        {"en": "concern", "pos": "v.", "zh": "关乎；涉及", "ex": "concerns the question whether they have obligations"},
        {"en": "come under pressure", "pos": "phr.", "zh": "受到压力；受到挑战", "ex": "this view has come under pressure"},
        {"en": "lead to insights", "pos": "phr.", "zh": "带来洞见", "ex": "the discussion has led to insights about the nature"},
    ],
}

ANN["p059"] = {
    "zh": "一些作者指出，应当认真考虑当前机器人是否必须被分配权利（Gunkel 2018; Turner 2019; Danaher 2020）。这一立场似乎主要依赖于对反对者的批评，以及如下经验观察：机器人及其他非人格者有时被**对待**得仿佛拥有权利。循此思路，有人提出了一种“关系性转向”（relational turn）：如果我们与机器人打交道时就当它们仿佛拥有权利，那么再去探究它们是否**真正**拥有此类权利或许就是徒劳（Coeckelbergh 2010, 2012, 2018）。这就引出一个问题：这种反实在论究竟能走多远，而在以人类为中心的进路中说“机器人拥有权利”又意味着什么（Gerdes 2016）。在论争的另一方，Bryson 坚持认为机器人不应享有权利（Bryson 2010），尽管她也把这视为一种可能性（Gunkel and Bryson 2014）。看来，关于“权利”的讨论如今正转向超级智能（superintelligence）领域（Gordon 2022），或转向对“道德地位”的讨论，见（Clarke and Savulescu 2021; Clarke, Zohny, and Savulescu 2021; Müller 2021），在那里出现了一种趋势，即倾向于认为感知能力（sentience）至少是道德地位的必要条件（Königs 2025）。相应地，人们担忧造出具有意识（consciousness）的人工智能系统是否合乎伦理（Butlin et al. 2023 [Other Internet Resources]; Dung 2023），因为这可能使感知能力成为可能，从而带来痛苦。一些作者已呼吁“暂停合成现象体验”（moratorium on synthetic phenomenology）（Bentley et al. 2018, 28f; Metzinger 2021）。",
    "logic": [
        "概述支持方立场：主张应认真考虑当前机器人被分配权利，并指出其论据主要靠批评对手与经验观察。",
        "介绍“关系性转向”这一反实在论主张，即我们如何对待机器人比机器人是否真有权利更根本，并追问该立场的边界。",
        "摆出反方 Bryson 的立场，并说明权利讨论现已转向超级智能或道德地位，且出现“感知能力是道德地位必要条件”的趋势。",
        "由此引出造出有意识的人工智能系统是否合伦理的担忧，以及“暂停合成现象体验”的呼吁。",
    ],
    "terms": [
        {"en": "relational turn", "zh": "关系性转向", "def": "一种进路，认为我们与机器人的关系性对待具有优先性，不必再追问机器人是否“真正”拥有权利。"},
        {"en": "anti-realism", "zh": "反实在论", "def": "本文语境中否认“机器人是否真正拥有权利”这一问题具有独立于我们对待方式的客观事实。"},
        {"en": "consciousness", "zh": "意识", "def": "此处指人工智能系统可能具有的主观现象体验；造出有意识的系统可能使感知能力与痛苦成为可能。"},
        {"en": "moratorium on synthetic phenomenology", "zh": "暂停合成现象体验", "def": "部分作者发出的呼吁：在弄清人工系统的现象体验之前暂停相关研究，以免造成人工受苦。"},
    ],
    "background": [
        {"title": "乔安娜·布莱森（Joanna Bryson）", "body": "人工智能研究者，长期主张机器人在伦理上是人类工具、不应享有权利；本段将其置于论争反方。"},
    ],
    "vocab": [
        {"en": "allocate", "pos": "v.", "zh": "分配；赋予", "ex": "whether current robots must be allocated rights"},
        {"en": "rely on", "pos": "phr.", "zh": "依赖；依靠", "ex": "This position seems to rely largely on criticism"},
        {"en": "empirical observation", "pos": "n.", "zh": "经验观察", "ex": "the empirical observation that robots and other non-persons"},
        {"en": "futile", "pos": "adj.", "zh": "徒劳的；无用的", "ex": "it might be futile to search whether they really do"},
        {"en": "enjoy rights", "pos": "phr.", "zh": "享有权利", "ex": "robots should not enjoy rights"},
        {"en": "trend", "pos": "n.", "zh": "趋势；倾向", "ex": "there is a trend in favour of the view"},
        {"en": "moratorium", "pos": "n.", "zh": "（暂时）停止；中止", "ex": "called for a “moratorium on synthetic phenomenology”"},
    ],
}

ANN["p060"] = {
    "zh": "是否应当赋予机器人（或其他人工智能系统）“法律实体”（legal entities）或“法律人格”（legal persons）的地位，这是一个完全不同的问题——此处所谓“法律实体”，是指自然人以及国家、企业或组织在如下意义上所是的那种：它们可以拥有财产性权利并承担法律责任，但不承担刑事责任（参较 Bryson, Diamantis, and Grant 2017; Bertolini and Aiello 2018）。在环境伦理学中，关于自然物应否拥有法律权利，存在一场由来已久的讨论（C. D. Stone 1972）。",
    "logic": [
        "把“道德权利/地位”问题与“法律人格/法律实体地位”问题明确区分，指出二者是完全独立的议题。",
        "界定此处“法律实体”的含义：可享有财产性权利、承担法律责任，但不承担刑事责任。",
        "援引环境伦理学中关于自然物法律权利的长期讨论作为类比先例。",
    ],
    "terms": [
        {"en": "legal person / legal entity", "zh": "法律人格／法律实体", "def": "法律上可享有权利、承担义务与责任的主体；本段指出人工智能能否获得该地位是独立于道德地位的另一问题。"},
        {"en": "liability", "zh": "法律责任；赔偿责任", "def": "本段语境中指法律实体可承担的财产性法律责任，但不含刑事责任。"},
    ],
    "background": [
        {"title": "C. D. Stone《树木应有诉讼资格吗？》", "body": "Christopher D. Stone 1972 年的论文主张自然物可在法律上享有权利与诉讼资格，是环境伦理学与环境法的经典文献。"},
    ],
    "vocab": [
        {"en": "wholly separate", "pos": "phr.", "zh": "完全不同的；截然分开的", "ex": "There is a wholly separate issue whether robots"},
        {"en": "natural person", "pos": "n.", "zh": "自然人", "ex": "in which natural persons, but also states, businesses"},
        {"en": "criminal liability", "pos": "n.", "zh": "刑事责任", "ex": "but not criminal liability"},
        {"en": "long-standing", "pos": "adj.", "zh": "长期存在的；由来已久的", "ex": "there is a long-standing discussion about legal rights"},
    ],
}

# ---------------- 2.7.2 Agency ----------------
ANN["p061"] = {
    "zh": "经典的“厚重”（thick）道德能动者（moral agent）概念，其设计目的在于分配道德责任（moral responsibility），即承担指责与赞扬的能力。因此它蕴含一个认识论条件（关于世界的知识）、一个控制条件（在世界中行动的能力）、一个规范条件（出于理由而行动的能力，尤其是反思后的偏好），以及受痛苦或快乐影响的可能性——在技术上即带有效价的现象状态，亦即感知能力（sentience）（Müller 2021; Dung 2025）。一些从技术视角考察这一问题的作者得出结论说，大语言模型（LLM）缺乏道德能动性（moral agency）的本质特征：不存在个体能动者，该能动者不自己生成其规范，也不因其互动而被塑造（Barandiaran and Almendros 2024 [Other Internet Resources]）。人们很容易说，当前人工智能根本没有“真正的价值”，只有它据以行动的偏好。它并不对这些偏好负责，因为它无法反思价值，也无法改变价值。道德能动性与人格（personhood）密切相关，而人格又与自由意志相关联（Frankfurt 1971; Strawson 2004）。",
    "logic": [
        "界定经典“厚重”道德能动者概念的目的——分配道德责任——并列出其蕴含的四个条件：认识、控制、规范，以及受苦乐影响的可能。",
        "援引技术视角的结论：大语言模型缺乏道德能动性的本质特征（无个体能动者、不自生规范、不因互动被塑造）。",
        "进一步论断当前人工智能只有偏好而无真正价值，亦不对其负责，因为它不能反思或改变价值。",
        "收尾把道德能动性与人格、自由意志关联起来。",
    ],
    "terms": [
        {"en": "moral agency", "zh": "道德能动性", "def": "道德能动者所具备的、可承担指责与赞扬的地位；本段指出大语言模型缺乏其本质特征。"},
        {"en": "personhood", "zh": "人格（地位）", "def": "与道德能动性密切相关、并与自由意志相联的主体地位。"},
        {"en": "free will", "zh": "自由意志", "def": "本段将其与人格相联，作为道德能动性的传统前提。"},
        {"en": "valence", "zh": "效价", "def": "现象状态在技术上的好坏极性（苦或乐）；本段以此界定受苦乐影响的可能性即感知能力。"},
    ],
    "background": [],
    "vocab": [
        {"en": "be designed to", "pos": "phr.", "zh": "旨在；为……而设计", "ex": "is designed to assign moral responsibility"},
        {"en": "imply", "pos": "v.", "zh": "蕴含；意味着", "ex": "It thus implies an epistemic condition"},
        {"en": "reflected preferences", "pos": "n.", "zh": "反思后的偏好", "ex": "especially reflected preferences"},
        {"en": "lack", "pos": "v.", "zh": "缺乏；缺少", "ex": "LLMs lack essential features of moral agency"},
        {"en": "reflect on", "pos": "phr.", "zh": "反思", "ex": "it cannot reflect on values or change them"},
        {"en": "be associated with", "pos": "phr.", "zh": "与……相关联", "ex": "which is associated with free will"},
    ],
}

ANN["p062"] = {
    "zh": "然而，还存在一种“单薄”（thin）的能动作用（agency）概念，它取自关于能动作用的技术性定义——“做某件事的东西”——并被用于早期人工智能伦理学，在那里也使用了一种单薄的“机器伦理”（machine ethics）概念（见下文）。例如：“机器伦理将计算机伦理学的领域从关注人们用计算机做什么，扩展到机器自身做什么这一问题。”（Allen, Smit, and Wallach 2006, 15）",
    "logic": [
        "与上文“厚重”概念相对，引入“单薄”的能动作用概念，说明其来源是技术性定义“做某件事的东西”。",
        "指出这一单薄概念被早期人工智能伦理学沿用，并配套使用单薄的“机器伦理”概念。",
        "援引 Allen、Smit 与 Wallach 的引文，具体说明机器伦理被理解为“追问机器自身做什么”。",
    ],
    "terms": [
        {"en": "machine ethics", "zh": "机器伦理", "def": "此处在单薄意义上使用，指把机器自身的行为纳入伦理考察；本段引文中将其界定为追问机器自身做什么。"},
    ],
    "background": [],
    "vocab": [
        {"en": "be taken from", "pos": "phr.", "zh": "取自；来源于", "ex": "is taken from the technical notion of agency"},
        {"en": "extend ... beyond", "pos": "phr.", "zh": "把……扩展到……之外", "ex": "extends the field of computer ethics beyond concern"},
        {"en": "concern for", "pos": "phr.", "zh": "对……的关注", "ex": "beyond concern for what people do with their computers"},
        {"en": "e.g.", "pos": "abbr.", "zh": "例如", "ex": "E.g. “Machine ethics extends the field"},
    ],
}

ANN["p063"] = {
    "zh": "James Moor（Moor 2006, 19–20）区分了四类机器能动者：伦理影响能动者（ethical impact agents）（例：机器人赛马骑师）、隐含伦理能动者（implicit ethical agents）（例：安全的自动驾驶仪）、显式伦理能动者（explicit ethical agents）（例：使用形式化方法来估算效用），以及完全伦理能动者（full ethical agents）（“能够做出显式的伦理判断，并且一般说来有能力对这些判断做出合理的证成。一个普通的成年人就是一个完全伦理能动者”）。",
    "logic": [
        "援引 James Moor 的分类框架，把机器能动者按伦理卷入程度分为由弱到强的四类。",
        "每类配一个具体例子（机器人骑师、安全自动驾驶仪、形式化估算效用、普通成年人），使分类可操作。",
        "以引文界定“完全伦理能动者”的标准：能做出显式伦理判断并对其合理证成。",
    ],
    "terms": [
        {"en": "explicit ethical agent", "zh": "显式伦理能动者", "def": "Moor 四分类之一，指能运用形式化方法（如估算效用）来做出伦理判断的机器能动者。"},
        {"en": "full ethical agent", "zh": "完全伦理能动者", "def": "Moor 四分类中最强一级，能做出显式伦理判断并合理证成；普通成年人为其范例。"},
        {"en": "utility", "zh": "效用", "def": "功利主义框架中衡量后果好坏的量；此处作为形式化估算的对象出现。"},
    ],
    "background": [],
    "vocab": [
        {"en": "distinguish", "pos": "v.", "zh": "区分", "ex": "distinguishes four types of machine agents"},
        {"en": "formal methods", "pos": "n.", "zh": "形式化方法", "ex": "using formal methods to estimate utility"},
        {"en": "make judgments", "pos": "phr.", "zh": "做出判断", "ex": "can make explicit ethical judgments"},
        {"en": "competent", "pos": "adj.", "zh": "有能力的；胜任的", "ex": "generally is competent to reasonably justify them"},
        {"en": "justify", "pos": "v.", "zh": "证成；为……提供理由", "ex": "competent to reasonably justify them"},
    ],
}

ANN["p064"] = {
    "zh": "被编程的能动者有时不被视为“完全的”能动者，因为它们“有能力却无理解”（competent without comprehension），就像大脑中的神经元一样（Dennett 2017; Hakli and Mäkelä 2019）。Luciano Floridi 是一位对人工智能系统能力的强主张持著名批评态度的学者，他也建议我们应采用一种最低限度的能动作用（agency）概念，但一种要求很高的智能概念——于是，当前的人工智能系统，哪怕只是一个反应式的大语言模型，也算是能动者，但却不具有智能（Floridi 2023a; 2023b, ch. 2）——对这一进路的批评，见（Zafar 2024）。",
    "logic": [
        "指出被编程的能动者常因“有能力却无理解”而不被算作完全能动者，并以脑神经元作类比。",
        "介绍 Floridi 的对称主张：调低能动作用的门槛、抬高智能的门槛。",
        "给出该主张的推论——当前人工智能系统是能动者却无智能——并附一句批评性文献指引。",
    ],
    "terms": [
        {"en": "minimal notion of agency", "zh": "最低限度的能动作用概念", "def": "Floridi 主张的弱化版能动概念，使当前人工智能系统可被归入能动者，同时以严格的智能概念把它们排除在智能之外。"},
    ],
    "background": [
        {"title": "丹尼尔·丹尼特（Daniel Dennett）", "body": "美国心灵哲学家；“competent without comprehension”指系统可表现出胜任能力而无需理解其所为。"},
    ],
    "vocab": [
        {"en": "competent", "pos": "adj.", "zh": "有能力的", "ex": "competent without comprehension"},
        {"en": "comprehension", "pos": "n.", "zh": "理解", "ex": "competent without comprehension"},
        {"en": "come out as", "pos": "phr.", "zh": "结果是；被归为", "ex": "come out as agents, but without intelligence"},
        {"en": "reactive", "pos": "adj.", "zh": "反应式的", "ex": "even a merely reactive LLM"},
        {"en": "criticism", "pos": "n.", "zh": "批评", "ex": "for a criticism of this approach"},
    ],
}

# ---------------- 2.7.3 Machine Ethics ----------------
ANN["p065"] = {
    "zh": "机器伦理（machine ethics）是为机器、为“伦理机器”、把机器当作**主体**而设的伦理，而非把机器当作**对象**来考察人类使用的伦理。在较早的文献中，人们常常不太清楚它究竟应当覆盖人工智能伦理学的全部，还是只是其中的一部分（Floridi and Saunders 2004; Moor 2006; Anderson and Anderson 2011; Wallach and Asaro 2017），但所幸把人工智能伦理学等同于机器伦理的做法如今已被克服。有时还出现过如下有风险的推论：如果机器在伦理上是相关的，那么我们就需要一门机器伦理（Anderson and Anderson 2007, 15）。如果“机器伦理”取 Moor 机器能动者那种单薄含义，其中仅凭“伦理影响”就足以成为“伦理能动者”（Moor 2006, 19）或“人工道德能动者”（artificial moral agent, AMA）（Allen, Varner, and Zinser 2000），那么这一说法或许成立。机器伦理的这种单薄含义等同于“设计伦理”（ethics of design），后者如今是更通行的术语（Brey and Dainow 2024）（Friedman 1996; Houkes and Vermaas 2010; Verbeek 2011）。如果机器伦理取一种要求更高的含义，那么我们就回到了上文关于道德能动者与道德承受者的讨论。把“伦理机器”两种含义混为一谈的做法如今已不如从前常见，尽管现在偶尔也有人把“对齐”用于设计（如 van de Poel 2020, 388）以及单薄的机器伦理（Cave et al. 2019）。",
    "logic": [
        "开篇界定机器伦理的对象：以机器为主体而非对象，区别于考察人类如何使用机器的伦理。",
        "回顾早期文献中机器伦理与人工智能伦理学范围不清乃至等同的问题，并指出这一等同现已被克服。",
        "拆解“机器在伦理上相关就需要机器伦理”这一有风险推论，指出其在单薄含义下成立，并把单薄含义等同于“设计伦理”。",
        "区分单薄与要求更高两种含义：后者回到道德能动者与承受者的讨论；最后指出两种含义混淆虽减少，但“对齐”一词仍被混用。",
    ],
    "terms": [
        {"en": "artificial moral agent (AMA)", "zh": "人工道德能动者", "def": "单薄意义下仅凭“伦理影响”即可被称为伦理能动者的机器系统。"},
        {"en": "ethics of design", "zh": "设计伦理", "def": "即机器伦理的单薄含义，关注在设计阶段塑造技术的伦理属性；如今是更通行的术语。"},
    ],
    "background": [],
    "vocab": [
        {"en": "conflation", "pos": "n.", "zh": "混为一谈；混淆", "ex": "The conflation of both senses"},
        {"en": "at play", "pos": "phr.", "zh": "起作用；在场", "ex": "there was the risky inference at play"},
        {"en": "ethically relevant", "pos": "adj.", "zh": "在伦理上相关的", "ex": "if machines are ethically relevant"},
        {"en": "be identical to", "pos": "phr.", "zh": "等同于", "ex": "is identical to “ethics of design”"},
        {"en": "demanding", "pos": "adj.", "zh": "要求高的", "ex": "in a more demanding sense"},
        {"en": "occasional", "pos": "adj.", "zh": "偶尔的", "ex": "there is now occasional use of “alignment”"},
    ],
}

# ---------------- 2.7.4 Responsibility ----------------
ANN["p066"] = {
    "zh": "责任（responsibility）的分配往往是一件复杂的事情：汽车制造商对汽车的技术安全负责，驾驶员对驾驶负责，机械师对维护负责，公共主管部门对道路的技术条件负责，等等。一般而言，“基于人工智能的决策或行动，其后果往往是众多行动者之间无数次互动的结果，这些行动者包括设计者、开发者、用户、软件与硬件。……有了分布式的能动作用（distributed agency），也就有了分布式的责任（distributed responsibility）。”（Taddeo and Floridi 2018, 751）这种分配如何发生，并不是一个为人工智能所特有的问题，但在人工智能的语境下它显得尤为紧迫（Nyholm 2018a, 2018b）。在经典控制工程中，分布式控制往往是通过一个控制层级加上跨这些层级的控制回路（control loop）来实现的。如今，即便是个人的工作也变成了与人工智能的协同工作与共同创造。与此同时，许多社会制度却依赖于把责任分配给某一个人，例如为了指责与赞扬，或为了法律责任（liability）与著作权。",
    "logic": [
        "以汽车责任链的日常例子说明责任分配本就复杂、由多主体分担。",
        "援引 Taddeo 与 Floridi 的观点：基于人工智能的决策后果来自众多行动者的无数互动，故分布式能动作用带来分布式责任。",
        "指出该分配问题并非人工智能所特有，但在其语境下尤为紧迫，并借控制工程类比说明分布式如何实现。",
        "揭示张力：个人工作已变为与人工智能协同，但社会制度仍要求把责任归到个人（褒贬、赔偿、版权）。",
    ],
    "terms": [
        {"en": "distributed agency", "zh": "分布式能动作用", "def": "能动作用分散在设计者、开发者、用户、软硬件等众多行动者之间的状态；本段主张其伴随分布式责任。"},
        {"en": "distributed responsibility", "zh": "分布式责任", "def": "责任随分布式能动作用而分散于多主体，而非集中于单一可指认者。"},
        {"en": "control loop", "zh": "控制回路", "def": "控制工程中实现反馈控制的闭环；本段借来说明分布式控制如何在层级间实现。"},
    ],
    "background": [],
    "vocab": [
        {"en": "allocation", "pos": "n.", "zh": "分配", "ex": "Allocation of responsibility is often a complicated matter"},
        {"en": "maintenance", "pos": "n.", "zh": "维护；保养", "ex": "a mechanic is responsible for maintenance"},
        {"en": "countless", "pos": "adj.", "zh": "无数的", "ex": "the result of countless interactions among many actors"},
        {"en": "distributed", "pos": "adj.", "zh": "分布式的", "ex": "With distributed agency comes distributed responsibility"},
        {"en": "gain urgency", "pos": "phr.", "zh": "显得紧迫", "ex": "it gains particular urgency in this context"},
        {"en": "copyright", "pos": "n.", "zh": "著作权；版权", "ex": "for liability and copyright"},
    ],
}

ANN["p067"] = {
    "zh": "围绕如何为自主武器（autonomous weapons）的杀戮分配责任，已有不少讨论，并有人提出存在一种“责任缺口”（responsibility gap）（尤其见 Rob Sparrow 2007），其含义是：人和机器可能都无法承担责任。或许解决方案是让人类保持在“回路中”（in the loop）、“回路上”（on the loop），或处于“有意义的控制”（meaningful control）之下（Santoni de Sio and van den Hoven 2018），这将使我们能够把功劳归于应得者（Danaher and Nyholm 2021）。然而，或许确实存在悲剧性的抉择（Danaher 2022），又或者我们不应当假定每一个事件都有某个对该事件负责的人，于是真正的问题很可能在于风险的分配（Simpson and Müller 2016）。经典风险分析（Hansson 2013）指出，关键在于辨明谁**暴露**于风险之下、谁是潜在**受益者**、谁做出**决策**（Hansson 2018, 1822–1824）。对责任缺口持更怀疑态度的论述，见（Tigard 2021; Königs 2022; Da Silva 2024）。人工智能系统的出现究竟是真的挑战了我们的责任分配方式，还是只是造成了暂时的困惑，仍是一个悬而未决的问题。",
    "logic": [
        "以自主武器杀戮为例引入“责任缺口”问题：人与机器似乎都无法承担责任。",
        "列举一种应对思路——把人保持在回路中、回路上或有意义的控制之下，使责任可被正当归属。",
        "转而提出替代诊断：或承认存在悲剧性抉择，或否认“凡事必有责任人”，把真问题重新表述为风险分配。",
        "借经典风险分析给出辨明要点（谁暴露、谁受益、谁决策），并指出人工智能是否真正挑战责任分配尚无定论。",
    ],
    "terms": [
        {"en": "responsibility gap", "zh": "责任缺口", "def": "指自主武器致害时，人与机器似乎都无法恰当承担责任的责任真空状态。"},
        {"en": "meaningful control", "zh": "有意义的控制", "def": "让人对自主系统保持实质控制的进路，被提议用以填补责任缺口。"},
        {"en": "risk distribution", "zh": "风险分配", "def": "本段主张责任问题的实质或许是风险在暴露者、受益者与决策者之间的分配。"},
    ],
    "background": [
        {"title": "罗伯·斯帕罗（Rob Sparrow）", "body": "澳大利亚伦理学家，2007 年提出自主武器将造成“责任缺口”的著名论证，本段为其出处。"},
    ],
    "vocab": [
        {"en": "in the loop", "pos": "phr.", "zh": "在回路中（人类持续参与决策）", "ex": "keep humans “in the loop” or “on the loop”"},
        {"en": "credit where credit is due", "pos": "phr.", "zh": "把功劳归于应得者", "ex": "allow us to credit where credit is due"},
        {"en": "tragic choices", "pos": "n.", "zh": "悲剧性抉择", "ex": "there truly are tragic choices"},
        {"en": "be exposed to", "pos": "phr.", "zh": "暴露于", "ex": "who is exposed to risk"},
        {"en": "potential beneficiary", "pos": "n.", "zh": "潜在受益者", "ex": "who is a potential beneficiary"},
        {"en": "open question", "pos": "n.", "zh": "悬而未决的问题", "ex": "It remains an open question"},
    ],
}

# ---------------- 2.8.1 Singularity & Superintelligence ----------------
ANN["p068"] = {
    "zh": "至此的讨论仅限于当前以及可清楚预见的人工智能形式及其社会后果。除了这种“短期”人工智能伦理学之外，还存在“长期”人工智能伦理学，即讨论在更长的时期内是否会出现一组新的问题——其中或许包括那些严重到足以值得我们现在就加以关注的问题（Sætra and Danaher 2025）。",
    "logic": [
        "收束前文，指出迄今讨论限于当前及可预见的人工智能形式及其社会后果。",
        "引入“长期人工智能伦理学”这一新增板块，并界定其为对远期可能出现的新问题的讨论。",
        "说明该板块的正当性门槛：问题严重到值得当下关注，从而过渡到超级智能与存在性风险。",
    ],
    "terms": [
        {"en": "long-term AI ethics", "zh": "长期人工智能伦理学", "def": "相对于聚焦当前与可预见人工智能的“短期”伦理，讨论更远期可能出现的新问题的研究取向。"},
    ],
    "background": [],
    "vocab": [
        {"en": "foreseeable", "pos": "adj.", "zh": "可预见的", "ex": "current and clearly foreseeable forms of AI"},
        {"en": "in addition to", "pos": "phr.", "zh": "除……之外", "ex": "In addition to this “short-term” AI ethics"},
        {"en": "deserve attention", "pos": "phr.", "zh": "值得关注", "ex": "deserve our attention now"},
        {"en": "societal consequences", "pos": "n.", "zh": "社会后果", "ex": "and their societal consequences"},
    ],
}

ANN["p069"] = {
    "zh": "关于人工智能长期风险的经典叙事有两个步骤：1）当前的人工智能发展轨迹将上升到超越人类智能水平的系统，也就是它们是“超级智能的”（superintelligent），而在这一点上会出现一个急剧的断裂，即“奇点”（singularity），从那时起人工智能的发展便脱离人类控制、难以预测（Kurzweil 2005, 487）。2）一旦达到该点，大规模的负面后果——包括人类这一物种的存在性风险（existential risk, XRisk）——便具有相当大的概率。",
    "logic": [
        "把长期风险叙事拆解为逻辑上前后相继的两步，便于后文逐一检验。",
        "第一步：由当前轨迹上升到超级智能，并在奇点处发生脱离人类控制的急剧断裂。",
        "第二步：达到该点后，大规模负面后果（包括人类物种的存在性风险）具有显著概率。",
    ],
    "terms": [
        {"en": "superintelligence", "zh": "超级智能", "def": "在第一步中超越人类智能水平的人工智能系统。"},
        {"en": "singularity", "zh": "奇点", "def": "智能发展发生急剧断裂、此后人工智能发展脱离人类控制且难以预测的转折点。"},
        {"en": "existential risk (x-risk)", "zh": "存在性风险", "def": "第二步所指的、危及人类物种存续的大规模负面风险。"},
    ],
    "background": [],
    "vocab": [
        {"en": "trajectory", "pos": "n.", "zh": "轨迹；发展路径", "ex": "The current trajectory of artificial intelligence"},
        {"en": "surpass", "pos": "v.", "zh": "超越；超过", "ex": "systems that surpass the human level of intelligence"},
        {"en": "discontinuity", "pos": "n.", "zh": "断裂；不连续", "ex": "there is a sharp discontinuity"},
        {"en": "out of control", "pos": "phr.", "zh": "失去控制", "ex": "is out of human control"},
        {"en": "have probability", "pos": "phr.", "zh": "具有……概率", "ex": "have significant probability"},
    ],
}

ANN["p070"] = {
    "zh": "像 Kurzweil 或 Dario Amodei（Anthropic 的现任首席执行官）这样的乐观主义者会走完第一步，然后预期一个正面的发展；而像 Bostrom 或 Yudkowsky 这样的悲观主义者则预期第二步中的风险是由第一步推出的。话虽如此，近来一些关于长期风险的讨论正在从存在性风险与超级智能那里移开，回到对人工智能风险的一般性考察。",
    "logic": [
        "沿经典叙事第一步划分乐观与悲观两派：乐观者（Kurzweil、Amodei）走完第一步后预期向好。",
        "指出悲观者（Bostrom、Yudkowsky）主张第二步的风险由第一步必然推出。",
        "补充近期动向：部分讨论正从存在性风险与超级智能回撤，转向更一般的人工智能风险考察。",
    ],
    "terms": [
        {"en": "existential risk (x-risk)", "zh": "存在性风险", "def": "此处指悲观派由第一步推出的第二步风险；本段同时指出该议题正被部分讨论者边缘化。"},
    ],
    "background": [
        {"title": "尼克·波斯特洛姆（Nick Bostrom）", "body": "牛津大学哲学家，著有《超级智能》（2014），是存在性风险与超级智能论争的核心人物；本段将其列为悲观派代表。"},
        {"title": "埃利泽·尤德考斯基（Eliezer Yudkowsky）", "body": "美国人工智能研究者，长期倡导智能爆炸风险与价值对齐研究；本段将其列为悲观派代表。"},
        {"title": "达里奥·阿莫迪（Dario Amodei）", "body": "人工智能公司 Anthropic 的首席执行官；本段将其作为乐观派代表点名。"},
    ],
    "vocab": [
        {"en": "optimist", "pos": "n.", "zh": "乐观主义者", "ex": "Optimists like Kurzweil or Dario Amodei"},
        {"en": "pessimist", "pos": "n.", "zh": "悲观主义者", "ex": "pessimists like Bostrom or Yudkowsky"},
        {"en": "expect", "pos": "v.", "zh": "预期；期待", "ex": "expect that the risk in the 2nd step"},
        {"en": "having said that", "pos": "phr.", "zh": "话虽如此", "ex": "Having said that, more recently"},
        {"en": "move away from", "pos": "phr.", "zh": "从……移开；脱离", "ex": "moving away from XRisk and superintelligence"},
    ],
}

ANN["p071"] = {
    "zh": "从历史上看，“我们所造的机器人将接管世界”这一恐惧，早在计算机出现之前就已攫住人类的想象（如 Butler 1863），而且它正是恰佩克（Čapek）那部首次引入“机器人”（robot）一词的名剧的核心主题（Čapek 1920）：机器人在被赋予感受之后起而反抗人类。这一恐惧最初由 Irvin Good 表述为现有人工智能可能走向“智能爆炸”（intelligence explosion）的一种轨迹：",
    "logic": [
        "从思想史溯源“机器人接管世界”的恐惧，指出它早于计算机存在。",
        "以 Butler（1863）与恰佩克引入“robot”一词的名剧为例，说明该恐惧早已进入人类想象。",
        "把线索收束到 Irvin Good，指出是他首次把这一恐惧表述为人工智能的“智能爆炸”轨迹，为下段引文铺垫。",
    ],
    "terms": [
        {"en": "intelligence explosion", "zh": "智能爆炸", "def": "Good 所表述的轨迹：机器设计机器、智能自我增强，使人类智能被远远抛在后面。"},
    ],
    "background": [
        {"title": "卡雷尔·恰佩克（Karel Čapek）", "body": "捷克作家；其 1920 年剧作《罗素姆万能机器人》（R.U.R.）首次使用“robot”一词。"},
        {"title": "欧文·古德（I. J. Good）", "body": "英国数学家，曾与图灵共事；1965 年首次把“机器接管世界”表述为“智能爆炸”。"},
        {"title": "塞缪尔·巴特勒（Samuel Butler）", "body": "在 1863 年的文章《机器中的达尔文》中推演机器不断演替、终将取代人类的可能性。"},
    ],
    "vocab": [
        {"en": "take over", "pos": "phr.", "zh": "接管；夺取", "ex": "the robots we created will take over the world"},
        {"en": "capture imagination", "pos": "phr.", "zh": "攫住想象", "ex": "had captured human imagination"},
        {"en": "rise up", "pos": "phr.", "zh": "起义；反抗", "ex": "The robots rise up against humans"},
        {"en": "be provided with", "pos": "phr.", "zh": "被赋予", "ex": "after they have been provided with feelings"},
        {"en": "trajectory", "pos": "n.", "zh": "轨迹", "ex": "a possible trajectory of existing AI"},
    ],
}

ANN["p072"] = {
    "zh": "让我们把一台超智能机器定义为这样一种机器：它能够远远超越任何一个人——无论此人多么聪明——的一切理智活动。既然设计机器也是这些理智活动之一，那么一台超智能机器就能够设计出更好的机器；于是，毫无疑问，将会发生一场“智能爆炸”，而人类的智能将被远远抛在后面。因此，第一台超智能机器就是人类所需要做出的最后一项发明，只要这台机器足够温顺，肯告诉我们如何把它置于控制之下。（Good 1965, 33）。",
    "logic": [
        "界定“超智能机器”：远远超越任何人一切理智活动的机器。",
        "以“设计机器本身是一种理智活动”为关键前提，推出超智能机器可设计更好的机器，从而发生智能爆炸。",
        "得出结论：第一台超智能机器是人类最后的发明，并以“机器足够温顺”为附加条件，埋下失控风险的伏笔。",
    ],
    "terms": [
        {"en": "ultraintelligent machine", "zh": "超智能机器", "def": "Good 文中对“远超任何人类理智活动的机器”的定义，是智能爆炸论证的起点。"},
        {"en": "intelligence explosion", "zh": "智能爆炸", "def": "由超智能机器设计更好机器而引发的智能急剧自我增强过程。"},
    ],
    "background": [],
    "vocab": [
        {"en": "surpass", "pos": "v.", "zh": "超越", "ex": "far surpass all the intellectual activities of any man"},
        {"en": "intellectual activities", "pos": "n.", "zh": "理智活动", "ex": "all the intellectual activities of any man"},
        {"en": "provided that", "pos": "conj.", "zh": "只要；倘若", "ex": "provided that the machine is docile enough"},
        {"en": "docile", "pos": "adj.", "zh": "温顺的；听话的", "ex": "the machine is docile enough to tell us"},
        {"en": "under control", "pos": "phr.", "zh": "处于控制之下", "ex": "how to keep it under control"},
    ],
}

ANN["p073"] = {
    "zh": "从加速到奇点（singularity）的论证由 Ray Kurzweil 系统地加以阐发。他指出，计算能力一直呈指数级增长，即自 1970 年以来依据关于晶体管数量的“摩尔定律”（Moore's Law）大约每 2 年翻一番，而且这种增长在未来一段时间内还将持续。随后他在（Kurzweil 1999; 参较 Kurzweil 2005）中预测：到 2010 年超级计算机将达到人类的计算能力，到 2030 年“心灵上传”（mind uploading）将成为可能，到 2045 年“奇点”将会发生。",
    "logic": [
        "指出“由加速到奇点”的论证由 Kurzweil 系统阐发。",
        "给出经验前提：计算能力按摩尔定律自 1970 年起约每两年翻番，并将持续。",
        "列出 Kurzweil 的三个预测节点（2010 年达人类算力、2030 年心灵上传、2045 年奇点），供后文检验。",
    ],
    "terms": [
        {"en": "Moore's Law", "zh": "摩尔定律", "def": "关于集成电路上晶体管数量约每两年翻一番的经验规律；Kurzweil 以此论证算力指数增长。"},
        {"en": "mind uploading", "zh": "心灵上传", "def": "Kurzweil 预测的把人类心智完整移植到计算载体上的技术。"},
    ],
    "background": [
        {"title": "雷·库兹韦尔（Ray Kurzweil）", "body": "美国发明未来学家，著有《奇点临近》，以指数增长外推论证奇点的到来。"},
    ],
    "vocab": [
        {"en": "spell out", "pos": "phr.", "zh": "系统阐述；讲清楚", "ex": "was spelled out by Ray Kurzweil"},
        {"en": "exponentially", "pos": "adv.", "zh": "指数级地", "ex": "computing power has been increasing exponentially"},
        {"en": "in accordance with", "pos": "phr.", "zh": "依照；根据", "ex": "in accordance with “Moore’s Law”"},
        {"en": "continue", "pos": "v.", "zh": "持续", "ex": "it will continue to do so"},
        {"en": "predict", "pos": "v.", "zh": "预测", "ex": "He then predicted in"},
    ],
}

ANN["p074"] = {
    "zh": "尽管把“智能”等同于处理能力存在明显弱点，Kurzweil 似乎在一点上是对的：人类往往低估指数增长（exponential growth）的力量。小测试：如果你以每一步都是上一步两倍的方式跨步，从一步一米开始，走 30 步你能走多远？（答案：到达地球唯一的天然卫星。）确实，人工智能的多数进步都可轻易归因于更快数量级的处理器、更大的存储以及更高的投入（Müller 2018）。自约 2010 年以来，计算能力的实际发展正比 Kurzweil 预测的还要快地加速，这源于计算价格的大幅下降，再加上投入的大幅增加以及“缩放定律”（scaling laws）方面的相对成功——这已导致众多基准测试（benchmark）被攻破，也改变了人们对何时可能达到人类水平专业能力的估计，例如（Grace et al. 2024 [Other Internet Resources]）之于（Müller and Bostrom 2016）。",
    "logic": [
        "先让步承认“智能等于算力”有明显弱点，再肯定 Kurzweil 的一点洞见：人易低估指数增长。",
        "用“30 步翻倍”小测试直观展示指数增长的惊人后果。",
        "指认人工智能进步主要归因于更快处理器、更大存储与更高投入等算力因素。",
        "更新形势：约 2010 年后算力实际加速快于 Kurzweil 预测，并改变了对达到人类专业能力时点的估计。",
    ],
    "terms": [
        {"en": "exponential growth", "zh": "指数增长", "def": "本段用以说明人为何易低估其长期威力，并以“30 步翻倍”作直观测试。"},
        {"en": "scaling laws", "zh": "缩放定律", "def": "模型规模（参数、数据、算力）与性能之间可预测的经验关系；本段将其视为近年加速的原因之一。"},
        {"en": "benchmark", "zh": "基准测试", "def": "衡量人工智能系统能力的标准化测试；本段指众多基准已被攻破。"},
    ],
    "background": [],
    "vocab": [
        {"en": "identify ... with ...", "pos": "phr.", "zh": "把……等同于……", "ex": "the identification of “intelligence” with processing power"},
        {"en": "underestimate", "pos": "v.", "zh": "低估", "ex": "humans tend to underestimate the power"},
        {"en": "be attributable to", "pos": "phr.", "zh": "可归因于", "ex": "readily attributable to the availability"},
        {"en": "due to", "pos": "phr.", "zh": "由于", "ex": "due to the massive reduction in price"},
        {"en": "massive", "pos": "adj.", "zh": "大规模的；大幅的", "ex": "the massive reduction in price for computation"},
        {"en": "estimate", "pos": "n.", "zh": "估计；预测", "ex": "changed estimates of when human-level"},
    ],
}

ANN["p075"] = {
    "zh": "如今更常被使用的这一论证版本（Chalmers 2010）谈论的是人工智能系统“智能”提升到“超级智能”（superintelligence）水平。（Bostrom 2014）较为详细地解释了在那一时刻会发生什么、人类将面临哪些风险。相关讨论被综述于（Eden et al. 2012; Armstrong 2014; Shanahan 2015）。通往超级智能的可能路径不止算力增长这一条，例如在计算机或机器人上完整仿真人脑（Kurzweil 2012; Sandberg 2013）、生物学路径，或经由网络与组织（Bostrom 2014, 22–51）。",
    "logic": [
        "指出当前更流行的论证版本（Chalmers 2010）把焦点表述为人工智能智能提升至超级智能水平。",
        "以 Bostrom（2014）为代表，说明该传统详细刻画超级智能来临之时的情形与对人类的风险，并给出综述文献。",
        "拓宽思路：通向超级智能的路径不限于算力增长，还包括全脑仿真、生物学路径以及网络与组织路径。",
    ],
    "terms": [
        {"en": "superintelligence", "zh": "超级智能", "def": "本段指人工智能系统智能提升所达到的水平；Bostrom（2014）详论其来临后情形与人类风险。"},
        {"en": "whole brain emulation", "zh": "全脑仿真", "def": "本段所列通向超级智能的路径之一：在计算机或机器人上完整仿真人脑。"},
    ],
    "background": [],
    "vocab": [
        {"en": "version", "pos": "n.", "zh": "版本", "ex": "The version of this argument that is now used"},
        {"en": "in some detail", "pos": "phr.", "zh": "较为详细地", "ex": "explains in some detail what would happen"},
        {"en": "summarise", "pos": "v.", "zh": "综述；总结", "ex": "The discussion is summarised in"},
        {"en": "path to", "pos": "n.", "zh": "通往……的路径", "ex": "possible paths to superintelligence"},
        {"en": "emulation", "pos": "n.", "zh": "仿真", "ex": "complete emulation of the human brain"},
    ],
}

# ---------------- 2.8.2 Existential Risk ----------------
ANN["p076"] = {
    "zh": "一旦达到人工超级智能的阶段，它们似乎很可能拥有与人类在地球上的存在相冲突的偏好，并因而决定终结这一存在——而鉴于其优越的智能，它们将有能力这样做（或者，它们也可能只是因为并不真正在乎而恰好终结了人类的存在）：这就是人类这一物种灭绝的风险（XRisk），或至少是某种其他“灾难性风险”（catastrophic risk）。这第二步的具体细节尚有争议，但它们似乎涉及正交性（orthogonality）以及“技术发展已接近通用人工智能（AGI）”这一看法。",
    "logic": [
        "刻画存在性风险的核心机制：超级智能的偏好可能与人类存在相冲突，而其优越智能使其有能力付诸实施。",
        "区分两种动因：主动决定终结人类，或因不在乎而顺带导致人类灭绝。",
        "指出第二步的细节虽有争议，但公认依赖两个前提：正交性论题与“技术发展已接近通用人工智能”的看法。",
    ],
    "terms": [
        {"en": "existential risk (x-risk)", "zh": "存在性风险", "def": "此处具体化为人类物种灭绝的风险，或至少其他灾难性风险。"},
        {"en": "orthogonality", "zh": "正交性", "def": "本段指出存在性风险第二步所依赖的核心前提之一（详见后文 Bostrom 的表述）。"},
        {"en": "catastrophic risk", "zh": "灾难性风险", "def": "比存在性风险稍宽的一类，指危及人类重大但未必灭绝的风险。"},
    ],
    "background": [],
    "vocab": [
        {"en": "conflict with", "pos": "phr.", "zh": "与……相冲突", "ex": "preferences that conflict with the existence of humans"},
        {"en": "superior intelligence", "pos": "n.", "zh": "优越的智能", "ex": "given their superior intelligence"},
        {"en": "end existence", "pos": "phr.", "zh": "终结存在", "ex": "may decide to end that existence"},
        {"en": "disputed", "pos": "adj.", "zh": "有争议的", "ex": "The details of this 2nd step are disputed"},
        {"en": "be close to", "pos": "phr.", "zh": "接近", "ex": "technical development is close to AGI"},
    ],
}

ANN["p077"] = {
    "zh": "一个问题是，超级智能系统可能拥有何种目标与价值。支持存在性风险的经典论证认为，即便是一个目标相对无害的程序——如“在地球上最大化回形针数量”（Bostrom 2003b），或“优化国际象棋表现”（Omohundro 2014）——也会转向存在性风险，因为它们会意识到，要最好地实现自身目标，就必须同时达成某些子目标，例如获取资源。这一观念被称为“工具性趋同”（instrumental convergence）（Bales, D'Alessandro, and Kirk-Giannini 2024, 4; Gallow 2024）。",
    "logic": [
        "提出关键问题：超级智能系统可能拥有什么样的目标与价值。",
        "用“最大化回形针”“优化国际象棋”两个看似无害的思想实验说明：即便目标无害也可能导向存在性风险。",
        "给出机制解释——系统为达成主目标而追求获取资源等子目标——并定名该现象为“工具性趋同”。",
    ],
    "terms": [
        {"en": "paperclip maximizer", "zh": "回形针最大化者", "def": "Bostrom 的著名思想实验：一个目标仅为最大化回形针产量的系统，因工具性趋同而耗竭资源、危及人类。"},
        {"en": "instrumental convergence", "zh": "工具性趋同", "def": "指无论最终目标为何，智能体都会趋同地追求某些工具性子目标（如获取资源、自保）。"},
    ],
    "background": [
        {"title": "回形针最大化者（Paperclip Maximizer）", "body": "波斯特洛姆提出的著名思想实验，用以演示一个目标看似无害的超级系统如何因工具性趋同而带来灭绝风险。"},
    ],
    "vocab": [
        {"en": "benign", "pos": "adj.", "zh": "无害的；良性的", "ex": "even a programme with relatively benign goals"},
        {"en": "maximise", "pos": "v.", "zh": "最大化", "ex": "maximise paperclips on earth"},
        {"en": "turn towards", "pos": "phr.", "zh": "转向", "ex": "would turn towards XRisk"},
        {"en": "sub-goal", "pos": "n.", "zh": "子目标", "ex": "certain sub-goals, e.g. to acquire resources"},
        {"en": "acquire", "pos": "v.", "zh": "获取；取得", "ex": "to acquire resources"},
    ],
}

ANN["p078"] = {
    "zh": "这一切只有在如下假设下才成立，即超级智能并不蕴含仁慈——这与伦理学中康德主义（Kantian）的传统相反；后者论证说，理性或智能的更高水平会伴随对何为道德的更好理解，以及按道德而行的更强能力（Gewirth 1978; Chalmers 2010, 36f）。波斯特洛姆（Bostrom）把这一想法表述如下：",
    "logic": [
        "指出现存性风险论证依赖一个关键假设：超级智能并不蕴含仁慈。",
        "摆出对立的康德主义传统——理性或智能越高，越能理解并践行道德。",
        "引出 Bostrom 对该假设的正式表述，为下段正交性论题作铺垫。",
    ],
    "terms": [
        {"en": "benevolence", "zh": "仁慈；善意", "def": "存在性风险论证所否认的、与高智能相伴的道德善意；本段指出其对立于康德主义传统。"},
        {"en": "Kantian", "zh": "康德主义（者）（的）", "def": "本段指伦理学中认为理性程度与道德理解、道德行动能力正相关的传统。"},
    ],
    "background": [],
    "vocab": [
        {"en": "imply", "pos": "v.", "zh": "蕴含；意味着", "ex": "superintelligence does not imply benevolence"},
        {"en": "contrary to", "pos": "phr.", "zh": "与……相反", "ex": "contrary to Kantian traditions in ethics"},
        {"en": "go along with", "pos": "phr.", "zh": "伴随；与……相伴", "ex": "would go along with a better understanding"},
        {"en": "express", "pos": "v.", "zh": "表述；表达", "ex": "Bostrom expresses this thought as follows"},
    ],
}

ANN["p079"] = {
    "zh": "“正交性论题（The Orthogonality Thesis）：智能与最终目标（final goals）是两条正交的轴线，可能的能动者可以沿着它们自由变化。换言之，原则上几乎任何水平的智能都可以与几乎任何最终目标相结合。”（Bostrom 2012, 73; 参较 Bostrom 2014, 105–109）",
    "logic": [
        "给出 Bostrom 对正交性论题的正式表述：智能与最终目标是两条正交轴线。",
        "以重述句阐明其含义：任何智能水平原则上可与任何最终目标相组合。",
        "这一论题切断“高智能等于高道德”的联系，为存在性风险的第二步提供形而上学前提。",
    ],
    "terms": [
        {"en": "Orthogonality Thesis", "zh": "正交性论题", "def": "Bostrom 的主张：智能水平与最终目标相互独立、可自由组合，故高智能系统未必具有良善目标。"},
        {"en": "final goals", "zh": "最终目标", "def": "正交性中与智能并列的另一轴；指能动者所追求的终极目的而非工具性目的。"},
    ],
    "background": [],
    "vocab": [
        {"en": "orthogonal", "pos": "adj.", "zh": "正交的", "ex": "Intelligence and final goals are orthogonal axes"},
        {"en": "axes", "pos": "n.", "zh": "轴（复数）", "ex": "orthogonal axes along which possible agents"},
        {"en": "vary", "pos": "v.", "zh": "变化", "ex": "can freely vary"},
        {"en": "in principle", "pos": "phr.", "zh": "原则上", "ex": "could in principle be combined with"},
    ],
}

ANN["p080"] = {
    "zh": "一些作者（Müller and Cannon 2022）论证说，正交性加上工具性趋同（instrumental convergence），以一种不融贯的方式同时预设了两种智能概念——一种带有道德认知，一种不带（参较 Greene 2015）；而另一些作者则支持正交性（Dung 2024）。",
    "logic": [
        "引入对存在性风险核心前提组合的内在批评：正交性与工具性趋同合用是否融贯。",
        "给出批评要点：二者似同时要求“有道德认知的智能”与“无道德认知的智能”两种智能概念。",
        "摆出对立立场：仍有作者支持正交性，表明该前提尚存争议。",
    ],
    "terms": [
        {"en": "moral cognition", "zh": "道德认知", "def": "本段指出，若既主张智能可与任何目标组合、又要求工具性趋同，便会在“有无道德认知的智能”之间产生不融贯。"},
    ],
    "background": [],
    "vocab": [
        {"en": "argue", "pos": "v.", "zh": "论证", "ex": "Some authors have argued that orthogonality"},
        {"en": "plus", "pos": "prep.", "zh": "加上", "ex": "orthogonality plus instrumental convergence"},
        {"en": "incoherently", "pos": "adv.", "zh": "不融贯地", "ex": "incoherently imply two notions of intelligence"},
        {"en": "notion", "pos": "n.", "zh": "概念；观念", "ex": "two notions of intelligence"},
        {"en": "support", "pos": "v.", "zh": "支持", "ex": "others have supported orthogonality"},
    ],
}

ANN["p081"] = {
    "zh": "长期思考是这一文献的关键特征。奇点（singularity）（或另一场灾难性事件）是在 3 年后、30 年后还是 3000 年后发生，并不真正重要（Baum et al. 2019）。这些问题有时被更宽泛地理解为关乎人类这一物种面临的任何“灾难性风险”（catastrophic risk）（Rees 2018）——而人工智能只是其中之一（Häggström 2016; Ord 2020）。对存在性风险及来自人工智能的其他灾难性风险的评估，还取决于超级智能以何种方式出现的细节——是突然地还是渐进地（Kasirzadeh 2025）。当存在性风险文献聚焦于思辨性的毁灭情景时，Cappelen 等人（Cappelen, Goldstein, and Hawthorne forthcoming）则论证说，那些摈斥这些前景的人，其实也在推进同样思辨的“幸存故事”。",
    "logic": [
        "点明该文献的方法论特征：长期思考，故时间尺度（3 年、30 年或 3000 年）不影响其重要性。",
        "把存在性风险置于更宽的“物种灾难性风险”框架，指出人工智能只是其中一种。",
        "指出风险评估还取决于超级智能出现方式的细节（突变还是渐进）。",
        "引入方法论对称观察：摈斥灾难情景者自身也依赖同样思辨的“幸存故事”。",
    ],
    "terms": [
        {"en": "catastrophic risk", "zh": "灾难性风险", "def": "比存在性风险更宽的概念，指可能危及人类这一物种的重大风险；人工智能只是其中之一。"},
    ],
    "background": [],
    "vocab": [
        {"en": "crucial", "pos": "adj.", "zh": "关键的", "ex": "the crucial feature of this literature"},
        {"en": "matter", "pos": "v.", "zh": "要紧；重要", "ex": "does not really matter"},
        {"en": "broadly", "pos": "adv.", "zh": "宽泛地；广义地", "ex": "taken more broadly as concerning"},
        {"en": "abruptly", "pos": "adv.", "zh": "突然地", "ex": "abruptly or incrementally"},
        {"en": "dismiss", "pos": "v.", "zh": "摈斥；不予考虑", "ex": "those who dismiss these prospects"},
        {"en": "speculative", "pos": "adj.", "zh": "思辨的；推测性的", "ex": "speculative destruction scenarios"},
    ],
}

ANN["p082"] = {
    "zh": "已有若干论文集考察了通用人工智能（AGI）的风险，以及可能使这一发展或多或少富于风险的诸因素（Müller 2016b; Callaghan et al. 2017; Yampolskiy 2018）。在存在性风险一方，如今阵线似乎已经固化（Bostrom and Yudkovski 2014; Yampolskiy 2022; Yudkovski and Soares 2025），而在风险的一般性考察一方（Bengio et al. 2024; Gyevnár and Kasirzadeh 2025）或“工具性趋同”一方，则仍有较多变动。",
    "logic": [
        "概述已有论文集对通用人工智能风险及风险高低相关因素的系统考察。",
        "刻画当前论争格局：存在性风险一派阵线趋于固化。",
        "对照指出一般性风险考察与工具性趋同一线仍较活跃、有变动。",
    ],
    "terms": [
        {"en": "artificial general intelligence (AGI)", "zh": "通用人工智能（AGI）", "def": "在宽泛意义上具备人类通用认知能力的人工智能；本段论文集围绕其风险展开。"},
        {"en": "instrumental convergence", "zh": "工具性趋同", "def": "本段指出围绕它的讨论仍较活跃，与已固化的存在性风险阵线形成对照。"},
    ],
    "background": [],
    "vocab": [
        {"en": "collection of papers", "pos": "n.", "zh": "论文集", "ex": "Several collections of papers have investigated"},
        {"en": "risk-laden", "pos": "adj.", "zh": "富于风险的", "ex": "more or less risk-laden"},
        {"en": "battle lines", "pos": "n.", "zh": "阵线", "ex": "The battle lines on the XRisk side"},
        {"en": "hardened", "pos": "adj.", "zh": "固化的；变硬的", "ex": "now seem hardened"},
        {"en": "movement", "pos": "n.", "zh": "变动；动向", "ex": "there is more movement"},
    ],
}

ANN["p083"] = {
    "zh": "一旦论证出从人工智能通向存在性风险的诸步骤，问题就来了：如果可能，应如何避免这样的后果。这通常被称为“控制问题”（control problem）：人类如何才能控制一个超级智能的人工智能系统（Bostrom 2014, 127ff）？既然仅仅由人类来实际控制一个已部署的超级智能系统似乎非常困难（即便对于一个神谕型系统也是如此），讨论便主要集中于如何确保系统的价值在设计阶段就与人类价值“对齐”（aligned）——本着机器伦理的精神——从而只要这些价值保持稳定，该系统就无需进一步控制。这引出了许多技术问题，也引出了更多哲学问题，例如价值是什么（Zhi-Xuan et al. 2024）、对齐是什么、应当选择哪些价值（Gabriel 2020），以及如何识别人类价值（S. Russell 2019）。关于错配（mis-alignment）的讨论与关于人工智能滥用的讨论相关联，并且有人论证说二者都可能产生存在性风险（Hellrigel-Holderbaum and Dung forthcoming）。",
    "logic": [
        "在存在性风险论证成立的前提下，提出应对问题：如何避免此类后果，即“控制问题”。",
        "说明为何部署后的实际控制不可行，从而把方案转向设计阶段的价值对齐。",
        "列举该方案引出的技术与哲学难题（价值是什么、对齐是什么、选哪些价值、如何识别人类价值）。",
        "指出错配问题与人工智能滥用问题相关，二者皆可产生存在性风险。",
    ],
    "terms": [
        {"en": "control problem", "zh": "控制问题", "def": "即如何控制一个超级智能人工智能系统、避免其负面后果的问题。"},
        {"en": "value alignment / alignment problem", "zh": "价值对齐／对齐问题", "def": "本段指在设计阶段使系统价值与人类价值一致，从而免予事后控制。"},
        {"en": "mis-alignment", "zh": "错配；不对齐", "def": "系统价值与人类价值不一致的状态；本段指出它与人工智能滥用讨论相关。"},
    ],
    "background": [],
    "vocab": [
        {"en": "arise", "pos": "v.", "zh": "出现；产生", "ex": "the question arises how such consequences could"},
        {"en": "deployed", "pos": "adj.", "zh": "已部署的", "ex": "actual control of a deployed superintelligent system"},
        {"en": "oracle-type", "pos": "adj.", "zh": "神谕型的", "ex": "even for an oracle-type system"},
        {"en": "make sure", "pos": "phr.", "zh": "确保", "ex": "how to make sure the values of the system"},
        {"en": "remain stable", "pos": "phr.", "zh": "保持稳定", "ex": "if these remain stable"},
        {"en": "recognise", "pos": "v.", "zh": "识别；认出", "ex": "how to recognise human values"},
    ],
}

ANN["p084"] = {
    "zh": "关于存在性风险的讨论往往与一种版本的“狂热主义”（fanaticism）相绑定，即如下观点：长期而言极大的效用，即便概率很低，也会压倒中等大小但确定可预见的效用。这引发了近来关于狂热主义可接受性的一些讨论（Wilkinson 2022; J. S. Russell 2024; Bottomley and Williamson 2025）。看来，无论错在过于冒险一边，还是错在过于谨慎一边，都要付出代价（Müller 2026）。",
    "logic": [
        "指出存在性风险讨论常与“狂热主义”立场绑定：低概率但极大的长期效用压倒中等但确定可预见的效用。",
        "概述学界近来对狂热主义可接受性的讨论。",
        "以对称代价作结：过于冒险与过于谨慎两头都会出错并付出代价。",
    ],
    "terms": [
        {"en": "fanaticism", "zh": "狂热主义", "def": "本段指那种认为低概率但极大的长期效用应压倒中等且确定的效用的立场。"},
    ],
    "background": [],
    "vocab": [
        {"en": "be wedded to", "pos": "phr.", "zh": "与……绑定", "ex": "is often wedded to a version “fanaticism”"},
        {"en": "utility", "pos": "n.", "zh": "效用", "ex": "a very large utility in the long run"},
        {"en": "overrule", "pos": "v.", "zh": "压倒；推翻", "ex": "will overrule medium-size but securely foreseeable"},
        {"en": "err on the ... side", "pos": "phr.", "zh": "错在……一边", "ex": "erring on the too-risky and"},
        {"en": "cost", "pos": "n.", "zh": "代价", "ex": "there is cost both in erring"},
    ],
}

ANN["p085"] = {
    "zh": "这场论争的许多参与者共享着这样一个文化氛围：技术将迅速发展，并带来广泛而彻底的变化，其中包括“超人类主义”（transhuman）关于人类以另一种物质形式存续的看法，例如被上传到计算机上（Moravec 1998; Bostrom 2003a; More and Vita-More 2013）。他们还考察“人类增强”（human enhancement）的前景——在包括智能在内的多个方面（Erler and Müller 2024）。一些关于超级智能的讨论带有宗教色彩，例如对全知存在者的玄想、“末世”的彻底变化，以及通过超越我们当前的身体形式而获得永生的许诺（Capurro 1993; Geraci 2008, 2010; O'Connell 2017, 160ff; Gertz 2018）。",
    "logic": [
        "描绘参与论者的共享文化背景：技术快速发展将带来彻底变化。",
        "指出其中包含“超人类主义”式的存续观——以另一种物质形式（如上传到计算机）存续。",
        "补充其对“人类增强”（含智能增强）前景的关注。",
        "批评性地指出部分超级智能讨论带有宗教色彩（全知者、末世变化、超越肉体的永生许诺）。",
    ],
    "terms": [
        {"en": "transhumanism", "zh": "超人类主义", "def": "本段指主张人类可借技术以另一种物质形式存续（如上传到计算机）的立场。"},
        {"en": "human enhancement", "zh": "人类增强", "def": "指在智能等方面通过技术提升人类能力的前景。"},
    ],
    "background": [],
    "vocab": [
        {"en": "share a cultural sphere", "pos": "phr.", "zh": "共享文化氛围", "ex": "share a cultural sphere where technology will develop rapidly"},
        {"en": "radical", "pos": "adj.", "zh": "彻底的；激进的", "ex": "bring broadly radical changes"},
        {"en": "upload", "pos": "v.", "zh": "上传", "ex": "e.g. uploaded on a computer"},
        {"en": "undertone", "pos": "n.", "zh": "意味；色彩", "ex": "have religious undertones"},
        {"en": "immortality", "pos": "n.", "zh": "永生", "ex": "the promise of immortality"},
        {"en": "transcendence", "pos": "n.", "zh": "超越", "ex": "through transcendence of our current bodily form"},
    ],
}

ANN["p086"] = {
    "zh": "然而，这一讨论已进入主流，“避免来自 AGI 的存在性风险”已成为各大人工智能公司的常见主题，因为人工智能正在大规模地推进（Aguirre 2025）；而一些较早的论著则试图叫停关于奇点（singularity）“神话”的讨论（Floridi 2016; Ganascia 2017）。存在性风险的叙事提高了公众对哲学的意识，并在该领域内部引发了大量讨论，例如：奇点是否是当前人工智能的一种轨迹（Floridi 2023a; Müller 2025b; Thorstad 2025），它在概念上或实践上是否可能，以及其前提与核心术语——如效用、目标、能动作用、道德规则（D'Alessandro 2025）和风险——各自扮演什么角色。",
    "logic": [
        "指出讨论已进入主流，“避免来自通用人工智能的存在性风险”成为头部人工智能公司的常见主题。",
        "同时点出早期即有论著把奇点斥为“神话”、试图叫停讨论。",
        "总结存在性风险叙事的双重影响：提升公众对哲学的意识，并在领域内部催生大量关于前提与核心概念的讨论。",
    ],
    "terms": [
        {"en": "singularity", "zh": "奇点", "def": "本段回顾论争：有人视之为当前人工智能的轨迹，亦有人视之为“神话”，其可能性与前提仍受审查。"},
    ],
    "background": [],
    "vocab": [
        {"en": "move to the mainstream", "pos": "phr.", "zh": "进入主流", "ex": "the discussion has moved to the mainstream"},
        {"en": "advance", "pos": "v.", "zh": "推进；进展", "ex": "AI is advancing massively"},
        {"en": "myth", "pos": "n.", "zh": "神话", "ex": "the “myth” of singularity"},
        {"en": "raise awareness", "pos": "phr.", "zh": "提高意识", "ex": "raised public awareness of philosophy"},
        {"en": "trajectory", "pos": "n.", "zh": "轨迹", "ex": "a trajectory of current AI"},
        {"en": "central terms", "pos": "n.", "zh": "核心术语", "ex": "its assumptions and central terms"},
    ],
}

ANN["p087"] = {
    "zh": "即便是那些认为论证形势不应以奇点和存在性风险来分析、或认为有充分理由拒斥存在性风险论证的哲学家，也应当承认他们有可能是错的。因此，即便一个人认为来自人工智能的存在性风险概率非常低，这场讨论也可以是有正当理由的、富有成果的。",
    "logic": [
        "对怀疑派提出认识论上的让步要求：即便不认可存在性风险论证，也应承认自己可能错。",
        "由此论证该讨论的正当性与成果性不取决于风险概率高低。",
        "以低概率假设收束全节：讨论仍值得进行。",
    ],
    "terms": [
        {"en": "existential risk (x-risk)", "zh": "存在性风险", "def": "本段从认识论角度主张：即使概率很低，讨论来自人工智能的存在性风险仍正当且富有成果。"},
    ],
    "background": [],
    "vocab": [
        {"en": "argumentative situation", "pos": "n.", "zh": "论证形势", "ex": "the argumentative situation is not to be analysed"},
        {"en": "compelling reasons", "pos": "n.", "zh": "充分的理由", "ex": "compelling reasons to reject the arguments"},
        {"en": "acknowledge", "pos": "v.", "zh": "承认", "ex": "should acknowledge that they might be wrong"},
        {"en": "justified", "pos": "adj.", "zh": "有正当理由的", "ex": "the discussion can be justified and fruitful"},
        {"en": "fruitful", "pos": "adj.", "zh": "富有成果的", "ex": "justified and fruitful"},
    ],
}

# ---------------- assemble ----------------
blocks_out = []
for b in src["blocks"]:
    if b["kind"] == "heading":
        o = dict(b)  # copy every source field verbatim
        o["title_zh"] = HEADINGS[b["id"]]
    else:
        a = ANN[b["pid"]]
        o = {
            "kind": b["kind"],
            "pid": b["pid"],
            "text_en": b["text_en"],
            "html_en": b["html_en"],
            "zh": a["zh"],
            "logic": a["logic"],
            "terms": a["terms"],
            "background": a["background"],
            "vocab": a["vocab"],
        }
    blocks_out.append(o)

out = {"shard": "c", "blocks": blocks_out}
(ROOT / "content").mkdir(exist_ok=True)
outp = ROOT / "content" / "shard-c.json"
outp.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", outp, "blocks:", len(blocks_out))
