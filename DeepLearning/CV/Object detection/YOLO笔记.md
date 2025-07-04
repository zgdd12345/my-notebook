Yolo使用一个单独的CNN模型实现end to end的目标检测。速度由于RCNN系列目标检测算法，但精度略低。

[知乎链接](https://zhuanlan.zhihu.com/p/32525231)

---

# 算法思想
Yolo的CNN将输入的图片**分割成**![image](https://cdn.nlark.com/yuque/__latex/8eda040a64788851fdad3f88f1932654.svg)**网格**，然后由每个单元格检测中心点落在该格子内点目标。每个单元格会预测![image](https://cdn.nlark.com/yuque/__latex/e3e6ace30a115e42cae3163d49bdf119.svg)**个边界框（bounding box）**以及**边界框的置信度（confidence score）**。上述置信度包含两个方面，一个是边界框包含目标的可能性（ 记为![image](https://cdn.nlark.com/yuque/__latex/14f84b51bc2cb8192bcc240e59c8081c.svg)），一个是边界框的准确度（使用![image](https://cdn.nlark.com/yuque/__latex/214668b5b2ef3f2cde8718b88432a183.svg)计算）。**置信度的定义为**![image](https://cdn.nlark.com/yuque/__latex/5b3af1be565d76f95199e9716f47913c.svg)**。**

边界框的大小与位置用4个值来表征：![image](https://cdn.nlark.com/yuque/__latex/1addf9d5c3ec6fde1382b6e876ddd484.svg)。其中![image](https://cdn.nlark.com/yuque/__latex/77e36ce6fda575c648e7059bfa63fade.svg)为边界框中心坐标，![image](https://cdn.nlark.com/yuque/__latex/c9b08ae6d9fed72562880f75720531bc.svg)和![image](https://cdn.nlark.com/yuque/__latex/67df0f404d0960fadcc99f6258733f22.svg)为边界框的宽于高。值得注意的是中心坐标的预测值![image](https://cdn.nlark.com/yuque/__latex/77e36ce6fda575c648e7059bfa63fade.svg)是相对于每个单元格左上角坐标点的偏移值，并且单位是相当于单元格大小的。而边界框的![image](https://cdn.nlark.com/yuque/__latex/c9b08ae6d9fed72562880f75720531bc.svg)和![image](https://cdn.nlark.com/yuque/__latex/67df0f404d0960fadcc99f6258733f22.svg)预测值是相对于整个图片的宽与高的比例。这样理论上四个元素的大小应当是![image](https://cdn.nlark.com/yuque/__latex/12d16d9672fe55e37279ae7043b605de.svg)。最后，每个边界框的预测值实际上包含5个元素：![image](https://cdn.nlark.com/yuque/__latex/cd51c4bc0c9c5b584582970dfd28f40b.svg)，其中c是置信度。

分类问题：每个单元格需要给出预测出的![image](https://cdn.nlark.com/yuque/__latex/6f0e9db03441f0e41de3ad0600278f73.svg)个类别的概率值，其表征的是由该单元格负责预测的边界框其目标属于各单元格类别的概率。但是这些概率值其实是在各个边界框置信度下的条件概率，即![image](https://cdn.nlark.com/yuque/__latex/59345676b86d974a4ffcb2bf6f72a397.svg)在早先的yolo算法中，不管预测多少个边界框，只预测一组类别概率。在后来的改进版本中，Yolo9000把类别概率预测值与边界框绑定。各个边界框类别置信度如下：

![image](https://cdn.nlark.com/yuque/__latex/95c906150dec79da2ac14f65b5af17e0.svg)

边界框类别置信度表征的是该边界框中目标属于各个类别的可能性大小以及边界框匹配目标的好坏，后面根据类别置信度过滤网络的预测框。

小结：每个单元格需要预测![image](https://cdn.nlark.com/yuque/__latex/02ecc83332ad08a3c2bba56ec7828faf.svg)个值,若输入的图片分割成![image](https://cdn.nlark.com/yuque/__latex/8eda040a64788851fdad3f88f1932654.svg)网格，那么**最终预测值为**![image](https://cdn.nlark.com/yuque/__latex/636c20f34c00437b2bdd1b64614d85a6.svg)**大小的张量。**

---

# 网络设计
![](https://cdn.nlark.com/yuque/0/2023/png/29307286/1691662767709-2d6d0167-088e-4a67-8aa2-bfe3917773e1.png)





![](https://cdn.nlark.com/yuque/0/2023/png/29307286/1691663061346-a78b83b8-1398-46d1-8683-6649318e668f.png)



---

# 模型训练
## ImageNet预训练
## 损失函数
 

