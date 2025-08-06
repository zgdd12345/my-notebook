# 强化学习

# 第一章 绪论

## 1.1 强化学习概述

强化学习由两个部分组成：智能体和环境。

[Go to annotation](zotero://open-pdf/library/items/DK35Y6UG?page=1&annotation=undefined) “强化学习(reinforcement learning,RL)讨论的问题是智能体(agent)怎么在复杂、不确定的环境(environment)里面去最大化它能获得的奖励” ([“easy-rl”, p. 1](zotero://select/library/items/JNL4ZGTU))

智能体在环境中获取当前状态后会利用该状态输出一个动作，这个动作成为决策。然后这个动作会在环境中执行，环境会根据上述动作输出下一个状态以及这个动作带来的奖励。

### 1.1.1强化学习与监督学习的区别

监督学习的特点：1. 数据时独立同分布的，2. 数据有标签，即“监督”。这两个特点都时强化学习不具备的。

强化学习一是数据是序列数据，连续的数据有强相关性，二是数据只有奖励信号，而且是延迟的，不能及时反馈。

强化学习的特征：

1. 通过探索环境来获取对环境的理解；
2. 智能体会从环境里获得延迟的奖励；
3. 数据之间有时间相关性；
4. 智能体的动作会影响后续数据。

### 1.1.2 强化学习的例子

强化学习得到的模型可以有超过人类的表现；

监督学习的上限是人类的表现。

一个经典强化学习的过程：

[Go to annotation](zotero://open-pdf/library/items/DK35Y6UG?page=4&annotation=undefined) “预演是指我们从当前帧对动作进行采样,生成很多 局游戏。”

[Go to annotation](zotero://open-pdf/library/items/DK35Y6UG?page=4&annotation=undefined) “我们将当前的智能体与环境交互,会得到一系列观测。每一个观测可看成一个轨迹(trajectory)。 轨迹就是当前帧以及它采取的策略,即状态和动作的序列:”

[Go to annotation](zotero://open-pdf/library/items/DK35Y6UG?page=4&annotation=undefined) “我们可以通过观测序列以及最终奖励(eventual reward)来训练智能体,使它尽可能地采取可以获得最终奖励的动作。”

### 1.1.3 强化学习的历史

- 标准强化学习：[Go to annotation](zotero://open-pdf/library/items/DK35Y6UG?page=5&annotation=undefined) “标准强化学习先设计很多特征,这些特征可以描述现在整个状态。 得到这些特征后,我们就可以通过训练一个分类网络或者分别训练一个价值估计函数来采取动作。”
- 深度强化学习：[Go to annotation](zotero://open-pdf/library/items/DK35Y6UG?page=5&annotation=undefined) “不需要设计特征,直接输入状态就可以输出动作。我们可以用一个神经网络来拟合价值函数或策略网络,省去特征工程(feature engineering)的过程。”

## 1.2 序列决策

### 1.2.1 智能体和环境

智能体一直与环境进行交互，智能体把它的动作输出给环境，环境取得这个动作后会把下一步的观测与这个动作带来的奖励返还给智能体。这样的交互会产生很多观测，智能体的目的是从这些观测之中学到能最大化奖励的策略。

### 1.2.2 奖励

[Go to annotation](zotero://open-pdf/library/items/DK35Y6UG?page=7&annotation=undefined) “奖励是由环境给的一种标量的反馈信号”，表示智能体某一步采取某个策略的表现如何。

### 1.2.3 序列决策

[Go to annotation](zotero://open-pdf/library/items/DK35Y6UG?page=7&annotation=undefined) “智能体的目的就是选取一系列的动作来最大化奖励,所以这些选取的动作 必须有长期的影响。”

智能体的奖励是被延迟的

[Go to annotation](zotero://open-pdf/library/items/DK35Y6UG?page=7&annotation=undefined) “强化学习里面一个重要的课题就是近期奖励和远期奖励的权衡 (trade-off),研究怎么让智能体取得更多的远期奖励。”

环境状态分为：

[Go to annotation](zotero://open-pdf/library/items/DK35Y6UG?page=8&annotation=undefined) “完全可观测的(fully observed)”

[Go to annotation](zotero://open-pdf/library/items/DK35Y6UG?page=8&annotation=undefined) “部分可观测的(partially observed)”

## 1.3 动作空间

## 1.4 强化学习智能体的组成成分和类型

### 1.4.1 策略

### 1.4.2 价值函数

### 1.4.3 模型

### 1.4.4 强化学习智能体的类型