1. 基本信息：
    1. 姓名：Shihua Huang 、Zhichao Lu、 Ran Cheng、 Cheng He
    2. 标题：FaPN: Feature-aligned Pyramid Network for Dense Image Prediction
    3. 刊物：ICCV 2021
2. 内容：
    1. Abstract

However, the issue of feature alignment remains as neglected by most existing approaches for simplicity. Direct pixel addition between upsampled and local features leads to feature maps with misaligned contexts that, in turn, translate to mis-classifications in prediction, especially on object boundaries.

<font style="color:rgb(42, 43, 46);">大多数现有的方法都忽略了特征对齐的问题。</font>**<font style="color:rgb(42, 43, 46);">直接在上采样和局部特征之间添加像素会导致特征映射上下文不对齐，进而转化为预测中的错误分类，特别是在对象边界上。</font>**

<font style="color:rgb(42, 43, 46);">我们提出了一个特征对齐模块，学习像素的转换偏移量，以上下文对齐上采样的更高层次特征，另一个特征选择模块，赋予lower-level feature 更丰富的空域细节。</font>

<font style="color:rgb(42, 43, 46);">然后，我们将这两个模块集成在一个自上而下的金字塔结构中，</font>**<font style="color:rgb(42, 43, 46);">并提出特征对齐金字塔网络(FaPN)。</font>**

<font style="color:rgb(42, 43, 46);">在4个密集预测任务和4个数据集上的大量实验评估证明了FaPN的有效性。当与Faster / Mask RCNN配合使用时，AP / mIoU比FPN整体提高了1.2 - 2.6点。特别是，当集成到MaskFormer中时，我们的FaPN在ADE20K上达到了最高的56.7% mIoU。</font>

    2. Introduction

密集预测任务是计算机视觉任务中需要给每个像素分类的任务的集合。

<font style="color:rgb(42, 43, 46);">密集预测既需要丰富的空间信息用于目标定位，又需要足够的语义信息用于目标分类，这些信息往往存在于不同的分辨率/尺度级别上。有效地生成不同尺度的特征是密集预测任务的重难点。</font>

<font style="color:rgb(42, 43, 46);">重复的上采样与下采样操作加重了特征不对齐的问题，对后续学习产生不利影响，最终导致错误预测。</font>

**<font style="color:rgb(42, 43, 46);">我们提出了一个特征对齐模块，通过调整卷积核中的每个采样位置，学习将上采样的特征图对齐到一组参考特征图。我们进一步提出了一个特征选择模块，自适应地强化包含空间细节信息的自底向上的特征图，以实现精确定位。然后，我们将这两个模块集成在一个自上而下的金字塔结构中，称为特征对齐金字塔网络(FaPN)。</font>**

从概念上讲，FaPN 可以很容易地结合到现有的自下而上的CNN主干网络上。实验结果表明，**<font style="color:rgb(42, 43, 46);">FaPN显著提高了密集预测的性能，特别是对小物体和物体边界的预测。</font>**

<font style="color:rgb(42, 43, 46);">本文关键贡献：</font>

        1. <font style="color:rgb(42, 43, 46);">我们首先开发了一个特征对齐模块，它学习像素的转换偏移量，以上下文对齐上采样(更高级别)的特征;另一个特征选择模块，加强具有丰富空间细节的(低级)特征。</font>
        2. 通过整合上述两个模块，我们提出了特征对齐金字塔 (FaPN)，它是 FPN的增强型替代品，用于生成多尺度特征。
        3. 根据实验，我们证明了我们的 FaPN 与原始 FPN 相比，性能（AP / mIoU）显著提高了 1.2% - 2.6%。
    3. Related Work
        1. **Feature Pyramid Network Backbone**

现有的密集预测方法大致分为两类。一是利用空洞卷积来扩大感受野，以在不降低空间分辨率的情况下捕获长范围依赖关系，DeepLab等。二侧重于构建编解码网络，即自下而上和自上而下的路径。自上而下的路径用于通过逐步上采样将高级语义上下文反向传播到低级特征。有代表性的如转置卷积操作等。

        2. **Feature Alignment**

pass

