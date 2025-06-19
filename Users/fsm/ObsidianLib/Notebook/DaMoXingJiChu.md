# 1.语言模型基础

## 1. RNN

## 2.Transformer

1. [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=18&annotation=undefined) “相较于 RNN 模型串行的循环迭代模式,Transformer 并行输入的特性,使其容 易进行并行计算。” ([“大模型基础”, p. 18](zotero://select/library/items/SCHBS2IK))

2. [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=18&annotation=undefined) “但是,Transformer 并行输入的范式也导致网络模型的规模随输 入序列长度的增长而平方次增长。这为应用 Transformer 处理长序列带来挑战。” ([“大模型基础”, p. 18](zotero://select/library/items/SCHBS2IK))

### 2.1 Transformer基础

- Encoder

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=16&annotation=undefined) “Encoder 部分由六个级联的 encoder layer 组成,每个 encoder layer 包含一个注意力模块和一个全连接前馈模块” ([“大模型基础”, p. 16](zotero://select/library/items/SCHBS2IK))

- Decoder

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=16&annotation=undefined) “Decoder 部分由六个级联的 decoder layer 组成,每个 decoder layer 包含两个注意力模块和一个全连接前馈模块。 其中,第一个注意力模块为自注意力模块,第二个注意力模块为交叉注意力模块” ([“大模型基础”, p. 16](zotero://select/library/items/SCHBS2IK))

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=16&annotation=undefined) “Decoder 交叉注意力模块的输入分别是自注意力模块的输出(query) 和最后一个 encoder layer 的输出(key,value)。” ([“大模型基础”, p. 16](zotero://select/library/items/SCHBS2IK))

### 2.2 基于Transformer的语言模型

2.2.1 训练流程 ([“大模型基础”, page 17](zotero://select/library/items/SCHBS2IK))

p17

2.2.2 自回归 ([“大模型基础”, page 18](zotero://select/library/items/SCHBS2IK))

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=18&annotation=undefined) “在自回 归中,第一轮,我们首先将第一个词输入给 Transformer 语言模型,经过解码,得 到一个输出词。然后,我们将第一轮输出的词与第一轮输入的词拼接,作为第二轮 的输入,然后解码得到第二轮的输出。接着,将第二轮的输出和输入拼接,作为第 三轮的输入,以此类推。每次将本轮预测到的词拼接到本轮的输入上,输入给语言 模型,完成下一轮预测。在循环迭代的“自回归”过程中,我们不断生成新的词, 这些词便构成了一段文本。” ([“大模型基础”, p. 18](zotero://select/library/items/SCHBS2IK))

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=18&annotation=undefined) ““Teacher Forcing”” ([“大模型基础”, p. 18](zotero://select/library/items/SCHBS2IK))

## 3. 语言模型的采样方法 ([“大模型基础”, p. 18](zotero://select/library/items/SCHBS2IK))

将语言模型输出的向量解码为文本的过程被成为**语言模型解码**。解码过程显著影响着 生成文本的质量。 ([“大模型基础”, p. 18](zotero://select/library/items/SCHBS2IK))

### 3.1  概率最大化方法([“大模型基础”, page 19](zotero://select/library/items/SCHBS2IK))

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=19&annotation=undefined) “现有概率最大化方法通 常采用启发式搜索方法。” ([“大模型基础”, p. 19](zotero://select/library/items/SCHBS2IK))

1. **贪心搜索（Greedy Search）**
    
    贪心搜索在在每轮预测中都选择概率最大的词，当前概率大的词有可能导致后续 的词概率都很小。容易陷入局部最优，难以得到最优解。
    
2. **波束搜索（Beam Search）**

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=19&annotation=undefined) “波束搜索在每轮预测中都先保留 b 个可能性最高的词” ([“大模型基础”, p. 19](zotero://select/library/items/SCHBS2IK))

“在结束搜索时,得到 M 个集合,找出最优组合使得联合概率最大” ([“大模型基础”, p. 20](zotero://select/library/items/SCHBS2IK))

概率最大的文本通常是最为常见的文本,会生成缺乏多样性的废话文学。在解码过程中加入一些随机元素。这样的话就可以 解码到一些不常见的组合,从而使得生成的文本更具创意,更适合开放式文本任 务。

### 3.2 随机采样方法

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=21&annotation=undefined) “为了增加生成文本的多样性,随机采样的方法在预测时增加了随机性。” ([“大模型基础”, p. 21](zotero://select/library/items/SCHBS2IK))

1. Top-K采样
    
    Top-K 采样在每轮预测中都选取 K 个概率最高的词作为本轮的候选词集合,然后对这些词的概率用 softmax 函数进行归一化,得到如下分布函数p(x)。
    
          将候选集设置为固定的大小 K 将导致上述分布在不同轮次的预测中存在很大差异。
    
    - 当候选词的分布的方差较大的时候,可能会导致本轮预测选到概率较小、不符合常理的词,从而产生“胡言乱语“。
    - 而当候选词的分布的方差较小的时候,甚至趋于均匀分布时,固定尺寸的候选集中无法容纳更多的具有相近概 率的词,导致候选集不够丰富,从而导致所选词缺乏新颖性而产生“枯燥无趣”的文本。
    
2. Top-P采样([“大模型基础”, page 22](zotero://select/library/items/SCHBS2IK))
    
    为了解决固定候选集所带来的问题,Top-P 采样(即 Nucleus 采样)被提出 [9]。 其设定阈值 p 来对候选集进行选取。其候选集可表示为$S_p$
    
    应用阈值作为候选集选取的标准之后,Top-P 采样可以避免选到概率较小、不 符合常理的词,从而减少“胡言乱语”。 ([“大模型基础”, p. 22](zotero://select/library/items/SCHBS2IK))
    
3. Temperature机制
    
    不同的应用场景对随机性的要求不一样，所以引入了Temperature机制。该机制可以对解码随机性进行调节。[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=23&annotation=undefined) “Temperature 机制通过对 Softmax 函数中的自变量进行尺度变换,然后利用 Softmax 函数的非线性实现对分布的控 制。” ([“大模型基础”, p. 23](zotero://select/library/items/SCHBS2IK))
    

## 4. 语言模型的评测

### 4.1 内在评测（Intrinsic Evaluation）([“大模型基础”, page 24](zotero://select/library/items/SCHBS2IK))

不依赖具体任务,直接通过语言模型的输出来评测模型的生成能力。

评估指标，困惑度（Perplexity）如下：

等价形式见原文。([“大模型基础”, page 24](zotero://select/library/items/SCHBS2IK))

如果语言模型对测试文本越“肯定”(即生成测试文本的概 率越高),则困惑度的值越小。而语言模型对测试文本越“不确定”(即生成测试文 本的概率越低),则困惑度的值越大。

### 4.2 外在评测 (Extrinsic Evaluation) ([“大模型基础”, page 25](zotero://select/library/items/SCHBS2IK))

通过某些**具体任务**,如机器翻译、摘要生成等,来评测语言模型处理这些具体生成任务的能力。

1. **基于统计指标的评测**([“大模型基础”, page 25](zotero://select/library/items/SCHBS2IK))
    
    **BLEU**(BiLingual Evaluation Understudy)和 **ROUGE**(Recall-Oriented Understudy for Gisting Evaluation)是应用 最为广泛的两种统计指标。其中,BLEU 是精度导向的指标,而 ROUGE 是召回导 向的指标。
    
    - **BLEU：**机器翻译(Machine Translation, MT)任务
        
        在词级别上计算生成的翻译与参考翻译间的重合程度。BLEU计算多层次 n-gram 精度的几何平均。
        
        公式见原文
        
    
    - **Rouge ：**[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=26&annotation=undefined) “摘要生成(Summarization)任务”
        
        基于统计指标的评测方法通过对语言模型生成的答案和标准答案间的重叠程 度进行评分。
        
    
2. 基于语言模型的评测([“大模型基础”, page 27](zotero://select/library/items/SCHBS2IK))
    
    上述评分无法完全适应生成任务中表达的多样性,与人类的评测相差甚远,尤其是在生成的样本具有较强的创造性和多样性的时候。为解决此问题, 可以在评测中引入一个其他语言模型作为“裁判”,利用此“裁判”在预训练阶段 掌握的能力对生成的文本进行评测。
    
    - 基于上下文词嵌入的评测方法
        
        BERTScore 在 BERT 的上下文词嵌入向量的基础上,计算生成文本 sgen 和参 考文本 sref 间的相似度来对生成样本进行评测。
        
        相较于统计评测指标,BERTScore 更接近人类评测结果。但是,BERTScore 依 赖于人类给出的参考文本。
        
    
    - 基于生成模型的评测方法
        
        G-EVAL 利用 GPT-4 在没有参考文本的情况下对生 成文本进行评分。G-EVAL 通过提示工程(Prompt Engineering)引导 GPT-4 输出评 测分数。
        
        G-EVAL 的 Prompt 分为三部分:(1) 任务描述与评分标准;(2) 评 测步骤;(3) 输入文本与生成的文本。([“大模型基础”, page 28](zotero://select/library/items/SCHBS2IK))。直接将 GPT-4 给出 的得分作为评分会出现区分度不够的问题,因此,G-EVAL 还引入了对所有可能得 分进行加权平均的机制来进行改进。
        

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=28&annotation=undefined) “”

# 2.6 非Transformer架构

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=82&annotation=undefined) “Transformer并行输入的机制会导致模型 规模随输入序列长度平方增长,导致其在处理长序列时面临计算瓶颈。”

## 2.6.1 状态空间模型SSM

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=83&annotation=undefined) “可以有效处理长文本中存在的长程依赖性(Long-Range Dependencies, LRDs)问题,并且可以有效降低语言 模型的计算和内存开销。”

#### **2.6.1.1 SSM**

SSM思想源于控制理论中的动力系统。[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=83&annotation=undefined) “其通过利用一组状态变量来捕捉 系统状态随时间的连续变化,这种连续时间的表示方法天然地适用于描述长时间 范围内的依赖关系。”

优点：[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=83&annotation=undefined) “SSM 还具有递归和卷积的离散化表示形式, 所以既能在推理时通过递归更新高效处理序列数据,又能在训练时通过卷积操作捕捉全局依赖关系。”

SSM系统方程如下：

$$x'(t)=Ax(t)+Bu(t) \tag{1.1}$$

$$

y(t)=Cx(t)+Du(t)\tag{1.2}
$$

其中，

- $ x'(t)=Ax(t)+Bu(t) $ 为状态方程，描述了系统状态如何基于输入和前一个状态变化，其计算结果是状态关于时间的导数 $ x'(t) $,为了得到状态 $ x(t) $ ,还需要对其进行积分操作。
- $ y(t)=Cx(t)+Du(t)$为输出方程，描述了系统状态如何转化为输出，其中的 $x(t)$ 是通过状态方程更新且积分后的值。
- $Du(t)$ 表示残差连接，可忽略。

离散化(Discretization)是SSM中最为关键的步骤，能够将系统方程从连续形式转换为递归形式和卷积形式。

使用梯形法代替连续形式中的积分操作。其将定义在特定区间上的函数曲线下的区域视为梯形，并利用梯形面积公式计算其面积。

离散化后递归形式的系统方程如下：

$$x_{k}=\overline{\mathbf{A}} x_{k-1}+\overline{\mathbf{B}} u_{k} \tag{1.3}$$

$$y_k = \overline{\mathbf{C}} x_{k} \tag{1.4}$$

上述方程中，状态方程由前一步的状态和当前输入计算当前状态，体现了递归的思想。其中，$\overline{\mathbf{A}}, \overline{\mathbf{B}}, \overline{\mathbf{C}}$ 为离散形式下的矩阵，其与连续形式下的矩阵 $ \mathbf{A},\mathbf{B},\mathbf{C} $ 的关系分别为：

$\overline{\mathbf{A}}=\left(\mathbf{I}-\frac{\Delta}{2} \mathbf{A}\right)^{-1}\left(\mathbf{I}+\frac{\Delta}{2} \mathbf{A}\right), \overline{\mathbf{B}}=\left(\mathbf{I}-\frac{\Delta}{2} \mathbf{A}\right)^{-1} \Delta \mathbf{B}, \overline{\mathbf{C}}=\mathbf{C}$ 其中 $\Delta = t_{n+1}-t_n$。

将系统方程的递归形式进行迭代，可以得到卷积形式。迭代后的 $x_k$和$y_k$ 的结果：

？？？没看懂

#### **和2.6.1.2 RWKW**

#### **2.6.1.3 Mamba**

## 2.6.2 测试时训练TTT

# 2.大语言模型架构

大数据+大模型——>新智能

## 2.1 大数据+大模型

### 2.1.1 模型规模探究

1. OpenAI 的Kaplan-McCandlish 扩展法则([“大模型基础”, page 36](zotero://select/library/items/SCHBS2IK))
    
    模型的性能与模型以及数据规模这两个因素均高度正相关。然而,在模型规模相同的情况下,模型的具体架构对其性能的影响相对较小。因此,扩大模型规模和丰富数据集成为了提升大型模型性能的两个关键策略。
    
    模型规模的增长速度应该略快于数据规模的增长速度。
    
2. DeepMind 的Chinchilla 扩展法则
    
    数据集量 D 与 模型规模 N 几乎同等重要,如果总计算预算增加了 10 倍,那么模型规模以及数据 规模都应当扩大约 3.16 倍。
    
    Chinchilla 扩展法则进一步提出,理想的数据集大小应当是模型规模的 20 倍。例如,对于一个 7B(70 亿参数)的模型,最理想的训练数据集大小应为 140B(1400 亿)个 Token。
    
    不再单纯追求模型规模的增 加,而是优化模型规模与数据规模的比例。
    

### 2.1.2 大语言模型的涌现能力(Emergent Abilities)([“大模型基础”, page 38](zotero://select/library/items/SCHBS2IK))

并非通过在特定下游任务上通过训练获得,而是随着模型复杂度的提升凭空自然涌现的能力称为大模型的涌现能力。

1. 上下文学习
2. 常识推理
3. 代码生成
4. 逻辑推理

## 2.2 大语言模型架构

Transformer框架的问世代表着一个划时代的转折点。其独特的自注意力(Self-Attention)机制极大地提升了模型对序列数据的 处理能力,在捕捉长距离依赖关系方面表现尤为出色。此外,Transformer 框架对 并行计算的支持极大地加速了模型的训练过程。

### 2.2.1 主流模型架构

1. Encoder-only([“大模型基础”, page 41](zotero://select/library/items/SCHBS2IK))
    
    - 输入编码：
        
        原始输入文本会被分词器(Tokenizer)拆解为 Token 序列, 随后通过词表和词嵌入(Embedding)矩阵映射为向量序列,确保文本信息得以数字化表达。接着为了保留文本中单 词的顺序信息,每个向量序列会被赋予位置编码(Positional Encoding)
        
    - 特征编码
        
        先前得到的向量序列会依次通过一系列编码模块,这些模块通过自注意力机制和前馈网络进一步提取和深化文本特征。
        
    - 任务处理
        
        在预训练阶段,模型通常使用全连接层作为输出头, 用于完成掩码预测等任务。而在下游任务适配阶段,输出头会根据具体任务需求 进行定制。
        
2. Encoder-Decoder([“大模型基础”, page 42](zotero://select/library/items/SCHBS2IK))
    
    解码器包括如下三个部分：
    
    - 输出编码
    - 特征编码
    - 输出生成
    
    **训练流程：**
    
    1）编码为向量序列，2）特征编码模块转化为上下文表示，3）输入GT，标记start，并行输入特征解码模块。4）？使用Teacher Foring，将GT中的已知部分作为输入，并结合从最后一个编码块得到的上下文信息预测下一个Token。5）计算损失，反向传播。
    
    **推理流程：**每轮的输入依赖于上一轮的采样结果,因此只能一步步地串行输出。
    
3. Decoder-only
    
    Decoder-only 架构的核心 特点在于省略了每个编码模块中的交叉注意力子模块,这也是其与传统 EncoderDecoder 架构中解码器部分的主要区别。
    

### 2.2.2 模型架构的功能对比

1. 注意力矩阵([“大模型基础”, page 45](zotero://select/library/items/SCHBS2IK))
    
    1）**双向注意力机制**是完全的注意力机制，模型能够同时利用前后文信息,深入理解复杂的语义联系和上下文依赖。
    
    2）Encoder-Decoder中的**掩码自注意力**呈现下三角注意力确保在生成当 前 Token 时,模型只关注之前生成的 Token。
    
    3）**交叉注意力机制**允许解码器始终能够动态地参考编码器生成的完整上下文表示,确保输出与输入序列高度相关且连贯。
    
    4）Decoder-only中的**掩码自注意力**呈现出“下三角”的注意力模式。这意味着在预测当前 Token 时,模型只能依赖于已经生成的历史 Token 信息,体现了**单向注意力机制**。
    
2. 适用任务([“大模型基础”, page 46](zotero://select/library/items/SCHBS2IK))

## 2.3 基于Encoder-only架构的大语言模型

### 2.3.1 Encoder-only架构

1. 在处理输入序列时,**双向编码模型**融合了从左往右的正向 注意力以及从右往左的反向注意力,能够充分捕捉每个 Token 的上下文信息,因 此也被称为具有全面的注意力机制。
2. 双向编码器为每个词生成动**态的上下文嵌入(Contextual Embedding)**,这种嵌入依赖于输入序列的具体上下文,使得模型能够更加精准地理解词 与词之间的依赖性和语义信息,有效处理词语的多义性问题。

### 2.3.2 BERT语言模型

BERT 模型的结构与 Transformer 中的编码器几乎一致，

1. 预训练
    
    1）基于给定原始样本构造多个样本序列，每个样本序列由原始文本中的两个句子组成，这两个句子有 50% 的概率是来自原文的连续句子, 另外 50% 的概率是随机挑选的两个句子。
    
    2）分词，在序列的开头添加特殊标签 [CLS],在每个句子的结尾添加特殊标签 [SEP]。其 中 [CLS] 标签用于聚合整个序列的信息,而 [SEP] 标签则明确句子之间的界限。
    
    3）下文预测，利用模型判断样本序列中 的两个句子是否为连续的。这一任务训练 BERT 识别和理解句子之间的关系,捕捉 句子层面的语义特征。
    
    4）完形填空，BERT 随机选择样本序列中大约 15% 的 Token 进行遮掩,将其替换为特 殊标签 [MASK] 或者随机单词。模型需要预测这些被替换的 Token 的原始内容。
    
    3）和4）的结合,使 BERT 在理解语言的深度和广度上都有显 著提升。BERT 不仅能够捕捉到 Token 的细粒度特征,还能够把握长距离的依赖关 系和句子间的复杂联系,为各种下游任务提供了坚实的语言理解基础。
    
2. BERT的下游任务
    
    **[CLS] 标签**来提取整个输入序列的聚合表示。[CLS] 标签是专门为分类和汇总任务设计的特殊标记。其全称是 “Classification Token”,即分类标记。通过注意力机制,[CLS] 标签汇总整个输入序 列的信息,生成一个固定长度的向量表示,从而实现对所有 Token 序列信息的概 括,便于处理各种下游任务。
    
    1. **文本分类任务**中,可以将输出中 [CLS] 标签对应的向量提取出来,传递给 一个全连接层,从而用于分类。
    2. **问答系统任务**中,需要输入问题以及一段相关的文本,即“[CLS] 问题 [SEP] 文 本 [SEP]”。最终同样提取出 [CLS] 标签的对应向量,并传递给两个全连接层,用 于判断答案是否存在于相关文本中。如果存在,这两个全连接层分别用于输出答 案的起始和结束位置。
    3. **语义相似度任务**，计算两段或者多段文本之间的语义相似度。可以通过构造“[CLS] 文本 1[SEP] 文本 2[SEP]”的方式,结合一个 线性层来直接输出两个文本之间的相似度;也可以不添加额外的组件,直接提取 [CLS] 标签对应的向量,再利用额外的相似度度量方法(例如余弦相似度)来计算 多段文本之间的相似度。

### 2.2.3 BERT衍生语言模型

1. RoBERTa
    
    - [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=54&annotation=SCBVDYNC) “总数据量达到约 160GB”
    - [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=54&annotation=undefined) “RoBERTa 移除了 BERT 中的下文预测任务,并将 BERT 原生的静态掩码语言建模任务更改为**动态掩码语言建模**。”
2. ALBERT
    
    - [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=55&annotation=undefined) “轻量 级 BERT 模型,旨在通过参数共享和嵌入分解技术来减少模型的参数量和内存占 用,从而提高训练和推理效率。”
    - [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=55&annotation=undefined) “ALBERT 通过参数因子分解以及跨层参数共享,在相同的模型架构下,显著 减少了模型的参数量。”
    - **参数因子分解**
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=55&annotation=undefined) “ALBERT 将 Embedding 层的矩阵先进行分解,将词表对应的独热 编码向量通过一个低维的投影层下投影至维度 E,再将其上投影回隐藏状态的维 度 H。”
        
    - **跨层参数共享**
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=56&annotation=undefined) “只学习第一层编码模块的参数,并将其直接共享给其他所有 层。”[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=56&annotation=undefined) “牺牲了模型性能,但显著提升了参数存储空间的压缩比, 从而实现了更高效的资源利用。”
        
    - **预训练**
        
        - [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=56&annotation=undefined) “与 BERT 完全一致的数据集”约15G
        - 1）掩码语言建模
        - 2）将下文预测替换为句序预测
            
            [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=56&annotation=undefined) “ALBERT 从文本中 选择连续的两个句子,将这两个句子直接拼接起来,或是先将这两个句子的顺序”[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=57&annotation=undefined) “翻转后再进行拼接,并将拼接后的内容作为输入样本,而模型需要预测该样本中 的两个句子是正序还是反序。”
            
3. ELECTRA模型
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=57&annotation=undefined) “旨在解决大规模预训练语言模型中的效率和可扩展性问题。通 过使用生成器-判别器构,ELECTRA 能够更高效地利用预训练数据,提高了模 型在下游任务中的表现。”
    
    - 预训练
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=57&annotation=undefined) “ELECTRA 在 BERT 原有的掩码语言建模基础上结合了生成 对抗网络(Generative Adversarial Network, GAN)的思想,采用了一种生成器-判别器结构。”[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=57&annotation=undefined) “判别器(Discriminator)则使用替换词检测(Replaced Token Detection, RTD)预训练任务,负责检测生成器输出的内容中的每个 Token 是否是 原文中的内容。”
        

## 2.4 基于Encoder-Decoder架构的大语言模型

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=59&annotation=undefined) “Encoder-Decoder 架构在 Encoder-only 架构的基础上引入 Decoder 组件,以完成 机器翻译等序列到序列(Sequence to Sequence, Seq2Seq)任务。”

### 2.4.1 Encoder-Decoder架构

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=61&annotation=undefined) “通过自注意力和交叉注意力机制的结合,Encoder-Decoder 架构能够高效地编码输入信息并生成高质量的输出序列。”

### 2.4.2 T5（Text-to-Text Transfer Transformer）语言模型

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=61&annotation=undefined) “采用了统一的文本到文本的转换范式来处理多种任务”

1. 模型结构
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=61&annotation=undefined) “T5 模型的核心思想是将多种 NLP 任务统一到一个文本转文本的生成式框架 中。在此统一框架下,T5 通过不同的输入前缀来指示模型执行不同任务,然后生 成相应的任务输出”[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=62&annotation=undefined) “通过构造合理的输入前缀,T5 模型能够引导自身针对特定任务进行优 化,而无需对模型架构进行根本性的改变”
    
2. 预训练
    
    - 数据量[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=63&annotation=undefined) “总规模达到了约 750GB。”
    
    - [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=63&annotation=undefined) “Span Corruption 的预训练任务”
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=63&annotation=undefined) “这一预训练任 务从原始输入中选择 15% 的 Token 进行破坏,每次都选择连续三个 Token 作为一 个小段(span)整体被掩码成 [MASK]。与 BERT 模型中采用的单个 Token 预测不 同,T5 模型需要对整个被遮挡的连续文本片段进行预测。这些片段可能包括连续 的短语或子句,它们在自然语言中构成了具有完整意义的语义单元”
        
3. 下游任务
    
    “T5 模型可以在完全零样本(Zero-Shot)的情况下,利用 Prompt 工程技术直接适配 到多种下游任务。
    

### 2.4.3 BART语言模型

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=64&annotation=undefined) “BART 旨在通过多样化的预训练任务来提升模型在文 本生成任务和文本理解任务上的表现。”

1. 模型结构
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=64&annotation=undefined) “模型结构同样与原始的 Transformer 架构完全相同”
    
2. 预训练
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=64&annotation=undefined) “总数据量达到约 160GB。”
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=64&annotation=undefined) “在预训练任务上,BART 以重建被破坏的文本为目标”
    

## 2.5 基于Decoder-only架构的大语言模型

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=66&annotation=undefined) “在开放式(Open-Ended)生成任务中,通常输入序列较为简单,甚至没有具 体明确的输入,因此维持一个完整的编码器来处理这些输入并不是必要的。”

### 2.5.1 Decoder-only架构

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=67&annotation=undefined) “它通过自回归方法逐字生成文本,不仅保持了长文本的连贯性和内在一致性, 而且在缺乏明确输入或者复杂输入的情况下,能够更自然、流畅地生成文本。”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=67&annotation=undefined) “由于去除了编码器部分,使得模型更加轻量化,从而加快了 训练和推理的速度。”

### 2.5.2 GPT系列

1. GPT-1
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=68&annotation=undefined) “GPT-1 开创了 Decoder-only 架 构下,通过下一词预测解决无监督文本生成的先河,为自然语言处理领域带来了 革命性的影响。”
    
    1）模型结构：
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=68&annotation=undefined) “在模型架构方面,GPT-1 使用了 Transformer 架构中的 Decoder 部分,省略了 Encoder 部分以及交叉注意力模块。”
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=69&annotation=undefined) “从图中可以看出,GPT-1 在 结构上与 BERT-Base 高度类似,两者都包含 12 个编码或解码模块,每个模块也 同样由一个自注意力模块和一个全连接前馈模块组成。两者之间的本质区别在于 BERT-Base 中的自注意力模块是双向的自注意力机制,而 GPT-1 中的自注意力模 块则是带有掩码的单向自注意力机制。”
    
    2）预训练
    
    数据：5G。
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=69&annotation=undefined) “GPT-1 采用**下一词预测任务**,即 基于给定的上文预测下一个可能出现的 Token。以自回归的方法不断完成下一词预 测任务,模型可以有效地完成文本生成任务,”[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=69&annotation=undefined) “通过这种预训练策略, 模型可以在不需要人为构造大量带标签数据的前提下,学习到大量语言的“常识”, 学会生成连贯且上下文相关的文本。这不仅提高了模型的泛化能力,而且减少了 对标注数据的依赖,”
    
    3）下游任务
    
2. GPT-2
    
    1）模型结构
    
    总参数量达到15亿
    
    2）预训练
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=71&annotation=undefined) “采用了全新的 WebText 数据集,该数据集由 40GB 经过精心筛选和”[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=72&annotation=undefined) “清洗的网络文本组成。”
    
    3）下游任务
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=72&annotation=undefined) “在某些任务上可以不进行微调,直接进行 零样本学习。”
    
3. GPT-3
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=72&annotation=undefined) “GPT-3 在模型规模和预训练语料上进一步提升,并涌现 出了优良的上下文学习(In-Context Learning, ICL)能力。在上下文学习能力的加 持下,GPT-3 可以在不进行微调的情况下,仅通过任务描述或少量示例即可完成多 样化的下游任务。”
    
    1）模型结构
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=72&annotation=undefined) “在模型架构上,GPT-3 继承并扩展了前两代的架构,显著增加了解码块的数 量、隐藏层的维度和自注意力头的数量,参数量最高达到 1750 亿。”
    
    2）预训练
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=72&annotation=undefined) “使用了更大规模和更多样化的互联网文本数据集,数据量接近 1TB”[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=73&annotation=undefined) “。所有数据都经过了严格的筛选和清洗流程,以确保 数据的质量和多样性。”
    
    3）下游任务
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=73&annotation=undefined) “上 下文学习能力极大地增强了 GPT-3 的任务泛化能力,使其能够快速适应不同的应 用场景。”
    
4. InstructGPT
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=74&annotation=undefined) “InstructGPT,其也是 ChatGPT 的前身。它通 过引入了人类反馈强化学习(Reinforcement Learning from Human Feedback, RLHF), 显著提升了模型对用户指令的响应能力。”
    
    **人类反馈强化学习：**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=74&annotation=undefined) “人类反馈强化学习旨在缓解模型在遵循用户指令时可能出现的不准确性和不 可靠性,以使模型生成的内容更符合人类的要求。”
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=74&annotation=undefined) “在人类反馈强化学习中,人类评 估者首先提供关于模型输出质量的反馈,然后使用这些反馈来微调模型。”
    
    **1）有监督微调**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=74&annotation=undefined) “收集大量“问题-人 类回答”对作为训练样本,对大语言模型进行微调。”
    
    **2）训练奖励模型**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=74&annotation=undefined) “针对每个 输入,让模型生成多个候选输出,并由人工对其进行质量评估和排名,构成偏好数 据集。用此偏好数据集训练一个奖励模型,使其可以对输出是否符合人类偏好进 行打分。”
    
    **3）强化学习微调**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=74&annotation=undefined) “基于上一步中得到的奖励模型,使用强化学习方法优 化第一步中的语言模型,即在语言模型生成输出后,奖励模型对其进行评分,强化 学习算法根据这些评分调整模型参数,以提升高质量输出的概率。”
    
    **直接偏好优化：**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=75&annotation=undefined) “该算法直接利用人类偏好数据来训练模型,省略了单独构建奖励模型以及应用复杂 强化学习算法的步骤。”
    
5. ChatGPT以及GPT-4
    
    闭源
    

### 2.5.3 LLAMA系列

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=76&annotation=undefined) “LLaMA 与 GPT 系列的主要区别在于:GPT 系列的升级主”[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=77&annotation=undefined) “线聚焦于模型规模与预训练语料的同步提升,而 LLaMA 则在模型规模上保持相对 稳定,更专注于提升预训练数据的规模。”

1. LLaMA1
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=77&annotation=undefined) “在 Chinchilla[15] 扩展法则的指引下,实践**“小模型 + 大数据”的理念**,旨在以大规模的优 质数据训练相对较小的模型。”
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=77&annotation=undefined) “总数据量高达 5TB。”
    
2. LLaMA2
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=79&annotation=undefined) “语料库的规模扩展至约 7TB”
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=79&annotation=undefined) “在分组查询注意力机制下,键(key)以及值(value)不再与查询(query) 一一对应,而是一组查询共享相同的键和值,从而有效降低内存占用并减少模型 总参数量。”
    
3. LLaMA3
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=79&annotation=undefined) “规模高达 50TB 的预训练语料”
    
4. LLaMA衍生模型

# 3. Prompt工程

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=97&annotation=undefined) “泛化能力的增强使得模型能够处理和理解多种 未知任务,而指令跟随能力的提升则确保了模型能够准确响应人类的指令。两种 能力的结合,使得我们能够通过精心编写的指令输入,即 Prompt,来引导模型适 应各种下游任务,从而避免了传统微调方法所带来的高昂计算成本。” ([“大模型基础”, p. 97](zotero://select/library/items/SCHBS2IK))

## 3.1Prompt工程简介

### 3.1.1 Prompt的定义

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=99&annotation=undefined) “这种技术的核心在于,将新任务通过 Prompt 构建为模型在预训练阶段已经熟悉的形式,利用模型固有的泛化能力来执 行新的任务,而无需在额外的特定任务上进行训练。” ([“大模型基础”, p. 99](zotero://select/library/items/SCHBS2IK))

### 3.1.2 Prompt工程的定义

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=99&annotation=undefined) “Prompt 工程(Prompt Engineering),又称提示工程,是指设计和优化用于与生 成式人工智能模型交互的 Prompt 的过程” ([“大模型基础”, p. 99](zotero://select/library/items/SCHBS2IK))

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=99&annotation=undefined) “这种技术的核心在于,将新任务通过 Prompt 构建为模型在预训练阶段已经熟悉的形式,利用模型固有的泛化能力来执 行新的任务,而无需在额外的特定任务上进行训练。” ([“大模型基础”, p. 99](zotero://select/library/items/SCHBS2IK))

### 3.1.3 Prompt分词向量化

### 3.1.4 Prompt工程的意义

## 3.2 上下文学习

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=107&annotation=undefined) “一种通过构造特定的 Prompt,来 使得语言模型理解并学习下游任务的范式”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=110&annotation=undefined) “演示示例选择主要依靠相似性和多样性”

1. 预训练数据越丰富越好
2. 预训练模型，参数量越大越好
3. 演示示例
    

## [3.3 思维链](zotero://note/u/58RRDJBV/)

## 3.4 Prompt技巧

### 3.4.1 规范Prompt编写

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=122&annotation=undefined) “经典的 Prompt 通常由任务说明,上下文,问题,输出格式等部分中的一个或几个组成” ([“大模型基础”, p. 122](zotero://select/library/items/SCHBS2IK))

1. 清晰、明确的任务说明能够确保模型准确理解任务要求
2. 上下文丰富且清晰，能够显著提升模型的理解和回答准确率
3. [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=126&annotation=undefined) “规范的输出格式对于确保模型输出的可用性和准确性至关重要。通过指定明 确的输出格式,可以使模型的输出结构化,便于下游任务直接提取和使用生成内 容。” ([“大模型基础”, p. 126](zotero://select/library/items/SCHBS2IK))
4. 排版清晰：
    
    - 使用一致的分隔符
    - 合理使用空白和缩进
    - 清晰的标题和子标题

### 3.4.2 合理归纳提问

- 复杂问题拆解
- 追问

### 3.4.3 适时使用CoT

1. 适合需要复杂推理的任务[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=133&annotation=undefined) “,CoT 能够引导大语言模型生成逻辑严密、条理清晰的中 间推理步骤,从而提高正确答案的生成概率” ([“大模型基础”, p. 133](zotero://select/library/items/SCHBS2IK))
2. 适合参数量大的模型
3. 预训练时有适当的指令微调
4. 在应对复杂问题，需要指定CoT输出到详细程度时，[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=135&annotation=undefined) “我们需要通过样例进行引导,以 使其展示完整的推理步骤。”
5. [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=135&annotation=undefined) “在不需要特定领域知识,仅需对问题进行逻辑推理和逐步分析时,可以使用 Zero-Shot CoT 或者 Auto CoT 的方式,通过“让我们一步一步思考”这种 CoT 提示触发词,来引导模型以 CoT 的形式回答内容。”
6. [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=135&annotation=undefined) “在处理需要高准确度和 可靠性的任务时,可要求模型生成多个回答并提出最终结果,进而运用 Self-Consistency 方法筛选出一致性最强的答案。”

### 3.4.4 善用心理暗示

1. 角色扮演
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=136&annotation=undefined) “通过 Prompt 指导大语言模型扮演特定角色能够显著改善其与角色相关的技能。”[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=136&annotation=undefined) “为了构建一个有效的角色,需要在指令中包含具体属性、职责、知识和技能。”
    
2. 情景代入
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=137&annotation=undefined) “通过将模型置于特定的“情景”或“环境”中,可以影响其生成的文本 内容和风格。情景代入指的是将特定情境下所需的专业知识、历史背景等信息嵌 入到模型的响应中。”
    

## 3.5 相关应用

### 3.5.1 基于大语言模型的Agent

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=138&annotation=undefined) “智能体(Agent)是一种能够自主感知环境并采取行动以实现特定目标的实 体”

Agent的架构分为四个部分：进行角色定位的配置模块、使用CoT细化任务的计划模块、使用RAG检索相关信息的记忆模块、使用外部工具的行动模块。

1. 配置模块：[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=139&annotation=undefined) “利用 Prompt 工程中的角色扮演技术,来定义 Agent 的角色。设定 Agent 的 背景、技能、职责等信息,这些角色设定信息以上下文的形式嵌入到 Agent 每一次 交互的 Prompt 中。”
2. 记忆模块：[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=139&annotation=undefined) “是 Agent 的知识与交互记忆的存储中心。记忆模 块通过检索增强等技术获取记忆,这一过程涉及到使用 Prompt 工程中的上下文学”[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=140&annotation=undefined) “习技术来构造和优化查询,从而帮助更加精准检索到相关记忆。在获取记忆之后, 将这些记忆将被添加到交互的 Prompt 中,帮助 Agent 利用这些记忆知识,实现更 为准确高效的决策与行动。”
3. 计划模块：[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=140&annotation=undefined) “扮演着任务分解者的角色,它将复杂的任务细化为一系列更为简单、易于管理的子任务。在这一过程中,通过 Prompt 工 程中的思维链技术,让大语言模型分解任务并进行规划,按照链式顺序输出子任 务;同时还利用了上下文学习技术,构造少样本示例来调控分解出的子任务的粒 度,确保整个任务流程的顺畅与高效。”
4. 行动模块：[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=140&annotation=undefined) “将计划模块生成的计划转化为具体的行动步骤,并借助外部工具执行这些步骤以实现 Agent 的目标。通常会为Agent 提供工具 API 的接口,把调用 API 接口的示例作为上下文,让大语言模型生成调用 API 的代码,之后执行这些代码,从而得到执行步骤的结果。”
    

### 3.5.2 数据合成

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=141&annotation=undefined) “SelfInstruct [37]”：[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=141&annotation=undefined) “Self-Instruct 通过 Prompt 工程技术构建 Prompt,通过多步骤调用大语 言模型,并依据已有的少量指令数据,合成大量丰富且多样化的指令数据。”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=142&annotation=undefined) “Self-Instruct 包含构建任务池、指令生成、指令分类、数据生 成、数据过滤五个步骤。”

1. 构建任务池：构建初始任务池
2. 指令生成：从任务池中随机抽取若干现有指令组成Prompt上下文，以小样本学习的方式构造Prompt，让模型生成指令。
3. 指令分类：让模型判断指令是分类还是生成任务。
4. 数据生成：[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=143&annotation=undefined) “使用 Prompt 工程中的上下文学习技术, 构造不同的 Prompt 来生成指令数据中的输入部分和回答部分。”
5. 数据过滤。

### 3.5.3 Text-to-SQL

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=144&annotation=undefined) “Text-to-SQL 技术可以将自然语言查询翻译成可以在数据库中执行 的 SQL 语句,是实现零代码或低代码数据查询的有效途径。”

### 3.5.4 GPTS

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=146&annotation=undefined) “GPTs 是 OpenAI 推出的支持用户自定义的 GPT 应用,允许用户通过编写 Prompt, 添加工具等方式创建定制版的 GPT 应用,也可以使用别人分享的 GPTs 模型。”

# 3.3 思维链

模型规模的扩张不足以解决所有问题，尤其是复杂推理能力没得到预期的性能突破，出现了“Flat Scaling Curves” 。

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=115&annotation=undefined) “人类在解决复杂问题时,通常会逐步构建推理路径以导出最终答案。基于这一理念,一种创新的 Prompt 范式——思维链提示 (Chain-of-Thought,CoT) [38] 被用于引导模型进行逐步推理。CoT 可以显著提升 大语言模型处理复杂任务中的表现,从而突破“Flat Scaling Curves”的限制,激发大语言模型的内在推理潜能。”

## 3.3.1 思维链提示

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=115&annotation=undefined) “**思维链提示(Chain-of-Thought,CoT)**[38] 通过模拟人类解决复杂问题时的思考过程,引导大语言模型在生成答案的过程中引入一系列的中间推理步骤。”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=115&annotation=undefined) “**CoT 方法的核心**是构造合适的Prompt以触发大语言模型一步一步生成推理路径,并生成最终答案。”

