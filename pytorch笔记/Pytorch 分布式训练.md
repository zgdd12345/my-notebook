# Pytorch 分布式训练

## 0.概述

### torch.distributed 包支持

`Pytorch` 中通过 `torch.distributed` 包提供分布式支持，包括 `GPU` 和 `CPU` 的分布式训练支持。`Pytorch` 分布式**目前只支持 `Linux`**。

在此之前，`torch.nn.DataParallel` 已经提供**数据并行**的支持，但是其不支持多机分布式训练，且底层实现相较于 `distributed` 的接口，有些许不足。

**`torch.distributed` 的优势如下：**

**1.每个进程对应一个独立的训练过程，且只对梯度等少量数据进行信息交换。**

在每次迭代中，每个进程具有自己的 `optimizer` ，并独立完成所有的优化步骤，进程内与一般的训练无异。

在各进程梯度计算完成之后，各进程需要将梯度进行汇总平均，然后再由 `rank=0` 的进程，将其 `broadcast` 到所有进程。之后，各进程用该梯度来更新参数。

由于各进程中的模型，初始参数一致 (初始时刻进行一次 `broadcast`)，而每次用于更新参数的梯度也一致，因此，各进程的模型参数始终保持一致。

而在 `DataParallel` 中，全程维护一个 `optimizer`，对各 `GPU` 上梯度进行求和，而在主 `GPU` 进行参数更新，之后再将模型参数 `broadcast` 到其他 `GPU`。

相较于 `DataParallel`，`torch.distributed` 传输的数据量更少，因此速度更快，效率更高。

**2.每个进程包含独立的解释器和 GIL**。

由于每个进程拥有独立的解释器和 `GIL`，消除了来自单个 `Python` 进程中的多个执行线程，模型副本或 `GPU` 的额外解释器开销和 `GIL-thrashing` ，因此可以减少解释器和 `GIL` 使用冲突。这对于严重依赖 `Python runtime` 的 `models` 而言，比如说包含 `RNN` 层或大量小组件的 `models` 而言，这尤为重要。

