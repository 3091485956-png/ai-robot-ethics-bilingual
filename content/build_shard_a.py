# -*- coding: utf-8 -*-
"""Build content/shard-a.json from source + hand-written Chinese annotations.
Loads shard-a.source.json, copies every source field verbatim, adds Chinese fields.
"""
import json, os
from pathlib import Path

ROOT = Path(r"C:\Users\loong\Desktop\人工智能与机器人伦理学")
SRC = ROOT / "content-source" / "shard-a.source.json"
OUT = ROOT / "content" / "shard-a.json"

# ---------------------------------------------------------------- headings
HEADINGS = {
    "Int": "导论",
    "ScoEthAIRob": "范围：人工智能与机器人伦理学",
    "TecSocBac": "技术—社会背景",
    "MaiDeb": "主要论争",
    "PriDatPro": "隐私与数据保护",
    "sec-2-1-1": "数字领域",
    "sec-2-1-2": "失去对数据的控制？",
    "HumAutMan": "人的自主性与操纵",
}

# ---------------------------------------------------------------- paragraphs
A = {}

A["p001"] = {
"zh": "经过约70年的发展，如今已经清楚：人工智能（AI）与机器人技术**确实**对世界产生了重大影响，尽管这一影响的确切性质与深度仍不明确。人工智能与机器人技术**应当**产生何种影响，也在很大程度上仍是一个未解的问题，而这正是本文的核心问题。此外，人工智能与机器人技术还为我们提供了契机，去**在理论上**反思一些根本性的哲学与伦理问题。当前看起来具有实践影响或理论相关性的主要论争，涉及隐私、人的自主性、自动化决策、人—机互动、就业以及对整个社会的影响——此外还有自主性、能动性与超级智能等更为抽象的概念。对于上述每一个问题，本文都将概述已有的**立场**与**论证**，以及它们如何与其他问题相互关联。总体而言，人工智能与机器人伦理学的主要作用，应当是使我们能够理解并评估技术—社会发展，从而既能决定哪些发展应当避免，也能为一个配有人工智能与机器人技术、值得欲求的世界勾勒出一幅积极的愿景。",
"logic": [
 "开篇立论：指出AI与机器人技术已对世界产生重大现实影响，但其“应当”产生何种影响这一规范性问题远未解决，据此点明本文主旨。",
 "说明AI与机器人技术同时带来两类议题：具有实践影响的具体社会议题（隐私、自主性、就业等）与更为抽象的理论议题（自主性、能动性、超级智能）。",
 "交代本文的写作方法与目标：概述各议题已有立场与论证及其相互关联，最终服务于理解、评估技术—社会发展并塑造值得欲求的未来愿景。",
],
"terms": [
 {"en":"ethics of AI and robotics","zh":"人工智能与机器人伦理学","def":"对人工智能与机器人技术所引发的伦理问题作系统哲学研究的学科；本文认为其主旨在于理解、评估技术—社会发展并提出值得欲求的未来愿景。"},
 {"en":"agency","zh":"能动性","def":"行为主体发起行动、施加影响的能力；本文将其与超级智能等并列为比具体社会议题更抽象的哲学概念。"},
 {"en":"superintelligence","zh":"超级智能","def":"在几乎一切具有认知重要性的领域都远超人类的智能；本文将其列为较为抽象的核心议题之一。"},
],
"background": [],
"vocab": [
 {"en":"substantial","pos":"adj.","zh":"重大的；实质性的","ex":"do have substantial impact on the world"},
 {"en":"give occasion to","pos":"phr.","zh":"为……提供契机","ex":"have also given us occasion to reflect"},
 {"en":"hang together","pos":"phr.","zh":"相互关联；前后一贯","ex":"how these hang together with other issues"},
 {"en":"worth wanting","pos":"phr.","zh":"值得欲求的","ex":"a world with AI and robotics that is worth wanting"},
 {"en":"unsolved","pos":"adj.","zh":"未解决的","ex":"remains a largely unsolved question"},
],
}

A["p002"] = {
"zh": "人工智能与机器人技术的设计与使用引发了许多伦理问题，其中有些是这些技术所特有的，有些则更为一般。这些问题常常可以追溯到各种各样的“担忧”——而担忧是对新技术的典型反应。许多此类担忧事后看来颇为古怪（例如火车太快，灵魂跟不上），另一些则可被预料地是错误的，它们声称技术将从根本上改变人（电话将摧毁人际交往，文字将摧毁记忆）；还有一些大体正确但相关性有限（数字技术将摧毁诸多产业）；也有一些大体正确且意义深远（汽车将改变城镇，智能手机将造成依赖）。像本文这样一篇文章的任务，就是说明哲学研究在分析这些问题方面做了什么，把模糊的恐惧转化为被充分理解的问题，并消解那些并非真正问题的“伪问题”——同时在判断哪些才是真正重要的问题时保持审慎。",
"logic": [
 "指出AI与机器人技术引发的伦理问题常源于对新技术的“担忧”，并把历史上对新技术的担忧分为四类（古怪的、可预料地错误的、大体正确但相关有限的、大体正确且意义深远的），为后文甄别真问题提供类比标准。",
 "据此界定本文的任务：借助哲学研究把模糊恐惧厘清为可被充分理解的问题，消解伪问题。",
 "同时强调在判断“何为真正重要的问题”这一点上须保持审慎。",
],
"terms": [
 {"en":"ethics of AI and robotics","zh":"人工智能与机器人伦理学","def":"本文认为该学科的基本工作，是把对新技术的模糊担忧转化为可被哲学分析的清晰问题，并消解伪问题。"},
],
"background": [],
"vocab": [
 {"en":"raise","pos":"v.","zh":"引发；提出","ex":"have raised many ethical issues"},
 {"en":"go back to","pos":"phr.","zh":"追溯到","ex":"These often go back to “concerns”"},
 {"en":"turn out","pos":"phr.","zh":"事后证明；结果是","ex":"Many such concerns turn out to be rather quaint"},
 {"en":"deflate","pos":"v.","zh":"消解；使缩小","ex":"to deflate the non-issues"},
 {"en":"well-understood","pos":"adj.","zh":"被充分理解的","ex":"move from vague fears to well-understood problems"},
 {"en":"quaint","pos":"adj.","zh":"古怪的；离奇有趣的","ex":"turn out to be rather quaint"},
],
}

A["p003"] = {
"zh": "人工智能与机器人伦理学尤其困难，因为它既需要对规范伦理学与元伦理学的理解，又需要对相关技术的理解，还需要在诸多社会影响领域具备专门知识。关于AI伦理的讨论不仅出现在哲学与计算机科学内部，也出现在其他学术学科之中，尤其是政治学、经济学、媒介研究、教育学、环境研究与法学——以及学术界之外广大的社会领域。这似乎表明，我们需要更好地理解哪些问题应当由哲学来处理，并与其他学科形成更好的分工。在哲学内部，为关于AI与机器人技术的论争作出贡献的领域，已从心灵哲学与规范伦理学扩展到元伦理学、科学哲学、认识论、语言哲学与政治哲学。我们这一话题促使我们停下来反思：哲学路径与非哲学路径在AI伦理中的关系，以及哲学本身的一些基本概念——后一项活动有时被称为“AI哲学”（Müller 2025b; Müller and Löhr forthcoming）。",
"logic": [
 "指出本学科之所以特别困难，在于它同时要求规范伦理学与元伦理学素养、对技术的理解，以及在社会影响诸多领域的专门知识。",
 "描述AI伦理讨论已蔓延至众多学科与社会领域，据此提出需厘清哲学应处理哪些问题、并与其他学科合理分工。",
 "综述哲学内部参与AI论争的子领域之扩展，并引出“AI哲学”这一以哲学自身基本概念为反思对象的活动。",
],
"terms": [
 {"en":"normative ethics","zh":"规范伦理学","def":"研究“应当如何行动”之对错标准与原则的伦理学分支；本文将其与元伦理学并列为AI伦理所需的伦理学训练。"},
 {"en":"metaethics","zh":"元伦理学","def":"研究伦理判断的性质、意义与证成方式的伦理学分支，不直接提出具体行为规范。"},
 {"en":"epistemology","zh":"认识论","def":"关于知识与信念之证成的哲学分支；本文将其列为参与AI与机器人论争的哲学领域之一。"},
 {"en":"AI philosophy","zh":"AI哲学","def":"本文作者用法：以AI为契机反思哲学自身基本概念与方法的哲学活动。"},
],
"background": [],
"vocab": [
 {"en":"expertise","pos":"n.","zh":"专门知识；专长","ex":"plus expertise in the many areas of social impact"},
 {"en":"division of labour","pos":"n.","zh":"分工","ex":"a better division of labour with other disciplines"},
 {"en":"contribute to","pos":"phr.","zh":"为……作贡献","ex":"the fields that have contributed to the debates"},
 {"en":"give pause to","pos":"phr.","zh":"使停下来反思","ex":"gives us pause to reflect"},
 {"en":"widen","pos":"v.","zh":"拓宽；扩展","ex":"have widened from philosophy of mind"},
],
}

