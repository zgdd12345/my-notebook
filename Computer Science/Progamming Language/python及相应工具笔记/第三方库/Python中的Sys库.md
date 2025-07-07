# 1.简介
<font style="color:rgb(36, 41, 46);">sys”即“system”，“系统”之意。该模块提供了一些接口，用于访问 Python 解释器自身使用和维护的变量，同时模块中还提供了一部分函数，可以与解释器进行比较深度的交互。</font>

# <font style="color:rgb(36, 41, 46);">2.常用功能</font>
## 2.1 sys.argv
<font style="color:rgb(36, 41, 46);">“argv”即“argument value”的简写，是一个</font>**<font style="color:rgb(36, 41, 46);">列表对象</font>**<font style="color:rgb(36, 41, 46);">，其中存储的是在命令行调用 Python 脚本时提供的“命令行参数”。</font>

<font style="color:rgb(36, 41, 46);">这个列表中的第一个参数是被调用的脚本名称，也就是说，调用 Python 解释器的“命令”（</font><font style="color:rgb(199, 37, 78);">python</font><font style="color:rgb(36, 41, 46);">）本身并没有被加入这个列表当中。这个地方要注意一下，因为这一点跟 C 程序的行为有所不同，C 程序读取命令行参数是从头开始的。</font>

## 2.2 sys.platform
<font style="color:rgb(36, 41, 46);">查看</font><font style="color:rgb(199, 37, 78);">sys</font><font style="color:rgb(36, 41, 46);">模块中的</font><font style="color:rgb(199, 37, 78);">sys.platform</font><font style="color:rgb(36, 41, 46);">属性可以得到关于运行平台更详细的息”</font>

<font style="color:rgb(36, 41, 46);"></font>

## <font style="color:rgb(36, 41, 46);">2.3 sys.byteorder</font>
<font style="color:rgb(36, 41, 46);">“byteorder”即“字节序”，指的是在计算机内部存储数据时，数据的低位字节存储在存储空间中的高位还是低位。</font>

<font style="color:rgb(36, 41, 46);">“小端存储”时，数据的低位也存储在存储空间的低位地址中，此时</font><font style="color:rgb(199, 37, 78);">sys.byteorder</font><font style="color:rgb(36, 41, 46);">的值为</font><font style="color:rgb(199, 37, 78);">“little”</font><font style="color:rgb(36, 41, 46);">。如果不注意，在按地址顺序打印内容的时候，可能会把小端存储的内容打错。当前</font>**<font style="color:rgb(36, 41, 46);">大部分机器</font>**<font style="color:rgb(36, 41, 46);">都是使用的小端存储。</font>

<font style="color:rgb(36, 41, 46);"></font>

## <font style="color:rgb(36, 41, 46);">2.4 sys.executable</font>
<font style="color:rgb(36, 41, 46);">该属性是一个字符串，在正常情况下，其值是当前运行的 Python 解释器对应的可执行程序所在的绝对路径。</font>

<font style="color:rgb(36, 41, 46);"></font>

## <font style="color:rgb(36, 41, 46);">2.5 sys.modules</font>
<font style="color:rgb(36, 41, 46);">该属性是一个字典，包含的是各种已加载的模块的模块名到模块具体位置的映射。</font>

<font style="color:rgb(36, 41, 46);">通过手动修改这个字典，可以重新加载某些模块；但要注意，切记不要大意删除了一些基本的项，否则可能会导致 Python 整个儿无法运行。</font>

<font style="color:rgb(36, 41, 46);"></font>

## <font style="color:rgb(36, 41, 46);">2.6 sys.builtin_module_names</font>
<font style="color:rgb(36, 41, 46);">该属性是一个字符串元组，其中的元素均为当前所使用的的 Python 解释器内置的模块名称。</font>

<font style="color:rgb(36, 41, 46);">注意区别</font><font style="color:rgb(199, 37, 78);">sys.modules</font><font style="color:rgb(36, 41, 46);">和</font><font style="color:rgb(199, 37, 78);">sys.builtin_module_names</font><font style="color:rgb(36, 41, 46);">——前者的关键字（keys）列出的是导入的模块名，而后者则是解释器内置的模块名。</font>

<font style="color:rgb(36, 41, 46);"></font>

## <font style="color:rgb(36, 41, 46);">2.7 sys.path</font>
<font style="color:rgb(36, 41, 46);">A list of strings that specifies the search path for modules. Initialized from the environment variable</font><font style="color:rgb(36, 41, 46);"> </font>[PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)<font style="color:rgb(36, 41, 46);">, plus an installation-dependent default.</font>

<font style="color:rgb(36, 41, 46);">该属性是一个由字符串组成的列表，其中各个元素表示的是 Python 搜索模块的路径；在程序启动期间被初始化。</font>

<font style="color:rgb(36, 41, 46);">其中第一个元素（也就是</font><font style="color:rgb(199, 37, 78);">path[0]</font><font style="color:rgb(36, 41, 46);">）的值是最初调用 Python 解释器的脚本所在的绝对路径；如果是在交互式环境下查看</font><font style="color:rgb(199, 37, 78);">sys.path</font><font style="color:rgb(36, 41, 46);">的值，就会得到一个空字符串。</font>

<font style="color:rgb(36, 41, 46);"></font>

# 3.进阶功能




python程序中使用 import XXX 时，python解析器会在当前目录、已安装和第三方模块中搜索 xxx，如果都搜索不到就会报错。

使用sys.path.append()方法可以临时添加搜索路径，方便更简洁的import其他包和模块。这种方法导入的路径会在python程序退出后失效。

