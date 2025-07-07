[链接](https://zhuanlan.zhihu.com/p/362834539)

+ <font style="color:rgb(25, 27, 31);">官方文档：</font>[Intro - pybind11 documentation](https://link.zhihu.com/?target=https%3A//pybind11.readthedocs.io/en/stable/index.html)
+ <font style="color:rgb(25, 27, 31);">源码连接：</font>[pybind/pybind11](https://link.zhihu.com/?target=https%3A//github.com/pybind/pybind11)
+ <font style="color:rgb(25, 27, 31);">博客分享：</font>[pybind11使用指南_zhuikefeng的博客-CSDN博客_pybind11](https://link.zhihu.com/?target=https%3A//blog.csdn.net/zhuikefeng/article/details/107224507)

# 环境配置与依赖安装
百度一下你就知道

# 简明教程
```plain
PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("add", &add, "A function which adds two numbers");
  
    m.def("inadd",&inadd,"cin and count");
}
```

<font style="color:rgb(25, 27, 31);">最重要的就是这个python模块绑定</font>

<font style="color:rgb(25, 27, 31);">example：模型名，切记不需要引号</font>

<font style="color:rgb(25, 27, 31);">m：可以理解成模块对象把</font>

<font style="color:rgb(25, 27, 31);">m.doc()：help说明</font>

<font style="color:rgb(25, 27, 31);">m.def：用来注册函数和python打通界限</font>

  