A["p004"] = {
"zh": "人工智能不知为何比其他技术更“贴近我们的皮肤”：这与如下事实有关——人工智能这项事业的目标，是创造出具备某些特征的机器，而这些特征对于我们人类如何看待自身（即把自己视为能感受、能思考、有智能的存在者）至关重要。“人工智能能动性”的经典概念包含一个“感知—建模—规划—行动”（sense-model-plan-act）的序列，但当前的AI应用还包括感知、文本分析、自然语言处理（NLP）、逻辑推理、博弈对弈、决策（支持）系统、数据分析、预测分析，以及自动驾驶汽车、人形机器人和其他形式的机器人技术（P. Stone et al. 2021）。在后文中将会清楚：把AI设想为决策机器、也许是理性选择的实现，往往是有用的（参 S. Russell 2019, 23; S. Russell and Norvig 2020, 57）。",
"logic": [
 "解释AI为何比其他技术更切近人类：其工程目标是复现人类自我理解中居于核心的感受、思考与智能特征。",
 "从经典“人工智能能动性”的“感知—建模—规划—行动”序列出发，扩展列举当代AI应用的完整谱系。",
 "提出一个将贯穿后文的有用视角：把AI理解为决策机器，乃至理性选择的实现。",
],
"terms": [
 {"en":"artificial intelligent agency","zh":"人工智能能动性","def":"经典AI概念，指具备“感知—建模—规划—行动”能力序列的人造能动作用。"},
 {"en":"humanoid robot","zh":"人形机器人","def":"具有人类外形的机器人；本文将其列为当代AI应用之一。"},
 {"en":"autonomous vehicle (AV)","zh":"自动驾驶汽车","def":"可自主行驶的车辆；本文将其列为当代AI应用之一。"},
 {"en":"rational choice","zh":"理性选择","def":"以效用最大化等方式刻画行动选择的理论框架；本文建议据此把AI理解为决策机器。"},
],
"background": [],
"vocab": [
 {"en":"get close to","pos":"phr.","zh":"贴近；接近","ex":"AI somehow gets closer to our skin"},
 {"en":"have to do with","pos":"phr.","zh":"与……有关","ex":"This has to do with the fact that"},
 {"en":"sequence","pos":"n.","zh":"序列；顺序","ex":"involves a sequence of sense-model-plan-act"},
 {"en":"implementation","pos":"n.","zh":"实现；实现物","ex":"implementations of rational choice"},
 {"en":"cf.","pos":"phr.","zh":"参；参见（confer）","ex":"cf. S. Russell 2019, 23"},
],
}

A["p005"] = {
"zh": "本文讨论哪些问题、又以何种顺序排列？由于SEP是一部哲学百科全书，本文按**伦理**问题来组织，而其他综述则聚焦于政策与合规（Corrêa et al. 2023），或聚焦于某些技术的**安全**。因此，人们可以把AI伦理的版图设想为一张“伦理问题 × 技术”的矩阵。对AI伦理而言，什么算“重要问题”，往往与人们所处的语境有关：隐私保护对于个人自主性至关重要，而种族歧视或经济不公在某些社会中更为突出，对女性的歧视亦然；环境破坏与超级智能，也许对生活在富裕且和平社会中的人们显得更为核心。本文则力求一种相当宽广的理解，其依据既包括 a) 社会相关性，也包括 b) 理论兴趣。",
"logic": [
 "以设问自答说明本文编排原则：与按政策合规或技术安全组织的综述不同，本文按伦理问题组织，并把AI伦理版图设想为“问题×技术”矩阵。",
 "指出何为“重要问题”依赖论者所处的社会语境，列举不同语境下凸显的不同议题。",
 "申明本文取舍标准：兼顾社会相关性与理论兴趣，力求覆盖面宽广。",
],
"terms": [
 {"en":"policy","zh":"政策","def":"本文指由社会层面制定的、处理AI的结构与措施（含监管）；本文将其与哲学性伦理问题相区分。"},
 {"en":"compliance","zh":"合规","def":"遵守政策法规与规范要求的实践维度；本文指出另一些AI伦理综述以政策与合规为组织线索。"},
],
"background": [
 {"title":"斯坦福哲学百科全书（SEP）","body":"由斯坦福大学维护的同行评审在线哲学百科全书，本文即其中一个条目；这一性质决定了本文按哲学问题、而非按政策合规或技术安全来组织材料。"},
],
"vocab": [
 {"en":"survey","pos":"n.","zh":"综述；调查性文章","ex":"other surveys focus on policy"},
 {"en":"landscape","pos":"n.","zh":"版图；全貌","ex":"the landscape of AI ethics"},
 {"en":"prominent","pos":"adj.","zh":"突出的；显著的","ex":"more prominent in certain societies"},
 {"en":"affluent","pos":"adj.","zh":"富裕的","ex":"people in affluent and peaceful societies"},
 {"en":"aim for","pos":"phr.","zh":"力求；以……为目标","ex":"We aim for a fairly wide understanding"},
],
}

A["p006"] = {
"zh": "有两种视角常常被归入“伦理”的标题之下，但在本文中只扮演较为次要的角色。其一是“AI政策”，它规定用以应对AI的社会结构与措施，包括监管与标准化。然而，政策方面的论争如今似乎在很大程度上已与哲学相分离，更多带有政治、法律与技术的性质——尽管它们常常依赖于伦理判断；这一点在“AI原则”时代（约2015—2020年）甚至更为明显。在本文中，政策事宜放在一个简短的独立小节（2.10）中讨论，而非与每一个伦理问题并列展开。",
"logic": [
 "界定本文范围：两种常被冠以“伦理”之名的视角将只起次要作用，此处先介绍其一——AI政策。",
 "说明AI政策的内容（社会结构、监管、标准化），并指出其论争如今已脱离哲学、偏政治法律技术性质，但仍依赖伦理判断。",
 "交代本文对政策问题的处理方式：集中置于独立小节，而非分散于各伦理议题。",
],
"terms": [
 {"en":"AI policy","zh":"AI政策","def":"规定应对AI所需社会结构与措施（含监管、标准化）的视角；本文将其与哲学伦理学区分开来。"},
 {"en":"regulation","zh":"监管；规制","def":"由公权力对技术加以规范与管制；是AI政策的核心内容之一。"},
],
"background": [
 {"title":"“AI原则”（AI Principles）运动","body":"指约2015至2020年间科技公司、研究机构与政府密集发布AI伦理原则文件的潮流；本文指出这些文件虽带有政治、技术性质，背后仍依赖伦理判断。"},
],
"vocab": [
 {"en":"run under","pos":"phr.","zh":"归在……名下；冠以……之名","ex":"often run under the heading of “ethics”"},
 {"en":"specify","pos":"v.","zh":"明确规定；具体说明","ex":"which specifies societal structures"},
 {"en":"divorced from","pos":"adj. phr.","zh":"与……相分离","ex":"largely divorced from philosophy"},
 {"en":"rely on","pos":"phr.","zh":"依赖；依靠","ex":"they often rely on ethical judgments"},
 {"en":"standardisation","pos":"n.","zh":"标准化","ex":"including regulation and standardisation"},
],
}

A["p007"] = {
"zh": "另一种突出的视角，是从AI的**风险**以及如何在技术上免于风险的**安全**角度来讨论AI伦理（例如 Brundage et al. 2018; Bengio et al. 2024; Narayanan and Kapoor 2024; Bengio et al. 2025 [Other Internet Resources]; Hendrycks 2025）。这类讨论旨在弄清哪些后果是可能发生的，以及如何通过技术与社会手段来避免负面后果。尽管其中许多问题确属核心伦理问题，但似乎很清楚：对AI伦理的讨论不应**完全**以“风险”来框定：a) 有些伦理考量并非后果论的；b) 如何评估后果本身就是一个伦理学讨论的主题；c) 关于规避风险的技术性讨论不属于伦理学；d) 有些负面后果已经现实发生，而非尚属风险；e) 对AI伦理的讨论不应只以否定性的措辞来框定，而应勾勒出一幅值得欲求的未来的积极愿景。技术性AI安全（有时被称为“对齐”）是一项在社会层面极为重要、与AI伦理密切相关、却并不等同于AI伦理的任务。大型AI技术公司通常都曾设立某种形式的“伦理”或“安全”委员会，但其中大多数在2020年代被解散。风险问题将在大多数伦理问题的讨论中继续出现。",
"logic": [
 "介绍第二种次要视角——以“风险”与技术安全来框定AI伦理，概括其目标为预测可能后果并设法规避负面后果。",
 "提出五点理由，论证AI伦理不能完全以风险/后果论来框定（含非后果论考量、后果评估本身的伦理性质、技术规避不属于伦理、后果已现实发生、需正面愿景）。",
 "区分技术性AI安全（对齐）与AI伦理本身，补充业界伦理/安全委员会在2020年代多被解散的事实，并预告风险将贯穿后续各议题。",
],
"terms": [
 {"en":"consequentialism","zh":"后果论","def":"只依后果之善恶评判行动对错的伦理理论；本文指出并非所有伦理考量都是后果论的。"},
 {"en":"value alignment","zh":"价值对齐","def":"使AI系统的目标与人类价值保持一致；本文指出技术性“对齐”任务与AI伦理密切相关但并不等同。"},
 {"en":"technical AI safety","zh":"技术性AI安全","def":"通过工程手段使AI系统安全、避免负面后果的研究任务；本文将其与规范性AI伦理相区分。"},
],
"background": [],
"vocab": [
 {"en":"prominent","pos":"adj.","zh":"突出的；显著的","ex":"Another prominent perspective is"},
 {"en":"frame ... in terms of","pos":"phr.","zh":"以……来框定","ex":"should not be framed entirely in terms of “risk”"},
 {"en":"probable","pos":"adj.","zh":"很可能的","ex":"which consequences are probable"},
 {"en":"dismantle","pos":"v.","zh":"解散；废除","ex":"most were dismantled in the 2020s"},
 {"en":"feature in","pos":"phr.","zh":"在……中起重要作用","ex":"Problems of risk will feature in"},
],
}

