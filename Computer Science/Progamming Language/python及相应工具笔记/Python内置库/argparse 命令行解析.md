[链接](https://docs.python.org/zh-cn/3/library/argparse.html#module-argparse)

<font style="color:rgb(0, 0, 0);">命令行选项、参数和子命令解析器</font>

[<font style="color:rgb(0, 0, 0);">argparse</font>](https://docs.python.org/zh-cn/3/library/argparse.html#module-argparse)<font style="color:rgb(0, 0, 0);"> 模块对命令行接口的支持是围绕 </font>[<font style="color:rgb(0, 0, 0);">argparse.ArgumentParser</font>](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser)<font style="color:rgb(0, 0, 0);"> 的实例建立的。 它是一个用于参数规格说明的容器并包含多个全面应用解析器的选项:</font>

```plain
parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

```

[ArgumentParser.add_argument()](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser.add_argument)<font style="color:rgb(0, 0, 0);"> </font><font style="color:rgb(0, 0, 0);">方法将单个参数规格说明关联到解析器。 它支持位置参数，接受各种值的选项，以及各种启用/禁用旗标:</font>

```plain
parser.add_argument('filename')           # positional argument 
parser.add_argument('-c', '--count')      # option that takes a value 
parser.add_argument('-v', '--verbose',  action='store_true')  # on/off flag 
```

[ArgumentParser.parse_args()](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser.parse_args)<font style="color:rgb(0, 0, 0);"> </font><font style="color:rgb(0, 0, 0);">方法运行解析器并将提取的数据放入</font><font style="color:rgb(0, 0, 0);"> </font>[argparse.Namespace](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.Namespace)<font style="color:rgb(0, 0, 0);"> </font><font style="color:rgb(0, 0, 0);">对象:</font>

```plain
args = parser.parse_args() 
print(args.filename, args.count, args.verbose)
```

| <font style="color:rgb(0, 0, 0);">名称</font> | <font style="color:rgb(0, 0, 0);">描述</font> | <font style="color:rgb(0, 0, 0);">值</font> |
| :--- | :--- | :--- |
| [action](https://docs.python.org/zh-cn/3/library/argparse.html#action) | 指明应当如何处理一个参数 | <font style="background-color:rgb(236, 240, 243);">'store'</font>, <font style="background-color:rgb(236, 240, 243);">'store_const'</font>, <font style="background-color:rgb(236, 240, 243);">'store_true'</font>, <font style="background-color:rgb(236, 240, 243);">'append'</font>, <font style="background-color:rgb(236, 240, 243);">'append_const'</font>, <font style="background-color:rgb(236, 240, 243);">'count'</font>, <font style="background-color:rgb(236, 240, 243);">'help'</font>, <font style="background-color:rgb(236, 240, 243);">'version'</font> |
| [choices](https://docs.python.org/zh-cn/3/library/argparse.html#choices) | 将值限制为指定的可选项集合 | <font style="background-color:rgb(236, 240, 243);">['foo',</font><font style="background-color:rgb(236, 240, 243);"> </font><font style="background-color:rgb(236, 240, 243);">'bar']</font>, <font style="background-color:rgb(236, 240, 243);">range(1,</font><font style="background-color:rgb(236, 240, 243);"> </font><font style="background-color:rgb(236, 240, 243);">10)</font> 或 [Container](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Container) 实例 |
| [const](https://docs.python.org/zh-cn/3/library/argparse.html#const) | 存储一个常量值 | |
| [default](https://docs.python.org/zh-cn/3/library/argparse.html#default) | 当未提供某个参数时要使用的默认值 | 默认为 <font style="background-color:rgb(236, 240, 243);">None</font> |
| [dest](https://docs.python.org/zh-cn/3/library/argparse.html#dest) | 指定要在结果命名空间中使用的属性名称 | |
| [help](https://docs.python.org/zh-cn/3/library/argparse.html#help) | 某个参数的帮助消息 | |
| [metavar](https://docs.python.org/zh-cn/3/library/argparse.html#metavar) | 要在帮助中显示的参数替代显示名称 | |
| [nargs](https://docs.python.org/zh-cn/3/library/argparse.html#nargs) | 参数可被使用的次数 | [int](https://docs.python.org/zh-cn/3/library/functions.html#int), <font style="background-color:rgb(236, 240, 243);">'?'</font>, <font style="background-color:rgb(236, 240, 243);">'*'</font> 或 <font style="background-color:rgb(236, 240, 243);">'+'</font> |
| [required](https://docs.python.org/zh-cn/3/library/argparse.html#required) | 指明某个参数是必需的还是可选的 | <font style="background-color:rgb(236, 240, 243);">True</font> 或 <font style="background-color:rgb(236, 240, 243);">False</font> |
| [type](https://docs.python.org/zh-cn/3/library/argparse.html#argparse-type) | 自动将参数转换为给定的类型 | [int](https://docs.python.org/zh-cn/3/library/functions.html#int), [float](https://docs.python.org/zh-cn/3/library/functions.html#float), <font style="background-color:rgb(236, 240, 243);">argparse.FileType('w')</font> 或可调用函数 |


<font style="color:rgb(0, 0, 0);">  
</font>

### <font style="color:rgb(0, 0, 0);">解析参数</font>
[<font style="color:rgb(0, 0, 0);">ArgumentParser</font>](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser)<font style="color:rgb(0, 0, 0);"> </font><font style="color:rgb(0, 0, 0);">通过</font><font style="color:rgb(0, 0, 0);"> </font>[<font style="color:rgb(0, 0, 0);">parse_args()</font>](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser.parse_args)<font style="color:rgb(0, 0, 0);"> </font><font style="color:rgb(0, 0, 0);">方法解析参数。它将检查命令行，把每个参数转换为适当的类型然后调用相应的操作。在大多数情况下，这意味着一个简单的</font><font style="color:rgb(0, 0, 0);"> </font>[<font style="color:rgb(0, 0, 0);">Namespace</font>](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.Namespace)<font style="color:rgb(0, 0, 0);"> </font><font style="color:rgb(0, 0, 0);">对象将从命令行解析出的属性构建：</font>

```plain
>>>>>> parser.parse_args(['--sum', '7', '-1', '42']) 
Namespace(accumulate=<built-in function sum>, integers=[7, -1, 42]) 
```

<font style="color:rgb(0, 0, 0);">在脚本中，通常 </font>[<font style="color:rgb(0, 0, 0);">parse_args()</font>](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser.parse_args)<font style="color:rgb(0, 0, 0);"> 会被不带参数调用，而 </font>[<font style="color:rgb(0, 0, 0);">ArgumentParser</font>](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser)<font style="color:rgb(0, 0, 0);"> 将自动从 </font>[<font style="color:rgb(0, 0, 0);">sys.argv</font>](https://docs.python.org/zh-cn/3/library/sys.html#sys.argv)<font style="color:rgb(0, 0, 0);"> 中确定命令行参数。</font>

<font style="color:rgb(0, 0, 0);"></font>

<font style="color:rgb(0, 0, 0);"></font>

