**SHAP（SHapley Additive exPlanations）** 基于博弈论的 **沙普利值（Shapley Value）**，用于解释机器学习模型的预测结果。其核心思想是将单个样本的模型输出分解为各特征的加性贡献，形式为：

f(x)=ϕ0+∑j=1Mϕj(x)f(x) = \phi_0 + \sum_{j=1}^{M} \phi_j(x)f(x)=ϕ0​+j=1∑M​ϕj​(x)

其中，ϕj(x)\phi_j(x)ϕj​(x) 表示特征 jjj 对预测结果的 **平均边际贡献**，ϕ0\phi_0ϕ0​ 为模型在基线样本（背景分布）上的期望输出。  
SHAP 通过枚举特征加入顺序并计算边际增益的期望，实现了 **公平、可解释** 的特征归因，能够同时考虑特征之间的交互作用，并满足 **局部精确性（Local Accuracy）**、**零贡献性（Missingness）** 和 **一致性（Consistency）** 等理论公理，因此结果具有明确的数学依据。

在实现上，**TreeSHAP** 可在树模型中高效（近似）精确计算，**KernelSHAP** 适用于任意黑盒模型。  
全局层面可通过 mean(∣ϕj∣)\text{mean}(|\phi_j|)mean(∣ϕj​∣) 对特征重要性排序；  
局部层面可使用依赖图（Dependence Plot）揭示非线性与交互效应，或通过瀑布图（Waterfall Plot）解释单个样本的预测来源。  
需注意背景分布的选择及强相关特征可能导致的归因偏差。