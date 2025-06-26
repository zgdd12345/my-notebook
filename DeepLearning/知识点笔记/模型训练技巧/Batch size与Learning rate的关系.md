<h1 id="OCkPe">batch size的增加</h1>
增加batch size的优点：

1. 增大batch size后数据处理速度快，跑完一个epoch时间短
2. <font style="color:rgba(0, 0, 0, 0.75);">在一定范围内，一般来说 Batch Size 越大，其确定的下降方向越准，引起训练震荡越小。尤其是网络中</font>**<font style="color:rgba(0, 0, 0, 0.75);">有BN层，过小的batch size网络性能会急剧下降</font>**<font style="color:rgba(0, 0, 0, 0.75);">。</font>
3. <font style="color:rgba(0, 0, 0, 0.75);">另一方面，大的batch size梯度的计算更加稳定，因为模型训练曲线会更加平滑。在</font>**<font style="color:rgba(0, 0, 0, 0.75);">微调的时候，大的batch size可能会取得更好的结果</font>**<font style="color:rgba(0, 0, 0, 0.75);">。</font>

<font style="color:rgba(0, 0, 0, 0.75);">缺点：</font>

1. <font style="color:rgba(0, 0, 0, 0.75);">训练一个epoch的迭代次数变少，从而对参数的修正也就显得更加缓慢，要想达到相同的精度，其所花费的时间大大增加了。大的batchsize性能下降是因为训练时间不够长，本质上并不是batchsize的问题，在</font>**<font style="color:rgba(0, 0, 0, 0.75);">同样的epochs下的参数更新变少了，因此需要更长的迭代次数</font>**<font style="color:rgba(0, 0, 0, 0.75);">。</font>
2. <font style="color:rgba(0, 0, 0, 0.75);">Batch Size 增大到一定程度，其确定的下降方向已经基本不再变化。</font>
3. <font style="color:rgba(0, 0, 0, 0.75);">增加batch size会导致模型泛化能力下降，小的batchsize带来的噪声有助于逃离局部极小值。总之batchsize在变得很大（</font>**<font style="color:rgba(0, 0, 0, 0.75);">超过临界点)时，会降低模型的泛化能力</font>**<font style="color:rgba(0, 0, 0, 0.75);">。在这个临界点之下，模型的性能变换随batchsize通常没有学习率敏感。</font>

<h1 id="iHAcu"><font style="color:rgba(0, 0, 0, 0.75);">Batch size 与学习率的关系</font></h1>
通常当我们增加batch size为原来的N倍时，要保证经过同样的样本后更新的权重相等，按照线性缩放规则，学习率应该增加为原来的N倍（因为许多loss函数是除以了N，所以增大batchsize之后，loss并没有增加，故一样多的样本，却更新的更少。所以，对于那种增加batchsize，loss也会跟着增大的损失函数，还不能一味的增大lr）。如果要保证权重的方差不变，则学习率应该增加为原来的sqrt(N)倍，目前这两种策略都被研究过，使用前者的明显居多。

<font style="color:rgb(77, 77, 77);">从两种常见的调整策略来看，学习率和batchsize都是同时增加的。学习率是一个非常敏感的参数，不可能太大，否则模型会不收敛。同样batchsize也会影响模型性能，那实际使用中都如何调整这两个参数呢？</font>

<font style="color:rgb(77, 77, 77);">研究表明，衰减学习率可以通过增加batchsize来实现类似的效果（同样，因为许多loss函数是除以了N)，你从从SGD的权重更新式子就可以看出来两者确实是等价的。比如：在pytorch中torch.nn.MSELoss(size_average=True)如果size_average=True, 返回loss.mean();就是平均数如果为False,返回loss.sum()，此时batchsize增大loss也会增大！默认情况下，size_average=True</font>

<h1 id="TiV1V"><font style="color:rgb(77, 77, 77);">小结</font></h1>
<font style="color:rgb(77, 77, 77);">如果增加了学习率，那么batchsize最好也跟着增加，这样收敛更稳定（因为batchsize大的话，每一步更新的准确性会更好，也就可以放心的往前走了）。适当使用大的学习率，因为很多研究都表明更大的学习率有利于提高泛化能力。如果要衰减，可以先尝试其他办法，比如增加batchsize，学习率对模型的收敛影响比较大，需慎重且多次调整。</font>

<font style="color:rgba(0, 0, 0, 0.75);">  
</font>