A["p008"] = {
"zh": "最后，一个问题若要够得上“伦理学问题”的资格，我们要求的是：在该具体情形中，何为合伦理之事并不清楚——由此排除那些干脆就是“伦理上有问题的”或“不道德的”事情（例如诈骗与谋杀）。话虽如此，处于社会语境中的技术系统（即技术—社会系统）总会使某些人类决策与某些社会发展比另一些更有可能发生，例如它们提供一种“助推”，它们具有可供性（affordance），或者它们改变了认识论处境。举例来说，一个大语言模型可能使某个人得以制造病毒、入侵数据库、实施诈骗或冒充他人（OpenAI 2025）。因此，考察AI与机器人技术在何处**促成**了此类行为或某种特定的社会发展，便属于本文的范围。",
"logic": [
 "提出“伦理学问题”的判定标准：仅当具体情形中何为合伦理之事并不明确时，才属伦理学问题，从而排除显然不道德之事。",
 "转折指出技术—社会系统总会改变人类决策与社会发展的概率分布（助推、可供性、改变认识论处境）。",
 "以大语言模型可被用于作恶为例，把“AI与机器人在何处促成了有害行为或特定社会发展”纳入本文范围。",
],
"terms": [
 {"en":"nudge","zh":"助推","def":"不禁止选项、而通过架构设计引导人们选择的做法；本文指技术系统对行为概率的结构性影响。"},
 {"en":"affordance","zh":"可供性","def":"环境或物品使得某种行动容易或困难的属性；本文指技术系统改变行动可能性的方式。"},
 {"en":"epistemic","zh":"认识论的","def":"与知识及信念之证成相关的；本文指技术系统会改变行动者据以形成信念的认识论处境。"},
 {"en":"LLM","zh":"大语言模型","def":"基于海量文本训练、可生成自然语言的生成式AI模型；本文指其可被人用以实施多种（含有害）行为。"},
],
"background": [],
"vocab": [
 {"en":"qualify as","pos":"phr.","zh":"够得上……的资格","ex":"for a problem to qualify as a “problem for ethics”"},
 {"en":"having said that","pos":"phr.","zh":"话虽如此","ex":"Having said that, technical systems"},
 {"en":"enable","pos":"v.","zh":"使能够；促成","ex":"where AI and robotics enable such behaviour"},
 {"en":"make it possible","pos":"phr.","zh":"使……成为可能","ex":"might make it possible for a person to build a virus"},
 {"en":"impersonate","pos":"v.","zh":"冒充；仿冒","ex":"to impersonate someone else"},
],
}

A["p009"] = {
"zh": "在某种程度上，“应用伦理学”这一领域是被技术驱动的：当一类新的系统问世，新的问题便随之出现。尽管预测本身有其风险，但似乎很清楚：倘若AI的技术进步照目前这样的态势持续下去（2026年初），我们所面对的将是一场重大的技术、社会与环境变迁，其根本程度不亚于工业革命所带来的那场变迁——那场变迁把动力从人力与畜力转向了水力/蒸汽/电力。",
"logic": [
 "提出“应用伦理学由技术驱动”的论点：新技术系统一旦问世，新的伦理问题便随之出现。",
 "以工业革命的动力转型为类比，预判AI若按当前势头发展将带来同等根本的技术—社会—环境变迁。",
],
"terms": [
 {"en":"applied ethics","zh":"应用伦理学","def":"把伦理理论应用于现实实践问题的伦理学分支；本文指出其议题常由新技术催生。"},
 {"en":"industrial revolution","zh":"工业革命","def":"以生产与动力方式根本转型为标志的历史事件；本文以其作为衡量AI变革深度的类比尺度。"},
],
"background": [
 {"title":"工业革命（Industrial Revolution）","body":"约18世纪下半叶发端于英国的生产与动力方式根本转型，水力、蒸汽、电力逐步取代人力与畜力；本文以此类比AI技术变革的根本程度。"},
],
"vocab": [
 {"en":"be driven by","pos":"phr.","zh":"由……驱动","ex":"is driven by technology"},
 {"en":"come out","pos":"phr.","zh":"问世；出现","ex":"When a new kind of system comes out"},
 {"en":"look at","pos":"phr.","zh":"面对；面临","ex":"we are looking at a major technical"},
 {"en":"fundamental","pos":"adj.","zh":"根本的","ex":"as fundamental as the one generated by"},
 {"en":"prediction","pos":"n.","zh":"预测","ex":"Though prediction has its risks"},
],
}

A["p010"] = {
"zh": "在20世纪，AI通常被理解为一项研究纲领：认知科学把人类智能发展为“对有意义的符号进行计算”的模型，计算机科学则把这些模型在数字硬件上加以实现，从而既检验了这些模型，又实现了一种通用形式的人工智能。这一纲领在塞尔（Searle）的“强AI”概念中表现得很清楚：“被赋予恰当程序的计算机，可以在字面上被说成是**理解**并具有其他认知状态的”（Searle 1980, 417）。这一纲领后来被称为“经典AI”，它与“联结主义AI”存在某种竞争关系；后者主张应着眼于在“神经网络”中建模大脑，而非建模其功能架构。这两种AI都在约1975—1995年的“AI之冬”期间遇到了重大问题，并分化出若干专门的技术学科（例如图像模式识别或机器人学），这些学科常常刻意避开“AI”这个声名不佳的名称。",
"logic": [
 "概述20世纪主流AI研究纲领：认知科学提供符号计算式智能模型、计算机科学加以实现，以求同时检验模型并达成通用智能。",
 "援引塞尔“强AI”表述作为该纲领的典型表述，介绍“经典AI”及其与“联结主义AI”（以神经网络建模大脑）的竞争。",
 "指出两派在“AI之冬”中遭遇重大困境，并分化出刻意回避“AI”之名的专门技术学科。",
],
"terms": [
 {"en":"strong AI","zh":"强人工智能","def":"塞尔用语：认为恰当编程的计算机本身即可具有理解等真实认知状态；是经典AI纲领的核心主张。"},
 {"en":"classical AI","zh":"经典AI","def":"以“对有意义符号的计算”为智能模型的符号主义AI纲领，与联结主义AI相对。"},
 {"en":"connectionist AI","zh":"联结主义AI","def":"主张以神经网络建模大脑、而非符号功能架构的AI路径。"},
 {"en":"neural network","zh":"神经网络","def":"受大脑神经元联结启发的计算模型，是联结主义AI的核心工具。"},
 {"en":"AI winter","zh":"AI之冬","def":"指约1975—1995年间AI研究因预期落空而遭遇资金与兴趣锐减的时期。"},
],
"background": [
 {"title":"约翰·塞尔（John Searle）","body":"美国哲学家，1980年提出“中文屋”论证以批评强AI立场；本文引用其对“强AI”的界定——恰当编程的计算机可在字面上被说成理解。"},
],
"vocab": [
 {"en":"research programme","pos":"n.","zh":"研究纲领","ex":"understood as a research programme"},
 {"en":"evident","pos":"adj.","zh":"明显的；清楚的","ex":"This programme is evident in Searle’s notion"},
 {"en":"run into","pos":"phr.","zh":"遭遇；撞上","ex":"ran into significant problems"},
 {"en":"spin off","pos":"phr.","zh":"分离出；派生","ex":"they spun off some specialised technical disciplines"},
 {"en":"tainted","pos":"adj.","zh":"声名不佳的；被玷污的","ex":"avoided the tainted name “AI”"},
],
}

