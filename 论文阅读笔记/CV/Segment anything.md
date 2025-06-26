# 基本信息：
    1. 姓名：Alexander Kirillov1,2,4 Eric Mintun2 Nikhila Ravi1,2 Hanzi Mao2 Chloe Rolland3 Laura Gustafson3 Tete Xiao3 Spencer Whitehead Alexander C. Berg Wan-Yen Lo Piotr Doll ́ ar4 Ross Girshick4

1project lead， 2joint first author， 3equal contribution， 4directional lead

    2. 单位：Meta
    3. 标题：Segment anything
    4. 刊物：arXiv

# 主要内容
## 文章内容：


## 该文所处理的问题：
## 为什么已有工作不能有效处理该工作：
## 该文采取的思路和方法：
## 为什么该文方法能解决所处理的问题：
## 该文所获得的好处：
## 该文工作的不足：
# 原文阅读与翻译：
## Abstract
We introduce the Segment Anything (SA) project: a new task, model, and dataset for image segmentation. Using our efficient model in a data collection loop, we built the largest segmentation dataset to date (by far), with over 1 billion masks on 11M licensed and privacy respecting images. The model is designed and trained to be promptable, so it can transfer zero-shot to new image distributions and tasks. We evaluate its capabilities on numerous tasks and find that its zero-shot performance is impressive – often competitive with or even superior to prior fully supervised results. We are releasing the Segment Anything Model (SAM) and corresponding dataset (SA-1B) of 1B masks and 11M images at [https://segment-anything.com](https://segment-anything.com) to foster research into foundation models for computer vision.

## Introduction


## Segment Anything Task


## Segment Anything Model
## Segment Anything Data Engine
## Segment Anything Dataset
## Segment Anything RAI Analysis
## Experiments


## Discussion


# Data-centric
<font style="color:rgb(25, 27, 31);">验证了data-centric AI是未来。模型没有什么特别之处，亮点在数据标注。</font>

![](https://cdn.nlark.com/yuque/0/2024/png/29307286/1710240703935-8bb0a9a5-d6a9-4ba5-b65a-3ad61ff644c9.png)



:::danger
<font style="color:rgb(83, 88, 97);">Data-centric AI is the discipline of systematically engineering the data used to build an AI system.  
</font>_<font style="color:rgb(83, 88, 97);">— Andrew Ng</font>_

:::

<font style="color:rgb(25, 27, 31);">  
</font>**	传统的搭建AI模型的方法主要是去迭代模型，数据相对固定。**比如，我们通常会聚焦于几个[基准数据集](https://www.zhihu.com/search?q=%E5%9F%BA%E5%87%86%E6%95%B0%E6%8D%AE%E9%9B%86&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A%222972047807%22%7D)，然后设计各式各样的模型去提高预测准确率。这种方式我们称作以模型为中心（model-centric）。然而，model-centric没有考虑到实际应用中数据可能出现的各种问题，例如不准确的标签，数据重复和异常数据等。**准确率高的模型只能确保很好地「拟合」了数据，并不一定意味着实际应用中会有很好的表现。**

与model-centric不同，**Data-centric更侧重于提高数据的质量和数量。**也就是说Data-centric AI关注的是数据本身，而模型相对固定。采用Data-centric AI的方法在实际场景中会有更大的潜力，因为数据很大程度上决定了模型能力的上限。

<font style="color:rgb(25, 27, 31);">需要注意的是，</font>**<font style="color:rgb(25, 27, 31);">「Data-centric」与「</font>**[Data-driven](https://www.zhihu.com/search?q=Data-driven&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A%222972047807%22%7D)**<font style="color:rgb(25, 27, 31);">」（数据驱动），是两个根本上不同的概念。</font>**<font style="color:rgb(25, 27, 31);">后者仅强调使用数据去指导AI系统的搭建，这仍是聚焦于开发模型而不是去改变数据。</font>

<font style="color:rgb(25, 27, 31);"></font>

  


# SAM中的Data-centric
<font style="color:rgb(25, 27, 31);">训练</font>Segment Anything<font style="color:rgb(25, 27, 31);">的核心在于大量的标注数据。这篇论文最突出的贡献在于标注了一个数据集，其中包含10亿个masks，比已有的segmentation数据集大400倍。</font>

:::success
<font style="color:rgb(25, 27, 31);">本文用了一个数据引擎（data engine）做标注。大体上分为三步：</font>

1. **在模型的帮助下人工标注：**<font style="color:rgb(25, 27, 31);">这一步可以理解成一个</font>[<font style="color:rgb(25, 27, 31);">active learning</font>](https://www.zhihu.com/search?q=active%20learning&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A%222972047807%22%7D)<font style="color:rgb(25, 27, 31);">的过程。首先，在公开数据集上训练一个初始的模型。其次，让标注者修改预测出的</font>[<font style="color:rgb(25, 27, 31);">mask</font>](https://www.zhihu.com/search?q=mask&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A%222972047807%22%7D)<font style="color:rgb(25, 27, 31);">。最后，用新标注的数据训练模型。上面三步一共重复了6次，最终得到了430万个mask标注。</font>
2. **半自动标注：**<font style="color:rgb(25, 27, 31);">这一步的目标是提高mask的多样性，仍然可以理解成一个active learning的过程。简单来说就是模型能自动标好的就不要人来标了，</font><u><font style="color:rgb(25, 27, 31);">把人力聚焦在模型不够confident的masks上面</font></u><font style="color:rgb(25, 27, 31);">。这里找到</font>[<font style="color:rgb(25, 27, 31);">confident masks</font>](https://www.zhihu.com/search?q=confident%20masks&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A%222972047807%22%7D)<font style="color:rgb(25, 27, 31);">的方法比较巧妙。做法是在第一步的mask上做</font>[<font style="color:rgb(25, 27, 31);">object detection</font>](https://www.zhihu.com/search?q=object%20detection&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A%222972047807%22%7D)<font style="color:rgb(25, 27, 31);">。这样如果一片区域mask比较一致，那么就很有可能会被识别成一个object。</font>**举个例子。**<font style="color:rgb(25, 27, 31);">比如一张图里一共有20个可能的masks（也就是说可以分成20个区域）。那么我们首先用当前的模型去做segmentation，但是这样大概率只能标注出其中一部分masks，有些masks也标注得不好。我们现在需要自动识别出哪些mask是好的（confident的）。这篇的做法是对预测出mask的结果再做一个object detection看能否识别出图片中有物体。如果有物体，那我们认为对应的mask比较confident。假设这么做发现了8个confident的masks，那么标注者就要标注剩下的12个，这样就节省了人力。以上过程重复了5次，最终又增加了590万个mask标注。</font>
3. **全自动标注：**<font style="color:rgb(25, 27, 31);">简单来说就是拿上一步训练好的模型去标注数据。用到了一些策略去提高标注质量，包括</font><u><font style="color:rgb(25, 27, 31);">（1）用预测的</font></u>[<u><font style="color:rgb(25, 27, 31);">IoU值</font></u>](https://www.zhihu.com/search?q=IoU%E5%80%BC&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A%222972047807%22%7D)<u><font style="color:rgb(25, 27, 31);">去过滤掉不够 confident的masks（模型有个head预测IoU）</font></u><font style="color:rgb(25, 27, 31);">。（</font><u><font style="color:rgb(25, 27, 31);">2）只考虑稳定的masks。如果把threshold在0.5上下调，masks基本不变，那么这样的masks是稳定的。</font></u><font style="color:rgb(25, 27, 31);">具体来说，对每个像素模型会输出一个0到1的值。一般来说我们用0.5当</font>[<font style="color:rgb(25, 27, 31);">threshold</font>](https://www.zhihu.com/search?q=threshold&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A%222972047807%22%7D)<font style="color:rgb(25, 27, 31);">去决定每个像素是否mask住。稳定的意思是，当把这个threshold在0.5附近上下调一定程度的时候（比如0.45～0.55），对应的mask基本保持不变。也就是说模型预测的值在边界两边区分度比较大。我个人认为这也是一种confidence。</font><u><font style="color:rgb(25, 27, 31);">（3）做了去重。</font></u><font style="color:rgb(25, 27, 31);">这一步又标注了11亿的masks（数量增加了大于100倍）。</font>

:::

