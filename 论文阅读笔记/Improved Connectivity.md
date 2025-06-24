1）文献信息：

1. 姓名：Anil Batra  Suriya Singh  Guan Pang   Saikat Basu   C.V. Jawahar  Manohar Paluri
2. 论文题目：Improved Road Connectivity by Joint Learning of Orientation and Segmentation
3. 刊物：CVPR 2019

2）该文所处理的问题：

增强道路分割的连通性。

3）为什么已有工作不能有效处理该工作：



4）该文采取的思路和方法：

方法分为两个阶段：1.以多任务的方式联合学习道路方向和道路分割。2.细化结果

    1. **方向学习：**

<font style="color:rgb(25, 25, 25);">所谓的“方向学习”，即给道路图增加方向的属性。给道路图中的每个点赋以该点处的道路走向矢量，通过真值矢量的监督信息，使得网络能够捕获相邻点之间的关系信息。</font>

我们将每条路线视为平面上两个连续点之间的定向向量。定向向量提供了每个路段的方向。

我们预测的单位向量指向相同或者相连的相邻路段。

 基于像素交叉熵损失的方向学习在编码表示中构成了连通性的约束，因为学习道路方向有利于提升道路分割的连通性，而且联合学习通常会获得泛化性更好的特征。  

**Motivation:**通过显式地学习相邻像素之间的方向来捕获它们的关系信息。

**生成方向GT：**

假设路网无向。

道路上每个点的取向由该点和其邻接点之间的单位矢量确定。



![](https://cdn.nlark.com/yuque/0/2022/png/29307286/1657008704809-3a555cbd-12dc-4fde-b40f-f0d70299fed2.png)



    2. **联合学习方法：**

****



    3. **连通性细化操作：**

**针对问题：**1.方向预测失败，2.模型将与道路相似的特征误认为道路。

**解决方法：**受到图像修复方法的启发，我们将路段丢失和假阳性结果认为是损坏的道路真值Mask。我们使用图像修复方法修复该Mask即可。

![](https://cdn.nlark.com/yuque/0/2022/png/29307286/1656917749139-49d7e838-f03a-41b2-b9e7-5f6ffeb5fd20.png)

**预训练阶段：**

为了避免过拟合，训练时不会使用分割模型生成的mask，而是使用我们自己在Ground Truth的基础上自己造的数据，表示为![image](https://cdn.nlark.com/yuque/__latex/a94b066276ab7c671f6d0a673d4a93d2.svg)。在预训练阶段，我们将卫星图像X，![image](https://cdn.nlark.com/yuque/__latex/a94b066276ab7c671f6d0a673d4a93d2.svg)以及先前的道路预测结果![image](https://cdn.nlark.com/yuque/__latex/eeb90ec15a0f26903222d8827bff0195.svg)（![image](https://cdn.nlark.com/yuque/__latex/29697bce836193817b70cc8129859ba9.svg)）,作为模型的输入。

****![image](https://cdn.nlark.com/yuque/__latex/4459f7d81e426f72254fa58291c5d633.svg)

**微调阶段：**

在实际使用中对分割结果进行微调的时候，将![image](https://cdn.nlark.com/yuque/__latex/a94b066276ab7c671f6d0a673d4a93d2.svg)换成道路分割结果，表示为![image](https://cdn.nlark.com/yuque/__latex/a5e8faa212780fd7d755593138757279.svg)。

****![image](https://cdn.nlark.com/yuque/__latex/a37a5435d68383186cff841376499581.svg)

在实际使用中T=3，并且f与g相同。

    4. **堆叠多分枝模块：**

堆叠的多分枝CNN同时学习道路方向和分割。堆叠模块能够在不同尺度上计算分割损失和方向损失。我们使用两个堆叠的多分枝模块。但仅在第一个模块中使用特征融合。![](https://cdn.nlark.com/yuque/0/2022/png/29307286/1656923701426-ac190612-f5fd-4ed3-aa57-4cb7b69ff215.png)

多分枝模块如下：

![](https://cdn.nlark.com/yuque/0/2022/png/29307286/1656923723770-0a8c8a65-4bd5-4ec5-b378-ede48a287dc1.png)

**共享编码器：**

学习一个映射函数E，E将输入的图像X映射为编码表示作为两个任务的输入。

                                                        ![image](https://cdn.nlark.com/yuque/__latex/58d339db3fa1cee5051110b93bd00401.svg)

z将被送入堆叠多分枝模块学习粗糙的预测结果



**多分枝的迭代融合：**

**Motivation:**1）大感受野以获取空域的上下文信息。2）迷你编解码结构学习以重复的方式重新校准特征并进行粗略预测。3）信息流通更加顺畅，信息可以从前一个stack流向后一个stack并完善粗略预测结果。

我们用函数![image](https://cdn.nlark.com/yuque/__latex/fc0109663bdc1a0ba67ed64ffb9370ad.svg)定义stack，n是stack的数量。![image](https://cdn.nlark.com/yuque/__latex/556bdf3285f9774227671b690d66ef41.svg)分别表示粗略预测结果中的方向结果和分割结果。

为了从粗糙结果![image](https://cdn.nlark.com/yuque/__latex/556bdf3285f9774227671b690d66ef41.svg)中学习细化结果![image](https://cdn.nlark.com/yuque/__latex/06321c95e917a48f43258ba328e9dc22.svg)，我们为每个任务创建了两个同步分支，每个分支对预测结果进行上采样并进行像素级分类。

![image](https://cdn.nlark.com/yuque/__latex/9e7d3637a15d172228e66a392f5a8702.svg)



    5. **损失函数**

在![image](https://cdn.nlark.com/yuque/__latex/bbde287610dcb235639788bf6f42b693.svg)三个尺度上计算损失。

公式如下：

![image](https://cdn.nlark.com/yuque/__latex/89b28936ee4aa69f9364ecd0fc5bdcd5.svg)

其中，![image](https://cdn.nlark.com/yuque/__latex/613e60c264d6a9c163fccbb81cc6e6a2.svg)为数据集中的输入，![image](https://cdn.nlark.com/yuque/__latex/0a8dfe926ed300ab62fd307c2666282b.svg),![image](https://cdn.nlark.com/yuque/__latex/0edde51a555130f26f36bf6c92b0811d.svg)分别为分割预测函数和方向预测函数。![image](https://cdn.nlark.com/yuque/__latex/79ce3c7a71877c2ff01695e38ade43ca.svg)是尺度。

5）为什么该文方法能解决所处理的问题：



6）该文所获得的好处：



7）该文工作的不足：





8）评估标准：

+ IoU， F1-score



+ (平均路径长度相似性)APLS

  