A["p011"] = {
"zh": "随着2010年代更为成功的机器学习（ML）系统的出现——主要是多层（即“深度”）神经网络（LeCun, Bengio, and Hinton 2015; Schmidhuber 2015），尤其是随着2020年前后广受欢迎的生成式人工智能，如大语言模型（LLM）——“AI”一词的用法已极大地拓宽。向ML的这一重大转变，与算法上的进步（例如生成对抗网络或Transformer模型）有关，也与如下事实有关：算力与存储的成本下降了，而投资却增加了。由此带来的算力与数据存储方面的指数级增长，使人们能够在海量数据（实质上即所有可用数据）上训练模型，并生成非常庞大的模型（其规模通常达到训练数据的20%—50%）。这种“规模化”（scaling）带来了ML系统的根本性改进，其表现往往在短短数年内就从人类水平的10%跃升至超越人类水平。当前的AI趋势在若干地方都有追踪；其中一个突出来源是HAI AI指数。",
"logic": [
 "叙述2010年代以来以深度神经网络为核心的机器学习、以及2020年前后生成式AI与大语言模型的兴起，指出“AI”一词用法随之极大拓宽。",
 "分析转向ML的两大驱动：算法进步（对抗网络、Transformer）与算力存储成本下降、投资上升。",
 "说明规模化训练带来指数级性能跃升（从人类水平10%到超越人类），并指出追踪当前AI趋势的权威来源。",
],
"terms": [
 {"en":"machine learning","zh":"机器学习","def":"让机器从数据中归纳规律而非显式编程的AI路径，2010年代后成为主流。"},
 {"en":"deep learning","zh":"深度学习","def":"基于多层（“深度”）神经网络的机器学习方法。"},
 {"en":"generative AI","zh":"生成式人工智能","def":"能够生成文本、图像等新内容的AI系统，如大语言模型。"},
 {"en":"scaling","zh":"规模化","def":"通过持续扩大模型规模与训练数据量来提升机器学习系统性能的做法。"},
],
"background": [
 {"title":"HAI AI指数（HAI AI Index）","body":"由斯坦福大学以人为本人工智能研究院（HAI）发布的年度报告，系统追踪AI技术、经济与伦理趋势；本文视其为追踪当前AI趋势的一个突出来源。"},
],
"vocab": [
 {"en":"advent","pos":"n.","zh":"出现；到来","ex":"With the advent of more successful machine learning"},
 {"en":"broaden","pos":"v.","zh":"拓宽；扩大","ex":"the use of the term “AI” has broadened massively"},
 {"en":"exponential","pos":"adj.","zh":"指数级的","ex":"exponential gains in computing power"},
 {"en":"track","pos":"v.","zh":"追踪；记录","ex":"Current AI trends are tracked in several places"},
 {"en":"radical","pos":"adj.","zh":"根本性的；彻底的","ex":"achieves radical improvements"},
],
}

A["p012"] = {
"zh": "经典AI的这一总体目标，在AI之冬之后几乎已被悄然放弃，尽管仍有一小群人主张经典AI应直接聚焦于“通用人工智能”（AGI）——他们自2008年起便以该名称组织了一个小众的会议系列。在过去10年里，人们再次普遍地追问：我们是否正走在通往某种通用AI的道路上？而这种通用AI如今被理解为主要以机器学习为基础。旧标签“AGI”如今常被用来把“大致达到人类水平的通用人工智能”这一目标，与针对具体问题的技术性AI区分开来，其言下之意是：在那一点上将会发生某种重要的事情（正是这一假设驱动着当前对AI的部分过度投资）。AI是否正朝着通用智能前进，仍是一个开放问题（AAAI 2025, 58–63; Bengio et al. 2025）——这个问题在诸多方面关系到伦理学，例如有人主张，与AGI的巨大好处相比，AI那些细枝末节的争执无足轻重；或者，我们越接近AGI，来自超级智能的存在性风险论证就越紧迫。",
"logic": [
 "叙述经典AI的通用目标在AI之冬后几被放弃，仅由小众群体以AGI会议系列延续。",
 "指出近十年学界重提“是否正通往通用AI”，并说明AGI标签如今用于区分人类水平通用智能与狭义技术AI，及其对当前投资的影响。",
 "指出AI是否正走向通用智能仍是开放问题，并说明该问题为何对伦理学重要（影响对具体问题的权重判断，以及存在性风险论证的紧迫性）。",
],
"terms": [
 {"en":"AGI","zh":"通用人工智能（AGI）","def":"在广泛认知任务上达到大致人类水平的通用智能；本文指出其是否可及仍是开放问题。"},
 {"en":"existential risk","zh":"存在性风险","def":"可能导致人类文明生存性灾难的风险；本文指来自超级智能的此类风险论证随AGI临近而更趋紧迫。"},
],
"background": [],
"vocab": [
 {"en":"all but","pos":"phr.","zh":"几乎；差一点","ex":"had been all but quietly given up"},
 {"en":"push for","pos":"phr.","zh":"力主；推动","ex":"a small group pushed for the idea"},
 {"en":"niche","pos":"adj.","zh":"小众的；利基的","ex":"organising a niche conference series"},
 {"en":"on course","pos":"phr.","zh":"在……轨道上；正朝着","ex":"whether AI is on course towards general intelligence"},
 {"en":"quibble","pos":"n.","zh":"吹毛求疵的争执","ex":"minor AI quibbles do not matter"},
],
}

A["p013"] = {
"zh": "既然AI运行于计算机之上，便有一个问题：量子计算可能扮演什么角色？量子计算凭借叠加态量子比特（qbit），可以在资源（例如时间）上高效得多地进行计算，使得一些原本实际上无法计算、即“不可处理的”（intractable）函数，变得实际上可以计算（例如只需几秒而非几个世纪）——尽管量子可计算函数的集合并不大于图灵可计算函数的集合（Deutsch 1985）。这一效率增益具有巨大的现实意义，因为公钥加密——亦即计算机安全与身份识别的大部分内容——依赖于“陷门函数”：这种函数在一个方向上实际容易计算，而在相反方向上却非常难以计算（例如，“把这两个素数相乘”对“找出哪两个素数相乘会得到这个数”）。因此，量子计算的安全问题——若其在实用层面得以实现——并非AI所特有，但它也会影响AI。",
"logic": [
 "引入量子计算议题：说明其凭借叠加态量子比特可在效率上实现量级提升，使原本不可处理的函数变得可计算，同时指出其可计算函数集并不超出图灵可计算范围。",
 "解释这一效率增益为何极具现实意义：公钥加密依赖陷门函数，量子计算会威胁现有计算机安全与身份体系。",
 "收束：量子计算的安全问题并非AI所特有，但同样会波及AI。",
],
"terms": [
 {"en":"quantum computing","zh":"量子计算","def":"利用叠加态量子比特进行计算、可在特定问题上实现资源效率跃升的计算范式。"},
 {"en":"Turing-computable","zh":"图灵可计算的","def":"可由图灵机在有限步骤内完成的计算；本文指出量子可计算函数集并未超出图灵可计算函数集。"},
 {"en":"trap-door function","zh":"陷门函数","def":"一个方向易算、反方向极难算的函数，是公钥加密的数学基础。"},
],
"background": [],
"vocab": [
 {"en":"given that","pos":"phr.","zh":"既然；考虑到","ex":"Given that AI runs on computers"},
 {"en":"intractable","pos":"adj.","zh":"不可处理的；难驾驭的","ex":"practically impossible to compute, or “intractable”"},
 {"en":"practical relevance","pos":"n.","zh":"现实意义；实用相关性","ex":"enormous practical relevance"},
 {"en":"rely on","pos":"phr.","zh":"依赖","ex":"relies on “trap-door functions”"},
 {"en":"specific to","pos":"adj. phr.","zh":"为……所特有","ex":"is not specific to AI"},
],
}

A["p014"] = {
"zh": "AI完全是软件，而机器人则是受物理力支配的物理机器；它们有“传感器”，并通过“执行器”（如夹持器或转动的车轮）对世界施加物理力。据此，自动驾驶汽车或飞机就是机器人，而当前机器人中只有极小一部分是“人形的”（人形状的）。有些机器人使用AI，有些则不使用：典型的工业机器人仍在一个受到最大限度控制的环境中，盲目地遵循完全被定义好的脚本，只接受极少的感觉输入，不进行学习或推理。然而，AI在机器人技术中的使用正在增加，包括在人形机器人中的使用，主要用于感知与动作控制。因此，机器人与AI系统可被视为两个相互重叠的集合：仅有AI的系统、仅有机器人技术的系统，以及二者兼具的系统。这三类我们都感兴趣；本文的范围就是这两个集合的并集。",
"logic": [
 "界定AI与机器人的本体论差别：AI纯属软件，机器人是受物理力支配、具备传感器与执行器的物理机器。",
 "据此推论自动驾驶汽车/飞机即机器人，人形机器人只占很小比例，并以工业机器人为例说明存在不用AI的机器人。",
 "指出AI在机器人中应用日增，最终把AI与机器人刻画为两个重叠集合，本文范围取二者之并集。",
],
"terms": [
 {"en":"robotics","zh":"机器人学","def":"研究物理机器（具备传感器、执行器）的设计与控制的技术领域；与AI软件相区分而又相互重叠。"},
 {"en":"sensor","zh":"传感器","def":"机器人用以感知外部世界的装置，与施加物理力的执行器相对。"},
 {"en":"actuator","zh":"执行器","def":"机器人借以对外部世界施加物理力的装置（如夹持器、车轮）。"},
],
"background": [],
"vocab": [
 {"en":"be subject to","pos":"phr.","zh":"受……支配；服从于","ex":"are subject to physical forces"},
 {"en":"exert ... onto","pos":"phr.","zh":"把……施加于","ex":"exert physical force onto the world"},
 {"en":"accordingly","pos":"adv.","zh":"据此；因此","ex":"Accordingly, autonomous cars or planes are robots"},
 {"en":"overlapping","pos":"adj.","zh":"相互重叠的","ex":"two overlapping sets"},
 {"en":"union","pos":"n.","zh":"并集；联合","ex":"the union of both sets"},
],
}

