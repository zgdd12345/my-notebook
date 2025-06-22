# 1.  基本概念
1. Line：是Backtrader系统中最重要的对象。Line本意是一连串的可以连接在一起的点，所有可以在坐标上形成一条线的数据就称为Line。 在量化投资领域，通常是指open、high、low、close、volume。除了数据本身可以形成Line之外，对数据进行处理后形成的数据也可以作为Line，比如计算close列的移动平均线，也可以形成一个Line。
2. Index 为0的理解：
	Backtrader系统中，对Line数据是逐行处理的：
 ![[line.png]]

	系统处理顺序从上至下，当处理到26.5的时候，对应的Index为0.如果要访问之前的数据，就是-1，-2.之后的数据，就是1,2.

	特别值得注意的是-1在python中用于访问一个列表的最后一个数据，而在backtrader中，-1指的是最后已经处理过得数据，在当前处理数据之前 ，值会随着系统的处理而不断变化。

3. Bar：
这种方法的好处就是无需知道已经处理了多少行（在Backtrader中，统一将行称之为Bar），也无需知道还有多少Bar需要处理，因为0唯一确定了系统正在处理的数据（Bar）。

在backtrader中，重写了len函数，返回的是已经处理过数据行（也就是Bar）。

# 2. 一些重要概念
## 2.1 数据源（data feed）
### 2.1.1数据源的传递
- 数据源是以***数组***的形式或者***对数组的快捷访问***的方式提供给strategy（策略）作为**成员变量**使用。
 - strategy这个类里面有个成员变量datas是个数组，用于存储数据源。数据源按照加入的先后顺序保存在datas中。策略在执行过程，会使用这些数据。 
- 访问数据源可以通过访问数组的方式，或者对数组的快捷方式访问。
- datas[0].close就是数组访问方式，self.data0.close就是快捷访问方式，两者保存的数据完全一样
strategy的__init__没有输入参数（除了self自身），我们的数组只是加入到cerebro中，它怎么就能直接使用datas数组了呢？这个是backtrader自身框架处理的，也就是，==系统加入的数据源会按照加入的顺序自动呈现到strategy内部的data变量上==，大家只需要知道如何使用即可。注意，与此类似的还要Indicators。

**数据源的快捷访问：**
上一节已经说明，这里总结下，对==数据源的快捷访问方式==如下：
* self.data 等价self.datas[0]
* self.dataX 等价 self.datas[X]
示例如下：
```
class MyStrategy(bt.Strategy):
    params = dict(period=20)
    def __init__(self):
        sma = btind.SimpleMovingAverage(self.data, period=self.params.period)
```
==数据源的缺省访问==
如果只有一个数据源，你甚至都不用显式指定，系统会缺省使用self.datas[0]，也就是第一个加入的数据源，示例：
```
class MyStrategy(bt.Strategy):
    params = dict(period=20)
    def __init__(self):
        sma = btind.SimpleMovingAverage(period=self.params.period)
```
调用SimpleMovingAverage的时候完全就丢掉self.data了。这种情况下， **Indicator（本例中就是SimpleMovingAverage）会使用策略创建时输入的第一个数据，就是self.data (或者self.data0 或者self.datas[0]，哥仨是一个意思])**

#### 2.1.2万物皆为数据源
在backtrader中，不仅仅输入的数据是数据源，==任何indicator（指标）以及任何对输入数据的操作（加，减，比较，求和，求平均... ）结果均可称为数据源。==上一个例子中SimpleMovingAverage对self.datas[0]进行求平均，其结果sma就是一个新的数据源。如下例子，展示了作为数据源的指标以及操作结果
``` python
class MyStrategy(bt.Strategy):
    params = dict(period1=20, period2=25, period3=10, period4)
    def __init__(self):
 
        sma1 = btind.SimpleMovingAverage(self.datas[0], period=self.p.period1)
        # sma2是对sma1进行移动平均的结果。
        sma2 = btind.SimpleMovingAverage(sma1, period=self.p.period2)
        # 对数据源进行算数加减的结果
        something = sma2 - sma1 + self.data.close
        # 对算数结果再进行移动平均的结果
        sma3 = btind.SimpleMovingAverage(something, period=self.p.period3)
        # 比较操作也可以
        greater = sma3 > sma1
        # 对True/False值进行移动平均操作，虽然没啥意义，但是也有效。
        sma3 = btind.SimpleMovingAverage(greater, period=self.p.period4)
```
所有的通过对数据源进行的各种操作，其结果也会生成一个数据源的对象。

## 2.2 参数
在backtrader中，所有的类都按照如下方法来使用参数：
1、声明一个带有缺省值的参数作为类的一个属性（元组或者字典结构）。
2、关键字类型参数（`**kwargs`）会扫描匹配的参数，将值赋值给对应的参数，完成后从 `**kwargs`删除。
3、这些参数都可以在类实例中通过访问成员变量`self.params`（也可以简写为`self.p`）来使用。
之前的实例中我们已经提供了参数的使用方法，下面看看使用元组（包含元组）以及字典方式的不同之处。

使用元组实例：
``` python
class MyStrategy(bt.Strategy):
    params = (('period', 20),)
    def __init__(self):
        sma = btind.SimpleMovingAverage(self.data, period=self.p.period)
```
使用字典的实例：
``` python
class MyStrategy(bt.Strategy):
    params = dict(period=20)
    def __init__(self):
        sma = btind.SimpleMovingAverage(self.data, period=self.p.period)
```

