1. 文献信息：
    1. 姓名：Alejandro Newell, Kaiyu Yang, and Jia Deng
    2. 标题：Stacked Hourglass Networks for Human Pose Estimation
    3. 刊物：ECCV 2016
    4. 链接：[知乎](https://zhuanlan.zhihu.com/p/45002720)，[CSDN](https://blog.csdn.net/qq_19784349/article/details/112524305)
2. 文章内容：

本文提出一种级联漏斗网络（Stacked Hourglass Networks， SHN)处理人体姿态估计任务，提升姿态估计的效果。其思想可以扩展到其他方向，例如目标识别中的CornerNet。本文的主要贡献是利用多尺度来识别姿态。

本文的核心思想是使用多尺度的特征，为此设计了<font style="color:rgb(18, 18, 18);">Top-down与Bottom-up结合的网络</font>

![网络由多个堆叠的Hourglass组成。](https://cdn.nlark.com/yuque/0/2022/png/29307286/1668520496316-a4af4295-675f-4008-94fa-098273bc54a7.png)





![单个Hourglass](https://cdn.nlark.com/yuque/0/2022/png/29307286/1668520813634-e4021306-ef86-4b1d-9112-a411b133da60.png)

在Hourglass模块中，卷积和max pooling被用来将特征降到一个很低的分辨率，在每一个<font style="color:rgb(18, 18, 18);">max pooling步骤中，网络产生分支并在原来提前池化的分辨率下使用更多的卷积，当到达最低的分辨率的时候，网络开始upsample并结合不同尺度下的特征。这里upsample（上采样）采用的方法是最近邻插值，之后再将两个特征集按元素位置相加。</font>

<font style="color:rgb(18, 18, 18);">当到达输出分辨率的时候，再接两个1×1的卷积层来进行最后的预测，网络的输出是一组heatmap，对于给定的heatmap，网络预测在每个像素处存在关节的概率。</font>

![](https://cdn.nlark.com/yuque/0/2022/png/29307286/1668607651790-a29020ba-9765-4046-9032-a3d89e9e8280.png)

![根据代码画出来的ResModule](https://cdn.nlark.com/yuque/0/2022/png/29307286/1668608544997-2814fd65-3e3d-4992-822a-2b89e5b294a5.png)



<font style="color:rgb(18, 18, 18);">Hourglass Module由上面的Residual Module组成，由于它是一个递归的结构，所以可以定义一个阶数来表示递归的层数，首先来看一下一阶的Hourglass Module：</font>

![一阶Hourglass Module](https://cdn.nlark.com/yuque/0/2022/png/29307286/1668609458914-e19afcdb-a24b-4a13-8027-744e21cb93b5.png)

<font style="color:rgb(18, 18, 18);">上图中的Max pool代表下采样，Res代表上面介绍的Residual Module，Up Sample代表上采样。多阶的Hourglass Module就是将上图虚线框中的块递归地替换为一阶Hourglass Module，由于作者在实验中使用的是4阶的Hourglass Moudle，所以我们画出了4阶的Hourglass Module的示意图：</font>

![4阶Hourglass Module](https://cdn.nlark.com/yuque/0/2022/png/29307286/1668609585306-955d8c44-d0ff-4afd-a9a5-9eb1d6dd313a.png)

<font style="color:rgb(18, 18, 18);"></font>

<font style="color:rgb(18, 18, 18);"></font>

<font style="color:rgb(18, 18, 18);">网络输入的图片分辨率为256×256，在hourglass模块中的最大分辨率为64×64，整个网络最开始要经过一个7×7的步长为2的卷积层，之后再经过一个残差块和Max pooling层使得分辨率从256降到64。</font>

![](https://cdn.nlark.com/yuque/0/2022/png/29307286/1668611295186-d6d07818-d5b6-4944-b710-a5b7ffa7ad61.png)

<font style="color:rgb(18, 18, 18);"></font>

**Intermediate Supervision（中间监督）：**

<font style="color:rgb(18, 18, 18);">上图中的4阶Hourglass Module就是前面讲的4阶Hourglass Module，可以看到整个网络还是挺庞大的，图中的渐变红色块就是加入了中间监督的地方，即在此处使用loss函数，下面讲一下中间监督。</font>

<font style="color:rgb(18, 18, 18);">作者在整个网络结构中堆叠了许多hourglass模块，从而使得网络能够不断重复自底向上和自顶向下的过程，作者提到采用这种结构的关键是要使用中间监督来对每一个hourglass模块进行预测，即对中间的heatmaps计算损失。</font>

<font style="color:rgb(18, 18, 18);">关于中间监督的位置，作者在文中也进行了讨论。大多数高阶特征仅在较低的分辨率下出现，除非在上采样最后。如果在网络进行上采样后进行监督，则无法在更大的全局上下文中重新评估这些特征；如果我们希望网络能够进行最佳的预测，那么这些预测就不应该在一个局部范围内进行。</font>

<font style="color:rgb(18, 18, 18);">由于hourglass模块整合了局部和全局的信息，若想要网络在早期进行预测，则需要它对图片有一个高层次的理解即使只是整个网络的一部分。最终，作者将中间监督设计在如下图所示位置：</font>

![](https://cdn.nlark.com/yuque/0/2022/png/29307286/1668611913536-b2cbc62d-2c12-45e1-82b8-3fee35c5d357.png)

<font style="color:rgb(18, 18, 18);"></font>

<font style="color:rgb(18, 18, 18);">在整个网络中，作者共使用了8个hourglass模块，需要注意的是，这些hourglass模块的权重不是共享的，并且所有的模块都基于相同的ground truth添加了损失函数。下面介绍训练过程的细节。</font>

<font style="color:rgb(18, 18, 18);"></font>

<font style="color:rgb(18, 18, 18);">所以，每个Hourglass Module的loss是单独计算的，这样使得后面的Hourglass Module能够更好地再评估。</font>

<font style="color:rgb(18, 18, 18);"></font>

<font style="color:rgb(18, 18, 18);"></font>

<font style="color:rgb(18, 18, 18);"></font>

<font style="color:rgb(18, 18, 18);"></font>

<font style="color:rgb(18, 18, 18);"></font>

<font style="color:rgb(18, 18, 18);"></font>

<font style="color:rgb(18, 18, 18);"></font>

<font style="color:rgb(18, 18, 18);"></font>

<font style="color:rgb(18, 18, 18);"></font>

<font style="color:rgb(18, 18, 18);"></font>

<font style="color:rgb(18, 18, 18);"></font>

3. 总结与思考：



