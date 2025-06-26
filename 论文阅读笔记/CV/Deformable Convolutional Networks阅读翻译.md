1. 基本信息：
    1. 姓名：Jifeng Dai，Haozhi Qi，Yuwen Xiong，Yi Li，Guodong Zhang，Han Hu Yichen Wei
    2. 单位：Microsoft Research Asia
    3. 标题：Deformable Convolutional Networks
    4. 刊物：ICCV2017
2. 内容：
    1. Abstract

_Convolutional neural networks (CNNs) are inherently limited to model geometric transformations due to the fixed geometric structures in their building modules. In this work, we introduce two new modules to enhance the transformation modeling capability of CNNs, namely, deformable convolution and deformable RoI pooling. Both are based on the idea of augmenting the spatial sampling locations in the modules with additional offsets and learning the offsets from the target tasks, without additional supervision. The new modules can readily replace their plain counterparts in existing CNNs and can be easily trained end-to-end by standard back-propagation, giving rise to deformable convolutional networks. Extensive experiments validate the performance of our approach. For the first time, we show that learning dense spatial transformation in deep CNNs is effective for sophisticated vision tasks such as object detection and semantic segmentation._

---

由于CNN构建模块中的固定几何结构，本质上仅限于对几何变换进行建模。在这项工作中，我们引入两个新模块来增强CNN的变形建模能力。即，可变形卷积和可变形RoI池化。两者都基于使用从目标任务中学习到的额外偏移量增加模块中的空间采样位置的想法，并且无需额外的监督。新模块可以很容易地替换现有 CNN 中的普通模块，并且可以通过标准反向传播轻松地进行端到端训练，从而产生可变形的卷积网络。大量实验验证了我们方法的性能。我们首次验证了在CNN 中学习密集空间变换对于复杂的视觉任务（如目标检测和语义分割）是有效的。

    2. Introduction

视觉识别的一个难点是适应目标尺度、姿势、视点、部分变形的几何变换或模型的几何变换。一般来说有两种方法，一种是构建具有足够期望变化的训练数据集，一般通过仿射变换增加现有数据集。可以从数据中学习鲁棒的表示，但是训练代价大，模型参数复杂。第二种是使用变换不变的特征和算法。包括SIFT（scale invariant feature transform）和基于滑动窗口的目标检测范式。

pass

我们引入了两个新模块，它们极大地增强了 CNN 建模几何变换的能力。

第一个是可变形卷积，它将二维偏移添加到标准卷积中的常规网格采样位置。它使采样网格能够自由变形。如图Figure1。**偏移量是通过额外的卷积层从前面的特征图中学习**。因此，变形以局部、密集和自适应的方式以输入特征为条件。

![Figure1   3 × 3 标准和可变形卷积中的采样位置示意图。（a）标准卷积的常规采样网格（绿点）。（b）在可变形卷积中具有增强偏移（浅蓝色箭头）的变形采样位置（深蓝色点）。(c)(d) 是 (b) 的特殊情况，表明可变形卷积泛化了缩放、（各向异性）纵横比和旋转的各种变换。](https://cdn.nlark.com/yuque/0/2022/png/29307286/1667742420979-e81f55bf-975b-4cd6-8b14-72179d447bd0.png)

 第二个是可变形的 RoI 池化。它为之前 RoI 池化的常规 bin 分区中的每个 bin 位置添加一个偏移量。类似地，偏移量从前面的特征图和 RoI 中学习，从而可以对不同形状的对象进行自适应局部定位。



    3. Method



    4. Result
    5. Conclusion