## 3.3.2 按部就班

1. Zero-Shot CoT
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=117&annotation=undefined) “Zero-Shot CoT [12] 通过简单的提示,如“Let’s think step by step”,引导模型自行生成一条推理链。”
    
2. Auto CoT
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=118&annotation=undefined) “在 Zero-Shot CoT 的基础之上,Auto-CoT [46] 引入与待解决问题相关的问题及其推理链作为示例,以继续提升CoT的效果。相关示例的生成过程是由大语言模 型自动完成的,无需手工标注。”
    
    - [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=119&annotation=undefined) “利用聚类技术从问题库中筛选出与用户提问位于一个簇中的问题。”
    - [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=119&annotation=undefined) “然后,借助 Zero-Shot CoT 的方式,为筛选出的问题生成推理链,形成示例。 这些示例包含了不同问题及其对应的推理内容,可为模型提供不同解题思路, 辅助模型做出更为审慎的推理。”
    - [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=119&annotation=undefined) “在这些示例的基础上,Auto-CoT 以“让我们一步一步思考” 引导大语言模型 生成针对用户问题的推理链和答案。”

## 3.3.3 三思后行

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=119&annotation=undefined) “在决策过程中的融入审慎和灵活性”

# 4. 参数高效微调

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=151&annotation=undefined) “对于预训练数据涉及较少的垂直领域,大语言模型无法仅通过提示工程来完成领 域适配。为了让大语言模型更好的适配到这些领域,需要对其参数进行微调。”

