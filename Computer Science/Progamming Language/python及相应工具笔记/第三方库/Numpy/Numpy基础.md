# [NumPy 教程 | 菜鸟教程](https://www.runoob.com/numpy/numpy-tutorial.html)
# Ndarray数组
<font style="color:rgb(51, 51, 51);">N 维数组对象 ndarray是一系列同类型数据的集合。ndarray中的每个元素在内存中都有相同大小的存储区域。</font>

---

## 存储原理与内存机制：
**<font style="color:rgb(51, 51, 51);">ndarray构成</font>**

+ <font style="color:rgb(51, 51, 51);">一个指向数据（内存或内存映射文件中的一块数据）的</font>**<font style="color:rgb(51, 51, 51);">指针</font>**<font style="color:rgb(51, 51, 51);">。</font>
+ **<font style="color:rgb(51, 51, 51);">数据类型</font>**<font style="color:rgb(51, 51, 51);">或 dtype，</font><u><font style="color:#DF2A3F;">描述在数组中的固定大小值的格子。</font></u>
+ <font style="color:rgb(51, 51, 51);">一个表示数组形状（</font>**<font style="color:rgb(51, 51, 51);">shape</font>**<font style="color:rgb(51, 51, 51);">）的元组，表示各维度大小的元组。</font>
+ <font style="color:rgb(51, 51, 51);">一个</font>**<font style="color:rgb(51, 51, 51);">跨度元组（stride</font>**<font style="color:rgb(51, 51, 51);">），其中的整数指的是</font>**<font style="color:rgb(51, 51, 51);">为了前进到当前维度下一个元素需要"跨过"的字节数。</font>**

<font style="color:rgb(51, 51, 51);">跨度可以是负数，这样会使数组在内存中后向移动，切片中</font>**<font style="color:rgb(51, 51, 51);background-color:rgb(236, 234, 230);"> obj[::-1]</font>**<font style="color:rgb(51, 51, 51);"> 或 </font>**<font style="color:rgb(51, 51, 51);background-color:rgb(236, 234, 230);">obj[:,::-1]</font>**<font style="color:rgb(51, 51, 51);"> 就是如此。</font>**<font style="color:rgb(51, 51, 51);">  
</font>**

<font style="color:rgb(51, 51, 51);">Numpy中将数据存储在一个</font>**<font style="color:rgb(51, 51, 51);">均匀连续的内存块</font>**<font style="color:rgb(51, 51, 51);">中，即，多维数组在numpy内部以一维数组的形式存储，我们只要知道每个元素所占的字节数（dtype），以及每个维度中元素的个数（shape），就可以快速定位到任意维度的任意一个元素。</font>

---

<font style="color:rgb(51, 51, 51);">创建Ndarray数组</font>

`<font style="color:rgb(51, 51, 51);">numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)</font>`

**<font style="color:rgb(51, 51, 51);">参数说明：</font>**

| <font style="color:rgb(255, 255, 255);">名称</font> | <font style="color:rgb(255, 255, 255);">描述</font> |
| :--- | :--- |
| <font style="color:rgb(51, 51, 51);">object</font> | <font style="color:rgb(51, 51, 51);">数组或嵌套的数列</font> |
| <font style="color:rgb(51, 51, 51);">dtype</font> | <font style="color:rgb(51, 51, 51);">数组元素的数据类型，可选</font> |
| <font style="color:rgb(51, 51, 51);">copy</font> | <font style="color:rgb(51, 51, 51);">对象是否需要复制，可选</font> |
| <font style="color:rgb(51, 51, 51);">order</font> | <font style="color:rgb(51, 51, 51);">创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）</font> |
| <font style="color:rgb(51, 51, 51);">subok</font> | <font style="color:rgb(51, 51, 51);">默认返回一个与基类类型一致的数组</font> |
| <font style="color:rgb(51, 51, 51);">ndmin</font> | <font style="color:rgb(51, 51, 51);">指定生成数组的最小维度</font> |


## 数据类型
Numpy中的数据类型比Python丰富，基本可以和C语言的数据类型对应，也包含了Python的内置类型。

| <font style="color:rgb(255, 255, 255);">类型</font> | 描述 |
| :--- | --- |
| <font style="color:rgb(51, 51, 51);">bool_</font> | <font style="color:rgb(51, 51, 51);">布尔型数据类型（True 或者 False）</font> |
| <font style="color:rgb(51, 51, 51);">int_</font> | <font style="color:rgb(51, 51, 51);">默认的整数类型（类似于 C 语言中的 long，int32 或 int64）</font> |
| <font style="color:rgb(51, 51, 51);">intc</font> | <font style="color:rgb(51, 51, 51);">与 C 的 int 类型一样，一般是 int32 或 int 64</font> |
| <font style="color:rgb(51, 51, 51);">intp</font> | <font style="color:rgb(51, 51, 51);">用于索引的整数类型（类似于 C 的 ssize_t，一般情况下仍然是 int32 或 int64）</font> |
| <font style="color:rgb(51, 51, 51);">int8</font> | <font style="color:rgb(51, 51, 51);">字节（-128 to 127）</font> |
| <font style="color:rgb(51, 51, 51);">int16</font> | <font style="color:rgb(51, 51, 51);">整数（-32768 to 32767）</font> |
| <font style="color:rgb(51, 51, 51);">int32</font> | <font style="color:rgb(51, 51, 51);">整数（-2147483648 to 2147483647）</font> |
| <font style="color:rgb(51, 51, 51);">int64</font> | <font style="color:rgb(51, 51, 51);">整数（-9223372036854775808 to 9223372036854775807）</font> |
| <font style="color:rgb(51, 51, 51);">uint8</font> | <font style="color:rgb(51, 51, 51);">无符号整数（0 to 255）</font> |
| <font style="color:rgb(51, 51, 51);">uint16</font> | <font style="color:rgb(51, 51, 51);">无符号整数（0 to 65535）</font> |
| <font style="color:rgb(51, 51, 51);">uint32</font> | <font style="color:rgb(51, 51, 51);">无符号整数（0 to 4294967295）</font> |
| <font style="color:rgb(51, 51, 51);">uint64</font> | <font style="color:rgb(51, 51, 51);">无符号整数（0 to 18446744073709551615）</font> |
| <font style="color:rgb(51, 51, 51);">float_</font> | <font style="color:rgb(51, 51, 51);">float64 类型的简写</font> |
| <font style="color:rgb(51, 51, 51);">float16</font> | <font style="color:rgb(51, 51, 51);">半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位</font> |
| <font style="color:rgb(51, 51, 51);">float32</font> | <font style="color:rgb(51, 51, 51);">单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位</font> |
| <font style="color:rgb(51, 51, 51);">float64</font> | <font style="color:rgb(51, 51, 51);">双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位</font> |
| <font style="color:rgb(51, 51, 51);">complex_</font> | <font style="color:rgb(51, 51, 51);">complex128 类型的简写，即 128 位复数</font> |
| <font style="color:rgb(51, 51, 51);">complex64</font> | <font style="color:rgb(51, 51, 51);">复数，表示双 32 位浮点数（实数部分和虚数部分）</font> |
| <font style="color:rgb(51, 51, 51);">complex128</font> | <font style="color:rgb(51, 51, 51);">复数，表示双 64 位浮点数（实数部分和虚数部分）</font> |