A["p015"] = {
"zh": "值得记住的是，人工智能与机器人伦理学是一门非常年轻的学科：关于机器人伦理或机器伦理的最早出版物出现于21世纪初（Moor 2006）；首届AI伦理会议于2012年召开（Müller 2014）；最早的一批著作则分别问世于超级智能（Bostrom 2014）、机器伦理（Misselhorn 2018/22）与控制问题（S. Russell 2019）等主题。此后，出现了最早的综述性文章（Müller 2020）与著作（Dignum 2019; Coeckelbergh 2020; Dubber, Pasquale, and Das 2020; Gordon and Nyholm 2021），以及更多政策导向的作品（Floridi et al. 2018; Taddeo and Floridi 2018; Taylor et al. 2018; Walsh 2018; Bryson 2019; Gibert 2019; Whittlestone et al. 2019）。我们很可能仍缺乏一个已牢固确立的范围、方法或经典著作（L. E. Frank and Klincewicz 2024）。此外，关于AI伦理史、以及关于更广义的计算机伦理或数字伦理的历史研究都很少（但可参见 Müller 2022）。机器人伦理学方面有用的综述包括（Calo, Froomkin, and Kerr 2016; Royakkers and van Est 2016; Tzafestas 2016; Coeckelbergh 2022b）；一部标准的论文集是（Lin, Abney, and Jenkins 2017）。AI伦理的手册与综述包括（Boddington 2023; Floridi 2023b; Bullock et al. 2024; Gunkel 2024; Floridi and Taddeo 2025; Hähnel and Müller 2025; Smuha 2025），其中（Hagendorff 2024）专论生成式AI，（Nyholm, Kasirzadeh, and Zerilli 2026）则讨论当代论争。",
"logic": [
 "以时间线说明本学科的年轻：21世纪初首批出版物、2012年首届会议、2014年起首批主题著作相继出现。",
 "指出学科至今尚未形成稳固的范围、方法与经典著作，相关学术史研究也很少。",
 "列举机器人伦理与AI伦理领域可用的综述、论文集与手册，为读者提供文献导航。",
],
"terms": [
 {"en":"machine ethics","zh":"机器伦理","def":"研究如何使机器本身具备伦理行为能力的领域；本文指出其首批出版物出现于21世纪初。"},
 {"en":"control problem","zh":"控制问题","def":"指如何使强AI/超级智能始终处于人类可控之下的问题；本文以S. Russell 2019为其代表著作。"},
],
"background": [
 {"title":"尼克·波斯特洛姆（Nick Bostrom）","body":"当代哲学家，2014年出版《超级智能》（Superintelligence），是超级智能与存在性风险议题的代表性著作。"},
 {"title":"斯图尔特·罗素（Stuart Russell）","body":"计算机科学家，2019年著作《人类兼容》（Human Compatible）系统讨论AI的“控制问题”，主张使AI与人类意图对齐。"},
],
"vocab": [
 {"en":"well-established","pos":"adj.","zh":"牢固确立的","ex":"lack a well-established scope, method"},
 {"en":"canonical","pos":"adj.","zh":"经典的；权威的","ex":"or canonical works"},
 {"en":"take place","pos":"phr.","zh":"举行","ex":"took place in 2012"},
 {"en":"survey","pos":"n.","zh":"综述","ex":"the first survey articles"},
 {"en":"it is worth remembering","pos":"phr.","zh":"值得记住的是","ex":"It is worth remembering that"},
],
}

A["p016"] = {
"zh": "世界在过去几年里已经改变。自本文初版（2020年初）以来，就本文主题发表的文献很可能比此前整个时期的文献总和还要多。而且，如今过去对AI与计算视而不见的主流哲学期刊也开始发表相关论文。因此，本文所引用文献的挑选范围必然更为狭窄，也更容易出错。2020年在尚无先前综述文章或著作的情况下提出的这一主要编排方式，如今看来保持得还算不错。",
"logic": [
 "指出本领域文献量在本文初版后爆炸式增长、主流哲学期刊也开始接纳相关研究。",
 "据此坦承文献选择范围更窄、也更易出错。",
 "回顾性地为本文2020年提出的编排框架辩护：其适用性至今保持良好。",
],
"terms": [
 {"en":"ethics of AI and robotics","zh":"人工智能与机器人伦理学","def":"一门文献量近年激增、仍在快速扩张的年轻学科；本文2020年提出的编排框架至今基本适用。"},
],
"background": [],
"vocab": [
 {"en":"prone to","pos":"adj. phr.","zh":"易于……的","ex":"more prone to errors"},
 {"en":"hold up","pos":"phr.","zh":"保持；站得住","ex":"appears to have held up reasonably well"},
 {"en":"in the absence of","pos":"phr.","zh":"在缺乏……的情况下","ex":"in the absence of a prior survey article"},
 {"en":"mainstream","pos":"adj.","zh":"主流的","ex":"papers are now published in mainstream philosophical journals"},
 {"en":"refer to","pos":"phr.","zh":"引用；提及","ex":"the literature that is referred to here"},
],
}

A["p017"] = {
"zh": "关于行文基调的一点说明：“关于x的伦理”这类研究的特点是，它倾向于处理x的伦理**问题**，而非讨论x本身的**价值**。其结果是，AI伦理显得“对AI持否定态度”。这是我们在此试图加以缓和的一种倾向：AI伦理的要旨在于弄清AI**应当**是什么样子，分析在对待AI时何为正确行动方式所面临的种种困难。因此，在理想情况下，AI伦理为“良好工程”提供方向（这一要求有各种名称，如“可信赖的”“人道的”“对齐的”“可靠的”或“合伦理的”）。于是，AI伦理的社会任务，就是为良好的AI设计与使用提供指引，指向一个值得欲求的世界（倘若AI是这样一个世界的组成部分）。",
"logic": [
 "说明“关于x的伦理”类研究的固有倾向：聚焦x的问题而非x的优点，致使AI伦理显得一味否定AI。",
 "提出本文自觉反对此倾向：AI伦理的要旨是追问AI应当如何、正确行动方式何在。",
 "据此把AI伦理定位为“良好工程”的方向指引与社会层面的设计使用指南，最终指向值得欲求的世界。",
],
"terms": [
 {"en":"value alignment","zh":"价值对齐","def":"此处作为“良好工程”的诸多别名之一（“aligned”），指AI系统与人类价值保持一致。"},
],
"background": [],
"vocab": [
 {"en":"characteristic","pos":"adj.","zh":"特有的；典型的","ex":"It is characteristic of the “ethics of x”"},
 {"en":"merit","pos":"n.","zh":"优点；价值","ex":"rather than with the merits of x"},
 {"en":"mitigate","pos":"v.","zh":"缓和；减轻","ex":"a tendency we try to mitigate here"},
 {"en":"guidance","pos":"n.","zh":"指引；指导","ex":"provide guidance for good AI design"},
 {"en":"with respect to","pos":"phr.","zh":"关于；对待","ex":"the right way to act with respect to AI"},
],
}

