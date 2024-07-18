# D-LinkNet:阅读笔记

## 1 论文基本信息

**1.1 姓名：**Lichen Zhou, Chuang Zhang, Ming Wu

**1.2 论文题目：**D-LinkNet: LinkNet with Pretrained Encoder and Dilated Convolution for High
Resolution Satellite Imagery Road Extraction

**1.3 刊物：**CVPR2018

**1.4 链接：**https://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w4/Zhou_D-LinkNet_LinkNet_With_CVPR_2018_paper.pdf

## 2 Abstract、Introduction and Conclusion

Abstract：

本文提出一个名为D-LinkNet的语义分割网络。使用编解码结构、空洞卷积和预训练编码器来解决road extraction任务。

网络由LinkNet结构和空洞卷积层组成。Linenet架构可以高效的计算和存储，空洞卷积可以在不降低特征图精度的情况下扩大感受野。

Introduction:

road extraction方法分三种，对道路进行像素级的标记、提取道路骨干和结合上述二者。

在DeepGlobe Road Extraction Challenge中，从卫星图像提取道路任务被简化为一个二分类问题。将每个像素标记为道路或者背景。本文将此问题视为二值语义分割任务并生成像素级标记的道路。

road extraction from satellite images is still a challenging task due to some special feature of the task.first,输入的高分辨率图像导致网络必须有很大的感受野。其次，road in satellite images are often slender,complex and cover a small part of the image. in this case,保留足够的细节信息非常重要。最后，road have natural connectivity and long span(大跨度).

D-LinkNet使用带pretrained encoder的Linknet作为backbone，并在核心部分增加了空洞卷积层。

## 3 Method



## 4 Experiments



## 5 Summary