## 2.3 Lines
Lines是一个非常重要的概念，在上一篇文章中做了详细的说明，从使用用户（通常是strategy）的角度来说，就是包括一个或多个line，这些line是一系列的数据，在图中可以形成一条线（line），例如使用股票的收盘价就可以形成一条线，这个大家在股票软件上就可以看到。

```
class MyStrategy(bt.Strategy):
    params = dict(period=20)
    def __init__(self):
        self.movav = btind.SimpleMovingAverage(self.data, period=self.p.period)
    def next(self):
        if self.movav.lines.sma[0] > self.data.lines.close[0]:
```
本例中，使用了两个Lines对象：
* self.data: 这个本身包含一个lines属性，该lines还包含一个close属性。这句话啥意思了？就是说，self.data本身包含多条line，其中一个line就是close（收盘价）。参见前一篇文章中的示例图。
* self.movav:这个是一个SimpleMovingAverage的指标（indicator），本身就包含一个具有lines属性的sma。这里特殊注意一下，计算SimpleMovingAverage使用的self.data，没有指定具体Line的话,缺省用的是close价进行计算。

这两个line，也就是close和sma，可以通过索引0来访问并比对，索引为0的含义前面讲过，就是系统当前正在处理的数据行（bar）。

还有简单的方法访问lines：

    xxx.lines 可以简化为 xxx.l

   xxx.lines.name可以简化为xxx.lines_name

  一些复杂的对象也可以通过如下方法访问：

    self.data_name 等于 self.data.lines.name

    如果有多个变量的话，也可以self.data1_name 替代self.data1.lines.name

此外，Line的名字也可以通过如下方式访问：

`self.data.close and self.movav.sma`

### 2.3.1 Lines的声明

如果开发一个indicator（指标），那么指标拥有的**所有的Line必须声明**。
	声明的方式：
	在类中增加一个lines的**类属性**，和参数不同的是，这里只能使用**元组**。
	没有使用字典的原因是字典无法存储按顺序插入的对象。元组是按顺序存储的。
示例如下：
```
class SimpleMovingAverage(Indicator):
    lines = ('sma',)[^1]
```
[^1]: 对于元组，如果只是输入一个字符串，那么后面的逗号必不可少，否则的话，字符串的每一个字母都会作为一个元素加入到元组中。

**多样的访问方式：**
1. 使用数字的方式
	self.lines[0] 指向 self.lines.sma
2. 可以通过1,2等数字作为索引来访问：
	- self.line等价 self.lines[0]
	- self.lineX 等价 self.lines[X]
	- self.line_X 等价 self.lines[X]
3. 对象如果接收了多个数据源，也可以通过如下数值索引方式访问：
	* self.dataY 等价 self.data.lines[Y]
	* self.dataX_Y 等价 self.dataX.lines[X] 也就等价 self.datas[X].lines[Y]

### 2.3.2 Line的长度
在Backtrader中提供了两个函数来度量长度：
- len：返回当前系统已经处理的数据（bars）。这个和python标准的len定义差异。
- lenbuf：返回本数据源预先加载的数据（bars）个数。

只有在如下情况下，这两个值相等：
- 数据源没有预先加载任何数据。
- 数据源所有数据已经处理完毕。

### 2.3.3 索引0和-1
Lines有一系列的Line组成（不然为啥Lines要用复数啊），Line则是由一组可以形成划线的数据点组成（比如一段时间的开盘价（close））。

和python不一样的是，0指的是系统当前正在处理的数据，而不是第一个数据。

strategy类只会进行取值操作，而indicator只会进行赋值操作。
```
def next(self):
    if self.movav.lines.sma[0] > self.data.lines.close[0]:
        print('Simple Moving Average is greater than the closing price')
```
这一段代码的逻辑就是：strategy通过索引0获取移动平均值和close价格的当前值并进行比较。
如果是索引0的话，系统可以按照如下的简单方法直接比对：
```
if self.movav.lines.sma > self.data.lines.close:
    ...
```
如下代码演示了如何通过获取当前值计算一个简单的移动平均指标：
```
def next(self):
  self.line[0] = math.fsum(self.data.get(0, size=self.p.period)) / self.p.period
```

而在backtrader中，-1指的是当前处理数据（索引为0）的上一个数据。

比如我们在strategy中比对当前一个close和上一个close，代码如下：
```
def next(self):
    if self.data.close[0] > self.data.close[-1]:
        print('今天的收盘价比昨天高！')
```
逻辑上，以当前值0为基准，上一个值索引-1，上上一个值为-2，还可以继续-3，-4...

### 2.3.4 Line的切片
与python不同，在backtrader中，不支持对lines的数据进行切片操作，
获取部分数据（切片）该怎么办呢？使用如下代码：
```
myslice = self.my_sma.get(ago=0, size=1)  #这个函数的缺省值为（0,1）
```
==含义就是以当前值（索引为0），向前返回1个数==，这个代码会返回当前值（和索引为0含义一样）如果，size为2，那么返回索引为0，-1的两个值。具体含义就是以索引为ago，向前返回size个值（包含ago索引对应的值）。
==返回的值是有顺序的==，最左的值对应离ago最远的值，最右的是ago索引对应的值。例如如下是返回最新的10个值（不包括正在处理的值）：
```
myslice = self.my_sma.get(ago=-1, size=10)
```


### 2.3.5 延迟索引

### 2.3.6Lines的耦合

### 2.3.7 操作符


# 3. 平台的使用
## 3.1 Line迭代器
## 3.2 Indicators的额外方法
## 3.3 最小周期（Minimum Period）
## 3.4 启动和运行
## 3.5 数据源（data Feed）
## 3.6 继承的strategy类
## 3.7 Cereebro

## 