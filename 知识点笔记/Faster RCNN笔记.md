# Faster RCNN笔记

## 算法流程

1. 首先将输入图片放缩到W*H，然后送入VGG16提取出feature map(W/16,H/16)。
2. 在feature map 上每个点都对应原图上的9个anchor,送入RPN层后输出两个：这9个anchor前背景的概率以及四个坐标的回归。
3. 每个anchor经过回归后对应到原图，然后再对应到feature map经过roi polling后输出7*7大小的map。
4. 最后对7*7的map进行分类和再次回归。



## IOU：

Intersection over Union 是一种测量在特定数据集中检测相应物体准确度的一个标准。

需要的数据：

1. ground-truth bounding boxes:人为在训练集图像中标出要检测物体的大概范围：
2. Predicted bounding box:算法得出的结果的范围。

即，该标准用于测量真实范围和预测结果之间的相关度，相关度越高，该值越高。

<img src="img\IOU.png" style="zoom:25%;" />

## Faster RCNN思想

