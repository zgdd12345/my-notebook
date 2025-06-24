**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">广播</font>**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">是</font>**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">两数组形同</font>**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">、对应位置上的元素做某种运算，如a和b数组做加法或减法，那么结果是a和b对应位置上的数据加、减后的计算值作为结果这个位置上的数据。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">对于不同的shape的数组NumPy使用了广播机制来预处理一下表达式里的数组使其最终可以实现广播计算功能，注意这里</font>**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">广播和广播机制</font>**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">是两个概念。</font>

**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">广播机制</font>**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">是Numpy让两个不同shape的数组能够做一些运算，需要对参与运算的两个数组做一些</font>**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">处理或者说扩展</font>**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">，最终是参与运算的两个数组的shape一样，然后广播计算(对应位置数据进行某运算)得到结果。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">广播时需要对两个数组做广播机制处理，不是所有情况下两个数组都能进行广播机制的处理，有要求即两数组需满足</font>**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">广播兼容</font>**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">，需判断两个数组能否进行广播机制处理成同型shape的数组然后广播。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">判断是否</font>**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">广播兼容</font>**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">，规则是，比较两个数组的shape，从shape的尾部开始一一比对。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">(1). 如果两个数组的维度相同，对应位置上轴的长度相同或其中一个的轴长度为1,广播兼容，可在轴长度为1的轴上进行广播机制处理。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">(2). 如果两个数组的维度不同，那么给低维度的数组</font>**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">前扩展</font>**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">提升一维，扩展维的轴长度为1,然后在扩展出的维上进行广播机制处理。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">广播机制在将两数组变成维度和shape相同时，对</font>**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">实施广播机制的数组的处理</font>**<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);">是拷贝赋值未广播处理的轴的数据。</font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);"></font>

<font style="color:rgb(64, 64, 64);background-color:rgb(252, 252, 252);"></font>

```plain

```