A["p018"] = {
"zh": "隐私有若干公认的面向，例如“不受打扰的权利”、对关于自身信息的控制（Rachels 1975）、隐私作为人格（personhood）的一个面向，以及——在英语中——还包括空间隐私与身体隐私（Bennett and Raab 2018; Roessler 2018）。信息技术中关于隐私与监控的讨论（例如 Macnish 2017; Roessler 2017）主要关乎可被个人识别的数据，即对该数据的**访问**与对该数据的**控制**，或二者的结合（Véliz 2024）。经典的隐私研究聚焦于情报机关实施的国家监控，但如今也涵盖其他国家机关、企业乃至个人实施的监控。相关信息技术在过去数十年里发生了重大变化，而监管却反应迟缓（尽管已有《通用数据保护条例》（GDPR, 2016））——其结果是某种程度的无序状态，最有权势的玩家在其中渔利，并由此引发了大量政治讨论（Véliz 2020）。",
"logic": [
 "罗列隐私的若干公认面向（不受打扰的权利、对自身信息的控制、人格面向、空间与身体隐私），界定概念范围。",
 "指出信息技术语境下的隐私讨论核心是个人可识别数据的访问与控制。",
 "描述监控主体从国家情报机关扩展到企业与个人的历史变化，以及技术剧变与监管迟缓之间的落差及其后果。",
],
"terms": [
 {"en":"privacy","zh":"隐私","def":"含“不受打扰的权利”、对自身信息的控制、人格面向等多重含义。"},
 {"en":"surveillance","zh":"监控","def":"对个人信息的持续收集与监视；其主体已从情报机关扩展至企业乃至个人。"},
 {"en":"personhood","zh":"人格（地位）","def":"本文将隐私视为人格的一个面向。"},
 {"en":"GDPR","zh":"《通用数据保护条例》（GDPR）","def":"欧盟2016年通过的数据保护法规；本文将其作为监管应对迟缓中仅有的重要例外。"},
],
"background": [
 {"title":"《通用数据保护条例》（GDPR）","body":"欧盟于2016年通过、2018年生效的数据保护立法，是数字时代最具影响力的隐私规制之一；本文用它说明监管虽有动作，但整体仍滞后于技术变化。"},
],
"vocab": [
 {"en":"well-recognised","pos":"adj.","zh":"公认的","ex":"several well recognised aspects"},
 {"en":"personally identifiable","pos":"adj.","zh":"可识别个人身份的","ex":"mainly concerns personally identifiable data"},
 {"en":"anarchy","pos":"n.","zh":"无序状态","ex":"a certain anarchy that is exploited"},
 {"en":"exploit","pos":"v.","zh":"利用；渔利","ex":"exploited by the most powerful players"},
 {"en":"slow to respond","pos":"adj. phr.","zh":"反应迟缓","ex":"regulation has been slow to respond"},
],
}

A["p019"] = {
"zh": "数字领域在近几十年里极大地扩张了：如今所有数据收集与存储都是数字化的，我们的生活日益数字化，越来越多的传感器技术被投入使用，用以生成关于我们生活中非数字化面向的数据，而且大多数数字数据都连接到同一个互联网上。此外，大量数据在能动者之间被交易，通常是有偿交易。其结果是：在数字世界中，控制“谁收集哪些数据、谁有权访问”，要比在纸张与电话构成的模拟世界中困难得多。",
"logic": [
 "描述数字领域的四重扩张（数据全数字化、生活数字化、传感器采集非数字生活、数据接入同一互联网）。",
 "补充数据在能动者之间被有偿交易这一经济事实。",
 "由此得出隐私控制在数字世界比模拟世界困难得多的结论。",
],
"terms": [
 {"en":"digital sphere","zh":"数字领域","def":"本文指一切信息被数字化、并接入同一互联网后所构成的信息空间。"},
],
"background": [],
"vocab": [
 {"en":"widen","pos":"v.","zh":"拓宽","ex":"The digital sphere has widened greatly"},
 {"en":"in use","pos":"phr.","zh":"在使用中","ex":"more and more sensor technology in use"},
 {"en":"trade","pos":"v.","zh":"交易；买卖","ex":"much of the data is traded between agents"},
 {"en":"analogue","pos":"adj.","zh":"模拟的；非数字的","ex":"the analogue world of paper and telephone calls"},
 {"en":"have access","pos":"phr.","zh":"有权访问","ex":"who has access"},
],
}

A["p020"] = {
"zh": "AI既增加了智能数据收集的可能性，也增加了数据分析的可能性——而且它还提高了数据的价值，因为数据可被用于训练机器学习系统。例如，照片与视频中的人脸识别、“设备指纹识别”以及计算机科学所研究的其他一大批技术（例如 Rocher, Hendrickx, and de Montjoye 2019），都允许实时识别，从而对个人或其设备进行画像与检索（Whittaker et al. 2018, 15ff.）。其结果是：“在这片浩瀚的数据海洋中，存在着一幅关于我们的、完整得令人恐惧的图景”（Smolan 2016, 1:01）……而这一说法如今听起来已近乎老生常谈。",
"logic": [
 "指出AI从三个维度加剧隐私问题：强化数据收集、强化数据分析、抬高数据价值（可用于训练机器学习）。",
 "以人脸识别、设备指纹等技术为例，说明实时识别→画像→检索个人及其设备的链条。",
 "引述“数据海洋中完整得令人恐惧的图景”一语，并指出它如今已显得平常，暗示问题进一步恶化。",
],
"terms": [
 {"en":"face recognition","zh":"人脸识别","def":"通过照片与视频自动识别人类身份的AI技术；本文将其列为实时画像的手段之一。"},
 {"en":"profiling","zh":"画像","def":"基于数据推断个体属性、行为或偏好的做法。"},
 {"en":"training data","zh":"训练数据","def":"用于训练机器学习系统的数据；AI的兴起使其价值上升。"},
],
"background": [],
"vocab": [
 {"en":"a host of","pos":"phr.","zh":"一大批；许多","ex":"a host of other techniques"},
 {"en":"real time","pos":"adj.","zh":"实时的","ex":"allow real time identification"},
 {"en":"search for","pos":"phr.","zh":"检索；搜寻","ex":"thus profiling and searching for individual humans"},
 {"en":"trivial","pos":"adj.","zh":"平常的；微不足道的","ex":"a remark that already seems trivial now"},
 {"en":"increase the value","pos":"phr.","zh":"提高……的价值","ex":"it increases the value of data"},
],
}

A["p021"] = {
"zh": "我们身后留下的数据痕迹，正是我们那些“免费”服务得以支付的方式——但我们并未被告知这种数据收集以及这种新原料的价值，而且我们还在被操纵着留下越来越多此类数据。对“五大”公司（亚马逊、谷歌/Alphabet、微软、苹果、脸书/Meta）而言，其业务中主要的数据收集部分，似乎建立在欺骗、利用人性弱点、助长拖延、制造成瘾以及操纵之上（Harris 2016; Klenk and Jongepier 2022）。在这种“监控经济”中，社交媒体、游戏以及互联网大部分领域的首要焦点，是获取、维持并引导**注意力**——从而获得源源不断的数据供给。正如施奈尔（Schneier）所言：“监控就是互联网的商业模式”（Schneier 2015）；这一点有时被概括为口号“监控资本主义”（Williams 2018; Zuboff 2019; Königs 2024）。",
"logic": [
 "揭示“免费”服务的真实对价：用户留下的数据痕迹，而用户对此既不知情又被操纵着多留数据。",
 "以“五大”公司为例，刻画其数据收集业务所依赖的欺骗、利用弱点、成瘾与操纵等机制。",
 "概括“监控经济”的运作逻辑在于争夺注意力以持续获取数据，并以施奈尔之言与“监控资本主义”口号收束。",
],
"terms": [
 {"en":"surveillance capitalism","zh":"监控资本主义","def":"以监控用户行为、提取并利用数据为核心盈利方式的资本主义形态；本文用其概括当代互联网经济。"},
 {"en":"manipulation","zh":"操纵","def":"本文指数字平台通过设计把用户操纵为留下更多数据。"},
],
"background": [
 {"title":"布鲁斯·施奈尔（Bruce Schneier）","body":"美国密码学与计算机安全专家，2015年提出“监控就是互联网的商业模式”，指数据监控已成为互联网经济的核心。"},
 {"title":"监控资本主义（surveillance capitalism）","body":"肖莎娜·祖博夫（Shoshana Zuboff）在《监控资本主义时代》（2019）中系统阐发的概念，指科技公司通过提取用户行为数据牟利并塑造行为的新经济形态。"},
],
"vocab": [
 {"en":"data trail","pos":"n.","zh":"数据痕迹；数据轨迹","ex":"The data trail we leave behind"},
 {"en":"exploit","pos":"v.","zh":"利用（弱点）","ex":"exploiting human weaknesses"},
 {"en":"addiction","pos":"n.","zh":"成瘾","ex":"generating addiction, and manipulation"},
 {"en":"catchword","pos":"n.","zh":"口号；流行语","ex":"captured in the catchword “surveillance capitalism”"},
 {"en":"raw material","pos":"n.","zh":"原料","ex":"the value of this new raw material"},
],
}