## 数据类型对象（dtype）
<font style="color:rgb(51, 51, 51);">数据类型对象（numpy.dtype 类的实例）用来描述与数组对应的内存区域是如何使用，它描述了数据的以下几个方面：</font>

+ <font style="color:rgb(51, 51, 51);">数据的类型（整数，浮点数或者 Python 对象）</font>
+ <font style="color:rgb(51, 51, 51);">数据的大小（例如， 整数使用多少个字节存储）</font>
+ <font style="color:rgb(51, 51, 51);">数据的字节顺序（小端法或大端法）</font>
+ <font style="color:rgb(51, 51, 51);">在结构化类型的情况下，字段的名称、每个字段的数据类型和每个字段所取的内存块的部分</font>
+ <font style="color:rgb(51, 51, 51);">如果数据类型是子数组，那么它的形状和数据类型是什么。</font><font style="color:rgb(51, 51, 51);">	</font>

<font style="color:rgb(51, 51, 51);">字节顺序是通过对数据类型预先设定 </font>**<font style="color:rgb(51, 51, 51);background-color:rgb(236, 234, 230);"><</font>**<font style="color:rgb(51, 51, 51);"> 或 </font>**<font style="color:rgb(51, 51, 51);background-color:rgb(236, 234, 230);">></font>**<font style="color:rgb(51, 51, 51);"> 来决定的。 </font>**<font style="color:rgb(51, 51, 51);background-color:rgb(236, 234, 230);"><</font>**<font style="color:rgb(51, 51, 51);"> 意味着小端法(最小值存储在最小的地址，即低位组放在最前面)。</font>**<font style="color:rgb(51, 51, 51);background-color:rgb(236, 234, 230);">></font>**<font style="color:rgb(51, 51, 51);"> 意味着大端法(最重要的字节存储在最小的地址，即高位组放在最前面)。</font><font style="color:rgb(51, 51, 51);">  
</font>

<font style="color:rgb(51, 51, 51);">dtype 对象是使用以下语法构造的：</font>

`<font style="color:rgb(51, 51, 51);">numpy.dtype(object, align, copy)</font>`

+ <font style="color:rgb(51, 51, 51);">object - 要转换为的数据类型对象</font>
+ <font style="color:rgb(51, 51, 51);">align - 如果为 true，填充字段使其类似 C 的结构体。</font>
+ <font style="color:rgb(51, 51, 51);">copy - 复制 dtype 对象 ，如果为 false，则是对内置数据类型对象的引用</font>

## Numpy数组属性
<font style="color:rgb(51, 51, 51);">NumPy 数组的</font>**<font style="color:rgb(51, 51, 51);">维数</font>**<font style="color:rgb(51, 51, 51);">称为</font>**<font style="color:rgb(51, 51, 51);">秩（rank</font>**<font style="color:rgb(51, 51, 51);">），</font><u><font style="color:rgb(51, 51, 51);">秩就是轴的数量，即数组的维度</font></u><font style="color:rgb(51, 51, 51);">。</font>

<font style="color:rgb(51, 51, 51);">在 NumPy中，</font><u><font style="color:rgb(51, 51, 51);">每一个线性的数组称为是一个轴（axis），也就是维度（dimensions）</font></u><font style="color:rgb(51, 51, 51);">。比如说，二维数组相当于是两个一维数组，其中第一个一维数组中每个元素又是一个一维数组。所以一维数组就是 NumPy 中的轴（axis），第一个轴相当于是底层数组，第二个轴是底层数组里的数组。而轴的数量——秩，就是数组的维数。</font>

<font style="color:rgb(51, 51, 51);">很多时候可以声明 axis。axis=0，表示沿着第 0 轴进行操作，即对每一列进行操作；axis=1，表示沿着第1轴进行操作，即对每一行进行操作。</font>

<font style="color:rgb(51, 51, 51);">NumPy 的数组中比较重要 ndarray 对象属性有：</font>

| <font style="color:rgb(255, 255, 255);">属性</font> | <font style="color:rgb(255, 255, 255);">说明</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">ndarray.ndim</font> | **<font style="color:rgb(51, 51, 51);">秩</font>**<font style="color:rgb(51, 51, 51);">，即轴的数量或维度的数量</font> |
| <font style="color:rgb(51, 51, 51);">ndarray.shape</font> | **<font style="color:rgb(51, 51, 51);">数组的维度</font>**<font style="color:rgb(51, 51, 51);">，对于矩阵，n 行 m 列</font> |
| <font style="color:rgb(51, 51, 51);">ndarray.size</font> | **<font style="color:rgb(51, 51, 51);">数组元素的总个数</font>**<font style="color:rgb(51, 51, 51);">，相当于 .shape 中 n*m 的值</font> |
| <font style="color:rgb(51, 51, 51);">ndarray.dtype</font> | <font style="color:rgb(51, 51, 51);">ndarray 对象的</font>**<font style="color:rgb(51, 51, 51);">元素类型</font>** |
| <font style="color:rgb(51, 51, 51);">ndarray.itemsize</font> | <font style="color:rgb(51, 51, 51);">ndarray 对象中每个元素的大小，以字节为单位</font> |
| <font style="color:rgb(51, 51, 51);">ndarray.flags</font> | <font style="color:rgb(51, 51, 51);">ndarray 对象的内存信息</font> |
| <font style="color:rgb(51, 51, 51);">ndarray.real</font> | <font style="color:rgb(51, 51, 51);">ndarray元素的实部</font> |
| <font style="color:rgb(51, 51, 51);">ndarray.imag</font> | <font style="color:rgb(51, 51, 51);">ndarray 元素的虚部</font> |
| <font style="color:rgb(51, 51, 51);">ndarray.data</font> | <font style="color:rgb(51, 51, 51);">包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。</font> |


