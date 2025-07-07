[什么是范数？](https://zhuanlan.zhihu.com/p/67120415)

[L1-norm (L1范数) L2-norm(L2范数)_l1 norm-CSDN博客](https://blog.csdn.net/w__Y__w/article/details/121792038)

# 范数的概念
<font style="color:rgb(25, 27, 31);">距离的定义是一个宽泛的概念，只要满足</font>**<font style="color:rgb(25, 27, 31);">非负、自反、三角不等式就可以称之为距离</font>**<font style="color:rgb(25, 27, 31);">。</font>**<font style="color:rgb(25, 27, 31);">范数是一种强化了的距离概念</font>**<font style="color:rgb(25, 27, 31);">，</font><u><font style="color:rgb(25, 27, 31);">它在定义上比距离多了一条数乘的运算法则</font></u><font style="color:rgb(25, 27, 31);">。有时候为了便于理解，我们可以把范数当作距离来理解。</font>

:::info
<font style="color:rgb(25, 27, 31);"> note：距离中的三角不等式是欧式空间度量的自然推广。三角不等式其实是要求度量（或距离）应该是集合中两点的“直线”距离，即最短距离。若不满足三角不等式</font>即直线(x，y)之间存在一个点z，使得x->z->y的距离小于x->y,<font style="color:rgb(25, 27, 31);">这不符合我们在欧氏空间中的”直线距离最短“的直观认识。所以三角不等式其实是要求定义的距离函数是两点间的”直线“距离。</font>

:::

<font style="color:rgb(25, 27, 31);">在数学上，</font>**<font style="color:rgb(25, 27, 31);">范数包括向量范数和矩阵范数</font>**<font style="color:rgb(25, 27, 31);">，</font>**<font style="color:rgb(25, 27, 31);">向量范数</font>**<u><font style="color:rgb(25, 27, 31);">表征向量空间中向量的大小</font></u><font style="color:rgb(25, 27, 31);">，</font>**<font style="color:rgb(25, 27, 31);">矩阵范数</font>**<u><font style="color:rgb(25, 27, 31);">表征矩阵引起变化的大小。</font></u><font style="color:rgb(25, 27, 31);">一种非严密的解释就是，对应</font>**<font style="color:rgb(25, 27, 31);">向量范数，</font>**<u><font style="color:rgb(25, 27, 31);">向量空间中的向量都是有大小的，这个大小如何度量，就是用范数来度量的，不同的范数都可以来度量这个大小，就好比米和尺都可以来度量远近一样；</font></u><font style="color:rgb(25, 27, 31);">对于</font>**<font style="color:rgb(25, 27, 31);">矩阵范数</font>**<font style="color:rgb(25, 27, 31);">，</font><u><font style="color:rgb(25, 27, 31);">学过线性代数，我们知道，通过运算AX=B，可以将向量X变化为B，矩阵范数就是来度量这个变化大小的。</font></u>

# <font style="color:rgb(25, 27, 31);">L-P范数</font>
<font style="color:rgb(25, 27, 31);">与闵可夫斯基距离的定义一样，L-P范数不是一个范数，而</font><u><font style="color:rgb(25, 27, 31);">是一组范数</font></u><font style="color:rgb(25, 27, 31);">，其定义如下：</font>

<font style="color:rgb(25, 27, 31);"></font>![image](https://cdn.nlark.com/yuque/__latex/4a385d198f53e594e9e18c60ec788291.svg)

<font style="color:rgb(25, 27, 31);">根据P的变化，范数也有着不同的变化，一个经典的有关P范数的变化图如下：</font>

![](https://cdn.nlark.com/yuque/0/2024/png/29307286/1710146858287-c10cd360-505a-4154-8386-377398b37234.png)

<font style="color:rgb(25, 27, 31);">上图表示了p从无穷到0变化时，三维空间中到原点的距离（范数）为1的点构成的图形的变化情况。以常见的L-2范数（p=2）为例，此时的范数也即欧氏距离，空间中到原点的欧氏距离为1的点构成了一个球面。</font>

<font style="color:rgb(25, 27, 31);">实际上，在0时，Lp并不满足三角不等式的性质，也就不是严格意义下的范数。以p=0.5，二维坐标(1,4)、(4,1)、(1,9)为例，</font>

![](https://cdn.nlark.com/yuque/0/2024/png/29307286/1710226652536-c74f55ee-283e-4e03-8d68-8c4ff5d8282f.png)

<font style="color:rgb(25, 27, 31);">因此这里的L-P范数只是一个概念上的宽泛说法。</font>

# L-0范数
<font style="color:rgb(25, 27, 31);">用来度量向量中</font><u><font style="color:rgb(25, 27, 31);">非零元素</font></u><font style="color:rgb(25, 27, 31);">的个数。</font>

# L-1范数
<font style="color:rgb(25, 27, 31);">向量x中非零元素的绝对值之和。</font>

![image](https://cdn.nlark.com/yuque/__latex/b9883ecbe9dbaf4b8b0d491a7fd72b61.svg)

<font style="color:rgb(25, 27, 31);">L1范数有很多的名字，例如我们熟悉的</font>**<font style="color:rgb(25, 27, 31);">曼哈顿距离、最小绝对误差</font>**<font style="color:rgb(25, 27, 31);">等。使用L1范数可以度量两个向量间的差异，如绝对误差和（Sum of Absolute Difference）：</font>

![image](https://cdn.nlark.com/yuque/__latex/40061100561b5811fe0fdbb7f51cf91e.svg)

<font style="color:rgb(25, 27, 31);">由于L1范数的天然性质，对L1优化的解是一个稀疏解，因此L1范数也被叫做稀疏规则算子。通过L1可以实现特征的稀疏，去掉一些没有信息的特征，例如在对用户的电影爱好做分类的时候，用户有100个特征，可能只有十几个特征是对分类有用的，大部分特征如身高体重等可能都是无用的，利用L1范数就可以过滤掉。</font>

<font style="color:rgb(77, 77, 77);"></font><font style="color:rgb(77, 77, 77);">L1-norm 又叫做 taxicab-norm 或者 Manhattan-norm，可能最早提出的大神直接用在曼哈顿区坐出租车来做比喻吧。下图中绿线是两个黑点的 L2 距离，而其他几根就是 taxicab 也就是 L1 距离，确实很像我们平时用地图时走的路线了。</font>

![](https://cdn.nlark.com/yuque/0/2024/png/29307286/1710229826118-cc05ad84-7646-4800-a989-42e127d50efe.png)

# L-2范数
<font style="color:rgb(25, 27, 31);">欧氏距离就是一种L2范数，它的定义如下：</font>

![image](https://cdn.nlark.com/yuque/__latex/0758ee50dd06acbda74fab96203c698e.svg)

<font style="color:rgb(25, 27, 31);">表示向量元素的平方和再开平方。</font>

<font style="color:rgb(25, 27, 31);">像L1范数一样，L2也可以度量两个向量间的差异，如平方差和（Sum of Squared Difference）:</font>

![image](https://cdn.nlark.com/yuque/__latex/cfb14eaf30d84cb5a40be7d2e0417a09.svg)

<font style="color:rgb(25, 27, 31);">L2范数通常会被用来做优化目标函数的正则化项，防止模型为了迎合训练集而过于复杂造成过拟合的情况，从而提高模型的泛化能力。</font>

# L1和L2范数<font style="color:rgb(77, 77, 77);">机器学习上的应用</font>
<font style="color:rgb(77, 77, 77);">（1）作为损失函数使用</font>

<font style="color:rgb(77, 77, 77);">（2）作为正则项使用也即所谓 L1-regularization 和 L2-regularization</font>

## 损失函数
在回归问题中，<font style="color:rgb(77, 77, 77);">待解决的</font>**<font style="color:rgb(77, 77, 77);">问题</font>**<font style="color:rgb(77, 77, 77);">是，找出一条线，让数据点到线上的总距离（也就是error）最小。</font>

![](https://cdn.nlark.com/yuque/0/2024/png/29307286/1710229993171-90f964d7-93b9-4914-bd3f-04074c04f4b8.png)

<font style="color:rgb(77, 77, 77);">因为范数可以表示距离，因此可以用能表示距离的L1-norm和L2-norm作为损失函数，度量预测值与实际目标之间的距离，最小化损失相当于在最小化预测值与实际值之间的距离。</font>

1. <font style="color:rgb(51, 51, 51);">L1-norm损失函数，又称为最小绝对偏差 (least absolute deviation,LAD)。</font><font style="color:rgb(77, 77, 77);">最小化损失函数，其实就是</font><u><font style="color:rgb(77, 77, 77);">最小化预测值和目标值的绝对值</font></u><font style="color:rgb(77, 77, 77);">。</font>
2. <font style="color:rgb(51, 51, 51);">L2-norm损失函数，又称为最小二乘误差（least squares error, LSE）。</font>

<font style="color:rgb(77, 77, 77);">利用微积分求一个方程的最小值，一般步骤为：求导、置零、解方程。但如果给出一个绝对值的方程，求最小值就有点麻烦了，因为绝对值的倒数是不连续的。</font>

<font style="color:rgb(77, 77, 77);">选择L2的原因就是：计算方便，可以直接求导获得取最小值时各个参数的取值。此外还有一点，用L2一定只有一条最好的预测线，L1则因为其性质可能存在多个最优解。L1也有优点，那就是鲁棒性更强，对异常值更不敏感。</font>

## 正则项
<font style="color:rgb(77, 77, 77);">对于实验过程中出现的过拟合问题，</font>**<font style="color:rgb(77, 77, 77);">正则化可以防止过拟合</font>**<font style="color:rgb(77, 77, 77);">。从数学角度，就是在损失函数中加个正则项，防止参数过度拟合。</font>

<font style="color:rgb(77, 77, 77);">L1-regularization 和 L2-regularization 都是常用的正则项，公式如下：</font>

![](https://cdn.nlark.com/yuque/0/2024/png/29307286/1710231083133-13482c1c-8810-4f92-b98f-1f40d00d8afe.png)

<font style="color:rgb(77, 77, 77);">这两个正则项主要有两点不同：</font>

:::info
1. _<font style="color:rgb(51, 51, 51);">L2可以让参数衰减，防止模型过拟合。</font>_
2. _<font style="color:rgb(51, 51, 51);">L1可以产生稀疏权值矩阵，即产生一个稀疏模型，把不重要的特征直接置零，也就是特征自动选择，所以L1是一个天然的特征选择器，而L2则不会。</font>_

:::

## 分析
我们常用梯度下降法优化网络，需要求导获得梯度，然后更新参数。

![](https://cdn.nlark.com/yuque/0/2024/png/29307286/1710231336256-303188a2-4351-4129-bba3-3694299a8574.png)

1. 分别先对 L1 正则项和 L2 正则项来进行求导。

![](https://cdn.nlark.com/yuque/0/2024/png/29307286/1710231389753-4bf54d69-6edb-482d-9457-a6d5295500a7.png)

（_Sign()符号函数：在数学和计算机运算中，其功能是取某个数的符号（正或负）： 当x>0，sign(x)=1;当x=0，sign(x)=0; 当x<0， sign(x)=-1。_）

2. 将L1和L2和导数画在图上。

![](https://cdn.nlark.com/yuque/0/2024/png/29307286/1710231441656-f55a7d97-f0ae-41fc-aa2c-6fa7e7ebc5eb.png)

发现，在梯度更新时，不管 L1 的大小是多少（只要不是0）梯度都是1或者-1，所以每次更新时，它都是稳步向0前进。

![](https://cdn.nlark.com/yuque/0/2024/png/29307286/1710231496804-27fefec2-7206-4dcd-ac90-c27d6a3179bd.png)

而看 L2 的话，就会发现它的梯度会越靠近0，就变得越小。

![](https://cdn.nlark.com/yuque/0/2024/png/29307286/1710231676111-81a6e917-1b18-4329-b968-cc3706b87e06.png)

总结：L1 防止模型过拟合的方式是产生稀疏解，实际上是减少特征数量。而 L2 是减小模型参数，尽管都能简化模型，但是一般来说 L2 模型的抗过拟合的能力更好一点。并且进一步说，L1 是假定参数符合拉普拉斯分布，L2 是假定参数符合高斯分布。



****