A["p022"] = {
"zh": "从“控制”角度理解隐私的一个有用视角，是把它视为这样一种要求：信息完整性在相关语境中得到保持——即“语境完整性”（contextual integrity）要求信息的流动受到恰当控制（Nissenbaum 2004）。AI生成真实人物图像与视频的问题，或许正适合用这一进路来处理。有人主张，“自由”的丧失是AI时代的特征性标志（Santoni de Sio 2024）。这种丧失引发了许多逃离监控资本主义掌控的尝试，例如实践“极简主义”（Newport 2019），或借助开源运动——但如今的公民是否具备所需的自主性，是令人怀疑的。",
"logic": [
 "介绍诺伊鲍姆“语境完整性”这一从控制角度理解隐私的进路，并指出AI生成真人影像问题适合用它处理。",
 "引述“自由的丧失是AI时代特征性标志”的论断。",
 "列举用户逃离监控资本主义的尝试（极简主义、开源运动），并对普通公民是否具备所需自主性表示怀疑。",
],
"terms": [
 {"en":"contextual integrity","zh":"语境完整性","def":"海伦·诺伊鲍姆提出的隐私理论，主张隐私在于信息在其原初社会语境中按恰当规范流动。"},
 {"en":"autonomy","zh":"自主性","def":"自我决定与独立行动的能力；本文质疑当代公民是否具备摆脱监控所需的自主性。"},
],
"background": [
 {"title":"海伦·诺伊鲍姆（Helen Nissenbaum）","body":"信息伦理学者，2004年提出“语境完整性”理论，主张隐私取决于信息在特定社会语境中是否按规范流动。"},
],
"vocab": [
 {"en":"perspective","pos":"n.","zh":"视角；观点","ex":"One useful perspective on privacy"},
 {"en":"preserve","pos":"v.","zh":"保持；维护","ex":"information integrity is preserved"},
 {"en":"suit","pos":"v.","zh":"适合；适宜","ex":"may suit this approach"},
 {"en":"escape from","pos":"phr.","zh":"逃离","ex":"attempts to escape from the grasp of"},
 {"en":"grasp","pos":"n.","zh":"掌控；掌握","ex":"the grasp of surveillance capitalism"},
],
}

A["p023"] = {
"zh": "监控系统往往会揭示出关于我们的、我们自己希望压抑或并未意识到的事实：它们比我们自己更了解我们自己。即便只是观察在线行为，也能让人洞察我们的心理状态（Burr and Christianini 2019）乃至操纵（见下文2.1.2节）。这引发了保护“派生数据”的呼声（Wachter and Mittelstadt 2019）。赫拉利在其畅销书《未来简史》（Homo Deus, 2016）的末句中追问AI的长期后果：“当没有意识却高度智能的算法比我们自己更了解我们时，社会、政治与日常生活将会变成什么样子？”（至于算法能否“知道”，暂且不论。）",
"logic": [
 "指出监控系统能揭示连主体自己都不愿承认或未曾意识到的事实，提出“它们比我们更了解我们自己”的命题。",
 "说明仅观察在线行为即可洞察心理状态，由此引出保护“派生数据”的主张。",
 "引述赫拉利《未来简史》末句，追问高度智能算法比我们更了解我们时社会、政治与日常生活的长远后果。",
],
"terms": [
 {"en":"derived data","zh":"派生数据","def":"由对原始数据的分析、推断所生成的数据（如从行为推得的心理状态）；本文指学界主张加以保护的数据类别。"},
],
"background": [
 {"title":"尤瓦尔·赫拉利《未来简史》（Homo Deus）","body":"以色列历史学家尤瓦尔·赫拉利2016年出版的畅销书，其末句追问：当无意识却高度智能的算法比人更了解人时，社会、政治与日常生活将走向何方。"},
],
"vocab": [
 {"en":"reveal","pos":"v.","zh":"揭示；显露","ex":"reveal facts about us"},
 {"en":"suppress","pos":"v.","zh":"压抑；压制","ex":"we ourselves wish to suppress"},
 {"en":"insight into","pos":"n. phr.","zh":"对……的洞察","ex":"allows insights into our mental states"},
 {"en":"call for","pos":"phr.","zh":"呼吁；要求","ex":"led to calls for the protection of"},
 {"en":"never mind","pos":"phr.","zh":"姑且不论","ex":"never mind whether an algorithm can “know”"},
],
}

A["p024"] = {
"zh": "机器人系统正开始在这一领域扮演重要角色，尤其是从空中。连同“物联网”、各种“智能”系统（手机、电视、烤箱、灯具、虚拟助手、家居……）、“智慧城市”（Sennett 2018）、“智能治理”以及“智能能动式AI”一道，它们注定将成为数据采集系统的组成部分，实时提供更详尽的数据，信息量越来越大。",
"logic": [
 "指出机器人系统（尤其空中平台）开始在数据采集领域扮演重要角色。",
 "将其置于“物联网—智能设备—智慧城市—智能治理—智能能动AI”的技术组合中加以定位。",
 "预判这些系统将一体化为实时、详尽、信息持续膨胀的数据采集网络。",
],
"terms": [
 {"en":"Internet of things","zh":"物联网","def":"把日常物理物品接入互联网并相互交换数据的技术范式；本文将其与机器人共同视为数据采集网络的组成部分。"},
 {"en":"smart city","zh":"智慧城市","def":"本文指以传感器与数据技术治理城市的范式，是数据采集网络的一环。"},
],
"background": [],
"vocab": [
 {"en":"play a role","pos":"phr.","zh":"发挥作用；扮演角色","ex":"play a major role in this area"},
 {"en":"esp.","pos":"adv.","zh":"尤其；特别是","ex":"esp. from the air"},
 {"en":"be set to","pos":"phr.","zh":"注定要；即将","ex":"they are set to become part of"},
 {"en":"real time","pos":"adj.","zh":"实时的","ex":"offers more detailed data in real time"},
 {"en":"ever more","pos":"phr.","zh":"越来越","ex":"with ever more information"},
],
}

A["p025"] = {
"zh": "监控与个人自由之间存在一场“军备竞赛”，而一个重要的社会问题在于：良好的平衡究竟应落在何处。“双方”都在使用信息技术，例如隐私可以通过加密、匿名性、加密货币来加以保护。出于某些研究目的，存在一些隐私保护技术，可以在很大程度上隐藏个人或群体的身份，例如“差分隐私”（differential privacy）——通过加入校准过的噪声来加密查询输出（Dwork et al. 2006; Garfinkel 2025）。当一些公司出售监控时，另一些公司则出售免受监控的保护，例如在计算机与手机的操作系统中。",
"logic": [
 "把监控与个人自由的关系刻画为一场“军备竞赛”，并提出如何在二者间取得良好平衡的社会问题。",
 "列举双方所用技术：隐私可由加密、匿名、加密货币保护，差分隐私等技术可在研究中隐藏身份。",
 "指出市场的两面性：既有公司出售监控，也有公司出售反监控保护。",
],
"terms": [
 {"en":"differential privacy","zh":"差分隐私","def":"通过向查询输出中加入校准噪声、防止个体身份被反推的隐私保护技术。"},
 {"en":"encryption","zh":"加密","def":"以密码学手段使数据不可被未授权者解读的技术，是保护隐私的主要手段之一。"},
],
"background": [
 {"title":"差分隐私（differential privacy）","body":"由辛西娅·德沃克（Cynthia Dwork）等人于2006年提出的隐私保护技术，通过向查询结果注入校准噪声，使数据使用者无法据此识别个体。"},
],
"vocab": [
 {"en":"arms race","pos":"n.","zh":"军备竞赛","ex":"an “arms race” between surveillance"},
 {"en":"conceal","pos":"v.","zh":"隐藏；掩盖","ex":"largely conceal the identity of persons"},
 {"en":"calibrate","pos":"v.","zh":"校准","ex":"adding calibrated noise to encrypt"},
 {"en":"privacy-preserving","pos":"adj.","zh":"保护隐私的","ex":"there are privacy-preserving techniques"},
 {"en":"lie","pos":"v.","zh":"在于；处于（某位置）","ex":"where a good balance lies"},
],
}

A["p026"] = {
"zh": "主要的实践困难之一，是如何真正执行监管——无论在国家层面，还是在享有主张权的个人层面。他们必须识别出负责任的法律实体，证明相关行为，也许还要证明意图，找到一家宣布自己有管辖权的法院……并最终促使法院真正执行其裁决。消费者权利、产品责任、其他民事责任或知识产权保护等已牢固确立的法律保护，在数字产品中往往付诸阙如，或难以执行。这意味着，具有“数字”背景的公司习惯于把产品直接在消费者身上测试而不必担心承担法律责任，同时却又极力维护自身的知识产权。这种“互联网自由至上主义”有时被认为假定了技术方案会自行解决社会问题（Mozorov 2013）。",
"logic": [
 "指出监管落地的根本实践困难：国家与主张权利的个人都须完成识别责任主体、举证、确立管辖、执行裁决等一连串环节。",
 "指出数字产品中成熟的消费者权利、产品责任、知识产权保护常常缺失或难以执行。",
 "由此揭示“数字”公司免责测试产品、却维护自身知识产权的不对称，并将其命名为“互联网自由至上主义”及其“技术自行解决社会问题”的假定。",
],
"terms": [
 {"en":"product liability","zh":"产品责任","def":"因产品缺陷致人损害而由生产者承担的法律责任；本文指出其在数字产品中常缺失或难执行。"},
 {"en":"intellectual property rights","zh":"知识产权","def":"对创造性成果的法定专有权；本文指出数字公司一面规避责任、一面强力维护知识产权。"},
 {"en":"Internet Libertarianism","zh":"互联网自由至上主义","def":"本文指一种假定技术方案可自行解决社会问题、反对监管干预的立场。"},
],
"background": [],
"vocab": [
 {"en":"enforce","pos":"v.","zh":"执行；强制执行","ex":"to actually enforce regulation"},
 {"en":"competent","pos":"adj.","zh":"有管辖权的；胜任的","ex":"a court that declares itself competent"},
 {"en":"liability","pos":"n.","zh":"法律责任","ex":"without fear of liability"},
 {"en":"be used to","pos":"phr.","zh":"习惯于","ex":"are used to testing their products"},
 {"en":"take care of","pos":"phr.","zh":"处理；解决","ex":"will take care of societal problems"},
],
}

