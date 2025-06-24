<font style="color:rgb(77, 77, 77);">Cpp源程序 (.h,.cpp)–> </font>预编译<font style="color:rgb(77, 77, 77);">处理 --> 编译优化 --> 汇编程序 --> 链接程序 --> 可执行文件</font>

<font style="color:rgb(77, 77, 77);">因此，从原始的CPP文件到最终的</font>可执行文件<font style="color:rgb(77, 77, 77);">，经历了4个步骤：</font>**<font style="color:rgb(77, 77, 77);">预处理、编译、汇编、链接。</font>**

[原理及基础：C和C++的编译过程--GCC编译器](https://www.yuque.com/zhengedaidan-knmgi/ye9qnn/zq45ayihyxn67d9e)

---

## 预处理：
  (1)、将所有的注释以空格代替；

  (2)、将所有的#define删除，并且展开所有的宏定义；

  (3)、处理条件编译指令#if，#ifdef、#elif，#else、#endif；

  (4)、处理#include，展开文件包含；

  (5)、保留编译器需要使用的#pragma指令

 预处理指令示例：

```cpp
  gcc -E *.c -o *.i
```

---

## 编译优化
(1)、对预处理生成的文件进行语法分析、词法分析、语义分析

      语法分析：分析表达式是否遵循语法规则

      词法分析：分析关键字，标识符，立即数是否合法

      语义分析：在语法分析基础上进一步分析表达式是否合法

(2)、分析结束后进行【代码优化】生成相应的汇编代码文件

     编译指令示例：

```cpp
gcc -S *.i -o *.s  
```

---

## 汇编
(1)、汇编过程是用汇编器将汇编代码转变为机器可以执行的指令，也就是机器指令，也称为目标文件(.o)。

(2)、每条汇编指令几乎都对应一条机器指令

      汇编指令示例：

```cpp
 gcc - c *.s  -o *.o
```



```cpp
-E  
只激活预处理,这个不生成文件,需要把它重定向到一个输出文件里.  
例子:  
gcc -E hello.c > pianoapan.txt  
gcc -E hello.c | more  
一个hello word 也要与处理成800行的代码 

-S  
只激活预处理和编译，就是指把文件编译成为汇编代码。  
例子：  
gcc -S hello.c  
他将生成.s的汇编代码，你可以用文本编辑器察看
    
-c   
只激活预处理,编译,和汇编,也就是他只把程序做成obj文件  
例子:  
gcc -c hello.c  
他将生成.o的obj文件  
```

---

## 链接
<font style="color:#000000;">链接是指将目标文件最终生成可执行文件。</font>

<font style="color:rgb(77, 77, 77);">一般在这个阶段，我们会提到动态库和静态库，本质上来说</font>**<font style="color:rgb(77, 77, 77);">库也是一种可执行文件的二进制形式</font>**<font style="color:rgb(77, 77, 77);">，可以被操作系统载入内存执行。</font>

<font style="color:rgb(77, 77, 77);">根据链接方式的不同，链接过程可以分为：</font>

      1、静态链接(.a、.lib）：目标文件直接加入到可执行文件

      2、动态链接(.so、.dll)：在程序启动后才动态加载目标文件



![](https://cdn.nlark.com/yuque/0/2024/png/29307286/1708250187065-38302edc-8946-4ee0-ab3e-8688ec28a3ca.png)

---

# 静态库和动态库


