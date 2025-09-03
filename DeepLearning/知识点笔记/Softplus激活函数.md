**Softplus** 是一种平滑版的 ReLU 激活函数，常写成

$$
\operatorname{softplus}(x)=\log(1+e^{x})
$$

更一般的 **β‑Softplus** 为

$$
\operatorname{softplus}_\beta(x)=\frac{1}{\beta}\log\!\big(1+e^{\beta x}\big)\quad(\beta>0)
$$

---

## 直观理解

- 它是 **log-sum-exp** 的二元特例：$\log(e^{0}+e^{x})$，可看作对 $\max(0,x)$（即 ReLU）的光滑近似。
    当$x\gg 0$：$\operatorname{softplus}(x)\approx x$；  
	当$x\ll 0$：$\operatorname{softplus}(x)\approx e^{x}$（很接近 0）；  
    在$x=0$：$\operatorname{softplus}(0)=\log 2\approx 0.693$。
- 与 ReLU 的差值有界：对任意 $x$，$\operatorname{softplus}(x)-\operatorname{ReLU}(x)\in(0,\log 2]$。

---

## 导数与性质

- 一阶导数（梯度）：
    
    ddxsoftplus⁡β(x)=σ(βx)=11+e−βx,\frac{d}{dx}\operatorname{softplus}_\beta(x)=\sigma(\beta x)=\frac{1}{1+e^{-\beta x}},dxd​softplusβ​(x)=σ(βx)=1+e−βx1​,
    
    即 **Sigmoid**。因此梯度在 (0,1)(0,1)(0,1) 之间，函数是 **1‑Lipschitz**（对 β=1）。
    
- 二阶导数：
    
    d2dx2softplus⁡β(x)=β σ(βx)(1−σ(βx))≥0,\frac{d^2}{dx^2}\operatorname{softplus}_\beta(x)=\beta\,\sigma(\beta x)\big(1-\sigma(\beta x)\big)\ge 0,dx2d2​softplusβ​(x)=βσ(βx)(1−σ(βx))≥0,
    
    所以 **凸** 且 **单调递增**，处处可导（比 ReLU 更“平滑”）。
    
- 由于输出恒为正且无上界，常用于“**需要正数**”的模型参数（如方差、速率、尺度）。
    

---

## 为什么用 Softplus？

**优点**

- **平滑**：避免 ReLU 在 0 处不可导的尖点，更利于一些二阶/变分方法与概率模型。
    
- **非零负区梯度**：x<0x<0x<0 时梯度虽小但非零，能一定程度缓解 “ReLU 死亡”。
    
- **正值约束**：天然保证输出 > 0，常用于高斯分布的 σ\sigmaσ、Poisson 强度、流模型/能量模型中的正参数等。
    
- **可调锐度**：通过 β 控制“像 ReLU 的程度”；β 越大，越接近 ReLU。
    

**可能的缺点**

- **非零均值**（不以 0 为中心）：可能导致激活均值偏移，需要配合归一化层或合适的偏置初始化。
    
- **负向饱和**：x≪0x\ll 0x≪0 时梯度接近 0，会带来一定的梯度消失风险（但通常比 Sigmoid/Tanh 好）。
    
- **略高的计算开销**：比 ReLU 稍贵，不过现代硬件上差异不大。
    

---

## 与其他激活的对比（简表）

|激活|形状|0 附近是否平滑|负区梯度|输出范围|典型用途|
|---|---|---|---|---|---|
|ReLU|分段线性|否|0|[0,∞)[0,\infty)[0,∞)|通用隐藏层|
|**Softplus**|平滑 ReLU|**是**|**>0（很小）**|(0,∞)(0,\infty)(0,∞)|正参数、概率建模、想要平滑性|
|GELU|近似门控高斯|是|>0|R\mathbb{R}R|大模型、Transformer|
|SiLU/Swish|x⋅σ(x)x\cdot\sigma(x)x⋅σ(x)|是|>0|R\mathbb{R}R|CNN/Transformer 常见|
|ELU/SELU|负区光滑|是|>0|R\mathbb{R}R 或带负饱和|深层网络、归一化友好|

---

## 数值与实现要点（PyTorch）

- **函数/模块**：
    
    `import torch import torch.nn.functional as F y = F.softplus(x, beta=1.0, threshold=20.0) # 或 act = torch.nn.Softplus(beta=1.0, threshold=20.0) y = act(x)`
    
- **稳定实现**：内部使用稳定公式  
    log⁡1p(e−∣x∣)+max⁡(x,0)\log1p(e^{-|x|})+\max(x,0)log1p(e−∣x∣)+max(x,0)，并在 `beta*x > threshold` 时近似为 xxx 以避免溢出。
    
- **正值约束示例**（给方差/尺度）：
    
    `raw_scale = torch.randn(batch, dim) scale = F.softplus(raw_scale) + 1e-6  # 加小常数防止为 0`
    
- **β 的作用**：`beta↑` → 曲线更陡，逼近 ReLU；`beta↓` → 更平滑、更接近线性。
    
- **反函数**（偶尔用于重参数化）：  
    softplus⁡−1(y)=log⁡(ey−1)=log⁡(expm1⁡(y))\operatorname{softplus}^{-1}(y)=\log(e^{y}-1)=\log(\operatorname{expm1}(y))softplus−1(y)=log(ey−1)=log(expm1(y))。
    

---

## 何时选用？

- **隐藏层**：若追求更平滑的优化或在概率模型中，Softplus 是 ReLU 的稳妥替代；但在主流判别模型里，GELU/SiLU 常更优。
    
- **输出层**：当你需要 **严格正值** 且 **梯度不过分爆炸** 的映射（比 `exp` 更温和），Softplus 非常合适（如方差、标准差、强度、速率等）。
    

如果你正把某个参数限制为正、又担心 `exp` 带来的梯度/数值不稳定，**Softplus 往往是首选**。