## 原因分析
Numpy数组以C语言的方式连续地存储在内存中，当Python解释器取值时，步骤如下：

+ 将arr[0]中的索引0，转换为C语言可以接收的值0
+ 经过Python-C的接口，获取np.array的第一个数字1。
+ 获取的数字1还是C语言的整型1，还需要先通过Python-C接口传给Python解释器，再类型转换为Python语言可以识别的数据类型（不是Python内建的int型，而是numpy定义的np.int型）。
+ 将1赋值给b，此时b为np.int型。

上述过程比直接从变量list中取元素多很多步，所以效率低，速度慢。

在Python解释器层面，list有过专门的优化。



## 表现
+ 使用numpy.array然后循环套循环地操作，常见于使用Python语言编制图像处理、方程求解等算法的场合。由于索引比较慢，所以这样的操作自然是十分缓慢的，速度甚至比不上直接用list来保存结果。
+ numpy是内存连续的，因此做np.c_、np.delete等增加一行/一列、删除操作时，会涉及到元素的成片移动、复制或者删除。效率上可能反而会不如使用Python原生的数据结构。



## List中的pop
之前在问题2中，原文是”numpy的增删操作，效率不如list.append/list.pop“。但是经过最近的学习发现，list.pop的效率需要分情况看待。如果从头部或者比较靠近头部的位置删除，那么也是开销很大的。因为Python的list是一个顺序表，删除头元素会导致列表的整体移动。因此将list.pop删去。

如果要实现先入先出的队列，建议用[queue包](https://www.zhihu.com/search?q=queue%E5%8C%85&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2122845051%7D)中的Queue；若要实现[双端队列](https://www.zhihu.com/search?q=%E5%8F%8C%E7%AB%AF%E9%98%9F%E5%88%97&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2122845051%7D)，则建议用collections包中的[deque](https://www.zhihu.com/search?q=deque&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2122845051%7D)。

总而言之：**为性能着想，不建议使用list来代替队列！**

