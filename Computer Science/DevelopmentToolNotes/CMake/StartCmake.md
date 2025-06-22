# Getting started with CMake

## 1. Introduction

CMake是一个跨平台的安装（编译）工具，可以用简单的语句来描述所有平台的安装(编译过程)。
我们开发的软件如果想跨平台，必须要保证能够在不同平台编译。目前在不同的平台有多种Make工具，例如GNU Make，QT的qmake，微软的MS nmake，BSD Make（pmake），Makepp，等等。这些Make工具遵循着不同的规范和标准，所执行的Makefile格式也千差万别。如果使用上面的Make工具，就得为每一种标准写一次makefile，
CMake就是针对上面问题所设计的工具：它首先允许开发者编写一种平台无关的CMakeList.txt文件来定制整个编译流程，然后再根据目标用户的平台进一步生成所需的本地化Makefile和工程文件，如Unix的Makefile或Windows的 Visual Studio工程。从而做到“Write once, run everywhere”。

Cmake并不直接建构出最终的软件，而是产生标准的建构档（如Unix的Makefile或Windows Visual C++的projects/workspaces），然后再依一般的建构方式使用。这使得熟悉某个集成开发环境（IDE）的开发者可以用标准的方式建构他的软件，这种可以使用各平台的原生建构系统的能力是CMake和SCons等其他类似系统的区别之处。

在linux平台下使用CMake生成Makefile并编译的流程如下：
- 写CMake 配置文件CMakeLists.txt 。
- 执行命令cmake PATH或者ccmake PATH生成Makefile（ccmake和cmake的区别在于前者提供了一个交互式的界面）。其中，PATH是CMakeLists.txt所在的目录。
- 使用make命令进行编译。

## 2. 编写 CMakeLists.txt
CMakeLists.txt文件保存在与main.cc 源文件同个目录下：

    # CMake 最低版本号要求
    cmake_minimum_required (VERSION 2.8)

    # 项目信息
    project (Demo1)

    # 指定生成目标
    add_executable(Demo main.cc)

CMakeLists.txt的语法由命令、注释和空格组成，其中命令是不区分大小写的。符号 # 后面的内容被认为是注释。命令由命令名称、小括号和参数组成，参数之间使用空格进行间隔。对于上面的 CMakeLists.txt 文件，依次出现了几个命令：
- cmake_minimum_required：指定运行此配置文件所需的CMake的最低版本；
- project：参数值是Demo1，该命令表示项目的名称是Demo1。
- add_executable：将名为 main.cc 的源文件编译成一个名称为 Demo 的可执行文件。

之后，在当前目录执行cmake .命令，得到 Makefile 后再使用 make 命令编译得到 Demo1 可执行文件。

## 3. 基本用法解释
CMakeLists.txt，这个文件是 cmake 的构建定义文件，文件名是大小写敏感的，如果工程存在多个目录，需要确保每个要管理的目录都存在一个
CMakeLists.txt。

    cmake_minimum_required(VERSION 3.9)

    project(HelloWorld)

    set(CMAKE_CXX_STANDARD 11)

    add_executable(HelloWorld main.cpp)

第一行cmake_minimum_required(VERSION 3.9),这行看意思都能够直接看出来了,表示指定运行此配置文件所需的 CMake 的最低版本；所以看到其他的CMakeList文件没有写这个也是正常的.但是还是推荐写,是因为避免引起cmake不同版本之间构建错误的问题.

第二行,project(HelloWorld) 该命令指定项目的名称,比如这里的项目名称为HelloWorld.更加详细的来说, project 指令的语法是：

    project(projectname [CXX] [C] [Java])

你可以用这个指令定义工程名称，并可指定工程支持的语言，支持的语言列表是可以忽略的，
默认情况表示支持所有语言。所以我们常见使用的时候,就直接使用project(projectname) 就够了. 这个指令隐式的定义了两个 cmake 变量:
_BINARY_DIR 以及_SOURCE_DIR，这里就是
HelloWorld_BINARY_DIR 和 HelloWorld_SOURCE_DIR.
因为采用的是内部编译，两个变量目前指的都是工程所在路径LearningCMake/HelloWorld/，后面我们会讲到外部编译，两者所指代的内容会有所不同。

同时 cmake 系统也帮助我们预定义了 PROJECT_BINARY_DIR 和 PROJECT_SOURCE_DIR变量，他们的值分别跟 HelloWorld_BINARY_DIR 与 HelloWorld_SOURCE_DIR 一致。 为了统一起见，建议以后直接使用 PROJECT_BINARY_DIR，PROJECT_SOURCE_DIR，即
使修改了工程名称，也不会影响这两个变量。如果使用了<projectname>_SOURCE_DIR，修改工程名称后，需要同时修改这些变量。

