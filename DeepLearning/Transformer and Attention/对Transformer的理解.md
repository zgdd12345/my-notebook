核心思想：使用Attention机制，在一个序列的不同位置之间建立distance=1的平行关系，从而解决RNN的长距离依赖问题（distance=N）。

## 1. Attention的细节
### 1.1 点积Attention
$$
Attention(Q,K,V) = softmax(\frac{QK^T}{\sqrt{d^k}})V
$$

![[src/transformer_atten.png]]
如图所示：$Q_{M \times d}, K_{N \times d}$ 分别是query和key。其中，query可以看作M个维度为d的向量(长度为M的sequence的向量表达)拼接而成，key可以看作N个维度为d的向量(长度为N的sequence的向量表达)拼接而成。

**为什么有缩放因子 $\sqrt{d^k}$ ?
- 作用：归一化。
- 解释：一般来说，输入的Q、K、V都是经过normalization操作的均值为0方差为1的数据。那么，$Q^TK$的结果则是均值仍然为0，但是方差为d（因为d个方差为1的数据相乘然后相加）当d变得很大时， A 中的元素的方差也会变得很大，如果 A 中的元素方差很大，那么$softmax⁡(A)$ 的分布会趋于陡峭(分布的方差大，分布集中在绝对值大的区域)。总结一下就是$softmax⁡(A)$的分布会和d有关。因此A 中每一个元素乘上 $\frac{1}{\sqrt{d^k}}$ 后，方差又变为1。这使得$softmax⁡(A)$ 的分布“陡峭”程度与d解耦，从而使得训练过程中梯度值保持稳定。
### 1.2 Attention机制涉及到的参数
- 把$q , k , v$分别映射到$Q , K , V$的线性变换矩阵$WQ(d_{model}\times d_k ), WK(d_{model}\times d_k ), WV(d_{model} \times d_v)$
- 把输出的表达 $O$ 映射为最终输出$o$ 的线性变换矩阵 $WO ( d_v \times d_{model})$
### 1.3 Query, Key, Value
Query和Key作用得到的attention权值会作用到Value上。因此它们之间的关系是:
	1. Query($M \times d_{qk}$) 和Key($N \times d_{qk}$)的维度必须一致，Value ($N \times d_v$) 和Query/Key的维度可以不一致。
	2. Key($N \times d_{qk}$)和Value ($N \times d_{v}$)的长度必须一致。Key和Value本质上对应了同一个Sequence在不同空间的表达。
	3. Attention得到的Output ($M \times d_v$) 的维度和Value的维度一致，长度和Query一致。
	4. Output每个位置 $i$ 是由value的所有位置的vector加权平均之后的向量；而其权值是由位置为$i$ 的query和key的所有位置经过attention计算得到的 ，权值的个数等于key/value的长度。
![[src/Pasted image 20250427164600.png]]

在经典的Transformer模型中，我们记线性映射之前的Query, Key, Value为$q, k, v$，映射之后为$Q, K, V$。那么:
	1. self-attention的$q, k, v$都是**同一个输入**, 即当前序列由上一层输出的高维表达。
	2. cross-attention的$q$代表当前序列，$k,v$是同一个输入，对应的是被编码的序列，也即encoder最后一层的输出结果(对decoder端的每一层来说，$k$和$v$保持不变)
而每一层线性映射参数矩阵都是独立的，所以经过映射后的$Q, K, V$各不相同，模型参数优化的目标在于将$q, k, v$被映射到新的高维空间，使得每层的$Q, K, V$在不同抽象层面上捕获到$q, k, v$之间的关系。一般来说，底层layer捕获到的更多是lexical-level的关系，而高层layer捕获到的更多是semantic-level的关系。