A["p027"] = {
"zh": "监控中AI所引发的伦理问题，超出了单纯的数据积累、数据流控制与注意力引导：它们还包括利用信息去操纵行为——无论在线还是离线。假定选择具有标准的“控制条件”与“认识论条件”，操纵则可以同时利用这两者。人类的行动选择往往远非冷静的理性选择，因此我们拖延以及其他次优行为的倾向，便可能被利用来进行操纵。操纵行为的努力虽与人类文明一样古老（Noggle 2022），但在AI系统手中获得了一种新的性质（Prunkl 2024; Schneider 2025）。杰伦·拉尼尔（Jaron Lanier）早在2014年就写道：“当你身上一直佩戴着传感器——例如智能手机上的GPS与摄像头——并持续不断地把数据输送给一台巨型计算机，而这台计算机属于一家由‘广告商’付费、以便暗中操纵你的公司时……你便逐渐变得不那么自由了。”（Lanier 2014）",
"logic": [
 "把AI监控的伦理问题从数据层面推进到行为层面：利用信息操纵在线与离线行为。",
 "借助选择的“控制条件”与“认识论条件”说明操纵何以可能，并指出人类远离冷静理性、存在拖延等次优倾向可供利用。",
 "指出操纵虽古已有之，但AI使其获得新性质，援引拉尼尔2014年文字收束为“逐渐变得不自由”。",
],
"terms": [
 {"en":"manipulation","zh":"操纵","def":"不通过理性论证而影响他人行为的做法；本文指AI利用人的认知弱点在线上线下左右其行为。"},
 {"en":"autonomy","zh":"自主性","def":"自我决定与独立行动的能力；本文把AI操纵视为对人自主性的威胁。"},
 {"en":"control condition","zh":"控制条件","def":"本文指行动选择中主体对行为的实际控制这一条件；操纵可对其加以利用。"},
],
"background": [
 {"title":"杰伦·拉尼尔（Jaron Lanier）","body":"美国计算机科学家、虚拟现实先驱与科技批评者，2014年即警告：持续佩戴传感器、数据被广告主付费的公司所利用，会使人逐渐丧失自由。"},
],
"vocab": [
 {"en":"go beyond","pos":"phr.","zh":"超出；超越","ex":"go beyond the mere accumulation of data"},
 {"en":"sub-optimal","pos":"adj.","zh":"次优的","ex":"other sub-optimal behaviour"},
 {"en":"procrastination","pos":"n.","zh":"拖延","ex":"our tendencies to procrastination"},
 {"en":"subtly","pos":"adv.","zh":"暗中地；微妙地","ex":"to subtly manipulate you"},
 {"en":"as old as","pos":"phr.","zh":"与……一样古老","ex":"as old as humanity"},
],
}

A["p028"] = {
"zh": "有了充分的先验数据，算法就可以被用来针对个人或小群体，施以恰好可能影响这些特定个体的那种个性化输入。鉴于用户与数据系统之间存在高强度互动，而这又提供了关于个体的深度知识，用户便容易受到正向“助推”（Thaler and Sunstein 2008）、情感操纵，以及负面操纵与欺骗的影响。逐利的企业利用行为偏差、欺骗与成瘾的制造（Costa and Halpern 2019）——例如通过网页或游戏中的“暗黑模式”（dark patterns）（Mathur et al. 2019; Luguri and Strahilevitz 2021; Klenk 2022）。离线赌博与成瘾性物质的销售受到高度监管，而在线操纵与成瘾却并未如此。系统锁定与软件垄断进一步强化了控制。这种丧失控制的一个细节，是人们在同意软件与IT服务的“条款与条件”时，“知情同意”（informed consent）的阙如（Faden and Beauchamp 1986）。当决策被**移交**给一个AI能动者、人类甚至不再需要被操纵时，这个问题便达到了顶点。",
"logic": [
 "说明算法如何凭借先验数据对个体实施高度个性化、精准影响。",
 "列举用户所受操纵的谱系（正向助推、情感操纵、负面操纵、欺骗），并以“暗黑模式”为例说明逐利企业的具体手段。",
 "指出在线操纵与成瘾缺乏对应线下赌博/成瘾性物质的监管，并以系统锁定、软件垄断、知情同意阙如刻画控制的强化。",
 "指出问题顶点：决策移交AI能动者后，人类连被操纵都不再需要。",
],
"terms": [
 {"en":"nudging / nudge","zh":"助推","def":"通过选择架构而非强制引导人的行为；本文指出用户在数字环境中易受此类操纵。"},
 {"en":"informed consent","zh":"知情同意","def":"在充分知情基础上自愿同意；本文指出用户同意服务条款时其实缺乏真正的知情同意。"},
 {"en":"dark patterns","zh":"暗黑模式","def":"网页或应用中刻意误导用户做出不利于己选择的设计；本文列为操纵手段之一。"},
],
"background": [
 {"title":"助推（nudge）","body":"理查德·塞勒（Richard Thaler）与卡斯·桑斯坦（Cass Sunstein）在《助推》（2008）中提出的概念，指通过选择架构在不强制的前提下引导人的行为；本文指其在数字环境中可能沦为操纵。"},
],
"vocab": [
 {"en":"target","pos":"v.","zh":"针对；以……为目标","ex":"algorithms can be used to target individuals"},
 {"en":"vulnerable to","pos":"adj. phr.","zh":"易受……影响的","ex":"they are vulnerable to positive “nudges”"},
 {"en":"lock-in","pos":"n.","zh":"锁定（效应）","ex":"Control is increased by system lock-in"},
 {"en":"culmination","pos":"n.","zh":"顶点；极点","ex":"The culmination of this problem is reached"},
 {"en":"hand over","pos":"phr.","zh":"移交；交给","ex":"decisions are handed over to an AI agent"},
],
}

A["p029"] = {
"zh": "改进了的AI“伪造”技术，使曾经可靠的证据变成了不可靠的证据——这已经发生在数字照片、录音与录像身上……如今，人们已可以相当容易地**凭空制作**（而非篡改）出任何所需内容的“深度伪造”文本、照片与视频素材。通过短信、电话或视频与人进行的复杂实时互动，同样可以被伪造。于是，我们无法再信任数字互动，而与此同时我们又日益依赖这种互动。有人主张，技术操纵对我们过有意义生活的机会构成重大威胁（Nyholm 2022），而且我们据以确立信念与知识的认识论实践的基础（见下一节），也受到这一发展的威胁（Rini 2020; Robert Sparrow and Flenady 2025）。",
"logic": [
 "指出AI伪造技术已使数字照片、录音、录像等原本可靠的证据变得不可靠，且如今可凭空生成任意内容的深度伪造。",
 "指出连实时互动都可被伪造，造成“无法信任却日益依赖数字互动”的两难。",
 "援引两项哲学后果：技术操纵威胁有意义生活的机会，并威胁我们确立信念与知识的认识论实践基础。",
],
"terms": [
 {"en":"deep fake","zh":"深度伪造","def":"利用AI凭空生成或以假乱真的文本、图像或视频内容的技术；本文指其摧毁了数字证据的可靠性。"},
 {"en":"epistemic","zh":"认识论的","def":"与知识及信念之证成相关的；本文指我们据以形成信念与知识的实践基础正受到深度伪造的威胁。"},
],
"background": [],
"vocab": [
 {"en":"reliable","pos":"adj.","zh":"可靠的","ex":"what once was reliable evidence"},
 {"en":"sophisticated","pos":"adj.","zh":"复杂的；精巧的","ex":"Sophisticated real-time interaction"},
 {"en":"dependent on","pos":"adj. phr.","zh":"依赖于","ex":"increasingly dependent on such interaction"},
 {"en":"pose a threat","pos":"phr.","zh":"构成威胁","ex":"poses significant threats to our opportunities"},
 {"en":"meaningful","pos":"adj.","zh":"有意义的","ex":"opportunities to live meaningful lives"},
],
}

# ---------------------------------------------------------------- build
src = json.loads(SRC.read_text(encoding="utf-8"))
out_blocks = []
for b in src["blocks"]:
    nb = dict(b)  # copy every source field verbatim
    if b["kind"] == "heading":
        nb["title_zh"] = HEADINGS[b["id"]]
    else:
        ann = A[b["pid"]]
        for k in ("zh", "logic", "terms", "background", "vocab"):
            nb[k] = ann[k]
    out_blocks.append(nb)

result = {"shard": "a", "blocks": out_blocks}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, "blocks:", len(out_blocks))
