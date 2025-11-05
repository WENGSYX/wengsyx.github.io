---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

My passion lies in the captivating world of natural language processing, where I love delving into its intricacies and uncovering its hidden potential. An explorer at heart, I am captivated by the thrill of investigating novel concepts, while tedious, repetitive engineering tasks hold little allure for me.

My research interest includes constructing Discoverative Intelligence using LLMs. My goal is to develop systems capable of forming falsifiable hypotheses, understanding real-world principles, and continuously refining their cognitive frameworks through interaction and reflection. I have garnered extensive research and engineering internship experience at the Chinese Academy of Sciences and Westlake University. To date, I have published a total of 6 Core A* (CCF-A) and 5 Core B (CCF-B) papers as either co-first author or last author, which have been published at AI conferences including the TPAMI, ICLR, ACL, EMNLP, and ICASSP, with total google scholar <a href='https://scholar.google.com/citations?user=O1XsDEMAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>. I was also invited to serve as an Area Chair for ICLR 2025.


# 🔥 News
- *2025.05*: &nbsp;🎉🎉 **DeepReview** have accept in ACL 2025!
- *2025.04*: &nbsp;🎉🎉 We organized a two-hour [discussion session](https://ai-researcher.net/social-iclr-2025) at ICLR 2025: **AI Co-scientist Discussion**
- *2025.01*: &nbsp;🎉🎉 Both **CycleResearcher** and **Personality Alignment** have accept in ICLR 2025!
- *2024.01*: &nbsp;🎉🎉 **Neural Comprehension** has accept in ICLR 2024 Poster!
- *2023.08*: &nbsp;🎉🎉 We've released **LMTuner**, a groundbreaking system where anyone can train large models in just 5 minutes!
- *2023.04*: &nbsp;🎉🎉 We've created **Neural Comprehension** - a breakthrough enabling LLMs to master symbolic operations! 

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2025 main</div><img src='images/deepreview.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[DeepReview: Improving LLM-based Paper Review with Human-like Deep Thinking Process](https://arxiv.org/abs/2503.08569)

 Minjun Zhu, **Yixuan Weng**, Linyi Yang , Yue Zhang

[**HomePage**](https://wengsyx.github.io/Researcher/) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
[**Project**](https://github.com/zhu-minjun/Researcher) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- By introducing mechanisms that simulate human thought processes and automatically retrieve literature, we trained a 14B DeepReviewer model, the first peer review system to reach human reviewer quality.
  
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025 Poster</div><img src='images/cycleresearcher.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[CycleResearcher: Improving Automated Research via Automated Review](https://openreview.net/pdf?id=bjcsVLoHYs)

**Yixuan Weng**, Minjun Zhu, Guangsheng Bao, Hongbo Zhang, Jindong Wang , Yue Zhang, Linyi Yang

[**HomePage**](https://wengsyx.github.io/Researcher/) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
[**Project**](https://github.com/zhu-minjun/Researcher) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- The first exploration of how large language models can act as scientists to make scientific discoveries in machine learning through large-scale training and reinforcement learning, generating ideas, experiments, and results that remain effective even in the real world.
  
[**OpenReview**](https://openreview.net/forum?id=bjcsVLoHYs) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025 Poster</div><img src='images/palign.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Personality Alignment of Large Language Models](https://openreview.net/pdf?id=0DZEs8NpUH)

Minjun Zhu, **Yixuan Weng**,  Linyi Yang, Yue Zhang

[**Project**](https://github.com/zhu-minjun/PAlign) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Studies how language models can better match individual users' preferences and behaviors from two personality perspectives - the positive Big Five personality traits and the negative Dark Triad traits.
  
[**OpenReview**](https://openreview.net/forum?id=0DZEs8NpUH) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2024 Poster</div><img src='images/NeuralCom.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Mastering Symbolic Operations: Augmenting Language Models with Compiled Neural Networks](https://arxiv.org/abs/2304.01665)

**Yixuan Weng**, Minjun Zhu, Fei Xia, Bin Li, Shizhu He, Kang Liu, Jun Zhao

[**Project**](https://github.com/WENGSYX/Neural-Comprehension) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- We have enabled language models to more fundamental comprehension of the concepts, to achieve completely absolute accuracy in symbolic reasoning without additional tools.
  
[**OpenReview**](https://openreview.net/forum?id=9nsNyN0vox) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2023 Findings</div><img src='images/SelfVer.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Large Language Models are Better Reasoners with Self-Verification](https://arxiv.org/abs/2212.09561)

**Yixuan Weng**, Minjun Zhu, Fei Xia, Bin Li, Shizhu He, Shengping Liu, Bin Sun, Kang Liu, Jun Zhao

[**Project**](https://github.com/WENGSYX/Self-Verification) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- We have demonstrated that language models have the capability for self-verification, and can further improve their own reasoning abilities.

[**Demo Video**](https://www.bilibili.com/video/BV1as4y1F74k/) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

</div>
</div>






<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TPAMI</div><img src='images/VPTSL.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Visual Answer Localization with Cross-Modal Mutual Knowledge Transfer](https://ieeexplore.ieee.org/abstract/document/10095026)

Shutao Li, Bin Li, Bin Sun, **Yixuan Weng**

[**Project**](https://github.com/WENGSYX/VPTSL) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- We design the text span-based predictor, where the input text question, video subtitles, and visual prompt features are jointly learned with the pre-trained language model for enhancing the joint semantic representations.
- 
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICASSP 2023 Oral</div><img src='images/MutualSL.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Visual Answer Localization with Cross-Modal Mutual Knowledge Transfer](https://ieeexplore.ieee.org/abstract/document/10095026)

**Yixuan Weng**, Bin Li

[**Project**](https://github.com/WENGSYX/MutualSL) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- We introduce a cross-modal mutual knowledge transfer approach for localizing visual answers in images and videos.

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">COLING 2024 Poster</div><img src='images/reasongraphqa.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Towards Graph-hop Retrieval and Reasoning in Complex Question Answering over Textual Database](https://arxiv.org/abs/2305.14211)

Minjun Zhu, **Yixuan Weng**, Shizhu He, Kang Liu, Haifeng Liu, Yang Jun, Jun Zhao

**Project** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- We propose to conduct Graph-Hop - a novel multi-chains and multi-hops retrieval and reasoning paradigm in complex question answering. We construct a new benchmark called ReasonGraphQA, which provides explicit and fine-grained evidence graphs for complex question to support comprehensive and detailed reasoning. 
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICASSP 2023 Poster</div><img src='images/CCGS.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Learning To Locate Visual Answer In Video Corpus Using Question](https://ieeexplore.ieee.org/abstract/document/10096391)

Bin Li, **Yixuan Weng**, Bin Sun, Shutao Li

[**Project**](https://github.com/WENGSYX/CCGS) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- We propose a novel approach to locate visual answers in a video corpus using a question.

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICASSP 2023 Poster</div><img src='images/ChainPath.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Learning to Build Reasoning Chains by Reliable Path Retrieval](https://ieeexplore.ieee.org/abstract/document/10097146)

Minjun Zhu, **Yixuan Weng**, Shizhu He, Cunguang Wang, Kang Liu, Li Cai, Jun Zhao

**Project** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- We propose ReliAble Path-retrieval (RAP) for complex QA over knowledge graphs, which iteratively retrieves multi-hop reasoning chains. It models chains comprehensively and introduces losses from two views. Experiments show state-of-the-art performance on evidence retrieval and QA. Additional results demonstrate the importance of modeling sequence information for evidence chains.

</div>
</div>




<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EACL 2023 Poster</div><img src='images/ATTEMPT.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Find Parent then Label Children: A Two-stage Taxonomy Completion Method with Pre-trained Language Model](https://aclanthology.org/2023.eacl-main.73/)

Fei Xia, **Yixuan Weng**, Shizhu He, Kang Liu, Jun Zhao

[**Project**](https://github.com/WENGSYX/ATTEMPT) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Proposed two-stage ATTEMPT method for taxonomy completion. Inserts new concepts by finding parent and labeling children. Combines local nodes with prompts for natural sentences. Utilizes pre-trained language models for hypernym/hyponym recognition. Outperforms existing methods on taxonomy completion and extension tasks.

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2022 Demo</div><img src='images/LingYi.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MedConQA: Medical Conversational Question Answering System based on Knowledge Graphs](https://aclanthology.org/2022.emnlp-demos.15/)

Fei Xia, Bin Li, **Yixuan Weng**, Shizhu He, Kang Liu, Bin Sun, Shutao Li, Jun Zhao

[**Project**](https://github.com/WENGSYX/LingYi) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- We propose MedConQA, a medical conversational QA system using knowledge graphs, to address weak scalability, insufficient knowledge, and poor controllability in existing systems. It is a pipeline framework with open-sourced modular tools for flexibility. We construct a Chinese Medical Knowledge Graph and a Chinese Medical CQA dataset to enable knowledge-grounded dialogues. We also use SoTA techniques to keep responses controllable, as validated through professional evaluations. Code, data, and tools are open-sourced to advance research.

[**Demo Video**](https://www.bilibili.com/video/BV1BP4y177r8/) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv</div><img src='images/controllm.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ControlLM: Crafting Diverse Personalities for Language Models](https://arxiv.org/abs/2402.10151)

**Yixuan Weng**, Shizhu He, Kang Liu, Shengping Liu, Jun Zhao

[**Project**](https://github.com/wengsyx/ControlLM) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- We have enabled to control the personality traits and behaviors of language models in real-time at inference without costly training interventions.

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NLPCC 2024</div><img src='images/HoT.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Large Language Models Need Holistically Thought in Medical Conversational QA](https://arxiv.org/abs/2305.05410)

**Yixuan Weng**, Bin Li, Fei Xia, Minjun Zhu, Bin Sun, Shizhu He, Kang Liu, Jun Zhao

[**Project**](https://github.com/WENGSYX/HoT) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- We propose a holistic thinking approach for improving the performance of large language models in both Chinese and English medical conversational QA task.

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv</div><img src='images/LMTuner.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[LMTuner: An user-friendly and highly-integrable Training Framework for fine-tuning Large Language Models](https://arxiv.org/abs/2308.10252)

**Yixuan Weng**, Zhiqi Wang, Huanxuan Liao, Shizhu He, Shengping Liu, Kang Liu, Jun Zhao

[**Project**](https://github.com/WENGSYX/LMTuner) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- We advocate that LMTuner's usability and integrality alleviate the complexities in training large language models. Remarkably, even a novice user could commence training large language models within five minutes. Furthermore, it integrates DeepSpeed frameworks and supports Efficient Fine-Tuning methodologies like Low Rank Adaptation (LoRA), Quantized LoRA (QLoRA), etc.,

[**Demo Video**](https://www.bilibili.com/video/BV1iN411a7fJ) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
[**Homepage**](https://wengsyx.github.io/LMTuner) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

# 🎖 Honors and Awards
- *2022.05* BioNLP-2022:   Medical Video Classification, **First Place**
- *2022.04* CBLUE **First Place**
- *2022.01* SemEval22-Task3 PreTENS, **First Place**
- *2021.11* SDU@AAAI-22:  Acronym Disambiguation, **First Place**