---

## 4.1 简介

### 4.1.1 下游任务适配

1. **上下文学习**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=152&annotation=undefined) “核心思想是将不同类型的任务都转化为生成任务,通过设计 Prompt 来驱动大语言模型完成这些 下游任务。”
    
    缺点：[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=153&annotation=undefined) “1)上下文学习的性能和微调依旧存在差距,并且 Prompt 设计需要花费大 量的人力成本,不同 Prompt 的最终任务性能有较大差异;2)上下文学习虽然完全 不需要训练,但在推理阶段的代价会随 Prompt 中样例的增多快速增加。因此,微 调大语言模型在许多场景和任务中依旧是必要的,尤其是在垂直领域。”
    
2. **指令微调**[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=153&annotation=undefined) “(Instruction Tuning)”
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=153&annotation=undefined) “指令微调 旨在对模型进行任务指令的学习,使其能更好地理解和执行各种自然语言处理任 务的指令。指令微调需首先构建指令数据集,然后在该数据集上进行监督微调。”
    
    - 指令数据构建：
    - 监督微调：
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=154&annotation=undefined) “监督微调需要较大的计算资源”
    

### 4.1.2 参数高效微调[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=152&annotation=undefined) “(Parameter-Efficient Fine-Tuning, PEFT)”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=154&annotation=undefined) “旨在避免微调全部参 数,减少在微调过程中需要更新的参数数量和计算开销,从而提高微调大语言模 型的效率。”

1. [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=155&annotation=undefined) “参数附加方法(Additional Parameters Methods)”
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=155&annotation=undefined) “在模型结构中附加新的、较小 的可训练模块。”
    
2. [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=155&annotation=undefined) “参数选择方法(Parameter Selection Methods)”
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=155&annotation=undefined) “仅选择模型的一部分参数进行微 调,而冻结其余参数。”
    
3. [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=155&annotation=undefined) “低秩适配方法(Low-rank Adaptation Methods)”
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=155&annotation=undefined) “通过低秩矩阵来近似原始权重 更新矩阵,并冻结原始参数矩阵,仅微调低秩更新矩阵。”
    

### 4.1.3 优势

计算效率高

存储效率高

---

## 4.2 参数附加方法

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=157&annotation=undefined) “参数附加方法(Additional Parameter Methods)通过增加并训练新的附加参数或模块对大语言模型进行微调。”

### 4.2.1 加在输入

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=157&annotation=undefined) “加在输入的方法将额外参数附加到模型的输入嵌入(Embedding)中,其中最经典的方法是 Prompt-tuning [23]。”

Prompt-tuning在输入中引入可微分的软提示作为输入的一部分，与实际文本一起被送入模型。在微调过程中，仅软提示的参数会被更新，其它参数不变。

a. 内存效率高

b.多任务适应：[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=158&annotation=undefined) “Prompt-tuning 只需要为每个任务存储一个特定的小的任务提示模块,并且可以使用原始预训练模型进行混合任务推理(在每个任务提示词前加上学到的 soft prompt”

c.缩放特性：参数量越多性能越强。

### 4.2.2 加在模型

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=158&annotation=undefined) “加在模型的方法将额外的参数或模型添加到预训练模型的隐藏层中,其中经 典的方法有 Prefix-tuning [24]、Adapter-tuning [18] 和 AdapterFusion [35]。”

1. **Prefix-tuning**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=159&annotation=undefined) “Prefix-tuning 将一系列连续的可训练前缀(Prefixes,即 Soft-prompt)插入到输入嵌入以及 Transformer 注意力模块中”
    
    相比Prompt-tuning，Prefix-tuning大幅增加了可学习参数量。
    
2. **Adapter-tuning**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=160&annotation=undefined) “Adapter-tuning [18] 向预训练语言模型中插入新的可学习的神经网络模块,称为适配器(Adapter)。” 添加在Transformer的多头注意力层和全连接层后。训练时仅更新adapter
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=160&annotation=undefined) “适配器模块通常采用瓶颈(Bottomneck)结构,即一个上 投影层、一个非线性映射和一个下投影层组成的全连接模块。其中,下投影层将 信息压缩到一个低维的表示,经过非线性映射后再通过上投影层扩展回原始维度。”
    
3. **AdapterFusion**

考虑结合多个任务的知识，可以把多个上述的adapter结合。[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=161&annotation=undefined) “基于该思路,AdapterFusion 提出一种两阶段学习的方法,先学习多个任务,对每个任务进行知识提取;再 “融 合”(Fusion)来自多个任务的知识。” ([“大模型基础”, p. 161](zotero://select/library/items/SCHBS2IK))

**第一阶段：知识提取：**针对N个给定任务，分别训练适配器模块，用于学习相应任务的知识。

- Single-Task Adapters: 对于N个任务，模型分别进行独立优化。
- Multi-Task Adapters：通过多任务学习对N个任务进行联合优化。
    
    **第二阶段：知识组合：**将不同适配器模块进行融合，以实现知识组合。
    

### 4.2.3 加在输出  

([Liu 等, 2024](zotero://select/library/items/MQJWH6SP))

**解决的问题：**1.参数量大时；2无法直接访问大语言模型的weights时。

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=163&annotation=undefined) “代理微调(Proxy-tuning) [27] 提供了一种轻量级的解码 时(Decoding-time)算法,允许我们在不直接修改大语言模型权重的前提下,通过 仅访问模型输出词汇表预测分布,来实现对大语言模型的进一步定制化调整。” ([“大模型基础”, p. 163](zotero://select/library/items/SCHBS2IK))

---

## 4.3 参数选择方法

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=164&annotation=undefined) “参数选择方法(Parameter Selection Methods)选择性的对预训练模型中的某个参数子集进行微调。” 不需要增加额外的参数。

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=167&annotation=undefined) “基于选择的方法通过选择性地更新预训练模型的参数,在保持大部分参数不 变的情况下对模型进行微调。”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=167&annotation=undefined) “然而,这些方法也面临挑战,比如,如何选择最佳参数子集, 以及如何平衡参数更新的数量和模型性能之间的关系。”

### 4.3.1 基于规则的方法

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=165&annotation=undefined) “根据人类专家的经验,确定哪些参数应该被更新。”

### 4.3.2 基于学习的方法

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=165&annotation=undefined) “基于学习的方法在模型训练过程中自动地选择可训练的参数子集。”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=165&annotation=undefined) “典型方法是 Child-tuning [49] 。其通过梯度掩码矩阵策略实现仅对选中的择子网 络进行梯度更新,而屏蔽子网络梯度以外的梯度,从而实现对微调参数的选择,达 到参数高效微调的目的。”

---

## 4.4 低稚适配方法

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=167&annotation=undefined) “过参数化模型的固有维度是很低的;换言之,存 在可以与全参数更新媲美的低维的参数更新”

### 4.4.1 [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=168&annotation=undefined) “低秩适配(Low-rank Adaptation, LoRA)”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=168&annotation=undefined) “低秩适配(Low-rank Adaptation, LoRA) [19] 提出利用低秩矩阵近似参数更新矩阵来实现低秩适配。该方法将参数更新矩阵低秩分解为两个小矩阵。在微调时, 通过微调这两个小矩阵来对大语言模型进行更新,大幅节省了微调时的内存开销。”

1. [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=168&annotation=undefined) **“方法实现”**
    
    **看原文**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=169&annotation=undefined) “,在训练时,LoRA 涉及的更新参数数量为 r × (d + k),远 小于全量微调 d × k。”
    
2. [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=169&annotation=undefined) **“参数效率”**
    
    **看原文**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=169&annotation=undefined) “与全量微调相比,LoRA 微调的参数不到原始参数量 的千分之一。”
    

### 4.4.2 LoRA相关变体

1. **打破低秩瓶颈**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=170&annotation=undefined) “全量微调的秩显著高于 LoRA 的秩(10-100 倍),并且增加 LoRA 的秩可以缩小 LoRA 与全量微调之间的性能差距。”
    
2. **动态秩分配**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=171&annotation=undefined) “LoRA 的秩并不总是越高越好,冗余的 LoRA 秩可能会导致性能和效率 的退化。”
    
3. **训练过程优化**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=172&annotation=undefined) “在实际微调过程中,LoRA 的收敛速度比全量微调要慢。此外,它还对超参数 敏感,并且容易过拟合。”
    

### 4.4.3 基于LoRA插件的任务泛化

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=172&annotation=undefined) “在 LoRA 微调结束后,我们可以将参数更新模块 B 和 A 从模型上分离出来, 并封装成参数插件。这些插件具有即插即用、不破坏原始模型参数和结构的优良性质。我们可以在不同任务上训练的各种 LoRA 模块,将这些模块插件化地方式保存、共享与使用。”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=172&annotation=undefined) “LoRAHub [20] 提供了一个可用的多 LoRA 组合的方法 框架。”

---

## 4.5 实践与运用

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=174&annotation=undefined) “Hugging Face 开发的 开源库 HF-PEFT”

### 4.5.1 PEFT实践

HF- PEFT和Huggingface的工具无缝集成，支持从单机到分布式环境到多样化训练和推理场景。其特别适用于达模型，能够再消费级硬件上实现高性能，并且可以与模型量化技术兼容，进一步减少模型的内存需求。

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=175&annotation=undefined) **“PEFT 相关技巧”** 看原文

### 4.5.2 PEFT应用

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=177&annotation=undefined) “利用少量数据进行全 参数微调时则容易导致大模型过拟合,因此采用 PEFT 技术进行部分参数微调十分 适合金融等垂直领域 Text-to-SQL 任务。”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=177&annotation=undefined) “,FinSQL [51] 提出了一套针对金融垂直领域 Text-to-SQL 训 练推理框架。如图 4.10 所示,该框架包含提示构造、参数高效微调和输出校准三 个部分。”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=178&annotation=undefined) “TabLLM [17] 提出基于大语言模型的少样本表格数据分类框架”。**该方法有参考价值**

# 5. 模型编辑

## 5.1 模型编辑简介

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=187&annotation=undefined) “模型编辑旨在精准、高效 地修正大语言模型中的特定知识点,能够满足大语言模型对特定知识点进行更新 的需求。” ([“大模型基础”, p. 187](zotero://select/library/items/SCHBS2IK))

### 5.1.1 模型编辑思想

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=187&annotation=undefined) “模型编辑通过增加或修改模型参数,快速有效地改变模型行为和输出。” ([“大模型基础”, p. 187](zotero://select/library/items/SCHBS2IK))

### 5.1.2 模型编辑的定义

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=188&annotation=undefined) “模型编辑的目标可被归纳为:修正大语言模型使其输出期望结果,同时不影 响其他无关输出。” ([“大模型基础”, p. 188](zotero://select/library/items/SCHBS2IK))

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=188&annotation=undefined) “由于**知识的内关联性**:当修改模型对某一特定知识点的认知时,由于该知识点可能与其它知识点相关 联,所以可能会影响模型对其它相关知识点的理解,从而产生” 牵一发而动全身” 的效应。” ([“大模型基础”, p. 188](zotero://select/library/items/SCHBS2IK))

精确控制模型编辑的范围是一个关键挑战

### 5.1.3 模型编辑的性质

- 准确性
- 泛化性：[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=190&annotation=undefined) “泛化性用来衡量编辑后模型能否适应目标问题的其他表达形式” ([“大模型基础”, p. 190](zotero://select/library/items/SCHBS2IK)) 需要构建泛化数据集
- 可迁移性：[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=191&annotation=undefined) “指编辑后模型将特定知识点 k 迁移到其它相关问题上的能力” ([“大模型基础”, p. 191](zotero://select/library/items/SCHBS2IK)) 需要构建可迁移性数据集
- 局部性：[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=191&annotation=undefined) “局部性要求编辑后的模型不影响其他不相关问题的输出” ([“大模型基础”, p. 191](zotero://select/library/items/SCHBS2IK)) 需要构建局部性数据集
- 高效性：

### 5.1.4 常用数据集

TODO

## 5.2 模型编辑经典方法

### 5.2.1 外部拓展法

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=195&annotation=undefined) “外部拓展法的核心思想是将新知识存储在附加的外部参数或外部知识库中, 将其和原始模型一起作为编辑后模型。” ([“大模型基础”, p. 195](zotero://select/library/items/SCHBS2IK))

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=195&annotation=undefined) “根据外部组件是否直接整合进模型本身的推理过程,外部拓展法又可划分为 知识缓存法和附加参数法。” ([“大模型基础”, p. 195](zotero://select/library/items/SCHBS2IK))

1. **知识缓存法**
    
    **三个重要主件**：[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=196&annotation=undefined) “门控单元、编辑缓存和推理模块” ([“大模型基础”, p. 196](zotero://select/library/items/SCHBS2IK))
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=196&annotation=undefined) “**门控单元：**用于判断输入问题与编辑缓存中的知识的相关程度” ([“大模型基础”, p. 196](zotero://select/library/items/SCHBS2IK))。[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=196&annotation=undefined) “可 通过分类 [20] 或噪声对比估计 [21] 等任务进行训练。” ([“大模型基础”, p. 196](zotero://select/library/items/SCHBS2IK))
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=196&annotation=undefined) “**编辑缓存：**充当一个知识存储库,用于保存需要修改的知识,这些知识由用户通过不同的形式指定。” ([“大模型基础”, p. 196](zotero://select/library/items/SCHBS2IK))
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=196&annotation=undefined) “**推理模块：**获取原始输入问题和编辑缓存中的知识作为输入,通过监督训练的方式学习预测用户期望的结果。” ([“大模型基础”, p. 196](zotero://select/library/items/SCHBS2IK))
    
    **工作流：门控单元**首先判断输入的问题是否与**编辑缓存**中的某个知识点相关，如果相关，则从**编辑缓存**中取出该知识点，将其与输入一起交给**推理模块**，由**推理模块**给出答案；若不相关，则用**原始模型**给出答案。
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=197&annotation=undefined) “编辑缓存中知识点的存储形式可以分为事实知识、自然语言补丁和正则 表达式三种” ([“大模型基础”, p. 197](zotero://select/library/items/SCHBS2IK))
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=197&annotation=undefined) “知识缓存法直接通过编辑缓存中的信息进行检索,不依赖目标标签的梯度信 息,因此可以简化模型编辑过程,使其更加高效直接。” ([“大模型基础”, p. 197](zotero://select/library/items/SCHBS2IK))
    
2. **附加参数法**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=197&annotation=undefined) “附加参数法可以将外部参数整合进模型结构,从而有效 利用和扩展模型的功能。” ([“大模型基础”, p. 197](zotero://select/library/items/SCHBS2IK))
    

### 5.2.2 内部修改法

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=199&annotation=undefined) “内部修改法旨在通过更新原始模型的内部参 数来为模型注入新知识,能够优化模型的自我学习和适应能力,提高其在特定任 务上的表现,而不是仅仅停留在表面的知识积累。” ([“大模型基础”, p. 199](zotero://select/library/items/SCHBS2IK))

1. **元学习法**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=199&annotation=undefined) “核心思想是使模型从一系列编辑任务中提取通用的知识,并将其应用于未见过的编辑任务,这部分知识被称为元知识ω” ([“大模型基础”, p. 199](zotero://select/library/items/SCHBS2IK))
    
2. **定位编辑法**
    

## 5.3 附加参数方法

## 5.4 定位编辑方法

## 5.5 模型编辑的应用

通过对预训练模型进行细粒度编辑，可以灵活地修改和优化模型，而无需从头训练。可以针对性地修改特定事实，有效保护营私信息，降低数据泄漏风险。此外，通过对模型编辑过程进行精细控制，能够及时识别并消除模型中潜在的安全隐患，如有害信息、偏见内容等，从而提升模型等安全性和可靠性。

### 5.5.1 精准模型更新

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=221&annotation=undefined) “模型编辑技术可以快速、精准地修正模型的特定行为。通过识别并修改相关 的模型参数,可以在短时间内修复模型的回答。”

### 5.5.2 保护被遗忘权

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=222&annotation=undefined) “能够有效地从模型中删除或修改这些信息”

### 5.5.3 提升模型安全性

1. [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=223&annotation=undefined) “大语言模型可能因为有害输入而产生有害语言,影响其实用性” ([“大模型基础”, p. 223](zotero://select/library/items/SCHBS2IK))

# 6.检索增强生成

## 6.1 Introduction

## 6.2 检索增强生成架构

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=236&annotation=undefined) “检索增强生成(RAG)系统是一个集成了**外部知识库、检索器、生成器**等多个 功能模块的软件系统。”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=236&annotation=undefined) “在不同的协作方式下,检索器检索到的信息 质量会有所不同,生成器生成的内容质量也会随之变化。”

### 6.2.1 RAG架构分类

### 6.2.2黑盒增强架构

不能微调模型是黑盒

按是否微调检索器可分为两种：无微调和检索器微调

- **无微调：**

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=238&annotation=undefined) “直接将检索器检索到的文档前 置到输入问题前作为上下文”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=238&annotation=undefined) “一个 RAG 任务可能涉及多次执行检索和 生成。例如,在一个长文本生成任务中,每生成一定量的文本后,模型就可能会执 行一次检索,以确保随着话题的发展,后续生成的内容能够持续保持与话题相关。”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=239&annotation=undefined) “**检索查询长度**指的是用于检索的 文本片段的长度,通常被设置为语言模型输入中的最后几个词”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=238&annotation=undefined) “**检索步长**是指模型在生成文本时,每隔多少个词进行一次检索”

- **检索器微调**

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=239&annotation=undefined) “REPLUG LSR”框架[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=239&annotation=undefined) “使用**大语言模型的困惑度分数**作为监督信号来微调检索器,使其能更有效地检索 出能够显著降低语言模型困惑度的文档。”

**文档概率分布** ：[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=240&annotation=undefined) “基于检索器计算的上下文与文档之间的相似度,通过余 弦相似度来衡量,并将这些相似度分数转化为概率值”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=240&annotation=undefined) **“文档对语言模型 的贡献分布”****：**

## 6.2.3 白盒增强架构

1. **仅微调语言模型**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=241&annotation=undefined) “检索器作为一个预先训练好的组件其参数保持不变, 大语言模型根据检索器提供的上下文信息,对自身参数进行微调。”
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=241&annotation=undefined) “SELF-RAG[3] 通过在微调语言模型时引 入反思标记,使语言模型在生成过程中动态决定是否需要检索外部文本,并对生 成结果进行自我批判和优化。”
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=241&annotation=undefined) “RETRO 首先将知识库中的文本进行切 块,然后用 BERT 对每个文本块生成嵌入向量”[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=241&annotation=undefined) “在微调模型时的自回归过程中,每 当模型生成一段文本块后,就去知识库中检索出与之最相似的嵌入向量。然后,这 些嵌入向量和模型注意力层的输出一起被送入一个外部的 Transformer 编码器进行 编码。得到的编码向量直接输入给模型的块交叉编码器的键(key)和值(value), 以捕捉外部知识的关键信息。通过交叉编码,模型能够结合检索到的相关信息来 生成新的文本块”
    
2. **检索器和语言模型协同微调**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=242&annotation=undefined) “在预训练和微调阶段使用 KL 散度损失函数来联合训练检索器和语言模型,” ([“大模型基础”, p. 242](zotero://select/library/items/SCHBS2IK))
    

## 6.2.4对比分析

…

## 6.3 知识检索

- [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=244&annotation=undefined) “检索的效果(召回率、精度、多样性等)会直接影响大语言模型 的生成质量。”
- [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=244&annotation=undefined) “检索的时间也是 RAG 总耗时 的关键部分,因此检索的效率将影响用户的使用体验”

### 6.3.1 知识库构建

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=244&annotation=undefined) “全面、优质、高效的知识库,检索才能有的放矢,检索效果才能有保障。”

1. 数据采集及预处理
    
    - 数据清洗
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=245&annotation=undefined) “数据清洗旨在清除文本中的干扰元素,如特殊字符、异常编码和无用的HTML标签,以及删除重复或高度相似的冗余文档,从而提高**数据的清晰度和可用性**。”
        
    - 文本分块
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=245&annotation=undefined) “文本分块是将长文本分割成较小文本块的过程,”
        
        - [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=245&annotation=undefined) “一是为了**适应检索模型的上下文窗口长度限制**,避免超出其处理能力”
        - [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=245&annotation=undefined) “二是通过分块可以减少长文本中的不相关内容,降低噪音,从而 提高检索的效率和准确性。”
            
        
        分块策略：
        
        - “确定切分方法 (如按句子或段落切分)、
        - 设定块大小,
        - 以及是否允许块之间有重叠。”
            
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=245&annotation=undefined) “文本分块的具体实施流程通常开始于将长文本拆解为较小的语义单元,如句子或段落。随后,这些单元被逐步组合成更大的块,直到达到预设的块大小,构建出独立的文本片段。”
        
    
2. 知识库增强
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=246&annotation=undefined) “通过改进和丰富知识库的内容和结构,以提升其质量和实用性。”
    
    - 查询生成
        
        用大模型生成文档的“键”，供检索时与用户查询进行匹配。
        
    - 标题生成
        

### 6.3.2 查询增强

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=246&annotation=undefined) “用户遣词造句的方式以及描述问题的角度可能会与知识库中的存储的文本间存在差 异,这可能导致用户查询和知识库之间不能很好匹配,从而降低检索效果。为了解 决此问题,我们可以对用户查询的语义和内容进行扩展,即查询增强,以更好的匹 配知识库中的文本。”

1. 查询语义增强
    
    - 同义改写
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=247&annotation=undefined) “解决用户查询单一的表达形式可能无法全面覆盖到知识库中多样化表达的知识。”
        
    - 多视角分解
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=247&annotation=undefined) “采用分而治之的方法来处理复杂查询,将复杂查询分解为来自不 同视角的子查询,以检索到查询相关的不同角度的信息。”
        
2. 查询内容增强
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=247&annotation=undefined) “查询内容增强旨在通过**生成与原始查询相关的背景信息和上下文**,从而丰富查询内容,提高检索的准确性和全面性”
    

### 6.3.3 检索器

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=248&annotation=undefined) “检索器旨在找到知识库中与用户查询相关的知识文本。”

1. 判别式检索器
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=248&annotation=undefined) “判别式检索器通过判别模型对查询和文档是否相关进行打分。判别式检索器通常分为两大类:稀疏检索器和稠密检索器。”
    
    - **稀疏检索器**
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=248&annotation=undefined) “稀疏检索器(Sparse Retriever)是指使用**稀疏表示方法**来匹配文本的模型。”
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=248&annotation=undefined) “通过统计文档中特定词项出现的统计特征来对文档进行编码,然后基于 此编码计算查询与知识库中的文档的相似度来进行检索。”
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=249&annotation=undefined) “通过分析词项的分布和频率来评估文档与查询 的相关性。”
        
    - **稠密检索器**
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=249&annotation=undefined) “利用预训练语言模型对文本生成低维、密集的向量表示,通 过计算向量间的相似度进行检索。”
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=250&annotation=undefined) **“交叉编码类”**
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=250&annotation=undefined) **“双编码器类”**
        
