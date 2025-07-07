
Normalization, 即**标准化**, 和普通的数据标准化类似, 是将分散的数据统一的一种做法, 也是优化神经网络的一种方法。Normalization 可以将数据统一规格, 能让机器学习更容易学习到数据之中的规律。
在深度学习中，Normalization已经成为了标准技术。2015 年Google首先提出了**Batch Normalization**（BN），[源论文地址](https://arxiv.org/abs/1502.03167)。自 BN 之后， **Layer Norm / Weight Norm / Cosine Norm** 等也横空出世。

# 一、Normalization的作用
深度学习方法中已发展出了多种Normalization方法，如Batch Normalization（BN）,Layer Norm（LN）, Weight Norm（WN）, Cosine Norm(CN)等。在此，我们以最经典的Batch Normalization为例说明Normalization的作用。

我们知道，在神经网络中, 数据分布对训练会产生影响. 比如某个神经元x的值为1, 某个 Weights 的初始值为0.1, 这样后一层神经元计算结果就是 W x = 0.1; 又或者 x = 20 , 这样Wx的结果就为2. 现在还不能看出什么问题, 但是, 当我们加上一层激励函数, 激活这个Wx值的时候, 问题就来了. 如果使用tanh激励函数, Wx 的激活值就变成了 ~0.1 和 ~1, <span style="color:rgb(255, 0, 0)">接近于 1 的部分已经处在了激励函数的饱和阶段</span>, 也就是如果x无论再怎么扩大, tanh 激励函数输出值也还是接近1. 换句话说, 神经网络在初始阶段已经不对那些比较大的x特征范围敏感了. 这样很糟糕, 想象我轻轻拍自己的感觉和重重打自己的感觉居然没什么差别, 这就证明我的感官系统失效了.

当然，x不仅可以是输入层，在隐含层也可能出现这样的情况。

通过下图我们可以看到BN的效果：
![[Pasted image 20250701153817.png|500]]
 ![[Pasted image 20250701153900.png|500]]

计算结果在进入激励函数前的值很重要, 如果我们不单单看一个值, 我们可以说, 计算结果值的分布对于激励函数很重要. 对于数据值大多分布在这个区间的数据, 才能进行更有效的传递. 对比这两个在激活之前的值的分布. 上者没有进行 normalization, 下者进行了 normalization, 这样当然是下者能够更有效地利用 tanh 进行非线性化的过程.

没有 normalize 的数据 使用 tanh 激活以后, 激活值大部分都分布到了饱和阶段, 也就是大部分的激活值不是-1, 就是1, 而 normalize 以后, 大部分的激活值在每个分布区间都还有存在. 再将这个激活后的分布传递到下一层神经网络进行后续计算, 每个区间都有分布的这一种对于神经网络就会更加有价值.

我们需要知道得是，Batch normalization 不仅仅 normalize 了一下数据, 它还进行了反 normalize。关于这点,我们在第三章会讲到。

# 2. 为什么深度学习中需要Normalization