然后来看第三行set(CMAKE_CXX_STANDARD 11) 这里是把之后的编译选项设置为了C++ 11,

set 指令的语法是：

    set (VAR [VALUE] [CACHE TYPE DOCSTRING [FORCE]])

现阶段，你只需要了解set指令可以用来显式的定义变量即可。
比如我们用到的是set(SRC_LIST main.c)，如果有多个源文件，也可以定义成：set(SRC_LIST main.c t1.c t2.c)。


然后我们来看最后一行add_executable(HelloWorld main.cpp),这行的作用就是将名为main.cpp的源文件编译成一个名称为HelloWorld的可执行文件。同样的,更加详细的用法如下:

    add_executable(executable_name ${SRC_LIST})

定义了这个工程会生成一个文件名为executable_name的可执行文件，相关的源文件是SRC_LIST中定义的源文件列表.

## 4. 多个源文件

### 4.1 同一目录多个源文件
目录为如下的形式：

    ./Demo2
        |
        +--- main.cc
        |
        +--- MathFunctions.cc
        |
        +--- MathFunctions.h


这个时候，CMakeLists.txt 可以改成如下的形式：
    # CMake 最低版本号要求
    cmake_minimum_required (VERSION 2.8)

    # 项目信息
    project (Demo2)

    # 指定生成目标
    add_executable(Demo main.cc MathFunctions.cc)

唯一的改动只是在 add_executable 命令中增加了一个 MathFunctions.cc 源文件。这样写当然没什么问题，但是如果源文件很多，把所有源文件的名字都加进去将是一件烦人的工作。更省事的方法是使用 aux_source_directory 命令，该命令会查找指定目录下的所有源文件，然后将结果存进指定变量名。其语法如下：
   
    aux_source_directory(<dir> <variable>)

因此，可以修改 CMakeLists.txt 如下：

    # CMake 最低版本号要求
    cmake_minimum_required (VERSION 2.8)

    # 项目信息
    project (Demo2)

    # 查找当前目录下的所有源文件
    # 并将名称保存到 DIR_SRCS 变量
    aux_source_directory(. DIR_SRCS)

    # 指定生成目标
    add_executable(Demo ${DIR_SRCS})

这样，CMake 会将当前目录所有源文件的文件名赋值给变量 DIR_SRCS ，再指示变量 DIR_SRCS 中的源文件需要编译成一个名称为 Demo 的可执行文件。

### 4.2 多目录，多源文件

目录结构如下：

    ./Demo3
        |
        +--- main.cc
        |
        +--- math/
            |
            +--- MathFunctions.cc
            |
            +--- MathFunctions.h

对于这种情况，需要分别在项目根目录Demo3和math目录里各编写一个CMakeLists.txt文件。为了方便，我们可以先将math目录里的文件编译成静态库再由main函数调用。根目录中的CMakeLists.txt：

    # CMake 最低版本号要求
    cmake_minimum_required (VERSION 2.8)

    # 项目信息
    project (Demo3)

    # 查找当前目录下的所有源文件
    # 并将名称保存到 DIR_SRCS 变量
    aux_source_directory(. DIR_SRCS)

    # 添加 math 子目录
    add_subdirectory(math)

    # 指定生成目标 
    add_executable(Demo main.cc)

    # 添加链接库
    target_link_libraries(Demo MathFunctions)

该文件添加了下面的内容: 第3行，使用命令add_subdirectory指明本项目包含一个子目录 math，这样math目录下的CMakeLists.txt文件和源代码也会被处理。第6行，使用命令target_link_libraries指明可执行文件main需要连接一个名为MathFunctions的链接库 。子目录中的CMakeLists.txt：

    # 查找当前目录下的所有源文件
    # 并将名称保存到 DIR_LIB_SRCS 变量
    aux_source_directory(. DIR_LIB_SRCS)

    # 生成链接库
    add_library (MathFunctions ${DIR_LIB_SRCS})

在该文件中使用命令add_library将src目录中的源文件编译为静态链接库。


## 5. 自定义编译选项

CMake 允许为项目增加编译选项，从而可以根据用户的环境和需求选择最合适的编译方案。例如，可以将 MathFunctions 库设为一个可选的库，如果该选项为 ON ，就使用该库定义的数学函数来进行运算。否则就调用标准库中的数学函数库。

