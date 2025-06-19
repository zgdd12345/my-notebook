### 1.ImageNet数据集简介

ImageNet图像数据集始于2009年，当时李飞飞教授等在CVPR2009上发表了一篇名为《ImageNet: A Large-Scale Hierarchical Image Database》的论文，之后就是基于ImageNet数据集的7届ImageNet挑战赛(2010年开始)。

数据下载：http://image-net.org

ImageNet1k：



ImageNet21k：



Tiny ImageNet：

Tiny Imagenet 有 200 个类。 每个类有 500 张训练图像、50 张验证图像和 50 张测试图像。



### 2.ImageNet处理

以ImageNet1k为例：

数据集下载之后的相关压缩包：

```text
ILSVRC2012_img_train.tar
ILSVRC2012_img_val.tar
```

注：1.这里没有下载test集，只下载了训练和验证集，这用来测试模型是完全够用的；

2.数据的详细说明可以参考这个[中文翻译版](https://link.zhihu.com/?target=https%3A//blog.csdn.net/qq_43205738/article/details/86543766)；也可以在官网直接查看；

#### 训练集数据预处理

ILSVRC2012_img_train.tar压缩包，里面包含120多万的自然图像，大概有150G。含有1000个类别的压缩包，分别对应1000个类别。每个压缩包解压之后都可以得到对应的类别照片。

训练集预处理的目标是将1000个tar解压至train文件中，对应的每类图片建立自己的对应文件夹，即在tran文件中含有1000个子文件夹。具体文件结构如下：

> ---train
> ---------n01440764
> ---------n01443537
> ---------...
> ---------n15075141

处理的过程可以使用shell脚本或python程序进行处理。我是直接使用的命令，跟shell脚本是一样的，只是我是一个命令进行的，具体形式如下：

```text
# step 1
# 创建train文件夹，将tar转移到train文件中，并cd到train文件夹
mkdir train && mv ILSVRC2012_img_train.tar train/ && cd train

# step 2
# 解压 train压缩包并删除train压缩包
# tar -xvf ILSVRC2012_img_train.tar && rm -f ILSVRC2012_img_train.tar

# step 3
# 解压1000个类别压缩包并创建对应的子文件。
# find . -name "*.tar" | while read NAME ; do mkdir -p "${NAME%.tar}"; tar -xvf "${NAME}" -C "${NAME%.tar}"; rm -f "${NAME}"; done
```

#### 验证集数据预处理

ILSVRC2012_img_val.tar中含有50000张图片，解压之后是直接是图像，并没有按照类别区分开，具体形式如下：

```text
ILSVRC2012_val_00000001.JPEG
ILSVRC2012_val_00000002.JPEG
...
ILSVRC2012_val_00049999.JPEG
ILSVRC2012_val_00050000.JPEG
```

关于val的处理方式，根train类似，都是得到根train一样的文件结构：

```text
---val
---------n01440764
---------n01443537
---------...
---------n15075141
```

具体命令如下：

```text
# Step 1
#创建val文件夹，将val.tar移动到val文件中，cd到val文件，解压
mkdir val && mv ILSVRC2012_img_val.tar val/ && cd val && tar -xvf ILSVRC2012_img_val.tar
# Step 2
# 重新分类
wget -qO- https://raw.githubusercontent.com/soumith/imagenetloader.torch/master/valprep.sh | bash
```

注：在step 2重新分类中用到了一个[valprep.sh](https://link.zhihu.com/?target=https%3A//raw.githubusercontent.com/soumith/imagenetloader.torch/master/valprep.sh)文件，这样可以帮助我们得到和训练集一样的文件结构；