# Numpy数组创建
## 新建数组
### <font style="color:rgb(51, 51, 51);">numpy.empty</font>
<font style="color:rgb(51, 51, 51);">numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且</font>**<font style="color:rgb(51, 51, 51);">未初始化的数组</font>**<font style="color:rgb(51, 51, 51);">：</font>

`numpy.empty(shape, dtype = float, order = 'C')`

<font style="color:rgb(51, 51, 51);">参数说明：</font>

| <font style="color:rgb(255, 255, 255);">参数</font> | <font style="color:rgb(255, 255, 255);">描述</font> |
| :--- | :--- |
| <font style="color:rgb(51, 51, 51);">shape</font> | <font style="color:rgb(51, 51, 51);">数组形状</font> |
| <font style="color:rgb(51, 51, 51);">dtype</font> | <font style="color:rgb(51, 51, 51);">数据类型，可选</font> |
| <font style="color:rgb(51, 51, 51);">order</font> | <font style="color:rgb(51, 51, 51);">有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。</font> |


### <font style="color:rgb(51, 51, 51);">numpy.zeros</font>
<font style="color:rgb(51, 51, 51);">创建指定大小的数组，数组元素以 0 来填充：</font>

`numpy.zeros(shape, dtype = float, order = 'C')`

参数说明同上，数据类型默认为浮点数

### <font style="color:rgb(51, 51, 51);">numpy.ones</font>
<font style="color:rgb(51, 51, 51);">创建指定形状的数组，数组元素以 1 来填充：</font>

`numpy.ones(shape, dtype = None, order = 'C')`

参数说明同上

### <font style="color:rgb(51, 51, 51);">numpy.zeros_like</font>
<font style="color:rgb(51, 51, 51);">numpy.zeros_like 用于</font><u><font style="color:#DF2A3F;">创建一个与给定数组具有相同形状的数组</font></u><font style="color:rgb(51, 51, 51);">，数组元素以 0 来填充。</font>

<font style="color:rgb(51, 51, 51);">numpy.zeros 和 numpy.zeros_like 都是用于创建一个指定形状的数组，其中所有元素都是0。</font>

<font style="color:rgb(51, 51, 51);">它们之间的区别在于：numpy.zeros 可以直接指定要创建的数组的形状，而 numpy.zeros_like 则是创建一个与给定数组具有相同形状的数组。</font>

`<font style="color:rgb(51, 51, 51);">numpy.zeros_like(a, dtype=None, order='K', subok=True, shape=None)</font>`

<font style="color:rgb(51, 51, 51);">参数说明：</font>

| <font style="color:rgb(255, 255, 255);">参数</font> | <font style="color:rgb(255, 255, 255);">描述</font> |
| :--- | :--- |
| <font style="color:rgb(51, 51, 51);">a</font> | <font style="color:rgb(51, 51, 51);">给定要创建相同形状的数组</font> |
| <font style="color:rgb(51, 51, 51);">dtype</font> | <font style="color:rgb(51, 51, 51);">创建的数组的数据类型</font> |
| <font style="color:rgb(51, 51, 51);">order</font> | <font style="color:rgb(51, 51, 51);">数组在内存中的存储顺序，可选值为 'C'（按行优先）或 'F'（按列优先），默认为 'K'（保留输入数组的存储顺序）</font> |
| <font style="color:rgb(51, 51, 51);">subok</font> | <font style="color:rgb(51, 51, 51);">是否允许返回子类，如果为 True，则返回一个子类对象，否则返回一个与 a 数组具有相同数据类型和存储顺序的数组</font> |
| <font style="color:rgb(51, 51, 51);">shape</font> | <font style="color:rgb(51, 51, 51);">创建的数组的形状，如果不指定，则默认为 a 数组的形状。</font> |


### <font style="color:rgb(51, 51, 51);">numpy.ones_like</font>
<font style="color:rgb(51, 51, 51);">numpy.ones_like 用于创建一个与给定数组具有相同形状的数组，数组元素以 1 来填充。</font>

<font style="color:rgb(51, 51, 51);">numpy.ones 和 numpy.ones_like 都是用于创建一个指定形状的数组，其中所有元素都是 1。</font>

<font style="color:rgb(51, 51, 51);">它们之间的区别在于：numpy.ones 可以直接指定要创建的数组的形状，而 numpy.ones_like 则是创建一个与给定数组具有相同形状的数组。</font>  
`numpy.ones_like(a, dtype=None, order='K', subok=True, shape=None)`

## 从已有数组中创建
### <font style="color:rgb(51, 51, 51);">numpy.asarray</font>
<font style="color:rgb(51, 51, 51);">numpy.asarray 类似 numpy.array，但 numpy.asarray 参数只有三个，比 numpy.array 少两个。</font>

`<font style="color:rgb(51, 51, 51);">numpy.asarray(a, dtype = None, order = None)</font>`

<font style="color:rgb(51, 51, 51);">参数说明：</font>

| <font style="color:rgb(255, 255, 255);">参数</font> | <font style="color:rgb(255, 255, 255);">描述</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">a</font> | **<font style="color:#DF2A3F;">任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组</font>** |
| <font style="color:rgb(51, 51, 51);">dtype</font> | <font style="color:rgb(51, 51, 51);">数据类型，可选</font> |
| <font style="color:rgb(51, 51, 51);">order</font> | <font style="color:rgb(51, 51, 51);">可选，有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。</font> |


### <font style="color:rgb(51, 51, 51);">numpy.frombuffer</font>
<font style="color:rgb(51, 51, 51);">numpy.frombuffer 用于实现动态数组。</font>

<font style="color:rgb(51, 51, 51);">numpy.frombuffer 接受 buffer 输入参数，以流的形式读入转化成 ndarray 对象。</font>