相比之下，我们提出了一个基于自底向上网络的自顶向下路径，并以渐进的方式将特征从最粗略的分辨率（顶部）对齐到最精细的分辨率（底部）。具体来说，我们只将 2 倍上采样的特征与其对应的自下而上特征对齐。

    4. Feature-aligned Pyramid Network，FaPN

我们方法的框架包括一个特征选择模块（FSM，Feature Selection Module）和一个特征对齐模块（FAM，Feature Alignment Module），如Figure3。

![](https://cdn.nlark.com/yuque/0/2022/png/29307286/1667131064347-2925924a-1568-45f8-a343-4448679a84d8.png)

具体，我们将自底向上网络的第 i 阶段的输出定义为![image](https://cdn.nlark.com/yuque/__latex/b3e446f65eb8aeac98b741ad30fcea2e.svg),相对于输入图像的步幅为 ![image](https://cdn.nlark.com/yuque/__latex/29dd80278cfd3a3c9c5164b67a9700b0.svg) 个像素.

        1. **Feature Alignment Module**

由于递归使用下采样操作，上采样特征图 ![image](https://cdn.nlark.com/yuque/__latex/67ed125b26e6a29a8b7348f1c2910b16.svg)和相应的自底向上特征图 ![image](https://cdn.nlark.com/yuque/__latex/9feb81c3f00b91e3afd5934bc47496d4.svg)之间存在可预见的空间错位。因此，通过元素按位相加或通道维度相加的特征融合方式不利于对目标边界进行预测。因此，在进行特征聚合之前，进行特征对齐必不可少。

在这项工作中，空间位置信息由 2D 特征图表示，其中每个偏移值可以看作是 ![image](https://cdn.nlark.com/yuque/__latex/67ed125b26e6a29a8b7348f1c2910b16.svg)中的每个点与其在 ![image](https://cdn.nlark.com/yuque/__latex/87b9a67db78834bb4ad88889e7253f62.svg)中的对应点之间在 2D 空间中的偏移距离。如下所示，特征对齐可以用数学公式表示为：

![image](https://cdn.nlark.com/yuque/__latex/5f183085668900d16202466d40148181.svg)

其中![image](https://cdn.nlark.com/yuque/__latex/7cc58a6798c2363cb4a532bc1da1d20a.svg)是 ![image](https://cdn.nlark.com/yuque/__latex/87b9a67db78834bb4ad88889e7253f62.svg)和![image](https://cdn.nlark.com/yuque/__latex/f7898af1b37b2fae32565f65041c8218.svg)的concatenation，它提供了上采样特征和对应的自下而上特征之间的空间差异。![image](https://cdn.nlark.com/yuque/__latex/a19fd3817bf218383b0d78a3a1b780c1.svg)和![image](https://cdn.nlark.com/yuque/__latex/d14db6142220ebed645ebefa91656647.svg) 分别表示从空间差异中学习偏移量 (![image](https://cdn.nlark.com/yuque/__latex/becf66343623ddb7a4748fab0fdc618e.svg)) 的函数，并将特征与学习的偏移量对齐。在这项工作中，![image](https://cdn.nlark.com/yuque/__latex/a19fd3817bf218383b0d78a3a1b780c1.svg)和![image](https://cdn.nlark.com/yuque/__latex/d14db6142220ebed645ebefa91656647.svg)使用**可变形卷积**实现，然后是激活函数和相同内核大小的标准卷积。

![](https://cdn.nlark.com/yuque/0/2022/png/29307286/1667136525710-5d0306f8-0ab3-40b5-8d17-5b490d723bea.png)

（_<font style="color:rgb(42, 43, 46);">偏移字段与输入具有相同的分辨率，2N个通道对应N个2D偏移量。具体地，N表示N个采样点的卷积核，例如，对于一个3 × 3的conv, N等于9，并且第N个偏移场中的每个值都是第N个采样点的水平或垂直偏移量。</font>_）

在这里，我们简要回顾一下可变形卷积，并解释为什么它可以用作我们的特征对齐函数并提供一些重要的实现细节。我们首先定义一个输入特征图![image](https://cdn.nlark.com/yuque/__latex/d4454cc0dd213ef9781458829871c7f8.svg)，和一个![image](https://cdn.nlark.com/yuque/__latex/1234d0ee65b8b0ab0d93e60f15fc5aa4.svg)卷积层。那么，卷积操作后任意位置的输出特征 ![image](https://cdn.nlark.com/yuque/__latex/fbaa5ff88e47371f0ed79d4e0f0db3b3.svg)（其中，![image](https://cdn.nlark.com/yuque/__latex/79b128aa415b1340d6f1c23447bf16e2.svg)）可由下式得到:

![image](https://cdn.nlark.com/yuque/__latex/51647d57955304179b97a2925044a0fc.svg)

其中，N是 k × k 卷积层的大小（即 N = k × k），![image](https://cdn.nlark.com/yuque/__latex/fdbdbd009048a1d475873619ee733e11.svg)和![image](https://cdn.nlark.com/yuque/__latex/f41cf3ee91a2162854dc8499e4c8f27d.svg)分别指第 n 个卷积样本位置的权重和预先指定的偏移量。![image](https://cdn.nlark.com/yuque/__latex/d1b36ccc6096ddf2e95cc2fe81ba89cd.svg)。除了预先指定的偏移量之外，可变形卷积还尝试针对不同的样本位置自适应地学习额外的偏移量{![image](https://cdn.nlark.com/yuque/__latex/81dfca507bcc019faace472b8f48428a.svg)}，并且上述等式可以重新表述为：

![image](https://cdn.nlark.com/yuque/__latex/9512a9d3f6dad15df76ed63ff34a6eb9.svg)

其中每个![image](https://cdn.nlark.com/yuque/__latex/ffe5c4d73f623c560bd755b3292ad7b5.svg)是一个元组 ![image](https://cdn.nlark.com/yuque/__latex/49becf65ea0ae5a700d4d46b684cd81d.svg),其中![image](https://cdn.nlark.com/yuque/__latex/3b1dad27bc1c2823be8dfbd33a8b5eed.svg) 和 ![image](https://cdn.nlark.com/yuque/__latex/0dea61ad21104519f8f158ea69a0c163.svg) 。

当我们在![image](https://cdn.nlark.com/yuque/__latex/7a924a5612089a2fe10961736e64ba6b.svg)上应用可变形卷积，并以![image](https://cdn.nlark.com/yuque/__latex/87b9a67db78834bb4ad88889e7253f62.svg) 和 ![image](https://cdn.nlark.com/yuque/__latex/7a924a5612089a2fe10961736e64ba6b.svg) 的连接作为参考（即![image](https://cdn.nlark.com/yuque/__latex/6eb44f6fde608ce21b42d80a14f519c6.svg)可变形卷积可以根据公式 (1)的偏移量调整其卷积样本位置，即根据![image](https://cdn.nlark.com/yuque/__latex/87b9a67db78834bb4ad88889e7253f62.svg)和![image](https://cdn.nlark.com/yuque/__latex/7a924a5612089a2fe10961736e64ba6b.svg)之间的空间距离对齐![image](https://cdn.nlark.com/yuque/__latex/7a924a5612089a2fe10961736e64ba6b.svg)。

        2. **Feature Selection Module**

在缩减通道前，强化包含空间细节的重要特征通道非常重要，以便后续的准确分配，同时抑制冗余特征图。为了替代简单的使用1*1卷积，我们提出了一个特征选择模块（FSM）来明确地对特征图的重要性进行建模并重新校准。

![](https://cdn.nlark.com/yuque/0/2022/png/29307286/1667718993413-cf2ef3da-2cac-4dcd-ac44-e8201656c03f.png)

_Figure5:特征选择模块。_![image](https://cdn.nlark.com/yuque/__latex/14204cb9aecd1ba5f615d522a0fb81f1.svg)_ 和 _![image](https://cdn.nlark.com/yuque/__latex/25b1555a92913264e060d07eaee29d26.svg)_分别为输入和输出特征图，其中_![image](https://cdn.nlark.com/yuque/__latex/3017c4a549b8cca747e7d8524ae3ca65.svg)_和_![image](https://cdn.nlark.com/yuque/__latex/4e8d5b265b1c4407c8e47855c8e52d3f.svg)_,_![image](https://cdn.nlark.com/yuque/__latex/a428bd244ddaa5c11de20ca9cfd9d494.svg)_和_![image](https://cdn.nlark.com/yuque/__latex/b9524e16d8e410f778c005b1e0be7f42.svg)_分别是输入输出通道。_![image](https://cdn.nlark.com/yuque/__latex/e14c0070ecc8767a1fa8a7274215b22b.svg)_是特征重要性向量，_![image](https://cdn.nlark.com/yuque/__latex/836a4cbf45d61ae11cbbaf5440d2f53f.svg)_表示第d个输入特征图的重要性。_![image](https://cdn.nlark.com/yuque/__latex/014becbb1e08f3b5f28d35855ee237ff.svg)_和_![image](https://cdn.nlark.com/yuque/__latex/d27beb2d7658e72a5aa04c398550f187.svg)_分别代表特征重要性建模和特征选择层。_

**<font style="color:rgb(42, 43, 46);">首先，</font>**<font style="color:rgb(42, 43, 46);">通过全局平均池操作提取每个输入特征映射</font>![image](https://cdn.nlark.com/yuque/__latex/38b5152cd62b55b08f9bc8e2f02f91a4.svg)<font style="color:rgb(42, 43, 46);">的全局信息</font>![image](https://cdn.nlark.com/yuque/__latex/8ce572b39ace46d6c7b431732ae0d59b.svg)<font style="color:rgb(42, 43, 46);">，</font><font style="color:rgb(42, 43, 46);">而特征重要性建模层</font>![image](https://cdn.nlark.com/yuque/__latex/250d03ccbbb2331478db0844252939fa.svg)<font style="color:rgb(42, 43, 46);">(即一个1 × 1的卷积层，后面跟着一个sigmoid激活函数)学习使用这些信息对每个特征图的重要性进行建模，并输出一个重要性向量</font>![image](https://cdn.nlark.com/yuque/__latex/77c3adce895348f6083c425fe1ba2624.svg)<font style="color:rgb(42, 43, 46);">。</font>**<font style="color:rgb(42, 43, 46);">随后，</font>**使用重要性向量对原始输入特征图进行缩放，然后将缩放后的特征图添加到原始特征图中，称为重新缩放的特征图。**最后，**在重新缩放的特征图上引入特征选择层 ![image](https://cdn.nlark.com/yuque/__latex/5655f1127387251a8775447ddff5d5d8.svg)（即提高效率的 1×1 卷积层），用于选择性地维护重要的特征图并丢弃无用的特征图以减少通道。

![image](https://cdn.nlark.com/yuque/__latex/66bc59318caa38004db2bc265f72ff83.svg)

其中![image](https://cdn.nlark.com/yuque/__latex/e72419609bb32d2c61f3f2ceebc6ec25.svg),计算如下：

![image](https://cdn.nlark.com/yuque/__latex/226092054856616ff16cec00df333a62.svg)

FSM模块由SENet启发，<font style="color:rgb(42, 43, 46);">其区别在于在输入和缩放特征映射之间引入了额外的跳跃连接。根据经验，我们发现缩放特征的下界(通过跳跃连接)是必不可少的，这避免了任何特定的通道响应被过度放大或被抑制。从概念上讲，这两个模块都学会通过通道注意力自适应地重新校准通道方面的响应。</font>然而，SE 通常用于主干以增强特征提取，而 FSM 用于颈部（即自顶向下路径）以增强多尺度特征聚合。<font style="color:rgb(42, 43, 46);">此外，FSM中的选择/缩放操作所得到的特征也提供给FAM作为学习对齐偏移的参考。</font>

    5. Result

SOTA

    6. Conclusion

本文介绍了特征对齐金字塔网络 (FaPN)，这是一种简单而有效的自上而下的金字塔结构，可生成用于密集图像预测的多尺度特征。它由一个特征对齐模块组成，该模块学习像素的变换偏移，以根据上下文对齐上采样的高级特征；以及一个特征选择模块，用于强调具有丰富空间细节的低级特征。比原始特征金字塔好，此外，FaPN 在集成到强baseline时提高了最先进的分割性能。可以集成到实时分割任务中。

