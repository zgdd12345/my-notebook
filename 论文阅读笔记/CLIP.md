# 基本信息：
    1. 姓名：[Alec Radford](https://arxiv.org/search/cs?searchtype=author&query=Radford,+A)<font style="color:rgb(0, 0, 0);">, </font>[Jong Wook Kim](https://arxiv.org/search/cs?searchtype=author&query=Kim,+J+W)<font style="color:rgb(0, 0, 0);">, </font>[Chris Hallacy](https://arxiv.org/search/cs?searchtype=author&query=Hallacy,+C)<font style="color:rgb(0, 0, 0);">, </font>[Aditya Ramesh](https://arxiv.org/search/cs?searchtype=author&query=Ramesh,+A)<font style="color:rgb(0, 0, 0);">, </font>[Gabriel Goh](https://arxiv.org/search/cs?searchtype=author&query=Goh,+G)<font style="color:rgb(0, 0, 0);">, </font>[Sandhini Agarwal](https://arxiv.org/search/cs?searchtype=author&query=Agarwal,+S)<font style="color:rgb(0, 0, 0);">, </font>[Girish Sastry](https://arxiv.org/search/cs?searchtype=author&query=Sastry,+G)<font style="color:rgb(0, 0, 0);">, </font>[Amanda Askell](https://arxiv.org/search/cs?searchtype=author&query=Askell,+A)<font style="color:rgb(0, 0, 0);">, </font>[Pamela Mishkin](https://arxiv.org/search/cs?searchtype=author&query=Mishkin,+P)<font style="color:rgb(0, 0, 0);">, </font>[Jack Clark](https://arxiv.org/search/cs?searchtype=author&query=Clark,+J)<font style="color:rgb(0, 0, 0);">, </font>[Gretchen Krueger](https://arxiv.org/search/cs?searchtype=author&query=Krueger,+G)<font style="color:rgb(0, 0, 0);">, </font>[Ilya Sutskever](https://arxiv.org/search/cs?searchtype=author&query=Sutskever,+I)
    2. 单位：openai
    3. 标题：Learning Transferable Visual Models From Natural Language Supervision
    4. 刊物：ICML2021

# 内容：
**<font style="color:rgb(25, 27, 31);">CLIP(Contrastive Language-Image Pre-Training，以下简称 CLIP) 模型</font>**<font style="color:rgb(25, 27, 31);">是 OpenAI 在 2021 年初发布的用于匹配图像和文本的预训练神经网络模型，可以说是近年来在多模态研究领域的经典之作。该模型直接使用大量的互联网数据进行预训练，在很多任务表现上达到了目前最佳表现（SOTA） 。</font>

## Abstract
State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories. This restricted form of supervision limits their generality and usability since additional labeled data is needed to specify any other visual concept. Learning directly from raw text about images is a promising alternative which leverages a much broader source of supervision. We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch on a dataset of 400 million (image, text) pairs collected from the internet. After pre-training, natural language is used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks. We study the performance of this approach by benchmarking on over 30 different existing computer vision datasets, spanning tasks such as OCR, action recognition in videos, geo-localization, and many types of fine-grained object classification. The model transfers non-trivially to most tasks and is often competitive with a fully supervised baseline without the need for any dataset specific training. For instance, we match the accuracy of the original ResNet-50 on ImageNet zero-shot without needing to use any of the 1.28 million training examples it was trained on. We release our code and pre-trained model weights at [https://github.com/OpenAI/CLIP.](https://github.com/OpenAI/CLIP.)

1. 

## Introduction and Motivation
在计算机视觉中，zero-shot学习主要指研究对unseen datasets的泛化。之前的那些自监督和无监督的方法，主要研究的是特征学习的能力，目标就是学一种泛化性比较好的特征，但即使学到了很好的特征，想应用到下游任务，还是需要有标签的数据做微调，所以有限制，比如下游任务数据不好收集，可能有distribution shift的问题。怎么做到只训练一个模型，后面不再需要微调了呢，这就是作者研究zero-shot迁移的研究动机。借助文本训练了一个又大又好的模型之后，就可以借助这个文本作为引导，很灵活的做zero-shot的迁移学习。

在clip预训练好之后，就有2个编码器，一个是图像编码器，一个是文本编码器，推理时给定一张图片，通过编码器就能得到一个图片的特征，文本那边的输入就是感兴趣的标签有哪些，比如plane，car，dog等，这些词会通过prompt engineering得到对应的句子，比如‘A photo of a plane’,‘A photo of a dog’，有了这些句子以后，送入到文本编码器，就能得到对应的文本特征，这里假设是plane，car，dog这3个，然后拿这3个文本的特征去和那张图片的特征做余弦相似度，计算得到相似度以后再 通过一个softmax得到概率分布，概率最大的那个句子就是在描述这张照片。

## Method
**CLIP的训练过程：**

模型的输入是图片和文字对，

        1. 图片输入到图片的encoder得到一些特征，
        2. 文本输入到文本的encoder得到一些特征，
        3. 每个traning batch里有n个图片-文本对，就能得到n个图片的特征和n个文本的特征，然后在这些特征上做对比学习，对比学习非常灵活，就需要正样本和负样本的定义，其它都是正常套路（不懂对比学习），
        4. 配对的图片-文本对就是正样本，描述的是同一个东西，特征矩阵里对角线上的都是正样本，矩阵中非对角线上的元素都是负样本，有了正负样本，模型就可以通过对比学习的方式去训练了，

不需要任何手工标注。这种无监督的训练方式，是需要大量的训练数据的。

**CLIP的推理过程：**

预训练之后只能得到文本和图片的特征，没有分类头，作者提出一种利用自然语言的方法，**prompt template**。比如对于ImageNet的类别，首先把它变成"A photo of a {object}" 这样一个句子，ImageNet有1000个类，就生成1000个句子，然后这1000个句子通过之前预训练好的文本的encoder能得到1000个文本特征。直接用类别单词去抽取文本特征也可以，但是模型预训练的时候和图片配对的都是句子，推理的时候用单词效果会下降。

把需要分类的图片送入图片的encoder得到特征，拿图片的特征和1000个文本特征算余弦相似性，选最相似的那个文本特征对应的句子，从而完成了分类任务。不局限于这1000个类别，任何类别都可以。**彻底摆脱了categorical label的限制**，训练和推理的时候都不需要提前定义好的标签列表了。

**优点：**相比其它的训练方法，从自然语言的监督信号来学习，有几个好处。首先，不需要再去标注数据，比如用传统方法做分类，需要先确定类别，然后去下载图片再清洗，再标注，现在只需要去下载图片和文本的配对，数据集很容易就做大了，现在的监督对象是文本，而不是N选1的标签了。其次，训练的时候把图片和文本绑在了一起，学到的特征不再单是视觉特征了，而是多模态的特征，和语言连在一起以后，**很容易做zero-shot的迁移学习**。



**Loss function：**

[L2 normalization](https://blog.csdn.net/antkillerfarm/article/details/80475668)

[L1-norm (L1范数) L2-norm(L2范数)](https://www.yuque.com/zhengedaidan-knmgi/ebmqxu/xfxwkad7kynsz6ky)

1. 有两个输入，一个是图片，一个是文本，图片的维度是[n,h,w,c]，文本的维度是[n,l]，l是指序列长度，然后送入到各自的encoder提取特征，image encoder可以是ResNet也可以是Vision Transformer，text encoder可以是CBOW，也可以是Text Transformer，
2. 得到对应的特征之后，再经过一个投射层（即W_i和W_t)，投射层的意义是学习如何从单模态变成多模态，投射完之后再做l2 norm，就得到了最终的用来对比的特征I_e和T_e，
3. 现在有n个图像的特征，和n个文本的特征，接下来就是算consine similarity，算的相似度就是最后要分类的logits，
4. 最后logits和ground truth做交叉熵loss，正样本是对角线上的元素，logits的维度是[n,n]，ground truth label是np.arange(n)，算两个loss，一个是image的，一个是text的，最后把两个loss加起来就平均。这个操作在对比学习中是很常见的，都是用的这种对称式的目标函数。

![](https://cdn.nlark.com/yuque/0/2024/png/29307286/1710143314957-0d96438f-8cb5-453d-989c-5a9c733b994a.png)

![](https://cdn.nlark.com/yuque/0/2024/png/29307286/1710232678710-a115fff6-ec73-4c69-b86d-a1ceccbf6aec.png)

## Result


## Conclusion
