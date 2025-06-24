[参考](https://zhuanlan.zhihu.com/p/77151308)

# PCA相关的数学基础
## 向量表示与基变换
### 1.1 内积
<font style="color:rgb(18, 18, 18);">两个向量的 A 和 B 内积我们知道形式是这样的：</font>

<font style="color:rgb(18, 18, 18);"></font>![image](https://cdn.nlark.com/yuque/__latex/24c91b9f2dedfdf77608f53c2eda87b8.svg)

<font style="color:rgb(18, 18, 18);">内积运算将两个向量映射为实数，其计算方式非常容易理解，但我们无法看出其物理含义。接下来我们从几何角度来分析，为了简单起见，我们假设 A 和 B 均为二维向量，则：</font>

![image](https://cdn.nlark.com/yuque/__latex/8f771b1886b58e7e6bcfa030ebe566d9.svg)

<font style="color:rgb(18, 18, 18);">其几何表示见下图：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/29307286/1701921021174-5f4aeacb-a2f3-46ed-adcc-9890ccbec86c.png)

<font style="color:rgb(18, 18, 18);">我们看出 A 与 B 的内积等于 A 到 B 的投影长度乘以 B 的模。</font>

<font style="color:rgb(18, 18, 18);">如果假设 B 的模为 1，即让 </font><font style="color:rgb(18, 18, 18);">|B|=1</font><font style="color:rgb(18, 18, 18);"> ，那么就变成了：</font>

<font style="color:rgb(18, 18, 18);"></font>![image](https://cdn.nlark.com/yuque/__latex/f4180406fda6cdcc67fd1b0bed6a2e07.svg)

<font style="color:rgb(18, 18, 18);">也就是说，</font>**<font style="color:#DF2A3F;">A 与 B 的内积值等于 A 向 B 所在直线投影的标量大小。</font>**

<font style="color:rgb(18, 18, 18);">这就是内积的一种几何解释，也是我们得到的第一个重要结论。在后面的推导中，将反复使用这个结论。</font>

### <font style="color:rgb(18, 18, 18);">1.2 基</font>
<font style="color:rgb(18, 18, 18);">在我们常说的坐标系中，向量 (3,2) 其实隐式引入了一个定义：</font><u><font style="color:rgb(18, 18, 18);">以 x 轴和 y 轴上正方向长度为 1 的向量为标准。向量 (3,2) 实际是说在 x 轴投影为 3 而 y 轴的投影为 2。</font></u>**<font style="color:rgb(18, 18, 18);">注意</font>****<font style="color:rgb(18, 18, 18);background-color:#FBDE28;">投影是一个标量，所以可以为负</font>****<font style="color:rgb(18, 18, 18);">。</font>**

<font style="color:rgb(18, 18, 18);">所以，对于向量 (3, 2) 来说，如果我们想求它在</font><font style="color:rgb(18, 18, 18);"> </font><font style="color:rgb(18, 18, 18);">(</font><font style="color:rgb(18, 18, 18);">1</font><font style="color:rgb(18, 18, 18);">,</font><font style="color:rgb(18, 18, 18);">0</font><font style="color:rgb(18, 18, 18);">)</font><font style="color:rgb(18, 18, 18);">,</font><font style="color:rgb(18, 18, 18);">(</font><font style="color:rgb(18, 18, 18);">0</font><font style="color:rgb(18, 18, 18);">,</font><font style="color:rgb(18, 18, 18);">1</font><font style="color:rgb(18, 18, 18);">)</font><font style="color:rgb(18, 18, 18);"> </font><font style="color:rgb(18, 18, 18);">这组基下的坐标的话，分别内积即可。当然，内积完了还是 (3, 2)。</font>

<font style="color:rgb(18, 18, 18);">所以，我们大致可以得到一个结论，我们</font>**<font style="color:rgb(18, 18, 18);">要准确描述向量，首先要</font>****<font style="color:rgb(18, 18, 18);background-color:#FBDE28;">确定一组基</font>****<font style="color:rgb(18, 18, 18);">，然后给出</font>****<font style="color:rgb(18, 18, 18);background-color:#FBDE28;">在基所在的各个直线上的投影值</font>****<font style="color:rgb(18, 18, 18);">，就可以了</font>**<font style="color:rgb(18, 18, 18);">。为了方便求坐标，我们</font><font style="color:rgb(18, 18, 18);background-color:#FBDE28;">希望这组基向量模长为 1</font><font style="color:rgb(18, 18, 18);">。</font><u><font style="color:rgb(18, 18, 18);">因为向量的内积运算，当模长为 1 时，内积可以直接表示投影。</font></u><font style="color:rgb(18, 18, 18);">然后还需要这组基是</font><font style="color:rgb(18, 18, 18);background-color:#FBDE28;">线性无关</font><font style="color:rgb(18, 18, 18);">的，我们一般用</font><font style="color:rgb(18, 18, 18);background-color:#FBDE28;">正交基</font><font style="color:rgb(18, 18, 18);">，非正交的基也是可以的，不过正交基有较好的性质。</font>



### 1.3 <font style="color:rgb(18, 18, 18);">基变换的矩阵表示</font>
<font style="color:rgb(18, 18, 18);">这里我们先做一个练习：对于向量 (3,2) 这个点来说，在</font>![image](https://cdn.nlark.com/yuque/__latex/285d8e59846539b86bbe46b65aac48c9.svg)<font style="color:rgb(18, 18, 18);">和</font>![image](https://cdn.nlark.com/yuque/__latex/46fb6ec86f3fc5cec4b09bc93a6f9bb9.svg)<font style="color:rgb(18, 18, 18);">这组基下的坐标是多少？</font>

<font style="color:rgb(18, 18, 18);">我们拿 (3,2) 分别与之内积，得到</font>![image](https://cdn.nlark.com/yuque/__latex/17c62c402fa1dd446143d277b46ef231.svg)<font style="color:rgb(18, 18, 18);"> 这个新坐标。</font>

<font style="color:rgb(18, 18, 18);">我们可以用矩阵相乘的形式简洁的表示这个变换：</font>

<font style="color:rgb(18, 18, 18);"></font>![image](https://cdn.nlark.com/yuque/__latex/54a5c912ed363a7f4818dee8c833396c.svg)

<font style="color:rgb(18, 18, 18);">左边矩阵的两行分别为两个基，乘以原向量，其结果刚好为新基的坐标。推广一下，如果我们有 m 个二维向量，只要将二维向量按列排成一个两行 m 列矩阵，然后用“基矩阵”乘以这个矩阵就可以得到了所有这些向量在新基下的值。例如对于数据点 </font><font style="color:rgb(18, 18, 18);">(1,1)，(2,2)，(3,3)</font><font style="color:rgb(18, 18, 18);"> 来说，想变换到刚才那组基上，则可以这样表示：</font>

<font style="color:rgb(18, 18, 18);"></font>![image](https://cdn.nlark.com/yuque/__latex/21aa826d2fbd4a1d386b4aa6a42c83c4.svg)

<font style="color:rgb(18, 18, 18);">我们可以把它写成通用的表示形式：</font>

![image](https://cdn.nlark.com/yuque/__latex/b7d6dccff5fa6b64a42feba534d4ba35.svg)

<font style="color:rgb(18, 18, 18);">其中 </font>![image](https://cdn.nlark.com/yuque/__latex/39c69fbad0041c1d5caa9acf313cb0e6.svg)<font style="color:rgb(18, 18, 18);"> 是一个行向量，表示第 i 个基，</font>![image](https://cdn.nlark.com/yuque/__latex/aaf4e1a982dd205ca6d909a345b8eb81.svg)<font style="color:rgb(18, 18, 18);"> 是一个列向量，表示第 j 个原始数据记录。实际上也就是做了一个</font><font style="color:rgb(18, 18, 18);background-color:#FBDE28;">向量矩阵化</font><font style="color:rgb(18, 18, 18);">的操作。</font>

<font style="color:rgb(18, 18, 18);">上述分析给矩阵相乘找到了一种物理解释：</font>**<font style="color:#DF2A3F;">两个矩阵相乘的意义是将右边矩阵中的每一列向量 </font>**![image](https://cdn.nlark.com/yuque/__latex/aaf4e1a982dd205ca6d909a345b8eb81.svg)<font style="color:#DF2A3F;"> </font>**<font style="color:#DF2A3F;">变换到左边矩阵中以每一行行向量为基所表示的空间中去。</font>**<font style="color:rgb(18, 18, 18);">也就是说一个矩阵可以表示一种线性变换</font>

<font style="color:rgb(18, 18, 18);"></font>























## 最大可分性
<font style="color:rgb(18, 18, 18);">上面我们讨论了选择不同的基可以对同样一组数据给出不同的表示，如果基的数量少于向量本身的维数，则可以达到</font><font style="color:rgb(18, 18, 18);background-color:#FBDE28;">降维</font><font style="color:rgb(18, 18, 18);">的效果。</font>

<font style="color:rgb(18, 18, 18);">但是我们还没回答一个最关键的问题：</font><u><font style="color:rgb(18, 18, 18);">如何选择基才是最优的</font></u><font style="color:rgb(18, 18, 18);">。或者说，如果我们有一组 N 维向量，现在要将其降到 K 维（K 小于 N），那么我们应该如何选择 K 个基才能最大程度保留原有的信息？</font>

<font style="color:rgb(18, 18, 18);">一种直观的看法是：</font><font style="color:rgb(18, 18, 18);background-color:#FBDE28;">希望投影后的投影值尽可能分散，因为如果重叠就会有样本消失。当然这个也可以从熵的角度进行理解，熵越大所含信息越多。</font>

### 方差
<font style="color:rgb(18, 18, 18);">我们知道</font><font style="color:rgb(18, 18, 18);background-color:#FBDE28;">数值的分散程度</font><font style="color:rgb(18, 18, 18);">，可以用数学上的方差来表述。</font><u><font style="color:rgb(18, 18, 18);">一个变量的方差可以看做是每个元素与变量均值的差的平方和的均值</font></u><font style="color:rgb(18, 18, 18);">，即：</font>

<font style="color:rgb(18, 18, 18);"></font>![image](https://cdn.nlark.com/yuque/__latex/3a963af9b01eef63eaf5302309399421.svg)

<font style="color:rgb(18, 18, 18);">为了方便处理，我们将每个变量的</font><font style="color:rgb(18, 18, 18);background-color:#FBDE28;">均值都化为 0</font><font style="color:rgb(18, 18, 18);"> ，因此方差可以直接用每个元素的平方和除以元素个数表示：</font>

<font style="color:rgb(18, 18, 18);"></font>![image](https://cdn.nlark.com/yuque/__latex/59bdc406ddc6f9f663113f343f1cbba3.svg)



<font style="color:rgb(18, 18, 18);">于是上面的问题被形式化表述为：</font>**<u><font style="color:rgb(18, 18, 18);">寻找一个一维基，使得所有数据变换为这个基上的坐标表示后，方差值最大。</font></u>**

### 协方差
<font style="color:rgb(18, 18, 18);">在</font><u><font style="color:rgb(18, 18, 18);">一维空间中我们可以用方差来表示数据的分散程度</font></u><font style="color:rgb(18, 18, 18);">。而对于</font><u><font style="color:rgb(18, 18, 18);">高维数据，我们用协方差进行约束</font></u><font style="color:rgb(18, 18, 18);">，</font><font style="color:rgb(18, 18, 18);background-color:#FBDE28;">协方差可以表示两个变量(向量？)的相关性。</font><u><font style="color:rgb(18, 18, 18);">为了让两个变量（向量）尽可能表示更多的原始信息，我们希望它们之间</font></u><u><font style="color:rgb(18, 18, 18);background-color:#FBDE28;">不存在线性相关性</font></u><font style="color:rgb(18, 18, 18);">，</font><u><font style="color:rgb(18, 18, 18);">因为相关性意味着两个变量不是完全独立，必然存在重复表示的信息。</font></u>

<u><font style="color:rgb(18, 18, 18);">理解：协方差越小表示的信息越多，即两个向量正交时，表示的信息越多，两个向量内积越大表示起投影面积越大，必然存在更多的重复信息。</font></u>

<font style="color:rgb(18, 18, 18);">协方差公式为：</font>

![image](https://cdn.nlark.com/yuque/__latex/726e40f282ad24351c7d09576e380fac.svg)

<u>理解：两个向量的内积越大信息量越大。</u>

<font style="color:rgb(18, 18, 18);">由于均值为 0，所以我们的协方差公式可以表示为：</font>

![image](https://cdn.nlark.com/yuque/__latex/2115d950a190e41fdb670b87e6f4d08b.svg)

<font style="color:rgb(18, 18, 18);">当样本数较大时，不必在意其是 m 还是 m-1，为了简化表示，我们分母取 m。</font>

<u><font style="color:rgb(18, 18, 18);">当协方差为 0 时，表示两个变量完全独立。</font></u><font style="color:rgb(18, 18, 18);">为了让协方差为 0，我们选择第二个基时只能在与第一个基正交的方向上进行选择，因此最终选择的两个方向一定是正交的。（协方差为 0 时，两个变量只是线性不相关。完全独立是有问题的）</font>

<font style="color:rgb(18, 18, 18);">至此，我们得到了降维问题的优化目标：</font>**<font style="color:#000000;background-color:#FBDE28;">将一组 N 维向量降为 K 维，其目标是选择 K 个单位正交基，使得原始数据变换到这组基上后，各变量两两间协方差为 0，而变量方差则尽可能大（在正交的约束下，取最大的 K 个方差）。</font>**

<font style="color:#000000;">理解：上述所说的变量可以理解为向量。</font>

### 协方差矩阵
<font style="color:rgb(18, 18, 18);">针对我们给出的优化目标，接下来我们将从数学的角度来给出优化目标。</font>

<font style="color:rgb(18, 18, 18);">我们看到，最终要达到的目的与</font>**<font style="color:rgb(18, 18, 18);">变量内方差及变量间协方差</font>**<font style="color:rgb(18, 18, 18);">有密切关系。因此我们希望能将两者统一表示，仔细观察发现，</font><u><font style="color:rgb(18, 18, 18);">两者均可以表示为内积的形式，而内积又与矩阵相乘密切相关</font></u><font style="color:rgb(18, 18, 18);">。于是我们有：</font>

<font style="color:rgb(18, 18, 18);">假设我们只有 a 和 b 两个变量，那么我们将它们按行组成矩阵 X：</font>

![image](https://cdn.nlark.com/yuque/__latex/a856decc4c1d1917737ea4cdc4d90e04.svg)

<font style="color:rgb(18, 18, 18);">然后：</font>

![image](https://cdn.nlark.com/yuque/__latex/d5ab1ac7746814cbb1ba65d4c36afb15.svg)

<font style="color:rgb(18, 18, 18);">我们可以看到这个矩阵对角线上的分别是两个变量的方差和协方差。两者被统一到了一个矩阵里。</font>

<font style="color:rgb(18, 18, 18);">我们很容易将其推广到一般情况：</font>

**<font style="color:rgb(18, 18, 18);">设我们有 m 个 n 维数据记录，将其排列成矩阵</font>**![image](https://cdn.nlark.com/yuque/__latex/1300c579f50a812171a81b3ef20539dc.svg)**<font style="color:rgb(18, 18, 18);">，设 </font>**![image](https://cdn.nlark.com/yuque/__latex/42b2b87f9f4f5d5fc2b03587591c05fd.svg)**<font style="color:rgb(18, 18, 18);">,则 C 是一个对称矩阵，其对角线分别对应各个变量的方差，而第 i 行 j 列和 j 行 i 列元素相同，表示 i 和 j 两个变量的协方差</font>**<font style="color:rgb(18, 18, 18);">。</font>

### 矩阵对角化
<font style="color:rgb(18, 18, 18);">根据我们的优化条件，</font>**<font style="color:rgb(18, 18, 18);">我们需要将除</font>****<u><font style="color:rgb(18, 18, 18);">左对角线外的其它元素化为 0（协方差为0）</font></u>****<font style="color:rgb(18, 18, 18);">，并且在</font>****<u><font style="color:rgb(18, 18, 18);">左对角线上将元素按大小从上到下排列（变量方差尽可能大）</font></u>**<font style="color:rgb(18, 18, 18);">，这样我们就达到了优化目的。这样说可能还不是很明晰，我们进一步看下原矩阵与基变换后矩阵协方差矩阵的关系。</font>

<u><font style="color:rgb(18, 18, 18);">设原始数据矩阵 X 对应的协方差矩阵为 C，而 P 是一组基按行组成的矩阵，设 Y=PX，则 Y 为 X 对 P 做基变换后的数据。</font></u><font style="color:rgb(18, 18, 18);">设 Y 的协方差矩阵为 D，我们推导一下 D 与 C 的关系：</font>

![image](https://cdn.nlark.com/yuque/__latex/5164ae0886f939d51c7af92ff136042b.svg)

<font style="color:rgb(18, 18, 18);">这样我们就看清楚了，我们要找的 P 是能让原始协方差矩阵对角化的 P。换句话说，优化目标变成了</font>**<font style="color:rgb(18, 18, 18);">寻找一个矩阵 P，满足</font>**![image](https://cdn.nlark.com/yuque/__latex/ee1e8b14210074d190f3a9eb7f4d3108.svg)<font style="color:rgb(18, 18, 18);"> </font>**<font style="color:rgb(18, 18, 18);">是一个对角矩阵，并且</font>****<u><font style="color:rgb(18, 18, 18);">对角元素按从大到小依次排</font></u>****<font style="color:rgb(18, 18, 18);">列，那么 P 的前 K 行就是要寻找的基，</font>****<u><font style="color:rgb(18, 18, 18);">用 P 的前 K 行组成的矩阵乘以 X 就使得 X 从 N 维降到了 K 维并满足上述优化条件</font></u>**<u><font style="color:rgb(18, 18, 18);">。</font></u>

<font style="color:rgb(18, 18, 18);">至此，我们离 PCA 还有对角化这一步之遥。由上文知道，协方差矩阵 C 是一个是对称矩阵，在线性代数中实对称矩阵有一系列非常好的性质：</font>

1. <font style="color:rgb(18, 18, 18);">实对称矩阵不同特征值对应的特征向量必然正交。（元素为实数且矩阵的转置为其本身的我们称为实对称矩阵）</font>
2. <font style="color:rgb(18, 18, 18);">设特征向量</font>![image](https://cdn.nlark.com/yuque/__latex/3aa688dd88814862b803b2030766bd5f.svg)<font style="color:rgb(18, 18, 18);">重数为 r，则必然存在 r 个线性无关的特征向量对应于</font>![image](https://cdn.nlark.com/yuque/__latex/3aa688dd88814862b803b2030766bd5f.svg)<font style="color:rgb(18, 18, 18);">，因此可以将这 r 个特征向量单位正交化。</font>

<font style="color:rgb(18, 18, 18);">由上面两条可知，一个 n 行 n 列的实对称矩阵一定可以找到 n 个单位正交特征向量，设这 n 个特征向量为</font>![image](https://cdn.nlark.com/yuque/__latex/23e6e47553e4b32aa0d153922df05122.svg)<font style="color:rgb(18, 18, 18);">，我们将其按列组成矩阵：</font>![image](https://cdn.nlark.com/yuque/__latex/9bc2ef27a0559acb53f64614f9e3e293.svg)<font style="color:rgb(18, 18, 18);">。</font>

<font style="color:rgb(18, 18, 18);">则对协方差矩阵 C 有如下结论：</font>

![image](https://cdn.nlark.com/yuque/__latex/fd470cd03bbaee92802bab18231ce870.svg)

<font style="color:rgb(18, 18, 18);">其中 </font><font style="color:rgb(18, 18, 18);">Λ</font><font style="color:rgb(18, 18, 18);"> 为对角矩阵，其对角元素为各特征向量对应的特征值（可能有重复）。</font>

<font style="color:rgb(18, 18, 18);">到这里，我们发现我们已经找到了</font><u><font style="color:rgb(18, 18, 18);">需要的矩阵</font></u>![image](https://cdn.nlark.com/yuque/__latex/42a20045b0f8da88113c360c1a1d9bfc.svg)<u><font style="color:rgb(18, 18, 18);">。</font></u>

<font style="color:rgb(18, 18, 18);">P 是协方差矩阵的特征向量单位化后按行排列出的矩阵，其中每一行都是 C 的一个特征向量。如果</font><u><font style="color:rgb(18, 18, 18);">设 P 按照 </font></u><u><font style="color:rgb(18, 18, 18);">Λ</font></u><u><font style="color:rgb(18, 18, 18);"> 中特征值的从大到小，将特征向量从上到下排列</font></u><font style="color:rgb(18, 18, 18);">，则用 P 的前 K 行组成的矩阵乘以原始数据矩阵 X，就得到了我们需要的降维后的数据矩阵 Y。</font>

<font style="color:rgb(18, 18, 18);"></font>

### 补充
<font style="color:rgb(18, 18, 18);">(1) 拉格朗日乘子法</font>

<font style="color:rgb(18, 18, 18);">在叙述求协方差矩阵对角化时，我们给出希望变化后的变量有：</font>**<font style="color:rgb(18, 18, 18);">变量间协方差为 0 且变量内方差尽可能大</font>**<font style="color:rgb(18, 18, 18);">。然后我们通过实对称矩阵的性质给予了推导，此外我们还可以把它转换为最优化问题利用拉格朗日乘子法来给予推导。</font>

## <font style="color:rgb(18, 18, 18);">求解步骤</font>
<font style="color:rgb(18, 18, 18);">总结一下 PCA 的算法步骤：</font>

<font style="color:rgb(18, 18, 18);">设有 m 条 n 维数据。</font>

1. <font style="color:rgb(18, 18, 18);">将原始数据按列组成 n 行 m 列矩阵 X；</font>
2. <font style="color:rgb(18, 18, 18);">将 X 的每一行进行零均值化，即减去这一行的均值；</font>
3. <font style="color:rgb(18, 18, 18);">求出协方差矩阵</font>![image](https://cdn.nlark.com/yuque/__latex/b43788f8b480c8bccaaf8b720ccfa8e6.svg)<font style="color:rgb(18, 18, 18);">;</font>
4. <font style="color:rgb(18, 18, 18);">求出协方差矩阵的特征值及对应的特征向量；</font>
5. <font style="color:rgb(18, 18, 18);">将特征向量按对应特征值大小从上到下按行排列成矩阵，取前 k 行组成矩阵 P；</font>
6. ![image](https://cdn.nlark.com/yuque/__latex/6e344f484713a7c2f622868c642baa30.svg)<font style="color:rgb(18, 18, 18);">即为降维到 k 维后的数据。</font>

## <font style="color:rgb(18, 18, 18);">性质</font>
1. **<font style="color:rgb(18, 18, 18);">缓解维度灾难</font>**<font style="color:rgb(18, 18, 18);">：PCA 算法通过舍去一部分信息之后能使得样本的采样密度增大（因为维数降低了），这是缓解维度灾难的重要手段；</font>
2. **<font style="color:rgb(18, 18, 18);">降噪</font>**<font style="color:rgb(18, 18, 18);">：当数据受到噪声影响时，最小特征值对应的特征向量往往与噪声有关，将它们舍弃能在一定程度上起到降噪的效果；</font>
3. **<font style="color:rgb(18, 18, 18);">过拟合</font>**<font style="color:rgb(18, 18, 18);">：PCA 保留了主要信息，但这个主要信息只是针对训练集的，而且这个主要信息未必是重要信息。有可能舍弃了一些看似无用的信息，但是这些看似无用的信息恰好是重要信息，只是在训练集上没有很大的表现，所以 PCA 也可能加剧了过拟合；</font>
4. **<font style="color:rgb(18, 18, 18);">特征独立</font>**<font style="color:rgb(18, 18, 18);">：PCA 不仅将数据压缩到低维，它也使得降维之后的数据各特征相互独立；</font>

## <font style="color:rgb(18, 18, 18);">细节</font>
### <font style="color:rgb(18, 18, 18);">零均值化</font>
<font style="color:rgb(18, 18, 18);">当对训练集进行 PCA 降维时，也需要对验证集、测试集执行同样的降维。而</font>**<font style="color:rgb(18, 18, 18);">对验证集、测试集执行零均值化操作时，均值必须从训练集计算而来</font>**<font style="color:rgb(18, 18, 18);">，不能使用验证集或者测试集的中心向量。</font>

<font style="color:rgb(18, 18, 18);">其原因也很简单，因为我们的训练集是可观测到的数据，测试集不可观测所以不会知道其均值，而验证集再大部分情况下是在处理完数据后再从训练集中分离出来，一般不会单独处理。如果真的是单独处理了，不能独自求均值的原因是和测试集一样。</font>

<font style="color:rgb(18, 18, 18);">另外我们也需要保证一致性，我们拿训练集训练出来的模型用来预测测试集的前提假设就是两者是独立同分布的，如果不能保证一致性的话，会出现Variance Shift的问题。</font>

### <font style="color:rgb(18, 18, 18);">与 SVD 的对比</font>
<font style="color:rgb(18, 18, 18);">这是两个不同的数学定义。我们先给结论：</font>**<font style="color:rgb(18, 18, 18);">特征值和特征向量是针对方阵</font>**<font style="color:rgb(18, 18, 18);">才有的，而</font>**<font style="color:rgb(18, 18, 18);">对任意形状的矩阵都可以做奇异值分解</font>**<font style="color:rgb(18, 18, 18);">。</font>

**<font style="color:rgb(18, 18, 18);">PCA</font>**<font style="color:rgb(18, 18, 18);">：方阵的特征值分解，对于一个方阵A，总可以写成：</font>![image](https://cdn.nlark.com/yuque/__latex/5ead7171c5aa52ff68ae9fa9ff0a99d5.svg)<font style="color:rgb(18, 18, 18);">。</font>

<font style="color:rgb(18, 18, 18);">其中，Q 是这个矩阵 A 的特征向量组成的矩阵， </font><font style="color:rgb(18, 18, 18);">Λ</font><font style="color:rgb(18, 18, 18);"> 是一个对角矩阵，每一个对角线元素就是一个特征值，里面的特征值是由小排列的，这些特征值所对应的特征向量就是描述这个矩阵变化方向（从主要的变化到次要的变化排列）。也就是说矩阵 A 的信息可以由其特征值和特征向量表示。</font>

**<font style="color:rgb(18, 18, 18);">SVD</font>**<font style="color:rgb(18, 18, 18);">：矩阵的奇异值分解其实就是对于矩阵 A 的协方差矩阵</font>![image](https://cdn.nlark.com/yuque/__latex/dd8ef5e6cdc4ee13855bc4cfbee8c3e4.svg)<font style="color:rgb(18, 18, 18);">和 </font>![image](https://cdn.nlark.com/yuque/__latex/8962133df4487c91759a74e97ee2a528.svg)<font style="color:rgb(18, 18, 18);"> 做特征值分解推导出来的：</font>

![image](https://cdn.nlark.com/yuque/__latex/aa6d9a0b641450fbba5686ce20865841.svg)

<font style="color:rgb(18, 18, 18);">其中， U V 都是正交矩阵，有 </font>![image](https://cdn.nlark.com/yuque/__latex/428b11653466ba4f4ebbe33e637dbf47.svg)<font style="color:rgb(18, 18, 18);">=</font>![image](https://cdn.nlark.com/yuque/__latex/be9117e24893080c98acdc66c229bcbf.svg)<font style="color:rgb(18, 18, 18);">,</font>![image](https://cdn.nlark.com/yuque/__latex/ee4701fc4291c0eb41673cf18ca213e7.svg)<font style="color:rgb(18, 18, 18);">=</font>![image](https://cdn.nlark.com/yuque/__latex/cb38912c98bfefaa15e16dcd6acaeae2.svg)<font style="color:rgb(18, 18, 18);"> 。这里的约等于是因为 </font><font style="color:rgb(18, 18, 18);">Λ</font><font style="color:rgb(18, 18, 18);"> 中有 n 个奇异值，但是由于排在后面的很多接近 0，所以我们可以仅保留比较大的 k 个奇异值。</font>

![image](https://cdn.nlark.com/yuque/__latex/68ea47e2772d0a4ee79bb86f5681e560.svg)

<font style="color:rgb(18, 18, 18);">所以，V U 两个矩阵分别是</font>![image](https://cdn.nlark.com/yuque/__latex/dd8ef5e6cdc4ee13855bc4cfbee8c3e4.svg)<font style="color:rgb(18, 18, 18);">和</font>![image](https://cdn.nlark.com/yuque/__latex/8962133df4487c91759a74e97ee2a528.svg)<font style="color:rgb(18, 18, 18);">的特征向量，中间的矩阵对角线的元素是</font>![image](https://cdn.nlark.com/yuque/__latex/dd8ef5e6cdc4ee13855bc4cfbee8c3e4.svg)<font style="color:rgb(18, 18, 18);">和</font>![image](https://cdn.nlark.com/yuque/__latex/8962133df4487c91759a74e97ee2a528.svg)<font style="color:rgb(18, 18, 18);"> 的特征值。我们也很容易看出 A 的奇异值和</font>![image](https://cdn.nlark.com/yuque/__latex/dd8ef5e6cdc4ee13855bc4cfbee8c3e4.svg)<font style="color:rgb(18, 18, 18);">的特征值之间的关系。</font>

<font style="color:rgb(18, 18, 18);">PCA 需要对协方差矩阵 </font>![image](https://cdn.nlark.com/yuque/__latex/b43788f8b480c8bccaaf8b720ccfa8e6.svg)<font style="color:rgb(18, 18, 18);"> 。进行特征值分解； SVD 也是对</font>![image](https://cdn.nlark.com/yuque/__latex/dd8ef5e6cdc4ee13855bc4cfbee8c3e4.svg)<font style="color:rgb(18, 18, 18);"> 进行特征值分解。如果取</font>![image](https://cdn.nlark.com/yuque/__latex/19120c0c78a58820caa5fdec9cd7e04b.svg)<font style="color:rgb(18, 18, 18);">则两者基本等价。所以 PCA 问题可以转换成 SVD 求解。</font>

<font style="color:rgb(18, 18, 18);">而实际上 Sklearn 的 PCA 就是用 SVD 进行求解的，原因有以下几点：</font>

1. <font style="color:rgb(18, 18, 18);">当样本维度很高时，协方差矩阵计算太慢；</font>
2. <font style="color:rgb(18, 18, 18);">方阵特征值分解计算效率不高；</font>
3. <font style="color:rgb(18, 18, 18);">SVD 除了特征值分解这种求解方式外，还有更高效更准确的迭代求解方式，避免了</font>![image](https://cdn.nlark.com/yuque/__latex/dd8ef5e6cdc4ee13855bc4cfbee8c3e4.svg)<font style="color:rgb(18, 18, 18);">的计算；</font>
4. <font style="color:rgb(18, 18, 18);">其实 PCA 与 SVD 的右奇异向量的压缩效果相同。</font>

  
  


















