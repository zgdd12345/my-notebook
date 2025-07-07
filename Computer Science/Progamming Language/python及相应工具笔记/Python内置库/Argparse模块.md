# Argparse模块

### 一、简介

`argparse`是python用于解析命令行参数和选项的标准模块，用于代替已经过时的optparse模块。`argparse`模块的作用是用于解析命令行参数。

### 二、使用步骤

```python
1：import argparse

2：parser = argparse.ArgumentParser(description="your script description")

3：parser.add_argument()

4：parser.parse_args()
```

1. 首先导入该模块；
2.  然后创建一个解析对象；description参数可以用于插入描述脚本用途的信息，可以为空;
3.  然后向该对象中添加你要关注的命令行参数和选项，每一个add_argument方法对应一个你要关注的参数或选项；
4.  最后调用parse_args()方法进行解析；
5.  解析成功之后即可使用。

### 三、创建解析器对象ArgumentParse

```python
ArgumentParser(prog=None, usage=None,description=None, epilog=None, parents[],
               formatter_class=argparse.HelpFormatter, prefix_chars=''
               ,fromfile_prefix_chars=None,argument_default=None,
               conflict_handler='error', add_help=True)
```

**prog**：程序的名字，默认为sys.argv[0]，用来在help信息中描述程序的名称。
 **usage**：描述程序用途的字符串
 **description**：help信息前的文字。
 **epilog**：help信息之后的信息

```python
import argparse
parse = argparse.ArgumentParser(prog = 'argparseDemo',prefix_chars= '+',
                                description='the message info before help info',
                                epilog="the message info after help info")
parse.print_help()
```

```bash
$ python argparseDemo.py 
usage: argparseDemo [+h]

the message info before help info

optional arguments:
  +h, ++help  show this help message and exit

the message info after help info
```

**add_help**：设为False时，help信息里面不再显示-h --help信息。
**prefix_chars**：参数前缀，默认为'-'

```python
import argparse
parse = argparse.ArgumentParser(prog = 'argparseDemo',prefix_chars= '+')
parse.add_argument('+f')
parse.add_argument('++bar')
print parse.parse_args()
```

```bash
 $python argparseDemo.py ++bar 123 +f 123
Namespace(bar='123', f='123')
```

**fromfile_prefix_chars**：前缀字符，放在文件名之前
 **argument_default**：参数的全局默认值。
 **conflict_handler**：对冲突的处理方式，默认为返回错误“error”。还有“resolve”，智能解决冲突。当用户给程序添加了两个一样的命令参数时，“error”就直接报错，提醒用户。而“resolve”则会去掉第一次出现的命令参数重复的部分或者全部（可能是短命令冲突或者全都冲突）。



### 四、add_argument()方法，用来指定程序需要接受的命令参数

```python
add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices
            [,required][, help][, metavar][, dest])
```

**name or flags**：参数有两种，可选参数和位置参数。parse_args()运行时，会用'-'来认证可选参数，剩下的即为位置参数。定位参数必选，可选参数可选。

添加可选参数：

```python
 parser.add_argument('-f', '--foo')
```

添加位置参数:

```python
 parser.add_argument('bar')
```

```python
import argparse
parse = argparse.ArgumentParser()
parse.add_argument('-f', '--foo')
parse.add_argument('bar')
parse.parse_args(['baffr'])
```



# Argparse用法总结

### 1.位置参数（positional arguments）

命令行中传入参数时候，传入的参数的先后顺序不同，运行结果往往会不同，这是因为采用了位置参数,例如

```python
import argparse

parser = argparse.ArgumentParser(description='姓名')
parser.add_argument('param1', type=str,help='姓')
parser.add_argument('param2', type=str,help='名')
args = parser.parse_args()

#打印姓名
print(args.param1+args.param2)
```

用法是不用带-

<img src="C:\Users\Administrator\Desktop\笔记\python及相应工具笔记\source\positional arguments.jpg" alt="positional arguments" style="zoom:60%;" />

### 2.可选参数（optional arguments）

​		为了在命令行中避免上述位置参数的bug（容易忘了顺序），可以使用可选参数，这个有点像关键词传参，但是需要在关键词前面加`--`

- “-”指定短参数，如：-h

- "--"指定长参数，如：--help

  两种方式可以同时存在，也可只有一个。如下：

<img src="C:\Users\Administrator\Desktop\笔记\python及相应工具笔记\source\optional arguments.jpg" alt="optional arguments" style="zoom:60%;" />

```python
import argparse

parser = argparse.ArgumentParser(description='姓名')
parser.add_argument('--family', type=str,help='姓')
parser.add_argument('--name', type=str,help='名')
args = parser.parse_args()

#打印姓名
print(args.family+args.name)
```

### 3.类型（type）

默认参数类型为str，进行数学计算需要对参数解析后进行类型转换。

<img src="C:\Users\Administrator\Desktop\笔记\python及相应工具笔记\source\type.jpg" alt="type" style="zoom:67%;" />

### 4.可选值（choice=[]）

使用choice限制某个值的取值范围，如下：限制取值范围为0，1，2

![choice](C:\Users\Administrator\Desktop\笔记\python及相应工具笔记\source\choice.jpg)

### 5.程序用法帮助

![usages](C:\Users\Administrator\Desktop\笔记\python及相应工具笔记\source\usages.jpg)

打印帮助信息即可显示 calculate X to the power of Y

### 6.互斥参数

![mutex](C:\Users\Administrator\Desktop\笔记\python及相应工具笔记\source\mutex.jpg)

### 7.参数默认值（default）

​		add_argument中有一个default参数。有的时候需要对某个参数设置默认值，即如果命令行中没有传入该参数的值，程序使用默认值。如果命令行传入该参数，则程序使用传入的值。具体请看下面的例子

```python
import argparse

parser = argparse.ArgumentParser(description='姓名')
parser.add_argument('--family', type=str, default='张',help='姓')
parser.add_argument('--name', type=str, default='三', help='名')
args = parser.parse_args()

#打印姓名
print(args.family+args.name)
```

### 8.必须参数（required=True）

add_argument有一个required参数可以设置该参数是否必需。

```python
import argparse

parser = argparse.ArgumentParser(description='姓名')
parser.add_argument('--family', type=str, help='姓')
parser.add_argument('--name', type=str, required=True, default='', help='名')
args = parser.parse_args()

#打印姓名
print(args.family+args.name)
```

### 9.操作args词典

结果是一种类似于python字典的数据类型。我们可以使用 `arg.参数名`来提取这个参数

```python
import argparse

parser = argparse.ArgumentParser(description='命令行中传入一个数字')
#type是要传入的参数的数据类型  help是该参数的提示信息
parser.add_argument('integers', type=str, help='传入的数字')

args = parser.parse_args()

#获得integers参数
print(args.integers)
```

### 10.传入多个参数

```python
import argparse

parser = argparse.ArgumentParser(description='命令行中传入一个数字')
parser.add_argument('integers', type=str, nargs='+',help='传入的数字')
args = parser.parse_args()

print(args.integers)
```

**nargs是用来说明传入的参数个数，'+' 表示传入至少一个参数**。

