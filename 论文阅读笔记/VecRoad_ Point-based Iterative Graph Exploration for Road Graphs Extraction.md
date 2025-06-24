1. 基本信息：
    1. 姓名：Yong-Qiang Tan，Shang-Hua Gao， Xuan-Yi Li， Ming-Ming Cheng，Bo Ren
    2. 单位：TKLNDST, College of CS, Nankai University
    3. 标题：VecRoad: Point-based Iterative Graph Exploration for Road Graphs Extraction
    4. 刊物：CVPR2020
2. 内容：
    1. Abstract

Extracting road graphs from aerial images automatically is more efficient and costs less than from field acquisition. This can be done by a post-processing step that vectorizes road segmentation predicted by CNN, but imperfect predictions will result in road graphs with low connectivity. On the other hand, iterative next move exploration could construct road graphs with better road connectivity, but often focuses on local information and does not provide precise alignment with the real road. To enhance the road connectivity while maintaining the precise alignment between the graph and real road, we propose a point-based iterative graph exploration scheme with segmentation-cues guidance and flexible steps. In our approach, we represent the location of the next move as a ‘point’ that unifies the representation of multiple constraints such as the direction and step size in each moving step. Information cues such as road segmentation and road junctions are jointly detected and utilized to guide the next move and achieve better alignment of roads. We demonstrate that our proposed method has a considerable improvement over state-of-the-art road graph extraction methods in terms of F-measure and road connectivity metrics on common datasets.

使用道路分割的结果构建的道路图连通性较低。另一方面，迭代的下一步探索的方法可以构建具有更好的道路连通性的道路图，但是往往仅关注局部信息，无法提供与真实道路的精确对齐。 为了在增强道路连通性的同时保持图与真实道路的精确对齐，我们提出了一种基于分割线索引导和灵活步骤的点迭代图探索方案。  

    2. Introduction



    3. Method



    4. Result



    5. Conclusion