`<font style="color:rgb(51, 51, 51);">numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)</font>`

_**<font style="color:rgb(51, 51, 51);">注意：</font>**__<font style="color:rgb(51, 51, 51);background-color:rgb(243, 247, 240);">buffer 是字符串的时候，Python3 默认 str 是 Unicode 类型，所以要转成 bytestring 在原 str 前加上 b。</font>_

<font style="color:rgb(51, 51, 51);">参数说明：</font>

| <font style="color:rgb(255, 255, 255);">参数</font> | <font style="color:rgb(255, 255, 255);">描述</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">buffer</font> | <font style="color:rgb(51, 51, 51);">可以是任意对象，会以流的形式读入。</font> |
| <font style="color:rgb(51, 51, 51);">dtype</font> | <font style="color:rgb(51, 51, 51);">返回数组的数据类型，可选</font> |
| <font style="color:rgb(51, 51, 51);">count</font> | <font style="color:rgb(51, 51, 51);">读取的数据数量，默认为-1，读取所有数据。</font> |
| <font style="color:rgb(51, 51, 51);">offset</font> | <font style="color:rgb(51, 51, 51);">读取的起始位置，默认为0。</font> |


### <font style="color:rgb(51, 51, 51);">numpy.fromiter</font>
<font style="color:rgb(51, 51, 51);">numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，</font>**<font style="color:rgb(51, 51, 51);">返回一维数组</font>**<font style="color:rgb(51, 51, 51);">。</font>

`<font style="color:rgb(51, 51, 51);">numpy.fromiter(iterable, dtype, count=-1)</font>`

| <font style="color:rgb(255, 255, 255);">参数</font> | <font style="color:rgb(255, 255, 255);">描述</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">iterable</font> | <font style="color:rgb(51, 51, 51);">可迭代对象</font> |
| <font style="color:rgb(51, 51, 51);">dtype</font> | <font style="color:rgb(51, 51, 51);">返回数组的数据类型</font> |
| <font style="color:rgb(51, 51, 51);">count</font> | <font style="color:rgb(51, 51, 51);">读取的数据数量，默认为-1，读取所有数据</font> |


## 从数值范围创建数组
### <font style="color:rgb(51, 51, 51);">numpy.arange</font>
<font style="color:rgb(51, 51, 51);">numpy 包中的使用 arange 函数创建数值范围并返回 ndarray 对象，函数格式如下：</font>

numpy.arange(start, stop, step, dtype)

<font style="color:rgb(51, 51, 51);">根据 start 与 stop 指定的范围以及 step 设定的步长，生成一个 ndarray。</font>

<font style="color:rgb(51, 51, 51);">参数说明：</font>

| <font style="color:rgb(255, 255, 255);">参数</font> | <font style="color:rgb(255, 255, 255);">描述</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">start</font> | <font style="color:rgb(51, 51, 51);">起始值，默认为</font><font style="color:rgb(51, 51, 51);">0</font> |
| <font style="color:rgb(51, 51, 51);">stop</font> | <font style="color:rgb(51, 51, 51);">终止值（不包含）</font> |
| <font style="color:rgb(51, 51, 51);">step</font> | <font style="color:rgb(51, 51, 51);">步长，默认为</font><font style="color:rgb(51, 51, 51);">1</font> |
| <font style="color:rgb(51, 51, 51);">dtype</font> | <font style="color:rgb(51, 51, 51);">返回</font><font style="color:rgb(51, 51, 51);">ndarray</font><font style="color:rgb(51, 51, 51);">的数据类型，如果没有提供，则会使用输入数据的类型。</font> |


### <font style="color:rgb(51, 51, 51);">numpy.linspace</font>
<font style="color:rgb(51, 51, 51);">numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下：</font>

`np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)`

<font style="color:rgb(51, 51, 51);">参数说明：</font>

| <font style="color:rgb(255, 255, 255);">参数</font> | <font style="color:rgb(255, 255, 255);">描述</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">start</font> | <font style="color:rgb(51, 51, 51);">序列的起始值</font> |
| <font style="color:rgb(51, 51, 51);">stop</font> | <font style="color:rgb(51, 51, 51);">序列的终止值，如果</font><font style="color:rgb(51, 51, 51);">endpoint</font><font style="color:rgb(51, 51, 51);">为</font><font style="color:rgb(51, 51, 51);">true</font><font style="color:rgb(51, 51, 51);">，该值包含于数列中</font> |
| <font style="color:rgb(51, 51, 51);">num</font> | <font style="color:rgb(51, 51, 51);">要生成的等步长的样本数量，默认为</font><font style="color:rgb(51, 51, 51);">50</font> |
| <font style="color:rgb(51, 51, 51);">endpoint</font> | <font style="color:rgb(51, 51, 51);">该值为</font><font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">true</font><font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">时，数列中包含</font><font style="color:rgb(51, 51, 51);">stop</font><font style="color:rgb(51, 51, 51);">值，反之不包含，默认是True。</font> |
| <font style="color:rgb(51, 51, 51);">retstep</font> | <font style="color:rgb(51, 51, 51);">如果为 True 时，生成的数组中会显示间距，反之不显示。</font> |
| <font style="color:rgb(51, 51, 51);">dtype</font> | <font style="color:rgb(51, 51, 51);">ndarray</font><font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">的数据类型</font> |


### <font style="color:rgb(51, 51, 51);">numpy.logspace</font>
<font style="color:rgb(51, 51, 51);">numpy.logspace 函数用于创建一个于等比数列。格式如下：</font>

`<font style="color:rgb(51, 51, 51);">np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)</font>`

<font style="color:rgb(51, 51, 51);">base 参数意思是取对数的时候 log 的下标。</font>