### 5.1 修改CMakeList.txt
第一步是在顶层的 CMakeLists.txt 文件中添加该选项：


    # CMake 最低版本号要求
    cmake_minimum_required (VERSION 2.8)

    # 项目信息
    project (Demo4)

    # 加入一个配置头文件，用于处理 CMake 对源码的设置
    configure_file (
    "${PROJECT_SOURCE_DIR}/config.h.in"
    "${PROJECT_BINARY_DIR}/config.h"
    )

    # 是否使用自己的 MathFunctions 库
    option (USE_MYMATH
        "Use provided math implementation" ON)

    # 是否加入 MathFunctions 库
    if (USE_MYMATH)
    include_directories ("${PROJECT_SOURCE_DIR}/math")
    add_subdirectory (math)  
    set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
    endif (USE_MYMATH)

    # 查找当前目录下的所有源文件
    # 并将名称保存到 DIR_SRCS 变量
    aux_source_directory(. DIR_SRCS)

    # 指定生成目标
    add_executable(Demo ${DIR_SRCS})
    target_link_libraries (Demo  ${EXTRA_LIBS})

其中：第7行的configure_file命令用于加入一个配置头文件config.h，这个文件由CMake从config.h.in生成，通过这样的机制，将可以通过预定义一些参数和变量来控制代码的生成。第13行的option命令添加了一个USE_MYMATH选项，并且默认值为 ON 。第17行根据USE_MYMATH变量的值来决定是否使用我们自己编写的MathFunctions库。

### 5.2 修改main.cc文件
之后修改 [main.cc](http://main.cc )文件，让其根据USE_MYMATH的预定义值来决定是否调用标准库还是MathFunctions库：


    #include <stdio.h>
    #include <stdlib.h>
    #include "config.h"

    #ifdef USE_MYMATH
    #include "math/MathFunctions.h"
    #else
    #include <math.h>
    #endif


    int main(int argc, char *argv[])
    {
        if (argc < 3){
            printf("Usage: %s base exponent \n", argv[0]);
            return 1;
        }
        double base = atof(argv[1]);
        int exponent = atoi(argv[2]);
        
    #ifdef USE_MYMATH
        printf("Now we use our own Math library. \n");
        double result = power(base, exponent);
    #else
        printf("Now we use the standard library. \n");
        double result = pow(base, exponent);
    #endif
        printf("%g ^ %d is %g\n", base, exponent, result);
        return 0;
    }


### 5.3 编写config.h.in文件

上面的程序值得注意的是第2行，这里引用了一个 config.h 文件，这个文件预定义了 USE_MYMATH 的值。但我们并不直接编写这个文件，为了方便从 CMakeLists.txt 中导入配置，我们编写一个 config.h.in 文件，内容如下：

    #cmakedefine USE_MYMATH

这样 CMake 会自动根据 CMakeLists 配置文件中的设置自动生成 config.h 文件。

### 5.4 编译项目

现在编译一下这个项目，为了便于交互式的选择该变量的值，可以使用 ccmake 命令（也可以使用 cmake -i 命令，该命令会提供一个会话式的交互式配置界面）：

CMake的交互式配置界面从中可以找到刚刚定义的 USE_MYMATH 选项，按键盘的方向键可以在不同的选项窗口间跳转，按下 enter 键可以修改该选项。修改完成后可以按下 c 选项完成配置，之后再按 g 键确认生成 Makefile 。ccmake 的其他操作可以参考窗口下方给出的指令提示。我们可以试试分别将 USE_MYMATH 设为 ON 和 OFF 得到的结果：

## 6. 安装和测试

CMake 也可以指定安装规则，以及添加测试。这两个功能分别可以通过在产生 Makefile 后使用 make install 和 make test 来执行。在以前的 GNU Makefile 里，你可能需要为此编写 install 和 test 两个伪目标和相应的规则，但在 CMake 里，这样的工作同样只需要简单的调用几条命令。


### 6.1 定制安装规则

首先先在 math/CMakeLists.txt 文件里添加下面两行：

    # 指定 MathFunctions 库的安装路径
    install (TARGETS MathFunctions DESTINATION bin)
    install (FILES MathFunctions.h DESTINATION include)
指明 MathFunctions 库的安装路径。之后同样修改根目录的 CMakeLists 文件，在末尾添加下面几行：

    # 指定安装路径
    install (TARGETS Demo DESTINATION bin)
    install (FILES "${PROJECT_BINARY_DIR}/config.h"
            DESTINATION include)

