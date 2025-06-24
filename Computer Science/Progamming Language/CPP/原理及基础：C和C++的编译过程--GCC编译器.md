<font style="color:rgb(100, 100, 100);">GCC的基本概念</font>

<font style="color:rgb(100, 100, 100);">参考 </font>[知乎链接](https://zhuanlan.zhihu.com/p/404682058)

# <font style="color:rgb(100, 100, 100);"> </font><font style="color:#000000;">1.GCC工具</font>
## <font style="color:rgb(18, 18, 18);">GCC编译器：</font>
<font style="color:rgb(18, 18, 18);">GCC（GNU Compiler Collection）是由 GNU 开发的编程语言编译器。 GCC最初代表“GNU C Compiler”，当时只支持C语言。 后来又扩展能够支持更多编程语言，包括 C++、Fortran 和 Java 等。 因此，GCC也被重新定义为“</font>**<font style="color:#DF2A3F;">GNU Compiler Collection</font>**<font style="color:rgb(18, 18, 18);">”，成为历史上最优秀的编译器， 其执行效率与一般的编译器相比平均效率要高</font>**<font style="color:rgb(18, 18, 18);"> 20%~30%</font>**<font style="color:rgb(18, 18, 18);">。</font>



## <font style="color:rgb(18, 18, 18);">GCC编译工具链：</font>
<font style="color:rgb(18, 18, 18);">GCC编译工具链（toolchain），是指以GCC编译器为核心的一整套工具。它主要包含以下三部分内容：</font>

+ **<font style="color:rgb(18, 18, 18);">gcc-core：</font>**<font style="color:rgb(18, 18, 18);">即GCC编译器，用于完成预处理和编译过程，把C代码转换成汇编代码。</font>
+ **<font style="color:rgb(18, 18, 18);">Binutils ：</font>**<font style="color:rgb(18, 18, 18);">除GCC编译器外的一系列小工具包括了链接器ld，汇编器as、目标文件格式查看器readelf等。</font>
+ **<font style="color:rgb(18, 18, 18);">glibc：</font>**<font style="color:rgb(18, 18, 18);">包含了主要的 C语言标准函数库，C语言中常常使用的打印函数printf、malloc函数就在glibc 库中。</font>

<font style="color:rgb(18, 18, 18);">在很多场合下会直接用GCC编译器来指代整套GCC编译工具链。</font>

<font style="color:rgb(18, 18, 18);"></font>

#### <font style="color:rgb(18, 18, 18);">Binutils工具集：</font>
<font style="color:rgb(18, 18, 18);">Binutils（bin utility），是GNU二进制工具集，通常跟GCC编译器一起打包安装到系统。</font>

<font style="color:rgb(18, 18, 18);">在进行程序开发的时候通常不会直接调用这些工具，而是在</font>**<font style="color:rgb(18, 18, 18);">使用GCC编译指令的时候由GCC编译器间接调用</font>**<font style="color:rgb(18, 18, 18);">。下面是其中一些常用的工具：</font>

+ **<font style="color:rgb(18, 18, 18);">as：</font>**<font style="color:rgb(18, 18, 18);">汇编器，把汇编语言代码转换为机器码（目标文件）。</font>
+ **<font style="color:rgb(18, 18, 18);">ld：</font>**<font style="color:rgb(18, 18, 18);">链接器，把编译生成的多个目标文件组织成最终的可执行程序文件。</font>
+ **<font style="color:rgb(18, 18, 18);">readelf：</font>**<font style="color:rgb(18, 18, 18);">可用于查看目标文件或可执行程序文件的信息。</font>
+ **<font style="color:rgb(18, 18, 18);">nm ：</font>**<font style="color:rgb(18, 18, 18);"> 可用于查看目标文件中出现的符号。</font>
+ **<font style="color:rgb(18, 18, 18);">objcopy：</font>**<font style="color:rgb(18, 18, 18);"> 可用于目标文件格式转换，如.bin 转换成 .elf 、.elf 转换成 .bin等。</font>
+ **<font style="color:rgb(18, 18, 18);">objdump：</font>**<font style="color:rgb(18, 18, 18);">可用于查看目标文件的信息，最主要的作用是反汇编。</font>
+ **<font style="color:rgb(18, 18, 18);">size：</font>**<font style="color:rgb(18, 18, 18);">可用于查看目标文件不同部分的尺寸和总尺寸，例如代码段大小、数据段大小、使用的静态内存、总大小等。</font>



#### <font style="color:rgb(18, 18, 18);">glibc库：</font>
<font style="color:rgb(18, 18, 18);">glibc库是GNU组织为GNU系统以及Linux系统编写的C语言标准库，因为绝大部分C程序都依赖该函数库，该文件甚至会直接影响到系统的正常运行，例如常用的文件操作函数read、write、open，打印函数printf、动态内存申请函数malloc等。</font>

# 2.GCC编译 
<font style="color:rgb(18, 18, 18);">GCC 编译工具链在编译一个C源文件时需要经过以下 4 步：</font>

+ <font style="color:rgb(18, 18, 18);">预处理：为把头文件的代码、宏之类的内容转换成生成的.i文件，还是C代码。</font>
+ <font style="color:rgb(18, 18, 18);">编译：把预处理后的.i文件通过编译成.s文件，汇编语言。</font>
+ <font style="color:rgb(18, 18, 18);">汇编：将汇编语言文件生成目标文件.o文件，机器码。</font>
+ <font style="color:rgb(18, 18, 18);">链接：将每个源文件对应的.o文件链接起来，就生成一个可执行程序文件。</font>

![](https://cdn.nlark.com/yuque/0/2023/webp/29307286/1680765629174-6706cf2a-7ed1-4132-bd41-5e22340ff984.webp)

<font style="color:rgb(18, 18, 18);"></font>

### （1）预处理阶段：
<font style="color:rgb(18, 18, 18);">预处理过程中，对源代码文件中的文件包含 (include)、 预编译语句 (如宏定义define等)进行展开，生成 .i 文件。 可理解为把头文件的代码、宏之类的内容转换成更纯粹的C代码，不过生成的文件以.i为后缀。</font>

### <font style="color:rgb(18, 18, 18);">（2）编译阶段：</font>
<font style="color:rgb(18, 18, 18);">把预处理后的.i文件通过编译成为汇编语言，生成.s文件，即把代码从C语言转换成汇编语言，这是GCC编译器完成的工作。在这个过程，GCC会检查各个源文件的语法，即使我们调用了一个没有定义的函数，也不会报错。</font>

### <font style="color:rgb(18, 18, 18);">（3）汇编阶段：</font>
<font style="color:rgb(18, 18, 18);">将汇编语言文件经过汇编，生成目标文件.o文件，每一个源文件都对应一个目标文件。即把汇编语言的代码转换成机器码，这是as汇编器完成的工作。</font>

### <font style="color:rgb(18, 18, 18);">（4）链接阶段：</font>
<font style="color:rgb(18, 18, 18);">最后将每个源文件对应的目标.o文件链接起来，就生成一个可执行程序文件，这是链接器ld完成的工作。</font>

<font style="color:rgb(18, 18, 18);">链接分为两种：</font>

+ <font style="color:rgb(18, 18, 18);">动态链接：GCC编译时的默认选项。动态是指在应用程序运行时才去加载外部的代码库，不同的程序可以共用代码库。 所以动态链接生成的程序比较小，占用较少的内存。</font>
+ <font style="color:rgb(18, 18, 18);">静态链接：链接时使用选项 “--static”，它在编译阶段就会把所有用到的库打包到自己的可执行程序中。 所以静态链接的优点是具有较好的兼容性，不依赖外部环境，但是生成的程序比较大。</font>

# 3.交叉编译
<font style="color:rgb(18, 18, 18);">如果我们希望编译器运行在x86架构平台上，然后编译生成ARM架构的可执行程序，这种编译器和目标程序运行在不同架构的编译过程，被称为 </font>**<font style="color:#DF2A3F;">交叉编译</font>**<font style="color:rgb(18, 18, 18);">。</font>

<font style="color:rgb(18, 18, 18);"></font>