| <font style="color:rgb(255, 255, 255);">参数</font> | <font style="color:rgb(255, 255, 255);">描述</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">start</font> | <font style="color:rgb(51, 51, 51);">序列的起始值为：base ** start</font> |
| <font style="color:rgb(51, 51, 51);">stop</font> | <font style="color:rgb(51, 51, 51);">序列的终止值为：base ** stop。如果</font><font style="color:rgb(51, 51, 51);">endpoint</font><font style="color:rgb(51, 51, 51);">为</font><font style="color:rgb(51, 51, 51);">true</font><font style="color:rgb(51, 51, 51);">，该值包含于数列中</font> |
| <font style="color:rgb(51, 51, 51);">num</font> | <font style="color:rgb(51, 51, 51);">要生成的等步长的样本数量，默认为</font><font style="color:rgb(51, 51, 51);">50</font> |
| <font style="color:rgb(51, 51, 51);">endpoint</font> | <font style="color:rgb(51, 51, 51);">该值为</font><font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">true</font><font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">时，数列中中包含</font><font style="color:rgb(51, 51, 51);">stop</font><font style="color:rgb(51, 51, 51);">值，反之不包含，默认是True。</font> |
| <font style="color:rgb(51, 51, 51);">base</font> | <font style="color:rgb(51, 51, 51);">对数 log 的底数。</font> |
| <font style="color:rgb(51, 51, 51);">dtype</font> | <font style="color:rgb(51, 51, 51);">ndarray</font><font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">的数据类型</font> |


# Numpy数组的使用
<font style="color:rgb(33, 33, 33);">在NumPy中，三个点和逗号都是用来表示数组展示中的不同维度的符号。</font><u><font style="color:rgb(33, 33, 33);">三个点表示所有未展示的维度</font></u><font style="color:rgb(33, 33, 33);">，</font><u><font style="color:rgb(33, 33, 33);">逗号则用来分隔不同的维度</font></u><font style="color:rgb(33, 33, 33);">。使用三个点和逗号可以更方便地展示高维数组的内容，提高数据处理和分析的效率。</font>

<font style="color:rgb(77, 77, 77);">小结，Numpy数组中，逗号，区分的是维度，冒号：区分的是索引，省略号… 用来代替全索引长度。</font>

## 切片和索引
<font style="color:rgb(51, 51, 51);">ndarray对象的内容可以通过索引或切片来访问和修改，</font>**<font style="color:rgb(51, 51, 51);">与Python中list的切片操作一样</font>**<font style="color:rgb(51, 51, 51);">。</font>

<font style="color:rgb(51, 51, 51);">ndarray 数组可以基于0-n的下标进行索引，切片对象可以通过内置的 slice 函数，并设置 start, stop 及 step 参数进行，从原数组中切割出一个新数组。</font>

```python
a = np.arrange(10)
s = slice(2,7,2)   # 从索引 2 开始到索引 7 停止，间隔为2
print(a[s])
```

<font style="color:rgb(51, 51, 51);">我们也可以通过</font>**<font style="color:rgb(51, 51, 51);">冒号分隔切片参数</font>**<font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">start:stop:step</font>**<font style="color:rgb(51, 51, 51);"> 来进行切片操作：</font>

```python
a = np.arrange(10)  
b = a[2:7:2]   # 从索引 2 开始到索引 7 停止，间隔为 2
print(b)
```

<font style="color:rgb(51, 51, 51);">冒号 </font>**<font style="color:rgb(51, 51, 51);background-color:rgb(236, 234, 230);">:</font>**<font style="color:rgb(51, 51, 51);"> 的解释：如果只放置一个参数，如 </font>**<font style="color:rgb(51, 51, 51);">[2]</font>**<font style="color:rgb(51, 51, 51);">，将返回与该索引相对应的单个元素。如果为 </font>**<font style="color:rgb(51, 51, 51);">[2:]</font>**<font style="color:rgb(51, 51, 51);">，表示从该索引开始以后的所有项都将被提取。如果使用了两个参数，如 </font>**<font style="color:rgb(51, 51, 51);">[2:7]</font>**<font style="color:rgb(51, 51, 51);">，那么则提取两个索引(不包括停止索引)之间的项。</font>

<font style="color:rgb(51, 51, 51);">切片还可以包括省略号 </font>**<font style="color:rgb(51, 51, 51);background-color:rgb(236, 234, 230);">…</font>**<font style="color:rgb(51, 51, 51);">，来使选择</font>**<font style="color:rgb(51, 51, 51);">元组的长度与数组的维度相同</font>**<font style="color:rgb(51, 51, 51);">。 如果在行位置使用省略号，它将返回包含行中元素的 ndarray。</font>

```python
a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print (a[...,1])   # 第2列元素
print (a[1,...])   # 第2行元素
print (a[...,1:])  # 第2列及剩下的所有元素
```

```python
[2 4 5]
[3 4 5]
[[2 3]
 [4 5]
 [5 6]]
```

## 切片和索引之冒号、逗号与省略号使用详解
### 冒号使用详解
<font style="color:rgb(18, 18, 18);">seq[start:end:step] # 从start开始到end结束，每隔step输出一次</font>

<font style="color:rgb(18, 18, 18);">::将start和end省略意味着从开始到结束，省略谁就是采用默认。</font>

```python
a = [1,2,3,4,5,6]
a[::2]              ->1,3,5  #从1开始，每隔2-1个输出一下
a[::3]              ->1,4    #从1开始，每隔3-1个输出一下
a[2::3]             ->3,6    #从2开始，每隔2个输出一次，由于end缺省，默认到最后
a[:4:2]             ->1,3    #从最前开始，每隔1个输出一次，到4就结束了
a[:4]               ->1,2,3,4  #前四个，这就回到了单冒号，因为第一个位置缺省，所以从一开始进行切片
a[4:]               ->5,6    #结束的位置是缺省的，所以就选择从4到最后了
```

<font style="color:rgb(18, 18, 18);">现有列表：[0,1,2,3,4,5,6,7,8,9,10]</font>

