# ViT: Vision in Transformer学习笔记

​		VIT使用纯粹的Transformer结构并取得了很好的结果，在大规模数据集上比CNN效果更好。该论文展现了Transformer模型的通用性以及为大一统的通用编码器指引道路。

## 概述

​		在原文中的实现上，完全使用原始Bert的transformer结构，主要是对图片转换成类似token的处理，原文引入了一个patch的概念，即将输入图片划分为一个个的patch，然后对于每一个patch转换（flatten操作），转换成类似Bert的输入结构。框架图如下：

![VIT](C:\Users\Administrator\Desktop\笔记\image\VIT.jpg)

