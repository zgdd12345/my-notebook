# numpy模块

## 1.概述

## 2.常用方法

## 3.日常笔记

### 3.1np.savetxt()

将array保存到txt文件，并保持原格式

问题：1.如何将array保存到txt文件中？2.如何将存到txt文件中的数据读出为ndarray类型？

需求：科学计算中，往往需要将运算结果（array类型）保存到本地，以便进行后续的数据分析。

解决：直接用numpy中的方法。

1:numpy.savetxt(fname,X):第一个参数为文件名，第二个参数为需要存的数组（一维或者二维）。

2.numpy.loadtxt(fname)：将数据读出为array类型。

关于如何保存路径和保持格式

```
np.savetxt('C:/Users/lai/eclipse-workspace/Geolife Trajectories 1.3beijinglhsh/
			spcluster.txt',spcluster,fmt="%.18f,%.18f",delimiter="\n")
```

 第一个参数可以指定保存的路径以及文件名，注意指定的文件路径必须存在，它不会为你新建新的文件，会报错。fmt="%.18f,%.18f"指定保存的文件格式，delimiter="\n"表示分隔符，