2. 生成式检索器
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=251&annotation=undefined) “生成式检索器直接将知识 库中的文档信息记忆在模型参数中。然后,在接收到查询请求时,能够直接生成 相关文档的标识符(即 DocID),以完成检索”
    

### 6.3.4 检索效率增强

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=252&annotation=undefined) “为 提升检索效率,可以引入向量数据库来实现检索中的高效向量存储和查询”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=252&annotation=undefined) “常用的索引技术主要分成三大类:基于空间划分的方法、基于 量化方法和基于图的方法。”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=254&annotation=undefined) “常见软件库介绍”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=255&annotation=undefined) “表 6.1: 常见的向量数据库。” ([“大模型基础”, p. 255](zotero://select/library/items/SCHBS2IK))

### 6.3.5 检索结果重排

1. 基于交叉编码器，使用交叉编码器评估文档与查询之间的语义相关性。
2. 基于上下文学习的重排方法：使用大语言模型执行重排任务。

## 6.4 生成增强

1.非必要不增强，2.何处增强，3.对复杂查询和模糊查询多次迭代增强，4.[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=257&annotation=undefined) “知识压缩与缓存加速,以降低增强过程的计算成本”

### 6.4.1 何时增强

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=257&annotation=undefined) “内部知识可以解决的问题,我们可以不对该问题进行增强。”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=257&annotation=undefined) “判断模型是否具有内部知识的方 法可以分为两类:(1)外部观测法,”[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=257&annotation=undefined) “（2）内部观测法,”

> 1. 外部观测法：
>     
>     （1）Prompt直接询问；
>     
>     （2）反复询问，观察多次回答对一致性；
>     
>     （3）查看训练数据，[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=258&annotation=undefined) “设计伪训练数据统计量来拟合真实训练数据的分布”
>     
>     > - 知识在训练数据中出现的频率与模型对该知识的记忆程度是正相关的。问题是无法统计。
>     > - 构造伪训练数据统计量。[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=260&annotation=undefined) “由于模型对训练数据中低频出现的知识掌握不足,而对更“流行”(高 频)的知识掌握更好,因此实体的流行度作可以作为伪训练数据统计量。” ([“大模型基础”, p. 260](zotero://select/library/items/SCHBS2IK))
>     
> 2. 内部观测法
> 
> [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=261&annotation=undefined) “大语言模型在生成文本时,是对输入序列进行建模和预测,模型内部状 态的变化反映了模型对当前上下文理解和下一步预测的确定性。如果模型表现出 较高的内部不确定性,如注意力分布较为分散、激活值变化较大等,就可能对当前 上下文缺乏充分的理解,从而无法做出有把握的预测。” ([“大模型基础”, p. 261](zotero://select/library/items/SCHBS2IK))
> 
> [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=261&annotation=undefined) “模型的内部知识检索主要发生在中间层的前馈网络中 [36],因此在处理 包含或不包含内部知识的不同问题时,模型的中间层会展现出不同的动态变化。”[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=261&annotation=undefined) “基 于这一特性,我们可以训练分类器进行判别,这种方法被称为探针。” ([“大模型基础”, p. 261](zotero://select/library/items/SCHBS2IK))
> 
> 该探针即线性分类器，根据问题所对应的内部表示预测该问题属于模型**已知或未知**。
> 
> [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=261&annotation=undefined) “结果显示,不同大语言模型在利用中间层的 内部表示进行分类时,均能够实现较高的分类准确率。这表明中间层的内部隐藏 状态能够有效地反映模型对问题的理解和相关知识储备。” ([“大模型基础”, p. 261](zotero://select/library/items/SCHBS2IK))

### 6.4.2 何处增强

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=262&annotation=undefined) “得益于大语言模型的上下文学习能力、注意力机制的可扩展性以及自回归生成能力,其输入端、中间层和输出端都可以进行知识融合操作。”

（1）在输入端增强

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=263&annotation=undefined) “将检索到的外部知识文本与用户查询拼接到 Prompt 中,然后输入给大语言模型。”

**优点：**直观且易于实现

**缺点：**[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=263&annotation=undefined) “当检索到的文本过长时,可能导致输 入序列过长,甚至超出模型的最大序列长度限制”

（2）在中间层增强

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=263&annotation=undefined) “先将检索到的外部知识 转换为向量表示,然后将这些向量插入通过交叉注意力融合到模型的隐藏状态中。”[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=264&annotation=undefined) “这种方法能够 更深入地影响模型的内部表示,可能有助于模型更好地理解和利用外部知识。同时,由于向量表示通常比原始文本更为紧凑,这种方法可以减少对模型输入长度的依赖。”

（3）在输出端增强

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=264&annotation=undefined) “利用检索到的外部知识对大语言模型生成的文本进行校 准,是一种后处理的方法。”

### 6.4.3多次增强

- [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=264&annotation=undefined) “复杂问题往往涉及多个知识点,需要多跳(multi-hop)的理解”
- [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=264&annotation=undefined) “模糊问题往往指代范围不明, 难以一次就理解问题的含义”
- 处理复杂问题时,常采用分解式增强的方案。[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=265&annotation=undefined) “将复杂问题分解为多个子问题,子问题间进行迭代检索增强, 最终得到正确答案。”
- [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=265&annotation=undefined) “处理模糊问题时,常采用渐进式增强的方案。该方案将问题的 不断细化,然后分别对细化的问题进行检索增强,力求给出全面的答案,以覆盖用 户需要的答案。”

1. **分解式增强**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=265&annotation=undefined) “模型可以将多跳问题分解为一个个子问题,然后在子问题间迭代地进行检索增强,最后得出正确结论,即分解式增强。”
    
2. **渐进式增强**
    
    [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=266&annotation=undefined) “在模糊问题中,问题主体通常指代不明,容易引发歧义”
    
    递归式检索来引导大语言模型在树状结构中探索给定模糊问题的多种澄清路径。[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=267&annotation=undefined) “在此过程中,框架会根据细化问题与原问题的相关性及知识一致性进行剪枝。”[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=267&annotation=undefined) “最终,我们能够构建 出多条完整的知识路径,每条路径的末端(叶节点)都代表了对原始问题的不同但 是有效的解答。”
    
    **效率低**
    

### 6.4.4 降本增效

1. 去除冗余文本
    
    - **Token级别的方法**
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=268&annotation=undefined) “Token 级别的方法通过对 Token 进行评估,对文本中不必要的 Token 进行剔除。”
        
        判别指标：困惑度。[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=269&annotation=undefined) “基于困惑度删除冗余文本。”
        
        1）问题感知的粗粒度压缩：[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=269&annotation=undefined) “在给定问题条件下通过计算文档中所有 Token 困惑度的均值来评估文档 的重要性,困惑度越高表示文档信息量越大。”
        
        2）[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=269&annotation=undefined) “执行问题感知的细粒度压缩”：[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=269&annotation=undefined) “进一步计算文档中每个 Token 的困惑度并去除其中低困惑度的 Token。”
        
    - **子文本级别的方法**
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=269&annotation=undefined) “子文本级别的方法通过对子文本进行打分,对不必要的子文本成片删除。”
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=269&annotation=undefined) “对于检索到的文 档,首先利用滑动窗口将其分割成多个子文档,然后使用双标签子文档打分器对 这些子文档分别进行评分。最后,删除掉评分较低的子文档,从而有效地去除冗余文本。”
        
    - **全文本级别的方法**
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=269&annotation=undefined) “直接从整个文档中抽取出重要信息,以去除掉冗余信息”
        
        **1）上下文提取阶段：**
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=269&annotation=undefined) “以最小化压缩文本与原输入文档之间的差异为目标,对信息提取器进行监 督学习训练,学习如何将输入文档精炼为信息丰富的压缩文本。”
        
        **2）奖励驱动阶段：**
        
        [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=269&annotation=undefined) “大语言模型作为奖励模型,其根据压缩文本生成的答案与真实答案之间的相似度 作为奖励信号,通过强化学习对信息提取器进行优化。最终得到的信息提取器可 以直接将输入文档转化为压缩文本,端到端地去除冗余文本。”
        
2. 复用计算结果
    
    1）KV-cache
    
    2）[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=270&annotation=undefined) “RAG 系统专用的多级动态缓存机制”
    

## 6.5 实践

### 6.5.1搭建简单的RAG系统

- [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=272&annotation=undefined) “LangChain 提供了一个较为全面的模块支持,帮助开发者们轻松便捷地构建自己的 RAG 应用 框架。”
- [Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=272&annotation=undefined) “LlamaIndex 更加专注于数据索引与检索的部分。”

### 6.5.2 RAG的应用

1. 智能体（Agent）

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=276&annotation=undefined) “(1)配置模块通过设定基本信息来定义 Agent 的角色,这些信息 可以包括 Agent 的年龄、性别、职业等基本属性”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=276&annotation=undefined) “(2)记忆模块存储从环境中学习到的知识以及历史信息,支持记忆检索、记忆 更新和记忆反思等操作,允许 Agent 不断获取、积累和利用知识。在这一模块中, RAG 通过检索相关信息来辅助记忆的读取和更新;”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=276&annotation=undefined) “(3)计划模块赋予 Agent 将复 杂任务分解为简单的子任务的能力,并根据记忆和行动反馈不断调整。RAG 在此 模块中通过提供相关的信息,帮助 Agent 更合理有效地规划任务”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=276&annotation=undefined) “(4)行动模块则 负责将 Agent 的计划转化为具体的行动,包括网页检索、工具调用以及多模态输出 等,能够对环境或 Agent 自身状态产生影响,或触发新的行动链。在这一模块中, RAG 通过检索相关信息来辅助 Agent 的决策和行动执行。”

2. 多模态垂直领域

# 大模型基础笔记目录

# 1.[语言模型基础](zotero://note/u/TB83IKGC/)

# 2.[大语言模型架构](zotero://note/u/LUIATFUX/)

# 状态空间模型（SSM）

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=83&annotation=undefined) “状态空间模型(State Space Model,SSM)[13] 范式可以有效处理长文本中存 在的长程依赖性(Long-Range Dependencies, LRDs)问题,并且可以有效降低语言模型的计算和内存开销。”

【对SSM的思想的理解】

连续形式：

离散化（Discretization）:

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=84&annotation=undefined) “将系统方程从连续形式转换为递归形式和卷积形式”

# LLM classic paper list

# 大模型基础论文列表

