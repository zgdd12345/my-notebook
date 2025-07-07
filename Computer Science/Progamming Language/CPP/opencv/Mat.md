## <font style="color:rgb(25, 27, 31);">Mat概述</font>
<font style="color:rgb(25, 27, 31);">Mat类是OpenCV用于处理图像而引入的一个封装类，用于存储矩阵数据，由</font>**<font style="color:rgb(25, 27, 31);">矩阵头和指向矩阵数据的指针两部分组成</font>**<font style="color:rgb(25, 27, 31);">。</font><u><font style="color:rgb(25, 27, 31);">矩阵头存储了矩阵的尺寸，存储方法，引用次数等信息</font></u><font style="color:rgb(25, 27, 31);">，它的</font><u><font style="color:rgb(25, 27, 31);">大小是一个常量</font></u><font style="color:rgb(25, 27, 31);">，不会随着矩阵的尺寸的大小而改变，而</font><u><font style="color:rgb(25, 27, 31);">指针则指向存储数据的地址</font></u><font style="color:rgb(25, 27, 31);">。</font>

## Mat构造函数
### 声明指定类型的矩阵
```cpp
Mat value = Mat_<data_type>(row, col, initValue)
```

<font style="color:rgb(25, 27, 31);">data_type: 数据类型，可以是double， float， int， short， unsigned char, char等等</font>

<font style="color:rgb(25, 27, 31);">row：</font>[矩阵行数](https://www.zhihu.com/search?q=%E7%9F%A9%E9%98%B5%E8%A1%8C%E6%95%B0&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22article%22%2C%22sourceId%22%3A%22487572924%22%7D)

<font style="color:rgb(25, 27, 31);">col：矩阵列数</font>

<font style="color:rgb(25, 27, 31);">initValue: 矩阵初始数值</font>





### 指定尺寸和结构类型
```cpp
Mat value(row, col, type, scalar)
```

row: 矩阵行数

col：矩阵列数

type：矩阵数据类型，比如CV_8UC3表示三通道8字节，主要面向图像矩阵

scalar：矩阵初始值，注：Scalar用来表示颜色数据

```cpp
int main () {
    Mat value(10, 10, CV_32FC4, Scalar(0,1,2,3));
    cout << value << endl;
}
```

### 从原有矩阵抠图
```cpp
Mat value(image, lowerRange, upperRange)
```

<font style="color:rgb(25, 27, 31);">image: 已完成构建的Mat矩阵</font>

<font style="color:rgb(25, 27, 31);">lowerRange：在image矩阵中截取的行数范围</font>

<font style="color:rgb(25, 27, 31);">upperRange：在image矩阵中截取的列数范围</font>

## Mat成员函数
## Mat成员变量
## Mat元素存取


<font style="color:rgb(25, 27, 31);"></font>