| **<font style="color:rgb(18, 18, 18);">列表元素</font>** | **<font style="color:rgb(18, 18, 18);">0</font>** | **<font style="color:rgb(18, 18, 18);">1</font>** | **<font style="color:rgb(18, 18, 18);">2</font>** | **<font style="color:rgb(18, 18, 18);">3</font>** | **<font style="color:rgb(18, 18, 18);">4</font>** | **<font style="color:rgb(18, 18, 18);">5</font>** | **<font style="color:rgb(18, 18, 18);">6</font>** | **<font style="color:rgb(18, 18, 18);">7</font>** | **<font style="color:rgb(18, 18, 18);">8</font>** | **<font style="color:rgb(18, 18, 18);">9</font>** | **<font style="color:rgb(18, 18, 18);">10</font>** |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| <font style="color:rgb(18, 18, 18);">正向索引</font> | <font style="color:rgb(18, 18, 18);">0</font> | <font style="color:rgb(18, 18, 18);">1</font> | <font style="color:rgb(18, 18, 18);">2</font> | <font style="color:rgb(18, 18, 18);">3</font> | <font style="color:rgb(18, 18, 18);">4</font> | <font style="color:rgb(18, 18, 18);">5</font> | <font style="color:rgb(18, 18, 18);">6</font> | <font style="color:rgb(18, 18, 18);">7</font> | <font style="color:rgb(18, 18, 18);">8</font> | <font style="color:rgb(18, 18, 18);">9</font> | <font style="color:rgb(18, 18, 18);">10</font> |
| <font style="color:rgb(18, 18, 18);">逆向索引</font> | <font style="color:rgb(18, 18, 18);">-11</font> | <font style="color:rgb(18, 18, 18);">-10</font> | <font style="color:rgb(18, 18, 18);">-9</font> | <font style="color:rgb(18, 18, 18);">-8</font> | <font style="color:rgb(18, 18, 18);">-7</font> | <font style="color:rgb(18, 18, 18);">-6</font> | <font style="color:rgb(18, 18, 18);">-5</font> | <font style="color:rgb(18, 18, 18);">-4</font> | <font style="color:rgb(18, 18, 18);">-3</font> | <font style="color:rgb(18, 18, 18);">-2</font> | <font style="color:rgb(18, 18, 18);">-1</font> |


<font style="color:rgb(100, 100, 100);">注意：上面逆向索引的初始索引，从 -1 开始</font><font style="color:rgb(18, 18, 18);"></font>

### 逗号的使用详解
逗号分隔的是数组的纬度。

<font style="color:rgb(18, 18, 18);">X[:,0]就是取矩阵X的所有行的第0列的元素，X[:,1] 就是取所有行的第1列的元素。</font>

<font style="color:rgb(18, 18, 18);">X[:, m:n]即取矩阵X的所有行中的的第m到n-1列数据，含左不含右。</font>

```plain
a = np.arange(25).reshape(5,5)
print(a)
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
print(a[:,0])
[ 0  5 10 15 20]
print(a[:,1])
[ 1  6 11 16 21]
print(a[:, 1:3])
[[ 1  2]
 [ 6  7]
 [11 12]
 [16 17]
 [21 22]]
```

### <font style="color:rgb(18, 18, 18);">省略号使用详解</font>
<font style="color:rgb(77, 77, 77);">省略前面所有的 ‘：‘索引操作</font>

```sql
(...,None)=(:,:,None)
```

```sql
a= np.array([1,2,3,4,5,6])
a[...] = array([1, 2, 3, 4, 5, 6])

a[...,1] = 2
a[...,4] = 5
a[1,...] = 2

a = np.array([[1,2,3],[4,5,6]])

a[:,1] = [2,5]
a[...,1] = [2,5]  #以上二者是等同的
```

## 高级索引
Numpy 除了和Python一样的索引方式外还可以使用**<font style="color:#DF2A3F;background-color:#FBDE28;">整数数组索引、布尔索引以及花式索引</font>**。<font style="color:rgb(51, 51, 51);">NumPy 中的高级索引指的是使用整数数组、布尔数组或者其他序列来访问数组的元素。相比于基本索引，</font><u><font style="color:rgb(51, 51, 51);">高级索引可以访问到数组中的任意元素，并且可以用来对数组进行复杂的操作和修改。</font></u>

### <font style="color:rgb(51, 51, 51);">整数数组索引</font>
<font style="color:rgb(77, 77, 77);">Numpy数组的整数数组索引，返回数据副本，而不是创建视图。相比切片索引，整数数组的索引更具有通用性，因为其不要求索引值具有特定规律。</font>

<font style="color:rgb(77, 77, 77);">整数数组索引要点如下：</font>

+ <font style="color:rgb(77, 77, 77);">对于索引数组中</font><u><font style="color:rgb(77, 77, 77);">未建立索引的维度</font></u><font style="color:rgb(77, 77, 77);">（索引数组中的索引集数目小于被索引数组维度），默认被全部索引；</font>
+ <font style="color:rgb(77, 77, 77);">索引结果数组的形状由索引数组的形状与被索引数组中所有未索引的维的形状串联组成，也就是说，若对数组的所有维度建立索引，则</font><font style="color:#DF2A3F;">索引数组的形状等于结果数组的形状</font><font style="color:rgb(77, 77, 77);">；</font>
+ <font style="color:rgb(77, 77, 77);">若索引数组具有匹配的形状，即索引数组个数（索引集数）等于被索引数组的维度，此时结果数组与索引数组具有相同形状，且这些结果值对应于各维索引集的索引在索引数组中的位置；</font>

---

<font style="color:rgb(51, 51, 51);">整数数组索引是指使用一个数组来访问另一个数组的元素。这个数组中的每个元素都是目标数组中某个维度上的索引值。以下实例获取数组中 </font>**<font style="color:rgb(51, 51, 51);">(0,0)，(1,1)</font>**<font style="color:rgb(51, 51, 51);"> 和 </font>**<font style="color:rgb(51, 51, 51);">(2,0)</font>**<font style="color:rgb(51, 51, 51);"> 位置处的元素。</font>

```python
x = np.array([[1,  2],  [3,  4],  [5,  6]]) 
y = x[[0,1,2],  [0,1,0]]
print(y)
[1  4  5]
```

<font style="color:rgb(51, 51, 51);">以下实例获取了 4X3 数组中的四个角的元素。 行索引是 [0,0] 和 [3,3]，而列索引是 [0,2] 和 [0,2]。</font>

```python
x = np.array([[  0,  1,  2],
              [  3,  4,  5],
              [  6,  7,  8],
              [  9,  10,  11]])  
print ('我们的数组是：' )
print (x)
print ('\n')
rows = np.array([[0,0],[3,3]]) 
cols = np.array([[0,2],[0,2]]) 
y = x[rows,cols]  
print  ('这个数组的四个角元素是：')
print (y)

我们的数组是：
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]

这个数组的四个角元素是：
[[ 0  2]
 [ 9 11]]
```

<font style="color:rgb(51, 51, 51);">返回的结果是包含每个角元素的 ndarray 对象。</font>

