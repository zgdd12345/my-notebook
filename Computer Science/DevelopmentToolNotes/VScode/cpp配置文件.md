<font style="color:rgb(77, 77, 77);">在 vscode 中，需要根据项目建立单独的配置文件。</font>

<font style="color:rgb(77, 77, 77);">包含了以下3个最重要的：</font>

+ <font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">c_cpp_properties.json</font>
+ <font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">launch.json</font>
+ <font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">tasks.json</font>

<font style="color:rgb(77, 77, 77);">这三个文件需要存放在项目文件夹下面的 </font><font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.vscode</font><font style="color:rgb(77, 77, 77);"> 文件夹内。</font>

<font style="color:rgb(77, 77, 77);"></font>

+ <font style="color:rgb(77, 77, 77);">c_cpp_properties.json</font>

<font style="color:rgb(77, 77, 77);">这个文件的作用是配置 vscode 配置整体的 C++ 的环境，就是你要告诉你的 vscode IDE，我有哪些需要进行 include 的头文件 .hpp 和库文件 .lib，我把这个理解为一个准备工作。</font>

<font style="color:rgb(77, 77, 77);">这里主要注意两点：</font>

1. <font style="color:rgb(77, 77, 77);">“includePath” 后面就是放的就是头文件和库文件所在的路径，每个人的情况不同，可以把下面的路径输入进去查找一下有没有对应的文件，以进行确认。</font>
2. <font style="color:rgb(77, 77, 77);">后面的两个星号 ** 表示递归查找，就是查找目标目录的同时，该目录下的子目录也一并查找。</font>
+ <font style="color:rgb(79, 79, 79);">launch.json</font>

<font style="color:rgb(77, 77, 77);">这个是 vscode 用于调试的配置文件，比如指定调试语言环境，指定调试类型等。</font>

<font style="color:rgb(77, 77, 77);">这里最重要的是 </font><font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">"preLaunchTask"</font><font style="color:rgb(77, 77, 77);"> 的设置，表示在运行这个调试之前，需要告诉编译器哪些前置条件。其实也就是把 </font><font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">tasks.json</font><font style="color:rgb(77, 77, 77);"> 关联进来。</font>

<font style="color:rgb(77, 77, 77);"></font>

+ <font style="color:rgb(79, 79, 79);">tasks.json</font>

<font style="color:rgb(77, 77, 77);">这个文件是编译的配置，</font><font style="color:rgb(25, 27, 31);">告诉 VS Code 如何编译这个源文件，让 VS Code 去使用 g++ 编译器编译源文件为一个可执行文件</font><font style="color:rgb(77, 77, 77);">。</font>

<font style="color:rgb(77, 77, 77);">设置你在编译的过程中需要用到哪些库文件和头文件，用什么编译器，用什么编译方式等，都可以在这里进行设置。</font>

<font style="color:rgb(77, 77, 77);">这里的关键在于 </font><font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">"label"</font><font style="color:rgb(77, 77, 77);"> 的设置一定要和 launch.json 中的 </font><font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">"preLaunchTask"</font><font style="color:rgb(77, 77, 77);"> 一致！</font>

<font style="color:rgb(77, 77, 77);">在 主菜单栏 中选择 终端，并选择 配置默认生成任务，在下拉菜单中选择 C/C++:g++ 编译活跃文件。完成上面操作以后，会在 .vscode 文件夹中新建一个 tasks.json 文件，其内容大致和下面相同：</font>

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "type": "shell",
      "label": "g++ build active file",
      "command": "/usr/bin/g++",
      "args": ["-g", "${file}", "-o", "${fileDirname}/${fileBasenameNoExtension}"],
      "options": {
        "cwd": "/usr/bin"
      },
      "problemMatcher": ["$gcc"],
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```

[配置文件](https://code.visualstudio.com/docs/editor/variables-reference)

<font style="color:rgb(25, 27, 31);">关于里面变量的意义，可以去参考这个</font>[链接](https://link.zhihu.com/?target=https%3A//code.visualstudio.com/docs/editor/variables-reference)<font style="color:rgb(25, 27, 31);">进行深入学习。其中，</font>**<font style="color:rgb(25, 27, 31);background-color:rgb(248, 248, 250);">command</font>****<font style="color:rgb(25, 27, 31);"> 变量指定了那个编译器会被使用</font>**<font style="color:rgb(25, 27, 31);">，这里就是 </font><font style="color:rgb(25, 27, 31);background-color:rgb(248, 248, 250);">/usr/bin</font><font style="color:rgb(25, 27, 31);"> 目录下的 </font><font style="color:rgb(25, 27, 31);background-color:rgb(248, 248, 250);">g++</font><font style="color:rgb(25, 27, 31);"> 编译器；</font>**<font style="color:rgb(25, 27, 31);background-color:rgb(248, 248, 250);">args</font>****<font style="color:rgb(25, 27, 31);"> 这个参数列表给出了我们需要传递给 g++ 编译器的命令参数，需要符合 g++ 命令行的参数顺序</font>**<font style="color:rgb(25, 27, 31);">，</font><u><font style="color:rgb(25, 27, 31);background-color:rgb(248, 248, 250);">${file}</font></u><u><font style="color:rgb(25, 27, 31);"> 代表目前编辑器打开的文件，</font></u><u><font style="color:rgb(25, 27, 31);background-color:rgb(248, 248, 250);">${fileDirname}</font></u><u><font style="color:rgb(25, 27, 31);"> 代表当前活跃文件的目录，即 </font></u><u><font style="color:rgb(25, 27, 31);background-color:rgb(248, 248, 250);">projects/helloworld</font></u><u><font style="color:rgb(25, 27, 31);"> 目录，</font></u><u><font style="color:rgb(25, 27, 31);background-color:rgb(248, 248, 250);">${fileBasenameNoExtension}</font></u><u><font style="color:rgb(25, 27, 31);"> 为生成的文件名，与被编译的文件名相同。</font></u><font style="color:rgb(25, 27, 31);background-color:rgb(248, 248, 250);">label</font><font style="color:rgb(25, 27, 31);"> 变量的值为终端任务中名字，你可以任意修改；</font><font style="color:rgb(25, 27, 31);background-color:rgb(248, 248, 250);">group</font><font style="color:rgb(25, 27, 31);"> 变量中的 </font><font style="color:rgb(25, 27, 31);background-color:rgb(248, 248, 250);">"isDefault":true</font><font style="color:rgb(25, 27, 31);"> 代表了当按下 </font><font style="color:rgb(25, 27, 31);background-color:rgb(248, 248, 250);">Ctrl+Shift+B</font><font style="color:rgb(25, 27, 31);"> 时，会对当前活跃的文件进行编译，仅仅是为了方便。</font>

