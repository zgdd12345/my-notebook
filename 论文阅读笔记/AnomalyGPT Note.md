# 0. Basic Information
## Title: 
 <a href="https://ojs.aaai.org/index.php/AAAI/article/view/27963" title="超链接title">AnomalyGPT: Detecting Industrial Anomalies Using Large Vision-Language Models</a>

## Conforence: 
AAAI2024

## Author: 
Zhaopeng Gu, Bingke Zhu, Guibo Zhu, Yingying Chen, Ming Tang, Jinqiao Wang 

Foundation Model Research Center, Institute of Automation, Chinese Academy of Sciences, Beijing, China 

## Code
 <a href="https://github.com/CASIA-IVA-Lab/AnomalyGPT.git" title="超链接title">AnomalyGPT Github Code</a>

# 1. Abstract
1. 由于大量的训练数据，现有大模型有很强的图像理解能力，在常见对象识别上表现优异，但是其缺乏特定领域的知识，并且对对象内的局部细节的理解较弱，这阻碍了它们在工业异常检测（IAD， Industr Anomaly Detection）任务中的应用。
2. 该文探索利用LVLM来解决IAD问题，并提出一种基于LVLM的新型 IAD方法AnomalyGPT。
3. 通过模拟异常图像并为每个图像生成相应的文本描述来生成训练数据。
4. 优点：1）不需要手动调整阈值， 2）AnomalyGPT支持多轮对话，3）令人印象深刻的少样本上下文学习能力。
5. With only one normal shot, AnomalyGPT achieves the stateof-the-art performance with an accuracy of 86.1%, an imagelevel AUC of 94.1%, and a pixel-level AUC of 95.3% on the MVTec-AD dataset.

# 2. Introduction
1. Due to the rarity and unpredictability of real-world samples, models are required to be trained only on normal samples and distinguish anomalous samples that deviate from normal samples.
2. Current IAD methods (Jeong et al. 2023; Huang et al. 2022; You et al. 2022) typically only provide anomaly scores for test samples and require manually specification of thresholds to distinguish between normal and anomalous instances for each class of items, which is not suitable for real production environments.
3. Moreover, our method can provide information about the image and allows for interactive engagement, enabling users to ask follow-up questions based on their needs and the provided answers.
4. AnomalyGPT can also perform in-context learning with a small number of normal samples, enabling swift adaptation to previously unseen objects.
5. Specifically, we focus on fine-tuning the LVLM using synthesized anomalous visual-textual data, integrating IAD knowledge into the model.
6. Challenges：
   1. The first is data scarity: existing IAD datasets (Bergmann et al. 2019; Zou et al. 2022) contain only a few thousand samples, rendering direct fine-tuning easy to overfitting and catastrophic forgetting.
   2. The second challenge relates to fine-grained semantic.
7. Solution:
   1. we use prompt embeddings to fine-tune the LVLM instead of parameter fine-tuning. Additional prompt embeddings are added after image inputs, introducing supplementary IAD knowledge into the LVLM.
   2. We propose a lightweight, visual-textual feature-matching-based decoder to generate pixel-level anomaly localization results.
8. Contributions:
   1. Our method not only detects and locates anomaly without manually threshold adjustments but also supports multi-round dialogues.
   2. To the best of our knowledge, we are the first to successfully apply LVLM to the domain of industrial anomaly detection.
   3. The lightweight, visual-textual feature-matching-based decoder in our work addresses the limitation of the LLM’s weaker discernment of fine-grained semantic and alleviates the constraint of LLM’s restricted ability to solely generate text outputs.
   4. We employ prompt embeddings for fine-tuning and train our model concurrently with the data utilized during LVLM pre-training, thus preserving the LVLM’s inherent capabilities and enabling multi-turn dialogues.
   5. Our method retains robust transferability and is capable of engaging in in-context few-shot learning on new datasets, yielding outstanding performance.

# 3. Methods

# 4. Results

# 5. Conclusion
1. AnomalyGPT can determine whether an image contains anomalies and pinpoint their locations without the need for manually specified thresholds. 
2. Furthermore, AnomalyGPT enables multi-turn dialogues focused on anomaly detection 
3. and demonstrates remarkable performance in few-shot in-context learning. 
4. The effectiveness of AnomalyGPT is validated on two common datasets.