<font style="color:rgb(51, 51, 51);">可以借助切片 </font>**<font style="color:rgb(51, 51, 51);background-color:rgb(236, 234, 230);">:</font>**<font style="color:rgb(51, 51, 51);"> 或 </font>**<font style="color:rgb(51, 51, 51);background-color:rgb(236, 234, 230);">…</font>**<font style="color:rgb(51, 51, 51);"> 与索引数组组合。</font>

```python
a = np.array([[1,2,3], 
              [4,5,6],
              [7,8,9]])
b = a[1:3, 1:3]
c = a[1:3,[1,2]]
d = a[...,1:]
print(b)
print(c)
print(d)

[[5 6]
 [8 9]]
[[5 6]
 [8 9]]
[[2 3]
 [5 6]
 [8 9]]
```



### <font style="color:rgb(51, 51, 51);">布尔索引</font>
<font style="color:rgb(51, 51, 51);">布尔索引通过布尔运算（如：比较运算符）来</font>**<font style="color:rgb(51, 51, 51);">获取符合指定条件的元素的数组</font>**<font style="color:rgb(51, 51, 51);">。</font>

<font style="color:rgb(51, 51, 51);">以下实例获取大于 5 的元素：</font>

```python
x = np.array([[  0,  1,  2],
              [  3,  4,  5],
              [  6,  7,  8],
              [  9,  10,  11]])  
print ('我们的数组是：')
print (x)
print ('\n')
# 现在我们会打印出大于 5 的元素  
print  ('大于 5 的元素是：')
print (x[x >  5])

我们的数组是：
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]

大于 5 的元素是：
[ 6  7  8  9 10 11]
```

<font style="color:rgb(51, 51, 51);">以下实例使用了 </font>**<font style="color:rgb(51, 51, 51);background-color:rgb(236, 234, 230);">~</font>**<font style="color:rgb(51, 51, 51);">（取补运算符）来过滤 NaN。</font>

```python
a = np.array([np.nan,  1,2,np.nan,3,4,5])  
print(a[~np.isnan(a)])

[ 1.   2.   3.   4.   5.]
```

<font style="color:rgb(51, 51, 51);">以下实例演示如何从数组中过滤掉非复数元素。</font>

```python
a = np.array([1,  2+6j,  5,  3.5+5j])  
print (a[np.iscomplex(a)])

[2.0+6.j  3.5+5.j]
```

### 花式索引
<font style="color:rgb(51, 51, 51);">花式索引指的是利用整数数组进行索引。</font>**<font style="color:rgb(51, 51, 51);">花式索引根据索引数组的值作为目标数组的某个轴的下标来取值。</font>**<font style="color:rgb(51, 51, 51);">对于使用一维整型数组作为索引，如果目标是一维数组，那么索引的结果就是对应位置的元素，如果目标是二维数组，那么就是对应下标的行。花式索引跟切片不一样，它总是</font><u><font style="color:rgb(51, 51, 51);">将数据复制到新数组中</font></u><font style="color:rgb(51, 51, 51);">。</font>

#### <font style="color:rgb(51, 51, 51);">一维数组</font>
<font style="color:rgb(51, 51, 51);">一维数组只有一个轴 </font>**<font style="color:rgb(51, 51, 51);">axis = 0</font>**<font style="color:rgb(51, 51, 51);">，所以一维数组就在 </font>**<font style="color:rgb(51, 51, 51);">axis = 0</font>**<font style="color:rgb(51, 51, 51);"> 这个轴上取值：</font>

```python
x = np.arange(9)
print(x)
# 一维数组读取指定下标对应的元素
print("-------读取下标对应的元素-------")
x2 = x[[0, 6]] # 使用花式索引
print(x2)

print(x2[0])
print(x2[1])

[0 1 2 3 4 5 6 7 8]
-------读取下标对应的元素-------
[0 6]
0
6
```

#### 二维数组
1. <font style="color:rgb(51, 51, 51);">传入顺序索引数组</font>

```python
x=np.arange(32).reshape((8,4))
print(x)
# 二维数组读取指定下标对应的行
print("-------读取下标对应的行-------")
print (x[[4,2,1,7]])
```

**<font style="color:rgb(51, 51, 51);background-color:rgb(236, 234, 230);">print (x[[4,2,1,7]])</font>**<font style="color:rgb(51, 51, 51);"> 输出下表为 </font>**<font style="color:rgb(51, 51, 51);">4, 2, 1, 7</font>**<font style="color:rgb(51, 51, 51);"> 对应的行，输出结果为：</font>

```python
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]
 [24 25 26 27]
 [28 29 30 31]]
-------读取下标对应的行-------
[[16 17 18 19]
 [ 8  9 10 11]
 [ 4  5  6  7]
 [28 29 30 31]]
```

2. <font style="color:rgb(51, 51, 51);">传入倒序索引数组</font>

```python
x=np.arange(32).reshape((8,4))
print (x[[-4,-2,-1,-7]])

[[16 17 18 19]
 [24 25 26 27]
 [28 29 30 31]
 [ 4  5  6  7]]
```

3. <font style="color:rgb(51, 51, 51);">传入多个索引数组（要使用 np.ix_）</font>

<font style="color:rgb(51, 51, 51);">np.ix_ 函数就是输入两个数组，产生笛卡尔积的映射关系。笛卡尔乘积是指在数学中，两个集合 X 和 Y 的笛卡尔积（Cartesian product），又称直积，表示为 </font>**<font style="color:rgb(51, 51, 51);">X×Y</font>**<font style="color:rgb(51, 51, 51);">，第一个对象是X的成员而第二个对象是 Y 的所有可能有序对的其中一个成员。</font>

<font style="color:rgb(51, 51, 51);">例如</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">A={a,b}, B={0,1,2}</font>**<font style="color:rgb(51, 51, 51);">，则：</font>

```python
A×B={(a, 0), (a, 1), (a, 2), (b, 0), (b, 1), (b, 2)}
B×A={(0, a), (0, b), (1, a), (1, b), (2, a), (2, b)}
```

<font style="color:rgb(51, 51, 51);"></font>

```python
x=np.arange(32).reshape((8,4))
print (x[np.ix_([1,5,7,2],[0,3,1,2])])
```

```python
[[ 4  7  5  6]
 [20 23 21 22]
 [28 31 29 30]
 [ 8 11  9 10]]
```