- [语言模型基础](#%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E5%9F%BA%E7%A1%80)
    
    - [基于统计方法的语言模型](#%E5%9F%BA%E4%BA%8E%E7%BB%9F%E8%AE%A1%E6%96%B9%E6%B3%95%E7%9A%84%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B)
    - [基于 RNN 的语言模型](#%E5%9F%BA%E4%BA%8E-rnn-%E7%9A%84%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B)
    - [基于 Transformer 的语言模型](#%E5%9F%BA%E4%BA%8E-transformer-%E7%9A%84%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B)
    - [语言模型的采样方法](#%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E7%9A%84%E9%87%87%E6%A0%B7%E6%96%B9%E6%B3%95)
    - [语言模型的评测](#%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E7%9A%84%E8%AF%84%E6%B5%8B)
- [大语言模型](#%E5%A4%A7%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B)
    
    - [大数据+大模型→新智能](#%E5%A4%A7%E6%95%B0%E6%8D%AE%E5%A4%A7%E6%A8%A1%E5%9E%8B%E6%96%B0%E6%99%BA%E8%83%BD)
    - [大语言模型架构概览](#%E5%A4%A7%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E6%9E%B6%E6%9E%84%E6%A6%82%E8%A7%88)
    - [基于 Encoder-only 架构的大语言模型](#%E5%9F%BA%E4%BA%8E-encoder-only-%E6%9E%B6%E6%9E%84%E7%9A%84%E5%A4%A7%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B)
    - [基于 Encoder-Decoder 架构的大语言模型](#%E5%9F%BA%E4%BA%8E-encoder-decoder-%E6%9E%B6%E6%9E%84%E7%9A%84%E5%A4%A7%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B)
    - [基于 Decoder-only 架构的大语言模型](#%E5%9F%BA%E4%BA%8E-decoder-only-%E6%9E%B6%E6%9E%84%E7%9A%84%E5%A4%A7%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B)
    - [非 Transformer 架构](#%E9%9D%9E-transformer-%E6%9E%B6%E6%9E%84)
- [Prompt 工程](#prompt-%E5%B7%A5%E7%A8%8B)
    
    - [Prompt 工程简介](#prompt-%E5%B7%A5%E7%A8%8B%E7%AE%80%E4%BB%8B)
    - [上下文学习](#%E4%B8%8A%E4%B8%8B%E6%96%87%E5%AD%A6%E4%B9%A0)
    - [思维链](#%E6%80%9D%E7%BB%B4%E9%93%BE)
    - [Prompt 技巧](#prompt-%E6%8A%80%E5%B7%A7)
    - [相关应用](#%E7%9B%B8%E5%85%B3%E5%BA%94%E7%94%A8)
- [参数高效微调](#%E5%8F%82%E6%95%B0%E9%AB%98%E6%95%88%E5%BE%AE%E8%B0%83)
    
    - [参数高效微调简介](#%E5%8F%82%E6%95%B0%E9%AB%98%E6%95%88%E5%BE%AE%E8%B0%83%E7%AE%80%E4%BB%8B)
    - [参数附加方法](#%E5%8F%82%E6%95%B0%E9%99%84%E5%8A%A0%E6%96%B9%E6%B3%95)
    - [参数选择方法](#%E5%8F%82%E6%95%B0%E9%80%89%E6%8B%A9%E6%96%B9%E6%B3%95)
    - [低秩适配方法](#%E4%BD%8E%E7%A7%A9%E9%80%82%E9%85%8D%E6%96%B9%E6%B3%95)
    - [实践与应用](#%E5%AE%9E%E8%B7%B5%E4%B8%8E%E5%BA%94%E7%94%A8)
- [模型编辑](#%E6%A8%A1%E5%9E%8B%E7%BC%96%E8%BE%91)
    
    - [模型编辑简介](#%E6%A8%A1%E5%9E%8B%E7%BC%96%E8%BE%91%E7%AE%80%E4%BB%8B)
    - [模型编辑经典方法](#%E6%A8%A1%E5%9E%8B%E7%BC%96%E8%BE%91%E7%BB%8F%E5%85%B8%E6%96%B9%E6%B3%95)
    - [附加参数法：T-Patcher](#%E9%99%84%E5%8A%A0%E5%8F%82%E6%95%B0%E6%B3%95t-patcher)
    - [定位编辑法：ROME](#%E5%AE%9A%E4%BD%8D%E7%BC%96%E8%BE%91%E6%B3%95rome)
    - [模型编辑应用](#%E6%A8%A1%E5%9E%8B%E7%BC%96%E8%BE%91%E5%BA%94%E7%94%A8)
- [检索增强生成](#%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90)
    
    - [检索增强生成简介](#%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90%E7%AE%80%E4%BB%8B)
    - [检索增强生成架构](#%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90%E6%9E%B6%E6%9E%84)
    - [知识检索](#%E7%9F%A5%E8%AF%86%E6%A3%80%E7%B4%A2)
    - [生成增强](#%E7%94%9F%E6%88%90%E5%A2%9E%E5%BC%BA)
    - [实践与应用](#%E5%AE%9E%E8%B7%B5%E4%B8%8E%E5%BA%94%E7%94%A8)

## 语言模型基础

### 基于统计方法的语言模型

1. **Foundations of statistical natural language processing.** `BOOK`  
    _Chris Manning, Hinrich Sch{"{u}}tze_ [[PDF](https://nlp.stanford.edu/fsnlp/)], 1999
2. **Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics and Speech Recognition.Third Edition.** `BOOK`  
    _Daniel Jurafsky, James H. Martin_ [[PDF](https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf)], 2023

### 基于 RNN 的语言模型

1. **A learning algorithm for continually running fully recurrent neural networks.** `Neural computation`  
    _RJ Williams, D Zipser._ [[PDF](https://gwern.net/doc/ai/nn/rnn/1989-williams-2.pdf)], 1989
2. **Long Short-Term Memory.** `Neural Computing`  
    _Sepp Hochreiter, J{"{u}}rgen Schmidhuber_ [[PDF](https://deeplearning.cs.cmu.edu/F23/document/readings/LSTM.pdf)], 1997
3. **On the difficulty of training Recurrent Neural Networks.** `ICML`  
    _Razvan Pascanu, Tomas Mikolov, Yoshua Bengio._ [[PDF](https://arxiv.org/abs/1211.5063)], 2012
4. **Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling.** `arXiv`  
    _Junyoung Chung, Caglar Gulcehre, KyungHyun Cho, Yoshua Bengio_ [[PDF](https://arxiv.org/abs/1412.3555)], 2014
5. **Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks.** `NeurIPS`  
    _Samy Bengio, Oriol Vinyals, Navdeep Jaitly, Noam Shazeer_ [[PDF](https://arxiv.org/abs/1506.03099)], 2015

### 基于 Transformer 的语言模型

1. **Layer Normalization.** `arXiv`  
    _Jimmy Lei Ba, Jamie Ryan Kiros, Geoffrey E. Hinton_ [[PDF](https://arxiv.org/abs/1607.06450)], 2016
2. **Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer.** `JMLR`  
    _Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu._ [[PDF](https://arxiv.org/abs/1910.10683)], 2019
3. **Transformer Feed-Forward Layers Are Key-Value Memories.** `EMNLP`  
    _Mor Geva, Roei Schuster, Jonathan Berant, Omer Levy_ [[PDF](https://arxiv.org/abs/2012.14913)], 2021
4. **ResiDual: Transformer with Dual Residual Connections.** `arXiv`  
    _Shufang Xie, Huishuai Zhang, Junliang Guo, Xu Tan, Jiang Bian, Hany Hassan Awadalla, Arul Menezes, Tao Qin, Rui Yan._ [[PDF](https://arxiv.org/abs/2304.14802)], 2023

### 语言模型的采样方法

1. **Diverse Beam Search: Decoding Diverse Solutions from Neural Sequence Models.** `AAAI`  
    _Ashwin K Vijayakumar, Michael Cogswell, Ramprasath R. Selvaraju, Qing Sun, Stefan Lee, David Crandall, Dhruv Batra._ [[PDF](https://arxiv.org/abs/1610.02424)], 2018
2. **The Curious Case of Neural Text Degeneration.** `ICLR`  
    _Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, Yejin Choi_ [[PDF](https://arxiv.org/abs/1904.09751)], 2020

### 语言模型的评测

1. **Perplexity—a Measure of the Difficulty of Speech Recognition Tasks.** `JASA`  
    _F. Jelinek, R. L. Mercer, L. R. Bahl, J. K. Baker_ [[PDF](https://pubs.aip.org/asa/jasa/article/62/S1/S63/642598/Perplexity-a-measure-of-the-difficulty-of-speech)], 1997
2. **ROUGE: A Package for Automatic Evaluation of Summaries.** `ACL`  
    _Chin-Yew Lin_ [[PDF](https://aclanthology.org/W04-1013/)], 2004
3. **BLEU might be Guilty but References are not Innocent.** `EMNLP`  
    _Markus Freitag, David Grangier, Isaac Caswell_ [[PDF](https://arxiv.org/abs/2004.06063)], 2020
4. **BERTScore: Evaluating Text Generation with BERT.** `ICLR`  
    _Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger, Yoav Artzi._ [[PDF](https://arxiv.org/abs/1904.09675)], 2020
5. **Leveraging Large Language Models for NLG Evaluation: Advances and Challenges.** `arXiv`  
    _Zhen Li, Xiaohan Xu, Tao Shen, Can Xu, Jia-Chen Gu, Yuxuan Lai, Chongyang Tao, Shuai Ma_ [[PDF](https://arxiv.org/abs/2401.07103)], 2024
6. **G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment.** `EMNLP`  
    _Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang, Ruochen Xu, Chenguang Zhu_ [[PDF](https://arxiv.org/abs/2303.16634)], 2023
7. **INSTRUCTSCORE: Towards Explainable Text Generation Evaluation with Automatic Feedback.** `EMNLP`  
    _Wenda Xu, Danqing Wang, Liangming Pan, Zhenqiao Song, Markus Freitag, William Wang, Lei Li._ [[PDF](https://aclanthology.org/2023.emnlp-main.365/)], 2023

## 大语言模型

### 大数据+大模型→新智能

1. **Scaling laws for neural language models.** `arXiv`  
    _Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, Dario Amodei._ [[PDF](https://arxiv.org/pdf/2001.08361)], 2020.
2. **Training Compute-Optimal Large Language Models** `arXiv`  
    _Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals, Laurent Sifre._ [[PDF](https://arxiv.org/pdf/2203.15556)], 2022.
3. **PaLM 2 Technical Report.** `arXiv`  
    _Google._ [[PDF](https://arxiv.org/pdf/2305.10403)], 2023.

### 大语言模型架构概览

1. **Attention is all you need.** `NeurIPS`  
    _Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N and Kaiser, Lukasz and Polosukhin, Illia._ [[PDF](https://arxiv.org/pdf/1706.03762)], 2017.

### 基于 Encoder-only 架构的大语言模型

1. **A survey on contextual embeddings.** `arXiv`  
    _Qi Liu, Matt J. Kusner, Phil Blunsom._ [[PDF](https://arxiv.org/pdf/2003.07278)], 2020.
2. **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.** `NAACL` _Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova._ [[PDF](https://aclanthology.org/N19-1423.pdf)][[Code](https://github.com/google-research/bert)], 2018.
3. **RoBERTa: A Robustly Optimized BERT Pretraining Approach.** `arXiv` _Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, Veselin Stoyanov._ [[PDF](https://arxiv.org/abs/1907.11692)][[Code](https://github.com/pytorch/fairseq)], 2019.
4. **ALBERT: A Lite BERT for Self-supervised Learning of Language Representations.** `arXiv` _Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, Radu Soricut._ [[PDF](https://arxiv.org/pdf/1909.11942)][[Code](https://github.com/google-research/ALBERT)], 2019.
5. **ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators.** `arXiv` _Kevin Clark, Minh-Thang Luong, Quoc V. Le, Christopher D. Manning._ [[PDF](https://arxiv.org/pdf/2003.10555)][[Code](https://github.com/google-research/electra)], 2020.

### 基于 Encoder-Decoder 架构的大语言模型

1. **Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer.** `arXiv`  
    _Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu._ [[PDF](https://arxiv.org/pdf/1910.10683)][[Code](https://github.com/google-research/text-to-text-transfer-transformer)], 2019.
2. **Multitask Prompted Training Enables Zero-Shot Task Generalization.** `arXiv`  
    _Victor Sanh, Albert Webson, Colin Raffel, Stephen H. Bach, Lintang Sutawika, Zaid Alyafeai, Antoine Chaffin, Arnaud Stiegler, Teven Le Scao, Arun Raja, Manan Dey, M Saiful Bari, Canwen Xu, Urmish Thakker, Shanya Sharma Sharma, Eliza Szczechla, Taewoon Kim, Gunjan Chhablani, Nihal Nayak, Debajyoti Datta, Jonathan Chang, Mike Tian-Jian Jiang, Han Wang, Matteo Manica, Sheng Shen, Zheng Xin Yong, Harshit Pandey, Rachel Bawden, Thomas Wang, Trishala Neeraj, Jos Rozen, Abheesht Sharma, Andrea Santilli, Thibault Fevry, Jason Alan Fries, Ryan Teehan, Tali Bers, Stella Biderman, Leo Gao, Thomas Wolf, Alexander M. Rush._ [[PDF](https://arxiv.org/pdf/2110.08207)][[Code](https://github.com/bigscience-workshop/promptsource)], 2021.
3. **mT5: A Massively Multilingual Pre-trained Text-to-Text Transformer.** `NAACL`  
    _Linting Xue, Noah Constant, Adam Roberts, Mihir Kale, Rami Al-Rfou, Aditya Siddhant, Aditya Barua, Colin Raffel._ [[PDF](https://aclanthology.org/2021.naacl-main.41.pdf)][[Code](https://goo.gle/mt5-code)], 2021.
4. **Scaling Instruction-Finetuned Language Models.** `Journal of Machine Learning Research`  
    _Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, Albert Webson, Shixiang Shane Gu, Zhuyun Dai, Mirac Suzgun, Xinyun Chen, Aakanksha Chowdhery, Alex Castro-Ros, Marie Pellat, Kevin Robinson, Dasha Valter, Sharan Narang, Gaurav Mishra, Adams Yu, Vincent Zhao, Yanping Huang, Andrew Dai, Hongkun Yu, Slav Petrov, Ed H. Chi, Jeff Dean, Jacob Devlin, Adam Roberts, Denny Zhou, Quoc V. Le, Jason Wei._ [[PDF](https://www.jmlr.org/papers/volume25/23-0870/23-0870.pdf)][[Code](https://github.com/google-research/t5x/blob/main/docs/models.md#flan-t5-checkpoints)], 2024.
5. **Bart: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension.** `ACL`  
    _Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Ves Stoyanov, Luke Zettlemoyer._ [[PDF](https://aclanthology.org/2020.acl-main.703.pdf)][[Code](https://github.com/facebookresearch/fairseq/blob/main/examples/bart)], 2020.
6. **Multilingual denoising pre-training for neural machine translation.** `Transactions of the Association for Computational Linguistics`  
    _Yinhan Liu, Jiatao Gu, Naman Goyal, Xian Li, Sergey Edunov, Marjan Ghazvininejad, Mike Lewis, Luke Zettlemoyer._ [[PDF](https://arxiv.org/pdf/2001.08210)][[Code](https://github.com/facebookresearch/fairseq/blob/main/examples/mbart)], 2020.

### 基于 Decoder-only 架构的大语言模型

1. **Improving language understanding by generative pre-training.** `Online`  
    _Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever._ [[PDF](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)], 2018.
2. **Language models are unsupervised multitask learners.** `Online`  
    _Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever._ [[PDF](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)], 2019.
3. **Language models are few-shot learners.** `NeurIPS`  
    _Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei._ [[PDF](https://papers.nips.cc/paper_files/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf)], 2020.
4. **Evaluating Large Language Models Trained on Code.** `arXiv`  
    _Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov, Alethea Power, Lukasz Kaiser, Mohammad Bavarian, Clemens Winter, Philippe Tillet, Felipe Petroski Such, Dave Cummings, Matthias Plappert, Fotios Chantzis, Elizabeth Barnes, Ariel Herbert-Voss, William Hebgen Guss, Alex Nichol, Alex Paino, Nikolas Tezak, Jie Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain, William Saunders, Christopher Hesse, Andrew N. Carr, Jan Leike, Josh Achiam, Vedant Misra, Evan Morikawa, Alec Radford, Matthew Knight, Miles Brundage, Mira Murati, Katie Mayer, Peter Welinder, Bob McGrew, Dario Amodei, Sam McCandlish, Ilya Sutskever, Wojciech Zaremba._ [[PDF](https://arxiv.org/pdf/2107.03374)], 2021.
5. **WebGPT: Browser-assisted question-answering with human feedback.** `arXiv`  
    _Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, Xu Jiang, Karl Cobbe, Tyna Eloundou, Gretchen Krueger, Kevin Button, Matthew Knight, Benjamin Chess, John Schulman._ [[PDF](https://arxiv.org/pdf/2112.09332)], 2021.
6. **Training language models to follow instructions with human feedback.** `NeurIPS`  
    _Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, Ryan Lowe._ [[PDF](https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf)], 2022.
7. **Introducing chatgpt.** `Online`  
    _OpenAI._ [[PDF](https://openai.com/blog/chatgpt)], 2023.
8. **Gpt-4 technical report.** `Online`  
    _OpenAI._ [[PDF](https://openai.com/index/gpt-4-research)], 2023.
9. **Gpt-4 technical report.** `Online`  
    _OpenAI._ [[PDF](https://openai.com/index/hello-gpt-4o)], 2024.
10. **Gpt-4 technical report.** `Online`  
    _OpenAI._ [[PDF](https://openai.com/index/hello-gpt-4o)], 2024.
11. **LLaMA: Open and Efficient Foundation Language Models.** `arXiv`  
    _Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, Guillaume Lample._ [[PDF](https://arxiv.org/pdf/2302.13971)][[Code](https://github.com/facebookresearch/llama)], 2023.
12. **Llama 2: Open Foundation and Fine-Tuned Chat Models.** `arXiv`  
    _Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, Thomas Scialom._ [[PDF](https://arxiv.org/pdf/2307.09288)][[Code](https://github.com/facebookresearch/llama/)], 2023.
13. **Introducing Meta Llama 3: The most capable openly available LLM to date.** `Online`  
    _Meta AI._ [[PDF](https://ai.meta.com/blog/meta-llama-3/)][[Code](https://github.com/meta-llama/llama3)], 2024.
14. **Alpaca: A Strong, Replicable Instruction-Following Model.** `Online`  
    _Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin, Percy Liang, Tatsunori B. Hashimoto._ [[PDF](https://crfm.stanford.edu/2023/03/13/alpaca.html)][[Code](https://github.com/tatsu-lab/stanford_alpaca)], 2023.
15. **Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90%* ChatGPT Quality.** `Online`  
    _The Vicuna Team._ [[PDF](https://lmsys.org/blog/2023-03-30-vicuna)][[Code](https://github.com/lm-sys/FastChat)], 2023.
16. **QLoRA: Efficient Finetuning of Quantized LLMs.** `arXiv`  
    _Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer._ [[PDF](https://arxiv.org/pdf/2305.14314)][[Code](https://github.com/artidoro/qlora)], 2023.
17. **Code Llama: Open Foundation Models for Code.** `arXiv`  
    _Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi, Jingyu Liu, Romain Sauvestre, Tal Remez, Jérémy Rapin, Artyom Kozhevnikov, Ivan Evtimov, Joanna Bitton, Manish Bhatt, Cristian Canton Ferrer, Aaron Grattafiori, Wenhan Xiong, Alexandre Défossez, Jade Copet, Faisal Azhar, Hugo Touvron, Louis Martin, Nicolas Usunier, Thomas Scialom, Gabriel Synnaeve._ [[PDF](https://arxiv.org/pdf/2308.12950)][[Code](https://github.com/facebookresearch/codellama)], 2023.
18. **A Brief Report on LawGPT 1.0: A Virtual Legal Assistant Based on GPT-3.** `arXiv`  
    _Ha-Thanh Nguyen._ [[PDF](https://arxiv.org/pdf/2302.05729)], 2023.
19. **Goat: Fine-tuned LLaMA Outperforms GPT-4 on Arithmetic Tasks.** `arXiv`  
    _Tiedong Liu, Bryan Kian Hsiang Low._ [[PDF](https://arxiv.org/pdf/2305.14201)][[Code](https://github.com/liutiedong/goat)], 2023.
20. **Visual instruction tuning.** `NeurIPS`  
    _Haotian Liu, Chunyuan Li, Qingyang Wu, Yong Jae Lee._ [[PDF](https://papers.nips.cc/paper_files/paper/2023/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf)][[Code](https://llava-vl.github.io/)], 2023.
21. **MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models.** `arXiv`  
    _Deyao Zhu, Jun Chen, Xiaoqian Shen, Xiang Li, Mohamed Elhoseiny._ [[PDF](https://arxiv.org/pdf/2304.10592)][[Code](https://minigpt-4.github.io/)], 2023.

### 非 Transformer 架构

1. **Efficiently modeling long sequences with structured state spaces.** `arXiv`  
    _Albert Gu, Karan Goel, Christopher Ré._ [[PDF](https://arxiv.org/abs/2111.00396)][[Code](https://github.com/state-spaces/s4)], 2021.
2. **On the Parameterization and Initialization of Diagonal State Space Models.** `NeurIPS`  
    _Albert Gu, Karan Goel, Ankit Gupta, Christopher Ré._ [[PDF](https://arxiv.org/abs/2206.11893)], 2022.
3. **RWKV: Reinventing RNNs for the Transformer Era.** `EMNLP`  
    _Bo Peng, Eric Alcaide, Quentin Anthony, Alon Albalak, Samuel Arcadinho, Stella Biderman, Huanqi Cao, Xin Cheng, Michael Chung, Leon Derczynski, Xingjian Du, Matteo Grella, Kranthi Kiran GV, Xuzheng He, Haowen Hou, Przemyslaw Kazienko, Jan Kocon, Jiaming Kong, Bartlomiej Koptyra, Hayden Lau, Jiaju Lin, Krishna Sri Ipsit Mantri, Ferdinand Mom, Atsushi Saito, Guangyu Song, Xiangru Tang, Johan S. Wind, Stanislaw Wozniak, Zhenyuan Zhang, Qinghua Zhou, Jian Zhu, Rui-Jie Zhu_ [[PDF](https://arxiv.org/abs/2305.13048)][[Code](https://github.com/BlinkDL/RWKV-LM)], 2023.
4. **Mamba: Linear-Time Sequence Modeling with Selective State Spaces.** `arXiv`  
    _Albert Gu, Tri Dao._ [[PDF](https://arxiv.org/abs/2312.00752)][[Code](https://github.com/state-spaces/mamba)], 2023.
5. **Learning to (Learn at Test Time): RNNs with Expressive Hidden States.** `arXiv`  
    _Yu Sun, Xinhao Li, Karan Dalal, Jiarui Xu, Arjun Vikram, Genghan Zhang, Yann Dubois, Xinlei Chen, Xiaolong Wang, Sanmi Koyejo, et al._ [[PDF](https://arxiv.org/abs/2407.04620)][[Code](https://github.com/test-time-training/ttt-lm-pytorch)], 2024.

## Prompt 工程

### Prompt 工程简介

1. **A Survey of Large Language Models.** `arXiv`
    
    _Wayne Xin Zhao, Qian Liu, Zhicheng Dou, Jian-Yun Nie, and Ji-Rong Wen._[[PDF](https://arxiv.org/abs/2303.18223)], 2023.
    
2. **LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models** `EMNLP`
    
    _Huiqiang Jiang, Qianhui Wu, Chin-Yew Lin, Yuqing Yang, Lili Qiu._ [[PDF](https://arxiv.org/pdf/2310.05736)] [[Code](https://github.com/microsoft/LLMLingua)], 2023.
    
3. **FIT-RAG: Black-Box RAG with Factual Information and Token Reduction.** `arXiv`
    
    _Yuren Mao, Xuemei Dong, Wenyi Xu, Yunjun Gao, Bin Wei, Ying Zhang._[[PDF](https://arxiv.org/abs/2403.14374)], 2024.
    
4. **DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model** `arXiv`
    
    _DeepSeek-AI._ [[PDF](https://arxiv.org/abs/2405.04434)] [[Code](https://huggingface.co/papers/2405.04434)], 2024.
    
5. **Spider: A Large-Scale Human-Labeled Dataset for Complex and Cross-Domain Semantic Parsing and Text-to-SQL Task.** `EMNLP`
    
    _Tao Yu, Rui Zhang, Kai Yang, Michihiro Yasunaga, Dongxu Wang, Zifan Li, James Ma, Irene Li, Qingning Yao, Shanelle Roman, Zilin Zhang, Dragomir Radev._[[PDF](https://arxiv.org/abs/1809.08887)] [[Code](https://github.com/taoyds/spider)], 2018.
    
6. **Measuring Massive Multitask Language Understanding** `ICLR`
    
    _Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, Jacob Steinhardt._ [[PDF](https://arxiv.org/abs/2009.03300)] [[Code](https://github.com/hendrycks/test)], 2021.
    
7. **FinSQL: Model-Agnostic LLMs-based Text-to-SQL Framework for Financial Analysis.** `SIGMOD`
    
    _Chao Zhang, Yuren Mao, Yijiang Fan, Yu Mi, Yunjun Gao, Lu Chen, Dongfang Lou, Jinshu Lin._[[PDF](https://arxiv.org/abs/2401.10506)] [[Code](https://github.com/bigbigwatermalon/FinSQL)], 2024.
    
8. **Alpaca: A strong, replicable instruction-following model.** `Stanford Center for Research on Foundation Models`
    
    _Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, and Percy Liang._[[PDF](https://crfm.stanford.edu/2023/03/13/alpaca.html)] [[Code](https://github.com/tatsu-lab/stanford_alpaca)], 2023.
    
9. **Wizardcoder: Empowering code large language models with evol-instruct.** `arXiv`
    
    _Ziyang Luo, Can Xu, Pu Zhao, Qingfeng Sun, Xiubo Geng, Wenxiang Hu, Chongyang Tao, Jing Ma, Qingwei Lin, Daxin Jiang._[[PDF](https://arxiv.org/abs/2306.08568)] [[Code](https://wizardlm.github.io/WizardCoder/)], 2023.
    
10. **Generative Agents: Interactive Simulacra of Human Behavior.** `UIST`
    
    _Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein._[[PDF](https://arxiv.org/abs/2304.03442)] [[Code](https://github.com/joonspk-research/generative_agents)], 2023.
    

### 上下文学习

1. **Language Models are Few-Shot Learners** `NeurIPS`
    
    _Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei._ [[PDF](https://arxiv.org/abs/2005.14165)] [[Code](https://github.com/openai/gpt-3)], 2020.
    
2. **An Explanation of In-context Learning as Implicit Bayesian Inference.** `ICLR`
    
    _Sang Michael Xie, Aditi Raghunathan, Percy Liang, Tengyu Ma._[[PDF](https://arxiv.org/abs/2111.02080)], 2022.
    
3. **In-context Learning with Retrieved Demonstrations for Language Models: A Survey.** `arXiv`
    
    _Man Luo, Xin Xu, Yue Liu, Panupong Pasupat, Mehran Kazemi._[[PDF](https://arxiv.org/abs/2401.11624)], 2024.
    
4. **What Makes Good In-Context Examples for GPT-3?** `ACL`
    
    _Jiachang Liu, Dinghan Shen, Yizhe Zhang, Bill Dolan, Lawrence Carin, Weizhu Chen._[[PDF](https://arxiv.org/abs/2101.06804)] [[Code](https://github.com/jiachangliu/KATEGPT3)], 2022.
    
5. **Self-Prompting Large Language Models for Zero-Shot Open-Domain QA** `arXiv`
    
    _Junlong Li, Jinyuan Wang, Zhuosheng Zhang, Hai Zhao._ [[PDF](https://arxiv.org/abs/2212.08635)] [[Code](https://github.com/lockon-n/self-prompting)], 2024.
    
6. **Long Short-Term Memory** `Neural Computation`
    
    _Sepp Hochreiter, Jürgen Schmidhuber._ [[PDF](https://www.bioinf.jku.at/publications/older/2604.pdf)] [[Code](https://github.com/topics/long-short-term-memory)], 1997.
    
7. **The Mystery of In-Context Learning: A Comprehensive Survey on Interpretation and Analysis.** `arXiv`
    
    _Yuxiang Zhou, Jiazheng Li, Yanzheng Xiang, Hanqi Yan, Lin Gui, Yulan He._[[PDF](https://arxiv.org/abs/2311.00237)], 2024.
    
8. **On the Effect of Pretraining Corpora on In-context Learning by a Large-scale Language Model.** `NAACL`
    
    _Seongjin Shin, Sang-Woo Lee, Hwijeen Ahn, Sungdong Kim, HyoungSeok Kim, Boseop Kim, Kyunghyun Cho, Gichang Lee, Woomyoung Park, Jung-Woo Ha, Nako Sung._[[PDF](https://arxiv.org/abs/2204.13509)], 2022.
    
9. **Pretraining task diversity and the emergence of non-Bayesian in-context learning for regression.** `NeurIPS`
    
    _Allan Raventós, Mansheej Paul, Feng Chen, Surya Ganguli._[[PDF](https://arxiv.org/abs/2306.15063)] [[Code](https://github.com/mansheej/icl-task-diversity)], 2023.
    
10. **Data Distributional Properties Drive Emergent In-Context Learning in Transformers** `NeurIPS`

_Stephanie C.Y. Chan, Adam Santoro, Andrew K. Lampinen, Jane X. Wang, Aaditya Singh, Pierre H. Richemond, Jay McClelland, Felix Hill._ [[PDF](https://arxiv.org/abs/2205.05055)] [[Code](https://github.com/google-deepmind/emergent_in_context_learning)], 2022.

11. **Emergent Abilities of Large Language Models.** `Transaction of Machine Learning Research`
    
    _Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou, Donald Metzler, Ed H. Chi, Tatsunori Hashimoto, Oriol Vinyals, Percy Liang, Jeff Dean, William Fedus._[[PDF](https://arxiv.org/abs/2206.07682)], 2022.
    
12. **In-Context Learning Learns Label Relationships but Is Not Conventional Learning** `arXiv`
    
    _Jannik Kossen, Yarin Gal, Tom Rainforth._ [[PDF](https://arxiv.org/abs/2307.12375)] [[Code](https://github.com/jlko/in_context_learning)], 2024.
    
13. **Ground-Truth Labels Matter: A Deeper Look into Input-Label Demonstrations.** `EMNLP`
    
    _Kang Min Yoo, Junyeob Kim, Hyuhng Joon Kim, Hyunsoo Cho, Hwiyeol Jo, Sang-Woo Lee, Sang-goo Lee, Taeuk Kim._[[PDF](https://arxiv.org/abs/2205.12685)], 2022.
    
14. **What In-Context Learning "Learns" In-Context: Disentangling Task Recognition and Task Learning.** `ACL`
    
    _Jane Pan, Tianyu Gao, Howard Chen, Danqi Chen._[[PDF](https://arxiv.org/abs/2305.09731)] [[Code](https://github.com/princeton-nlp/WhatICLLearns)], 2023.
    
15. **Emergent Abilities of Large Language Models.** `Transaction of Machine Learning Research`
    
    _Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou, Donald Metzler, Ed H. Chi, Tatsunori Hashimoto, Oriol Vinyals, Percy Liang, Jeff Dean, William Fedus._[[PDF](https://arxiv.org/abs/2206.07682)], 2022.
    
16. **Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?** `EMNLP`
    
    _Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi, Luke Zettlemoyer._[[PDF](https://arxiv.org/abs/2202.12837)] [[Code](https://github.com/Alrope123/rethinking-demonstrations)], 2022.
    
17. **Unified Demonstration Retriever for In-Context Learning.** `ACL`
    
    _Xiaonan Li, Kai Lv, Hang Yan, Tianyang Lin, Wei Zhu, Yuan Ni, Guotong Xie, Xiaoling Wang, Xipeng Qiu._[[PDF](https://arxiv.org/abs/2305.04320)] [[Code](https://github.com/KaiLv69/UDR)], 2023.
    
18. **Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity.** `ACL`
    
    _Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, Pontus Stenetorp._[[PDF](https://arxiv.org/abs/2104.08786)] [[Code](https://github.com/yaolu/ordered-prompt)], 2022.
    

### 思维链

1. **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.** `NeurIPS`
    
    _Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou._[[PDF](https://arxiv.org/abs/2201.11903)], 2022.
    
2. **Large Language Models are Zero-Shot Reasoners** `NeurIPS`
    
    _Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, Yusuke Iwasawa._ [[PDF](https://arxiv.org/abs/2205.11916)] [[Code](https://github.com/kojima-takeshi188/zero_shot_cot)], 2022.
    
3. **Automatic Chain of Thought Prompting in Large Language Models.** `ICLR`
    
    _Zhuosheng Zhang, Aston Zhang, Mu Li, Alex Smola._[[PDF](https://arxiv.org/abs/2210.03493)] [[Code](https://github.com/amazon-science/auto-cot)], 2023.
    
4. **Tree of Thoughts: Deliberate Problem Solving with Large Language Models.** `NeurIPS`
    
    _Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan._[[PDF](https://arxiv.org/abs/2305.10601)] [[Code](https://github.com/princeton-nlp/tree-of-thought-llm)], 2023.
    
5. **Graph of Thoughts: Solving Elaborate Problems with Large Language Models** `AAAI`
    
    _Maciej Besta, Nils Blach, Ales Kubicek, Robert Gerstenberger, Michal Podstawski, Lukas Gianinazzi, Joanna Gajda, Tomasz Lehmann, Hubert Niewiadomski, Piotr Nyczyk, Torsten Hoefler._ [[PDF](https://arxiv.org/abs/2308.09687)] [[Code](https://github.com/spcl/graph-of-thoughts)], 2024.
    
6. **Self-Consistency Improves Chain of Thought Reasoning in Language Models.** `ICLR`
    
    _Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou._[[PDF](https://arxiv.org/abs/2203.11171)], 2023.
    

### Prompt 技巧

1. **Lost in the middle: How language models use long contexts.** `Transactions of the Association for Computational Linguistics`
    
    _Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang._[[PDF](https://arxiv.org/abs/2307.03172)] [[Code](https://github.com/nelson-liu/lost-in-the-middle)], 2024.
    
2. **C3: Zero-shot Text-to-SQL with ChatGPT** `arXiv`
    
    _Xuemei Dong, Chao Zhang, Yuhang Ge, Yuren Mao, Yunjun Gao, Lu Chen, Jinshu Lin, Dongfang Lou._ [[PDF](https://arxiv.org/abs/2307.07306)] [[Code](https://github.com/bigbigwatermalon/C3SQL)], 2023.
    
3. **PaLM: Scaling Language Modeling with Pathways** `Journal of Machine Learning Research`
    
    _Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, Parker Schuh, Kensen Shi, Sasha Tsvyashchenko, Joshua Maynez, Abhishek Rao, Parker Barnes, Yi Tay, Noam Shazeer, Vinodkumar Prabhakaran, Emily Reif, Nan Du, Ben Hutchinson, Reiner Pope, James Bradbury, Jacob Austin, Michael Isard, Guy Gur-Ari, Pengcheng Yin, Toju Duke, Anselm Levskaya, Sanjay Ghemawat, Sunipa Dev, Henryk Michalewski, Xavier Garcia, Vedant Misra, Kevin Robinson, Liam Fedus, Denny Zhou, Daphne Ippolito, David Luan, Hyeontaek Lim, Barret Zoph, Alexander Spiridonov, Ryan Sepassi, David Dohan, Shivani Agrawal, Mark Omernick, Andrew M. Dai, Thanumalayan Sankaranarayana Pillai, Marie Pellat, Aitor Lewkowycz, Erica Moreira, Rewon Child, Oleksandr Polozov, Katherine Lee, Zongwei Zhou, Xuezhi Wang, Brennan Saeta, Mark Diaz, Orhan Firat, Michele Catasta, Jason Wei, Kathy Meier-Hellstern, Douglas Eck, Jeff Dean, Slav Petrov, Noah Fiedel._ [[PDF](https://arxiv.org/abs/2204.02311)] [[Code](https://github.com/lucidrains/PaLM-pytorch)], 2023.
    
4. **Better Zero-Shot Reasoning with Role-Play Prompting** `arxiv`
    
    _Aobo Kong, Shiwan Zhao, Hao Chen, Qicheng Li, Yong Qin, Ruiqi Sun, Xin Zhou, Enzhi Wang, Xiaohang Dong._ [[PDF](https://arxiv.org/abs/2308.07702)] [[Code](https://github.com/NKU-HLT/Role-Play-Prompting)], 2023.
    

### 相关应用

1. **A survey on large language model based autonomous agents.** `Frontiers of Computer Science`
    
    _Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei, Ji-Rong Wen._[[PDF](https://arxiv.org/abs/2308.11432)] [[Code](https://github.com/paitesanshi/llm-agent-survey)], 2024.
    
2. **Generative Agents: Interactive Simulacra of Human Behavior.** `UIST`
    
    _Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein._[[PDF](https://arxiv.org/abs/2304.03442)] [[Code](https://github.com/joonspk-research/generative_agents)], 2023.
    
3. **HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face.** `Advances in Neural Information Processing Systems`
    
    _Yongliang Shen, Kaitao Song, Xu Tan, Dongsheng Li, Weiming Lu, Yueting Zhuang._[[PDF](https://arxiv.org/pdf/2303.17580)] [[Code](https://github.com/microsoft/JARVIS)], 2023.
    
4. **Garbage in, garbage out: Having useful data is everything.** `Measurement: Interdisciplinary Research and Perspectives`
    
    _L. Todd Rose and Kurt W. Fischer._[[PDF](https://psycnet.apa.org/record/2011-27585-006)], 2011.
    
5. **Will we run out of data? Limits of LLM scaling based on human-generated data.** `arxiv`
    
    _Pablo Villalobos, Colin Raffel, and Tim Dettmers._[[PDF](https://arxiv.org/abs/2211.04325)], 2022.
    
6. **Self-Instruct: Aligning Language Models with Self-Generated Instructions.** `ACL`
    
    _Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi, Hannaneh Hajishirzi._[[PDF](https://arxiv.org/abs/2212.10560)] [[Code](https://github.com/yizhongw/self-instruct)], 2023.
    
7. **C3: Zero-shot Text-to-SQL with ChatGPT** `arXiv`
    
    _Xuemei Dong, Chao Zhang, Yuhang Ge, Yuren Mao, Yunjun Gao, Lu Chen, Jinshu Lin, Dongfang Lou._ [[PDF](https://arxiv.org/abs/2307.07306)] [[Code](https://github.com/bigbigwatermalon/C3SQL)], 2023.
    

## 参数高效微调

### 参数高效微调简介

1. **Efficient Large Language Models: A Survey.** `arXiv`  
    _Zhongwei Wan, Xin Wang, Che Liu, Samiul Alam, Yu Zheng, Jiachen Liu, Zhongnan Qu, Shen Yan, Yi Zhu, Quanlu Zhang, Mosharaf Chowdhury, Mi Zhang._ [[PDF](https://arxiv.org/abs/2312.03863)] [[Code](https://github.com/AIoT-MLSys-Lab/Efficient-LLMs-Survey)], 2023.
2. **A Survey for In-context Learning.** `arXiv`  
    _Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Jingyuan Ma, Rui Li, Heming Xia, Jingjing Xu, Zhiyong Wu, Baobao Chang, Xu Sun, Lei Li, Zhifang Sui._ [[PDF](https://arxiv.org/abs/2301.00234)] [[Code](https://github.com/dqxiu/ICL_PaperList)], 2023.
3. **Instruction Tuning for Large Language Models: A Survey.** `arXiv`  
    _Shengyu Zhang, Linfeng Dong, Xiaoya Li, Sen Zhang, Xiaofei Sun, Shuhe Wang, Jiwei Li, Runyi Hu, Tianwei Zhang, Fei Wu, Guoyin Wang._ [[PDF](https://arxiv.org/abs/2308.10792)] [[Code](https://github.com/dqxiu/ICL_PaperList)], 2023.
4. **Finetuned language models are zero-shot learners.** `arXiv`  
    _Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai, Quoc V. Le._ [[PDF](https://arxiv.org/abs/2109.01652)] [[Code](https://github.com/google-research/flan)], 2021.
5. **Multitask Prompted Training Enables Zero-Shot Task Generalization.** `ICLR`  
    _Victor Sanh et al._ [[PDF](https://arxiv.org/abs/2110.08207)] [[Code](https://github.com/bigscience-workshop/promptsource.git)], 2022.
6. **Instruction in the Wild: A User-based Instruction Dataset.** `GitHub`  
    _Jinjie Ni and Fuzhao Xue and Kabir Jain and Mahir Hitesh Shah and Zangwei Zheng and Yang You._ [[Code](https://github.com/XueFuzhao/InstructionWild)], 2023.
7. **Self-Instruct: Aligning Language Models with Self-Generated Instructions.** `ACL`  
    _Yizhong Wang et al._ [[PDF](https://arxiv.org/abs/2212.10560)] [[Code](https://github.com/yizhongw/self-instruct.git)], 2023.
8. **Llama 2: Open foundation and fine-tuned chat models.** `arXiv`  
    _Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi, Hannaneh Hajishirzi._ [[PDF](https://arxiv.org/abs/2307.09288)] [[Code](https://github.com/meta-llama/llama.git)], 2023.

### 参数附加方法

1. **The Power of Scale for Parameter-Efficient Prompt Tuning.** `EMNLP`  
    _Brian Lester, Rami Al-Rfou, and Noah Constant_ [[PDF](https://arxiv.org/abs/2104.08691)] [[Code](https://github.com/mkshing/Prompt-Tuning.git)], 2021.
2. **Prefix-Tuning: Optimizing Continuous Prompts for Generation.** `ACL`  
    _Xiang Lisa Li and Percy Liang_ [[PDF](https://arxiv.org/abs/2101.00190)] [[Code](https://github.com/XiangLi1999/PrefixTuning.git)], 2021.
3. **Parameter-Efficient Transfer Learning for NLP.** `ICML`  
    _Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin de Laroussilhe, Andrea Gesmundo, Mona Attariyan, Sylvain Gelly._ [[PDF](https://arxiv.org/abs/1902.00751)] [[Code](https://github.com/google-research/adapter-bert.git)], 2019.
4. **AdapterFusion: Non-Destructive Task Composition for Transfer Learning** `` _Jonas Pfeiffer, Aishwarya Kamath, Andreas Rücklé, Kyunghyun Cho, Iryna Gurevych._ [[PDF](https://arxiv.org/abs/2005.00247)] [Code], 2020.
5. **SparseAdapter: An Easy Approach for Improving the Parameter-Efficiency of Adapters.** `Findings of EMNLP`  
    _Shwai He, Liang Ding, Daize Dong, Miao Zhang, Dacheng Tao._ [[PDF](https://arxiv.org/abs/2210.04284)] [[Code](https://github.com/Shwai-He/SparseAdapter.git)], 2022.
6. **Counter-Interference Adapter for Multilingual Machine Translation.** `Findings of EMNLP`  
    _Yaoming Zhu, Jiangtao Feng, Chengqi Zhao, Mingxuan Wang, Lei Li._ [[PDF](https://arxiv.org/abs/2104.08154)] [[Code](https://github.com/Yaoming95/CIAT.git)], 2021.
7. **Tuning Language Models by Proxy.** `arXiv`  
    _Alisa Liu, Xiaochuang Han, Yizhong Wang, Yulia Tsvetkov, Yejin Choi, Noah A. Smith._ [[PDF](https://arxiv.org/abs/2401.08565)] [[Code](https://github.com/alisawuffles/proxy-tuning)], 2024.
8. **Training Neural Networks with Fixed Sparse Masks.** `NIPS`  
    _Yi-Lin Sung, Varun Nair, Colin Raffel_ [[PDF](https://arxiv.org/abs/2111.09839)] [[Code](https://github.com/VITA-Group/ToST)], 2021.

### 参数选择方法

1. **BitFit: Simple Parameter-efficient Fine-tuning for Transformer-based Masked Language-models.** `ACL`  
    _Elad Ben Zaken, Shauli Ravfogel, Yoav Goldberg_ [[PDF](https://arxiv.org/abs/2106.10199)] [[Code](https://github.com/benzakenelad/BitFit.git)], 2022.
2. **What Would Elsa Do? Freezing Layers During Transformer Fine-Tuning.** `arXiv`  
    _Jaejun Lee, Raphael Tang, and Jimmy Lin_ [[PDF](https://arxiv.org/abs/1911.03090)], 2019.
3. **On the Effectiveness of Parameter-Efficient Fine-Tuning.** `AAAI`  
    _Zihao Fu, Haoran Yang, Anthony Man-Cho So, Wai Lam, Lidong Bing, Nigel Collier._ [[PDF](https://arxiv.org/abs/2211.15583)] [[Code](https://github.com/fuzihaofzh/AnalyzeParameterEfficientFinetune.git)], 2023.
4. **Parameter-Efficient Fine-Tuning without Introducing New Latency.** `ACL`  
    _Baohao Liao, Yan Meng, and Christof Monz_ [[PDF](https://arxiv.org/abs/2305.16742)], 2023.
5. **Raise a Child in Large Language Model: Towards Effective and Generalizable Fine-tuning.** `EMNLP`  
    _Runxin Xu, Fuli Luo, Zhiyuan Zhang, Chuanqi Tan, Baobao Chang, Songfang Huang, Fei Huang._ [[PDF](https://arxiv.org/abs/2109.05687)] [[Code](https://github.com/pkunlp-icler/ChildTuning.git)], 2021.
6. **Masking as an Efficient Alternative to Finetuning for Pre-trained Language Models.** `EMNLP`  
    _Mengjie Zhao, Tao Lin, Fei Mi, Martin Jaggi, Hinrich Schütze._ [[PDF](https://arxiv.org/abs/2004.12406)], 2020.
7. **Composable Sparse Fine-Tuning for Cross-Lingual Transfer.** `ACL`  
    _Alan Ansell, Edoardo Maria Ponti, Anna Korhonen, Ivan Vulić._ [[PDF](https://arxiv.org/abs/2110.07560)] [[Code](https://github.com/cambridgeltl/composable-sft.git)], 2022.
8. **GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding.** `ICLR`  
    _Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, Samuel R. Bowman._ [[PDF](https://arxiv.org/abs/1804.07461)] [[Code](https://github.com/nyu-mll/GLUE-baselines.git)], 2019.
9. **The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks.** `ICLR`  
    _Jonathan Frankle and Michael Carbin_ [[PDF](https://arxiv.org/abs/1803.03635)], 2019.
10. **Unified Low-Resource Sequence Labeling by Sample-Aware Dynamic Sparse Finetuning** `EMNLP` _Sarkar Snigdha Sarathi Das, Ranran Haoran Zhang, Peng Shi, Wenpeng Yin, Rui Zhang._ [[PDF](https://arxiv.org/abs/2311.03748)] [[Code](https://github.com/psunlpgroup/FISH-DIP.git)], 2023.

### 低秩适配方法

1. **LoRA: Low-Rank Adaptation of Large Language Models.** `ICLR`  
    _Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen_ [[PDF](https://arxiv.org/abs/2106.09685)] [[Code](https://github.com/microsoft/LoRA)], 2022
2. **Towards a Unified View of Parameter-Efficient Transfer Learning.** `ICLR`  
    _Junxian He, Chunting Zhou, Xuezhe Ma, Taylor Berg-Kirkpatrick, Graham Neubig._ [[PDF](https://arxiv.org/abs/2110.04366)] [[Code](https://github.com/jxhe/unify-parameter-efficient-tuning.git)], 2022.
3. **A Note on LoRA.** `arXiv`  
    _Vlad Fomenko, Han Yu, Jongho Lee, Stanley Hsieh, Weizhu Chen._ [[PDF](https://arxiv.org/abs/2404.05086)], 2024.
4. **KronA: Parameter Efficient Tuning with Kronecker Adapter** `arXiv` _Ali Edalati, Marzieh Tahaei, Ivan Kobyzev, Vahid Partovi Nia, James J. Clark, Mehdi Rezagholizadeh._ [[PDF](https://arxiv.org/abs/2212.10650)], 2022.
5. **Parameter-Efficient Model Adaptation for Vision Transformers.** `AAAI`  
    _Xuehai He,Chunyuan Li,Pengchuan Zhang,Jianwei Yang,Xin Eric Wang._ [[PDF](https://ojs.aaai.org/index.php/AAAI/article/view/25160/24932)], 2023.
6. **DoRA: Weight-Decomposed Low-Rank Adaptation.** `arXiv`  
    _Shih-Yang Liu, Chien-Yi Wang, Hongxu Yin, Pavlo Molchanov, Yu-Chiang Frank Wang, Kwang-Ting Cheng, Min-Hung Chen._ [[PDF](https://arxiv.org/abs/2402.09353)] [[Code](https://github.com/nbasyl/DoRA.git)], 2024.
7. **LoRA Learns Less and Forgets Less** `arXiv` _Dan Biderman, Jose Gonzalez Ortiz, Jacob Portes, Mansheej Paul, Philip Greengard, Connor Jennings, Daniel King, Sam Havens, Vitaliy Chiley, Jonathan Frankle, Cody Blakeney, John P. Cunningham._ [[PDF](https://arxiv.org/abs/2405.09673)], 2024.
8. **GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection** `arXiv` _Jiawei Zhao, Zhenyu Zhang, Beidi Chen, Zhangyang Wang, Anima Anandkumar, Yuandong Tian._ [[PDF](https://arxiv.org/abs/2403.03507)], 2024.
9. **S-LoRA: Serving Thousands of Concurrent LoRA Adapters.** `arXiv`  
    _Ying Sheng, Shiyi Cao, Dacheng Li, Coleman Hooper, Nicholas Lee, Shuo Yang, Christopher Chou, Banghua Zhu, Lianmin Zheng, Kurt Keutzer, Joseph E. Gonzalez, Ion Stoica._ [[PDF](https://arxiv.org/abs/2311.03285)] [[Code](https://github.com/S-LoRA/S-LoRA.git)], 2023.
10. **Sparse Low-rank Adaptation of Pre-trained Language Models.** `EMNLP`  
    _Ning Ding, Xingtai Lv, Qiaosen Wang, Yulin Chen, Bowen Zhou, Zhiyuan Liu, Maosong Sun._ [[PDF](https://arxiv.org/abs/2311.11696)] [[Code](https://github.com/TsinghuaC3I/SoRA)], 2023.
11. **DoRA: Enhancing Parameter-Efficient Fine-Tuning with Dynamic Rank Distribution.** `arXiv`  
    _Yulong Mao, Kaiyu Huang, Changhao Guan, Ganglin Bao, Fengran Mo, Jinan Xu_ [[PDF](https://arxiv.org/abs/2405.17357)] [[Code](https://github.com/MIkumikumi0116/DoRA)], 2024.
12. **ReLoRA: High-Rank Training Through Low-Rank Updates.** `NIPS Workshop`  
    _Vladislav Lialin, Namrata Shivagunde, Sherin Muckatira, Anna Rumshisky._ [[PDF](https://arxiv.org/abs/2307.05695)] [[Code](https://github.com/Guitaricet/relora)],2023.
13. **SLTrain: a sparse plus low-rank approach for parameter and memory efficient pretraining.** `arXiv`  
    _Andi Han, Jiaxiang Li, Wei Huang, Mingyi Hong, Akiko Takeda, Pratik Jawanpuria, Bamdev Mishra._ [[PDF](https://arxiv.org/abs/2406.02214)] [[Code](https://github.com/andyjm3/SLTrain)], 2024.
14. **Pissa: Principal singular values and singular vectors adaptation of large language models.** `arXiv`  
    _Fanxu Meng, Zhaohui Wang, Muhan Zhang_ [[PDF](https://arxiv.org/abs/2404.02948)] [[Code](https://github.com/GraphPKU/PiSSA)], 2024.
15. **MiLoRA: Harnessing Minor Singular Components for Parameter-Efficient LLM Finetuning.** `arXiv`  
    _Hanqing Wang, Zeguan Xiao, Yixia Li, Shuo Wang, Guanhua Chen, Yun Chen._ [[PDF](https://arxiv.org/abs/2406.09044)], 2024.
16. **A Survey on LoRA of Large Language Models.** `arXiv`  
    _Yuren Mao, Yuhang Ge, Yijiang Fan, Wenyi Xu, Yu Mi, Zhonghao Hu, Yunjun Gao._ [[PDF](https://arxiv.org/abs/2407.11046)] [[Code](https://github.com/ZJU-LLMs/Awesome-LoRAs.git)], 2024.
17. **Parameter-efficient fine-tuning of large-scale pre-trained language models.** `Nat. Mac. Intell.`  
    _Ding, Ning, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu._ [[PDF](https://www.nature.com/articles/s42256-023-00626-4.pdf)], 2023.
18. **LoTR: Low Tensor Rank Weight Adaptation.** `arXiv`  
    _Daniel Bershatsky, Daria Cherniuk, Talgat Daulbaev, Aleksandr Mikhalev, Ivan Oseledets._ [[PDF](https://arxiv.org/abs/2402.01376)], 2024.
19. **MoRA: High-Rank Updating for Parameter-Efficient Fine-Tuning.** `arXiv`  
    _Ting Jiang, Shaohan Huang, Shengyue Luo, Zihan Zhang, Haizhen Huang, Furu Wei, Weiwei Deng, Feng Sun, Qi Zhang, Deqing Wang, Fuzhen Zhuang._ [[PDF](https://arxiv.org/abs/2405.12130)] [[Code](https://github.com/kongds/MoRA)], 2024.
20. **Chain of LoRA: Efficient Fine-tuning of Language Models via Residual Learning.** `arXiv`  
    _Wenhan Xia, Chengwei Qin, Elad Hazan._ [[PDF](https://arxiv.org/abs/2401.04151)], 2024.
21. **Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning.** `ACL/IJCNLP`  
    _Armen Aghajanyan, Luke Zettlemoyer, Sonal Gupta._ [[PDF](https://arxiv.org/abs/2012.13255)],2021.
22. **Mini-Ensemble Low-Rank Adapters for Parameter-Efficient Fine-Tuning.** `arXiv`  
    _Pengjie Ren, Chengshun Shi, Shiguang Wu, Mengqi Zhang, Zhaochun Ren, Maarten de Rijke, Zhumin Chen, Jiahuan Pei_ [[PDF](https://arxiv.org/abs/2402.17263)], 2024.
23. **LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning.** `arXiv`  
    _Rui Pan, Xiang Liu, Shizhe Diao, Renjie Pi, Jipeng Zhang, Chi Han, Tong Zhang._ [[PDF](https://arxiv.org/abs/2403.17919)] [[Code](https://github.com/OptimalScale/LMFlow)], 2024.
24. **Chain of LoRA: Efficient Fine-tuning of Language Models via Residual Learning.** `arXiv`  
    _Wenhan Xia, Chengwei Qin, and Elad Hazan_ [[PDF](https://arxiv.org/abs/2401.04151)], 2024.
25. **Adaptive Budget Allocation for Parameter-Efficient Fine-Tuning.** `ICLR`  
    _Qingru Zhang, Minshuo Chen, Alexander Bukharin, Nikos Karampatziakis, Pengcheng He, Yu Cheng, Weizhu Chen, Tuo Zhao._ [[PDF](https://arxiv.org/abs/2303.10512)] [[Code](https://github.com/QingruZhang/AdaLoRA.git)], 2023.
26. **LoraHub: Efficient Cross-Task Generalization via Dynamic LoRA Composition.** `CoLM`  
    _Chengsong Huang, Qian Liu, Bill Yuchen Lin, Tianyu Pang, Chao Du, Min Lin._ [[PDF](https://arxiv.org/abs/2307.13269)] [[Code](https://github.com/sail-sg/lorahub.git)], 2023.
27. **Dylora: Parameter efficient tuning of pre-trained models using dynamic search-free low-rank adaptation** `EACL` _Mojtaba Valipour, Mehdi Rezagholizadeh, Ivan Kobyzev, Ali Ghodsi._ [[PDF](https://arxiv.org/abs/2210.07558)] [[Code](github.com/huawei-noah/Efficient-NLP/tree/main/DyLoRA)], 2023.
28. **DoRA: Enhancing Parameter-Efficient Fine-Tuning with Dy-namic Rank Distribution** `arXiv` _Yulong Mao, Kaiyu Huang, Changhao Guan, Ganglin Bao, Fengran Mo, Jinan Xu._ [[PDF](https://arxiv.org/abs/2405.17357)] [[Code](https://github.com/MIkumikumi0116/DoRA.git)],2023.

### 实践与应用

1. **FinSQL: Model-Agnostic LLMs-based Text-to-SQL Framework for Financial Analysis.** `SIGMOD`  
    _Chao Zhang, Yuren Mao, Yijiang Fan, Yu Mi, Yunjun Gao, Lu Chen, Dongfang Lou, Jinshu Lin._ [[PDF](https://arxiv.org/abs/2401.10506)], 2024.
2. **TabLLM: Few-shot Classification of Tabular Data with Large Language Models.** `AISTATS`  
    _Stefan Hegselmann, Alejandro Buendia, Hunter Lang, Monica Agrawal, Xiaoyi Jiang, David Sontag._ [[PDF](https://proceedings.mlr.press/v206/hegselmann23a/hegselmann23a.pdf)], 2023.

## 模型编辑

### 模型编辑简介

1. **Knowledge Editing for Large Language Models: A Survey.** `arXiv`  
    _Song Wang, Yaochen Zhu, Haochen Liu, Zaiyi Zheng, Chen Chen, Jundong Li._ [[PDF](https://arxiv.org/abs/2310.16218)], 2023
2. **A Comprehensive Study of Knowledge Editing for Large Language Models.** `arXiv`  
    _Ningyu Zhang, Yunzhi Yao, Bozhong Tian, Peng Wang, Shumin Deng, Mengru Wang, Zekun Xi, Shengyu Mao, Jintian Zhang, Yuansheng Ni, Siyuan Cheng, Ziwen Xu, Xin Xu, Jia-Chen Gu, Yong Jiang, Pengjun Xie, Fei Huang, Lei Liang, Zhiqiang Zhang, Xiaowei Zhu, Jun Zhou, Huajun Chen._ [[PDF](https://arxiv.org/abs/2401.01286)][[Code](https://github.com/zjunlp/EasyEdit)], 2024
3. **Editing Large Language Models: Problems, Methods, and Opportunities.** `EMNLP`  
    _Yunzhi Yao, Peng Wang, Bozhong Tian, Siyuan Cheng, Zhoubo Li, Shumin Deng, Huajun Chen, Ningyu Zhang._ [[PDF](https://arxiv.org/abs/2305.13172)][[Code](https://github.com/zjunlp/EasyEdit)], 2023
4. **A Survey on Knowledge Editing of Neural Networks.** `arXiv`  
    _Vittorio Mazzia, Alessandro Pedrani, Andrea Caciolai, Kay Rottmann, Davide Bernardi._ [[PDF](https://arxiv.org/abs/2310.19704)], 2023

### 模型编辑经典方法

1. **Memory-Based Model Editing at Scale.** `ICML`  
    _Eric Mitchell, Charles Lin, Antoine Bosselut, Christopher D. Manning, Chelsea Finn._ [[PDF](https://proceedings.mlr.press/v162/mitchell22a.html?_hsenc=p2ANqtz-8PcBZg33YLCBAVdcZ55PYZXm2xs6OJ8qM1z5cu9NWDbYyx8ey70v--e65rovexQfK34-tjgKdTMqKyU1nNVowzXjY-bA&_hsmi=226067236&utm_source=pocket_mylist)][[Code](https://sites.google.com/view/serac-editing)], 2022
2. **Fixing Model Bugs with Natural Language Patches.** `EMNLP`  
    _Shikhar Murty, Christopher D. Manning, Scott M. Lundberg, Marco Túlio Ribeiro._ [[PDF](https://arxiv.org/abs/2211.03318)], 2022
3. **Calibrating Factual Knowledge in Pretrained Language Models.** `EMNLP`  
    _Qingxiu Dong, Damai Dai, Yifan Song, Jingjing Xu, Zhifang Sui, Lei Li._ [[PDF](https://arxiv.org/abs/2210.03329)][[Code](https://github.com/dqxiu/CaliNet)], 2022
4. **Transformer-Patcher: One Mistake Worth One Neuron.** `ICLR`  
    _Zeyu Huang, Yikang Shen, Xiaofeng Zhang, Jie Zhou, Wenge Rong, Zhang Xiong._ [[PDF](https://arxiv.org/abs/2301.09785)][[Code](https://github.com/ZeroYuHuang/Transformer-Patcher)], 2023
5. **Aging with GRACE: Lifelong Model Editing with Discrete Key-Value Adaptors.** `NeurIPS`  
    _Tom Hartvigsen, Swami Sankaranarayanan, Hamid Palangi, Yoon Kim, Marzyeh Ghassemi._ [[PDF](https://proceedings.neurips.cc/paper_files/paper/2023/hash/95b6e2ff961580e03c0a662a63a71812-Abstract-Conference.html)][[Code](https://github.com/thartvigsen/grace)], 2023
6. **Meta-learning in neural networks: A survey.** `IEEE transactions on pattern analysis and machine intelligence`  
    _Timothy Hospedales, Antreas Antoniou, Paul Micaelli, Amos Storkey._ [[PDF](https://ieeexplore.ieee.org/abstract/document/9428530)], 2021
7. **Editable Neural Networks.** `ICLR`  
    _Anton Sinitsin, Vsevolod Plokhotnyuk, Dmitry V. Pyrkin, Sergei Popov, Artem Babenko._ [[PDF](https://arxiv.org/abs/2004.00345)][[Code](https://github.com/xtinkt/editable)], 2020
8. **Editing Factual Knowledge in Language Models.** `EMNLP`  
    _Nicola De Cao, Wilker Aziz, Ivan Titov._ [[PDF](https://arxiv.org/abs/2104.08164)][[Code](https://github.com/nicola-decao/KnowledgeEditor)], 2021
9. **Fast Model Editing at Scale.** `ICLR`  
    _Eric Mitchell, Charles Lin, Antoine Bosselut, Chelsea Finn, Christopher D. Manning._ [[PDF](https://arxiv.org/abs/2110.11309)][[Code](https://sites.google.com/view/mend-editing)], 2022
10. **Transformer Feed-Forward Layers Are Key-Value Memories.** `EMNLP`  
    _Mor Geva, Roei Schuster, Jonathan Berant, Omer Levy._ [[PDF](https://arxiv.org/abs/2012.14913)][[Code](https://github.com/mega002/ff-layers/)], 2021
11. **Knowledge Neurons in Pretrained Transformers.** `ACL`  
    _Damai Dai, Li Dong, Yaru Hao, Zhifang Sui, Baobao Chang, Furu Wei._ [[PDF](https://arxiv.org/abs/2104.08696)][[Code](https://github.com/Hunter-DDM/knowledge-neurons)], 2022
12. **Locating and Editing Factual Associations in GPT.** `NeurIPS`  
    _Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov._ [[PDF](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html)][[Code](https://github.com/kmeng01/rome)], 2022
13. **Mass-Editing Memory in a Transformer.** `ICLR`  
    _Kevin Meng, Arnab Sen Sharma, Alex J. Andonian, Yonatan Belinkov, David Bau._ [[PDF](https://arxiv.org/abs/2210.07229)][[Code](https://github.com/kmeng01/memit)], 2023

### 附加参数法：T-Patcher

1. **Transformer-Patcher: One Mistake Worth One Neuron.** `ICLR`  
    _Zeyu Huang, Yikang Shen, Xiaofeng Zhang, Jie Zhou, Wenge Rong, Zhang Xiong._ [[PDF](https://arxiv.org/pdf/2301.09785)][[Code](https://github.com/ZeroYuHuang/Transformer-Patcher)], 2023

### 定位编辑法：ROME

1. **Locating and Editing Factual Associations in GPT.** `NeurIPS`  
    _Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov._ [[PDF](https://arxiv.org/pdf/2202.05262)][[Code](https://github.com/kmeng01/rome)], 2022
2. **Mass-Editing Memory in a Transformer.** `ICLR`  
    _Kevin Meng, Arnab Sen Sharma, Alex J. Andonian, Yonatan Belinkov, David Bau._ [[PDF](https://arxiv.org/pdf/2210.07229)][[Code](https://github.com/kmeng01/memit)], 2023

### 模型编辑应用

1. **Scalable Extraction of Training Data from (Production) Language Models.** `arXiv`  
    _Milad Nasr, Nicholas Carlini, Jonathan Hayase, Matthew Jagielski, A Feder Cooper, Daphne Ippolito, Christopher A. Choquette-Choo, Eric Wallace, Florian Tramèr, Katherine Lee._ [[PDF](https://arxiv.org/pdf/2311.17035)], 2023
2. **DEPN: Detecting and Editing Privacy Neurons in Pretrained Language Models.** `arXiv`  
    _Xinwei Wu, Junzhuo Li, Minghui Xu, Weilong Dong, Shuangzhi Wu, Chao Bian, Deyi Xiong._ [[PDF](https://arxiv.org/pdf/2310.20138)][[Code](https://github.com/flamewei123/DEPN)], 2023
3. **Transformer Feed-Forward Layers Build Predictions by Promoting Concepts in the Vocabulary Space.** `arXiv`  
    _Mor Geva, Avi Caciularu, Kevin Ro Wang, Yoav Goldberg._ [[PDF](https://arxiv.org/pdf/2203.14680)][[Code](https://github.com/aviclu/ffn-values.)], 2022
4. **Locating and Mitigating Gender Bias in Large Language Models.** `arXiv`  
    _Yuchen Cai, Ding Cao, Rongxi Guo, Yaqin Wen, Guiquan Liu, Enhong Chen._ [[PDF](https://arxiv.org/pdf/2403.14409)], 2024
5. **Debiasing Algorithm through Model Adaptation.** `arXiv`  
    _Tomasz Limisiewicz, David Mareček, Tomáš Musil._ [[PDF](https://arxiv.org/pdf/2310.18913)][[Code](https://github.com/tomlimi/DAMA)], 2023

## 检索增强生成

### 检索增强生成简介

1. **No free lunch theorems for optimization.** `IEEE Transactions on Evolutionary Computation`  
    _David H. Wolp ert, William G. Macready_ [[PDF](https://ieeexplore.ieee.org/document/585893)], 1997
2. **Retrieval-augmented generation for knowledge-intensive nlp tasks.** `NeurIPS`  
    _Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela_ [[PDF](https://proceedings.neurips.cc/paper/2020/file/6b493230205f780e1bc26945df7481e5-Paper.pdf)], 2020

### 检索增强生成架构

1. **In-context retrieval-augmented language models.** `Transactions of the Association for Computational Linguistics`  
    _Ori Ram, Yoav Levine, Itay Dalmedigos, Dor Muhlgay, Amnon Shashua, Kevin Leyton-Brown, Yoav Shoham._ [[PDF](https://arxiv.org/pdf/2302.00083)][[Code](https://github.com/ai21labs/in-context-ralm)], 2023
2. **Replug: Retrieval-augmented black-box language models.** `arXiv`  
    _Weijia Shi, Sewon Min, Michihiro Yasunaga, Minjoon Seo, Rich James, Mike Lewis, Luke Zettlemoyer, Wen-tau Yih._ [[PDF](https://arxiv.org/abs/2301.12652)], 2023
3. **Atlas: Few-shot learning with retrieval augmented language models.** `Journal of Machine Learning Research`  
    _Gautier Izacard, Patrick Lewis, Maria Lomeli, Lucas Hosseini, Fabio Petroni, Timo Schick, Jane Dwivedi-Yu, Armand Joulin, Sebastian Riedel, Edouard Grave._ [[PDF](https://arxiv.org/pdf/2208.03299)][[Code](https://github.com/facebookresearch/atlas)], 2023
4. **Improving language models by retrieving from trillions of tokens.** `ICML` _Sebastian Borgeaud, Arthur Mensch, Jordan Hoffmann, Trevor Cai, Eliza Rutherford, Katie Millican, George Bm Van Den Driessche, Jean-Baptiste Lespiau, Bogdan Damoc, Aidan Clark._ [[PDF](https://arxiv.org/pdf/2112.04426)][[Code](https://github.com/lucidrains/RETRO-pytorch)], 2022
5. **Augmentation-Adapted Retriever Improves Generalization of Language Models as Generic Plug-In.** `arXiv` _Zichun Yu, Chenyan Xiong, Shi Yu, Zhiyuan Liu_. [[PDF](https://arxiv.org/abs/2305.17331)][[Code](https://github.com/openmatch/augmentation-adapted-retriever)], 2023
6. **Self-rag: Learning to retrieve, generate, and critique through self-reflection.** `arXiv`  
    _Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, Hannaneh Hajishirzi._ [[PDF](https://arxiv.org/abs/2310.11511)][[Code](https://github.com/AkariAsai/self-rag)], 2023

### 知识检索

1. **The Chronicles of RAG: The Retriever, the Chunk and the Generator.** `arXiv`  
    _Paulo Finardi, Leonardo Avila, Rodrigo Castaldoni, Pedro Gengo, Celio Larcher, Marcos Piau, Pablo Costa, Vinicius Carid{'a}_. [[PDF](https://arxiv.org/abs/2401.07883)], 2024
2. **LLM-Augmented Retrieval: Enhancing Retrieval Models Through Language Models and Doc-Level Embedding.** `arXiv`  
    _Mingrui Wu, Sheng Cao_. [[PDF](https://arxiv.org/abs/2404.05825)], 2024
3. **Generate rather than retrieve: Large language models are strong context generators.** `ICLR`  
    _Wenhao Yu, Dan Iter, Shuohang Wang, Yichong Xu, Mingxuan Ju, Soumya Sanyal, Chenguang Zhu, Michael Zeng, Meng Jiang._ [[PDF](https://arxiv.org/pdf/2209.10063)][[Code](https://github.com/wyu97/GenRead)], 2023
4. **An information-theoretic perspective of tf--idf measures.** `IPM`  
    _Akiko Aizawa._ [[PDF](https://doi.org/10.1016/S0306-4573\(02\)00021-3)], 2003
5. **The probabilistic relevance framework: BM25 and beyond.** `Foundations and Trends in Information Retrieval`  
    _Stephen Robertson, Hugo Zaragoza._ [[PDF](https://dl.acm.org/doi/10.1561/1500000019)], 2009
6. **Investigating the Effects of Sparse Attention on Cross-Encoders.** `ECIR`  
    _Ferdinand Schlatt, Maik Fr{"o}be, Matthias Hagen._ [[PDF](https://arxiv.org/pdf/2312.17649)][[Code](https://github.com/webis-de/ecir-24)], 2024
7. **A Thorough Comparison of Cross-Encoders and LLMs for Reranking SPLADE.** `arXiv`  
    _Herv{'e} D{'e}jean, St{'e}phane Clinchant, Thibault Formal._ [[PDF](https://arxiv.org/abs/2403.10407)], 2024
8. **Dense passage retrieval for open-domain question answering.** `EMNLP`  
    _Vladimir Karpukhin, Barlas O{\u{g}}uz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih._ [[PDF](https://arxiv.org/pdf/2004.04906)][[Code](https://github.com/facebookresearch/DPR)], 2020
9. **Colbert: Efficient and effective passage search via contextualized late interaction over bert.** `SIGIR`  
    _Omar Khattab, Matei Zaharia._ [[PDF](https://arxiv.org/pdf/2004.12832)][[Code](https://github.com/stanford-futuredata/ColBERT)], 2020
10. **Poly-encoders: Transformer architectures and pre-training strategies for fast and accurate multi-sentence scoring.** `arXiv`  
    _Samuel Humeau, Kurt Shuster, Marie-Anne Lachaux, Jason Weston._ [[PDF](https://arxiv.org/abs/1905.01969)][[Code](https://github.com/sfzhou5678/PolyEncoder)], 2019
11. **Transformer memory as a differentiable search index.** `Advances in Neural Information Processing Systems`  
    _Yi Tay, Vinh Tran, Mostafa Dehghani, Jianmo Ni, Dara Bahri, Harsh Mehta, Zhen Qin, Kai Hui, Zhe Zhao, Jai Gupta._ [[PDF](https://arxiv.org/pdf/2202.06991)][[Code](https://github.com/ArvinZhuang/DSI-transformers)], 2022
12. **From matching to generation: A survey on generative information retrieval.** `arXiv`  
    _Xiaoxi Li, Jiajie Jin, Yujia Zhou, Yuyao Zhang, Peitian Zhang, Yutao Zhu, Zhicheng Dou._ [[PDF](https://arxiv.org/abs/2404.14851)], 2024
13. **A Neural Corpus Indexer for Document Retrieval.** `arXiv`  
    _Yujing Wang, Ying Hou, Hong Wang, Ziming Miao, Shibin Wu, Hao Sun, Qi Chen, Yuqing Xia, Chengmin Chi, Guoshuai Zhao, Zheng Liu, Xing Xie, Hao Sun, Weiwei Deng, Qi Zhang, Mao Yang._ [[PDF](https://arxiv.org/abs/2206.02743)], 2022
14. **Multidimensional binary search trees used for associative searching.** `Communications of the ACM`  
    _Jon Louis Bentley._ [[PDF](https://dl.acm.org/doi/10.1145/361002.361007)], 1975
15. **Ball*-tree: Efficient spatial indexing for constrained nearest-neighbor search in metric spaces.** `arXiv`  
    _Mohamad Dolatshah, Ali Hadian, Behrouz Minaei-Bidgoli._ [[PDF](https://arxiv.org/abs/1511.00628)], 2015
16. **Approximate nearest neighbor algorithm based on navigable small world graphs.** `Information Systems`  
    _Yury Malkov, Alexander Ponomarenko, Andrey Logvinov, Vladimir Krylov._ [[PDF](https://doi.org/10.1016/j.is.2013.10.006)], 2014
17. **Non-metric similarity graphs for maximum inner product search.** `Advances in Neural Information Processing Systems`  
    _Stanislav Morozov, Artem Babenko._ [[PDF](https://proceedings.neurips.cc/paper_files/paper/2018/file/229754d7799160502a143a72f6789927-Paper.pdf)][[Code](https://github.com/stanis-morozov/ip-nsw)], 2018
18. **Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs.** `IEEE Transactions on Pattern Analysis and Machine Intelligence`  
    _Yu A Malkov, Dmitry A Yashunin._ [[PDF](https://arxiv.org/pdf/1603.09320)][[Code](https://github.com/nmslib/hnswlib)], 2018
19. **Product quantization for nearest neighbor search.** `IEEE Transactions on Pattern Analysis and Machine Intelligence`  
    _Herve Jegou, Matthijs Douze, Cordelia Schmid._ [[PDF](https://ieeexplore.ieee.org/document/5432202)], 2010
20. **Optimized product quantization for approximate nearest neighbor search.** `CVPR`  
    _Tiezheng Ge, Kaiming He, Qifa Ke, Jian Sun._ [[PDF](https://ieeexplore.ieee.org/document/6619223)], 2013
21. **Searching in one billion vectors: re-rank with source coding.** `ICASSP`  
    _Herv{'e} J{'e}gou, Romain Tavenard, Matthijs Douze, Laurent Amsaleg._ [[PDF](https://arxiv.org/pdf/1102.3828)], 2011
22. **Is ChatGPT good at search? Investigating large language models as re-ranking agent.** `arXiv`  
    _Weiwei Sun, Lingyong Yan, Xinyu Ma, Pengjie Ren, Dawei Yin, Zhaochun Ren._ [[PDF](https://arxiv.org/abs/2304.09542)][[Code](https://github.com/sunnweiwei/rankgpt)], 2023

### 生成增强

1. **Selfcheckgpt: Zero-resource black-box hallucination detection for generative large language models.** `EMNLP`  
    _Potsawee Manakul, Adian Liusie, Mark JF Gales_ [[PDF](https://aclanthology.org/2023.emnlp-main.557.pdf)] [[Code](https://github.com/potsawee/selfcheckgpt)], 2023
2. **Predicting Question-Answering Performance of Large Language Models through Semantic Consistency.** `arXiv`  
    _Ella Rabinovich, Samuel Ackerman, Orna Raz, Eitan Farchi, Ateret Anaby Tavor_ [[PDF](https://arxiv.org/pdf/2311.01152)], 2020
3. **Large language models struggle to learn long-tail knowledge.** `ICML`  
    _Nikhil Kandpal, Haikang Deng, Adam Roberts, Eric Wallace, Colin Raffel_ [[PDF](https://proceedings.mlr.press/v202/kandpal23a/kandpal23a.pdf)] [[Code](https://github.com/nkandpa2/long_tail_knowledge)], 2023
4. **When not to trust language models: Investigating effectiveness of parametric and non-parametric memories.** `ACL`  
    _Alex Mallen, Akari Asai, Victor Zhong, Rajarshi Das, Hannaneh Hajishirzi, Daniel Khashabi_ [[PDF](https://aclanthology.org/2023.acl-long.546)] [[Code](https://github.com/AlexTMallen/adaptive-retrieval)], 2023
5. **Locating and editing factual associations in GPT.** `NeurIPS`  
    _Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov_ [[PDF](https://proceedings.neurips.cc/paper_files/paper/2022/file/6f1d43d5a82a37e89b0665b33bf3a182-Paper-Conference.pdf)] [[Code](https://github.com/kmeng01/rome)], 2022
6. **Learning to trust your feelings: Leveraging self-awareness in llms for hallucination mitigation.** `arXiv`  
    _Yuxin Liang, Zhuoyang Song, Hao Wang, Jiaxing Zhang_ [[PDF](https://arxiv.org/pdf/2401.15449)][[Code](https://github.com/liangyuxin42/dreamcatcher)], 2024
7. **Improving Language Models via Plug-and-Play Retrieval Feed-back.** `arXiv`  
    _Wenhao Yu, Zhihan Zhang, Zhenwen Liang, Meng Jiang, Ashish Sabharwal_ [[PDF](https://arxiv.org/pdf/2305.14002)], 2023
8. **Demonstrate-search-predict: Composing retrieval and language models for knowledge-intensive nlp.** `arXiv`  
    _Omar Khattab, Keshav Santhanam, Xiang Lisa Li, David Hall, Percy Liang, Christopher Potts, Matei Zaharia_ [[PDF](https://arxiv.org/abs/2212.14024)][[Code](https://github.com/stanfordnlp/dsp)], 2022
9. **Tree of clarifications: Answering ambiguous questions with retrieval-augmented large language models.** `EMNLP`  
    _Gangwoo Kim, Sungdong Kim, Byeongguk Jeon, Joonsuk Park, Jaewoo Kang_ [[PDF](https://aclanthology.org/2023.emnlp-main.63/)][[Code](https://github.com/gankim/tree-of-clarifications)], 2023
10. **Longllmlingua: Accelerating and enhancing llms in long context scenarios via prompt compression.** `arXiv`  
    _Huiqiang Jiang, Qianhui Wu, Xufang Luo, Dongsheng Li, Chin-Yew Lin, Yuqing Yang, Lili Qiu_ [[PDF](https://arxiv.org/abs/2310.06839)][[Code](https://github.com/microsoft/LLMLingua)], 2023
11. **FIT-RAG: Black-Box RAG with Factual Information and Token Reduction.** `ACM Transactions on Information Systems`  
    _Yuren Mao, Xuemei Dong, Wenyi Xu, Yunjun Gao, Bin Wei, Ying Zhang_ [[PDF](https://dl.acm.org/doi/pdf/10.1145/3676957)], 2024
12. **Prca: Fitting black-box large language models for retrieval question answering via pluggable reward-driven contextual adapter.** `EMNLP`  
    _Haoyan Yang, Zhitao Li, Yong Zhang, Jianzong Wang, Ning Cheng, Ming Li, Jing Xiao_ [[PDF](https://aclanthology.org/2023.emnlp-main.326/)], 2023
13. **Triforce: Lossless acceleration of long sequence generation with hierarchical speculative decodingr.** `arXiv`  
    _Hanshi Sun, Zhuoming Chen, Xinyu Yang, Yuandong Tian, Beidi Chen_ [[PDF](https://arxiv.org/abs/2404.11912)][[Code](https://github.com/Infini-AI-Lab/TriForce)], 2024
14. **RAGCache: Efficient Knowledge Caching for Retrieval-Augmented Generation.** `arXiv`  
    _Chao Jin, Zili Zhang, Xuanlin Jiang, Fangyue Liu, Xin Liu, Xuanzhe Liu, Xin Jin_ [[PDF](https://arxiv.org/html/2404.12457v1)], 2024

### 实践与应用

1. **A survey on large language model based autonomous agents.** `Frontiers of Computer Science`  
    _Hanshi Sun, Zhuoming Chen, Xinyu Yang, Yuandong Tian, Beidi Chen_ [[PDF](https://link.springer.com/article/10.1007/s11704-024-40231-1)][[Code](https://github.com/Paitesanshi/LLM-Agent-Survey)], 2024
2. **Multimodal prompt retrieval for generative visual question answering.** `ACL`  
    _Timothy Ossowski, Junjie Hu_ [[PDF](https://aclanthology.org/2023.findings-acl.158.pdf)][[Code](https://github.com/tossowski/MultimodalPromptRetrieval)], 2023
3. **FinTextQA: A Dataset for Long-form Financial Question Answering.** `arXiv`  
    _Jian Chen, Peilin Zhou, Yining Hua, Yingxin Loh, Kehui Chen, Ziyuan Li, Bing Zhu, Junwei Liang_ [[PDF](https://arxiv.org/pdf/2405.09980)], 2024
4. **Retrieval-based controllable molecule generation.** `ICLR`  
    _Zichao Wang, Weili Nie, Zhuoran Qiao, Chaowei Xiao, Richard Baraniuk, Anima Anandkumarn_ [[PDF](https://openreview.net/pdf?id=vDFA1tpuLvk)][[Code](https://github.com/NVlabs/RetMol)], 2022
5. **Re-imagen: Retrieval-augmented text-to-image generator.** `arXiv`  
    _Wenhu Chen, Hexiang Hu, Chitwan Saharia, William W. Cohen_ [[PDF](https://arxiv.org/pdf/2209.14491)], 2022
6. **Using external off-policy speech-to-text mappings in contextual end-to-end automated speech recognition.** `arXiv`  
    _David M. Chan, Shalini Ghosh, Ariya Rastrow, Björn Hoffmeister_ [[PDF](https://arxiv.org/pdf/2301.02736)], 2023
7. **Language models with image descriptors are strong few-shot video-language learners.** `NeurIPS`  
    _Zhenhailong Wang, Manling Li, Ruochen Xu, Luowei Zhou, Jie Lei, Xudong Lin, Shuohang Wang, Ziyi Yang, Chenguang Zhu, Derek Hoiem, Shih-Fu Chang, Mohit Bansal, Heng Ji_ [[PDF](https://papers.neurips.cc/paper_files/paper/2022/file/381ceeae4a1feb1abc59c773f7e61839-Paper-Conference.pdf)][[Code](https://github.com/MikeWangWZHL/VidIL)], 2022

# RWKV

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=86&annotation=undefined) “既保留了推理阶段的高效性,又实现了训练阶段的并行化。”

[Go to annotation](zotero://open-pdf/library/items/YJA93SXQ?page=86&annotation=undefined) “RWKV 模型的核心模块有两个:时间混合模块和 通道混合模块。”

## 1.WKV机制——RWKV的核心