# Numpy数组操作
## 广播Broadcast
<font style="color:rgb(51, 51, 51);">广播(Broadcast)是 numpy 对不同形状(shape)的数组进行数值计算的方式， 对数组的算术运算通常在相应的元素上进行。如果两个数组 a 和 b 形状相同，即满足 </font>**<font style="color:rgb(51, 51, 51);">a.shape == b.shape</font>**<font style="color:rgb(51, 51, 51);">，那么 a*b 的结果就是 a 与 b 数组对应位相乘。这要求维数相同，且各维度的长度相同。</font>

```python
a = np.array([1,2,3,4]) 
b = np.array([10,20,30,40]) 
c = a * b 
print (c)

[ 10  40  90 160]
```



<font style="color:rgb(51, 51, 51);">当运算中的 2 个数组的形状不同时，numpy 将自动触发广播机制。如：</font>

```python
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([0,1,2])
print(a + b)

[[ 0  1  2]
 [10 11 12]
 [20 21 22]
 [30 31 32]]
```

<font style="color:rgb(51, 51, 51);">下面的图片展示了数组 b 如何通过广播来与数组 a 兼容。</font>

![](https://cdn.nlark.com/yuque/0/2023/png/29307286/1694428291736-b0302cd1-fba2-430b-b992-fb432cb93dbd.png)

<font style="color:rgb(51, 51, 51);">4x3 的二维数组与长为 3 的一维数组相加，等效于把数组 b 在二维上重复 4 次再运算：</font>

```python
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
bb = np.tile(b, (4, 1))  # 重复 b 的各个维度
print(a + bb)

[[ 1  2  3]
 [11 12 13]
 [21 22 23]
 [31 32 33]]
```



**<font style="color:rgb(51, 51, 51);">广播的规则:</font>**

+ <font style="color:rgb(51, 51, 51);">让所有输入数组都</font>**<font style="color:rgb(51, 51, 51);">向其中形状最长的数组看齐</font>**<font style="color:rgb(51, 51, 51);">，形状中不足的部分都通过在前面加 1 补齐。</font>
+ <font style="color:rgb(51, 51, 51);">输出数组的形状是输入数组形状的</font>**<font style="color:rgb(51, 51, 51);">各个维度上的最大值</font>**<font style="color:rgb(51, 51, 51);">。</font>
+ <font style="color:rgb(51, 51, 51);">如果输入数组的某个维度和输出数组的对应维度的</font>**<font style="color:rgb(51, 51, 51);">长度相同或者其长度为 1 </font>**<font style="color:rgb(51, 51, 51);">时，这个数组能够用来计算，否则出错。</font>
+ <font style="color:rgb(51, 51, 51);">当输入数组的</font>**<font style="color:rgb(51, 51, 51);">某个维度的长度为 1 时，沿着此维度运算时都用此维度上的第一组值</font>**<font style="color:rgb(51, 51, 51);">。</font>

**<font style="color:rgb(51, 51, 51);">简单理解：</font>**<font style="color:rgb(51, 51, 51);">对两个数组，分别比较他们的每一个维度（若其中一个数组没有当前维度则忽略），满足：</font>

+ <font style="color:rgb(51, 51, 51);">数组拥有相同形状。</font>
+ <font style="color:rgb(51, 51, 51);">当前维度的值相等。</font>
+ <font style="color:rgb(51, 51, 51);">当前维度的值有一个是 1。</font>

<font style="color:rgb(51, 51, 51);">若条件不满足，抛出 </font>**<font style="color:rgb(51, 51, 51);">"ValueError: frames are not aligned"</font>**<font style="color:rgb(51, 51, 51);"> 异常。</font>

## 迭代数组
<font style="color:rgb(51, 51, 51);">NumPy 迭代器对象 numpy.nditer 提供了一种灵活访问一个或者多个数组元素的方式。</font>

<font style="color:rgb(51, 51, 51);">迭代器最基本的任务的可以完成对数组元素的访问。</font>

<font style="color:rgb(51, 51, 51);">接下来我们使用 arange() 函数创建一个 2X3 数组，并使用 nditer 对它进行迭代。</font>

```python
实例
```

```python
a = np.arange(6).reshape(2,3)
print('原始数组是：')
print(a)
print('\n')
print('迭代输出元素：')
for x in np.nditer(a): 
    print(x, end=", ")
    print('\n')
```

<font style="color:rgb(51, 51, 51);">输出结果为：</font>

```python
原始数组是： [[0 1 2] 
			[3 4 5]] 

迭代输出元素： 0, 1, 2, 3, 4, 5, 
```

<font style="color:rgb(51, 51, 51);">以上实例不是使用标准 C 或者 Fortran 顺序，选择的顺序是和数组内存布局一致的，这样做是为了提升访问的效率，默认是行序优先（row-major order，或者说是 C-order）。</font>

<font style="color:rgb(51, 51, 51);">这反映了默认情况下只需访问每个元素，而无需考虑其特定顺序。我们可以通过迭代上述数组的转置来看到这一点，并与以 C 顺序访问数组转置的 copy 方式做对比，如下实例：</font>

```python
a = np.arange(6).reshape(2,3)
for x in np.nditer(a.T):
    print (x, end=", " )
print ('\n')
 
for x in np.nditer(a.T.copy(order='C')):
    print (x, end=", " )
print ('\n')
```

<font style="color:rgb(51, 51, 51);">输出结果为：</font>

```python
0, 1, 2, 3, 4, 5,  

0, 3, 1, 4, 2, 5, 
```

<font style="color:rgb(51, 51, 51);">从上述例子可以看出，a 和 a.T 的遍历顺序是一样的，也就是他们在内存中的存储顺序也是一样的，但是 </font>**<font style="color:rgb(51, 51, 51);background-color:rgb(236, 234, 230);">a.T.copy(order = 'C')</font>**<font style="color:rgb(51, 51, 51);"> 的遍历结果是不同的，那是因为它和前两种的存储方式是不一样的，默认是按行访问。</font>





## 数组操作
## 位运算
# Numpy中的函数
## 字符串函数
## 数学函数
## 算术函数
## 统计函数
## 排序、条件筛选函数
## 字节交换函数
## 副本和视图函数


# Numpy中的库  

## Matrix
## 线性代数
## IO库


<font style="color:rgb(51, 51, 51);">  
</font>

