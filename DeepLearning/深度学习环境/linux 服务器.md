# ssh命令

ssh fengsm@ip     # 192.168.20.6

密码：fengsm2021   

# sftp命令

1.打开终端，选择新建远程连接。2.选择安全文件传输，输入连接主机IP。3.连接主机。4.put 本地文件路径 远程主机路径（如下）5.get 远程主机路径 本地文件路径

```
put /Users/fsm/Desktop/vgg16_1.py /home/fengsm/pythonproject/catdog
get /home/fengsm/pythonproject/catdog/vgg16_2.py /Users/fsm/Desktop
```

# screen命令

screen -S yourname -> 新建一个叫yourname的session

screen -ls -> 列出当前所有的session

screen -r yourname -> 回到yourname这个session

screen -d yourname -> 远程detach某个session，将指定的screen作业离线。

离开会话并让程序断续运行：ctrl a d (按住ctrl不放，分别按 a 和 d)

screen -d -r yourname -> 结束当前session并回到yourname这个session

**问题：**用 screen -ls, 显式当前状态为Attached，screen -D -r ＜session-id>，-D -r 先踢掉前一用户，再登陆。

**结束：**exit

# conda命令

**创建虚拟环境**的命令：

conda create -n py37 python=3.7 

上述命令创建一个名称为py37的python版本为3.7的虚拟环境



**删除环境**（**不要乱删**）：conda remove -n py37 --all



用以下命令可以**列出已经创建出来的虚拟环境**：conda env list



**列出已经装好的包**：conda list



然后，**进入创建的虚拟环境**：conda activate p36

**进入虚拟环境之后，用conda命令安装的所有包，都是安装在这个虚拟环境里面，不会干扰到外面，即使重新安装一个Python也行。**

**更新所有包**：conda upgrade --all

**卸载包**

`conda remove package_name`

**退出虚拟环境：**

conda deactivate



**虚拟环境python这个执行器的路径**

/anaconda2/envs路径包含了所有的你创建的虚拟环境，环境py37的python执行器在/anaconda2/envs/py37/bin/pyhon路径下，pycharm在remote进行调用远程的编译器的时候需要知道这个路径。



**共享环境：**将当前使用的环境中所包含的python包的名称进行打包。

```
conda env export > 文件名.yaml
```

**载入别人共享的环境。**

```
conda env update -f=/path/文件名.yml
```



**问题：**

conda的激活命令出了问题，解决方法如下：

```
# 激活环境
source activate
# 退出环境
source deactivate
```

# **CUDA和GPU**

```
conda install pytorch torchvision torchaudio cudatoolkit=10.1 -c pytorch
```

```python
nvidia-smi
# 周期性的输出显卡的使用情况，可以用watch指令实现：
watch -n 10 nvidia-smi
# control+z退出查看显卡状态
```

执行上述指执行上述指执行上述指执行上述指执行上述指令可以查看服务器上gpu的使用状况。

```
fuser -v /dev/nvidia*  # 查看当前系统中GPU占用的线程
```

使用kill -9 线程号释放显存

# Linux操作

## 一、文件操作

#### 1.新建文件夹

mkdir 用于新建一个新目录

#### 2.删除给定文件

rm 

rm -rf    // 删除文件夹

#### 3.复制文件与文件夹

**cp命令**

- a 该选项通常在拷贝目录时使用。它保留链接、文件属性，并递归地拷贝目录，其作用等于dpR选项的组合。
- d 拷贝时保留链接。
- f 删除已经存在的目标文件而不提示。
- i 和f选项相反，在覆盖目标文件之前将给出提示要求用户确认。回答y时目标文件将被覆盖，是交互式拷贝。
- p 此时cp除复制源文件的内容外，还将把其修改时间和访问权限也复制到新文件中。
- r 若给出的源文件是一目录文件，此时cp将递归复制该目录下所有的子目录和文件。此时目标文件必须为一个目录名。
- l 不作拷贝，只是链接文件。

**1、复制文件到文件夹**
cp /home/downloads/xampp-linux-x64-7.3.6-0-installer.run /opt/
**2、复制文件夹到文件夹**
cp  -r /home/downloads/phpcms_v9_UTF8/install_package/  /opt/lampp/htdocs/

#### 4.文件夹改名

mv命令既可以重命名，又可以移动文件或文件夹。

用 mv 命令 将文件移动，目标地址如果加 / 就 代表文件夹，如果没有 / 就会重新命名

例子：将目录A重命名为B
`mv A B`

例子：将/a目录移动到/b下，并重命名为c
`mv /a /b/c`

其实在文本模式中要重命名文件或目录，只需要使用mv命令就可以了，比如说要将一个名为abc的文件重命名为1234：
`mv abc 1234`

注意，如果当前目录下也有个1234的文件的话，这个文件是会将它覆盖的。

## 二.压缩文件与解压缩

### 1、zip格式

zip可能是目前使用的最多的文档压缩格式。它最大的优点就是在不同的操作系统平台上使用。缺点就是支持的压缩率不是很高，而tar.gz和tar.bz2在压缩率方面做得非常好。

我们可以使用下列的命令压缩一个文件：

`zip -r archive_name.zip filename #-r是压缩文件`

下面是如果解压一个zip文件：

```
unzip archive_name.zip #（解压文件在当前文件下）
unzip archive_name.zip -d new_dir #（解压文件可以将文件解压缩至一个你指定的的目录，使用-d参数）
```

### 2、tar格式

tar是在Linux中使用的非常广泛的文档打包格式。它的好处就是它只消耗非常少的CPU以及时间去打包文件，它仅仅只是一个打包工具，并不负责压缩。下面是如何打包一个目录：

```
tar -cvf archive_name.tar directory_
to_compress
```

参数：

-c参数是建立新的存档

-v参数详细显示处理的文件

-f参数指定存档或设备

打包之后如何解包：

```
tar -xvf archive_name.tar
```

上面这个解包命令将会将文档解开在当前目录下面。当然，你也可以用下面的这个命令来解包到指定的路径：

```
tar -xvf archive_name.tar -C new_dir  #（解包的参数是-C，不是小写c）
```

### 3、tar.gz格式

它在压缩时不会占用太多CPU，而且可以得到一个非常理想的压缩率。

压缩方式：

```
tar -zcvf archive_name.tar.gz filename
```

解压缩方式：

```
tar -zxvf archive_name.tar.gz
```

上面这个解包命令将会将文档解包在当前目录下面。当然，你也可以用下面的这个命令来指定解包的路径：

```
tar -zxvf archive_name.tar.gz -C new_dir
```

### 4、tar.bz2格式

这种压缩格式是我们提到的所有方式中压缩率最好的。当然，这也就意味着，它比前面的方式要占用更多的CPU与时间。

压缩方式

```
tar -jcvf archive_name.tar.bz2 filename
```

解压缩方式：

```
tar -jxvf archive_name.tar.bz2
```

上面这个解包命令将会将文档解开在当前目录下面。当然，你也可以用下面的这个命令来指定解包的路径：

```
tar -jxvf archive_name.tar.bz2 -C new_dir
```

## 三.查看磁盘空间

Linux 查看磁盘空间可以使用 **df** 和 **du** 命令。

### 1.df

df 以磁盘分区为单位查看文件系统，可以获取硬盘被占用了多少空间，目前还剩下多少空间等信息。

例如，我们使用**df -h**命令来查看磁盘信息， **-h** 选项为根据大小适当显示：

显示内容参数说明：

- **Filesystem**：文件系统
- **Size**： 分区大小
- **Used**： 已使用容量
- **Avail**： 还可以使用的容量
- **Use%**： 已用百分比
- **Mounted on**： 挂载点　

**相关命令：**

- **df -hl**：查看磁盘剩余空间
- **df -h**：查看每个根路径的分区大小
- **du -sh [目录名]**：返回该目录的大小
- **du -sm [文件夹]**：返回该文件夹总M数
- **du -h [目录名]**：查看指定文件夹下的所有文件大小（包含子文件夹）

### 2.du

**du** 的英文原义为 **disk usage**，含义为显示磁盘空间的使用情况，用于查看当前目录的总大小。

例如查看当前目录的大小：

```
# du -sh
605M    .
```

显示指定文件所占空间：

```
# du log2012.log 
300     log2012.log
```

方便阅读的格式显示test目录所占空间情况：

```
# du -h test
608K    test/test6
308K    test/test4
4.0K    test/scf/lib
4.0K    test/scf/service/deploy/product
4.0K    test/scf/service/deploy/info
12K     test/scf/service/deploy
16K     test/scf/service
4.0K    test/scf/doc
4.0K    test/scf/bin
32K     test/scf
8.0K    test/test3
1.3M    test
```

du 命令用于查看当前目录的总大小：

- **-s**：对每个Names参数只给出占用的数据块总数。
- **-a**：递归地显示指定目录中各文件及子目录中各文件占用的数据块数。若既不指定-s，也不指定-a，则只显示Names中的每一个目录及其中的各子目录所占的磁盘块数。
- **-b**：以字节为单位列出磁盘空间使用情况（系统默认以k字节为单位）。
- **-k**：以1024字节为单位列出磁盘空间使用情况。
- **-c**：最后再加上一个总计（系统默认设置）。
- **-l**：计算所有的文件大小，对硬链接文件，则计算多次。
- **-x**：跳过在不同文件系统上的目录不予统计。
- **-h**：以K，M，G为单位，提高信息的可读性。

## 四.软连接与硬链接

**软连接**是linux中一个常用命令，它的功能是为某一个文件在另外一个位置建立一个同不的链接。

具体用法是：ln -s 源文件 目标文件。 

```
ln -s /usr/local/mysql/bin/mysql/usr/bin
```

对/usr/bin目录下的mysql命令创建了软连接 

【硬连接】
**硬连接指通过索引节点来进行连接**。在Linux的文件系统中，保存在磁盘分区中的文件不管是什么类型都给它分配一个编号，称为索引节点号(Inode Index)。在Linux中，多个文件名指向同一索引节点是存在的。一般这种连接就是硬连接。硬连接的作用是允许一个文件拥有多个有效路径名，这样用户就可以建立硬连接到重要文件，以防止“误删”的功能。其原因如上所述，因为对应该目录的索引节点有一个以上的连接。只删除一个连接并不影响索引节点本身和其它的连接，只有当最后一个连接被删除后，文件的数据块及目录的连接才会被释放。也就是说，文件真正删除的条件是与之相关的所有硬连接文件均被删除。

【软连接】
另外一种连接称之为**符号连接（Symbolic Link），也叫软连接**。软链接文件有类似于Windows的快捷方式。它实际上是一个特殊的文件。在符号连接中，文件实际上是一个文本文件，其中包含的有另一文件的位置信息。

**使用方式**

创建软链接

ln  -s [源文件或目录] [目标文件或目录]

例：

当前路径创建test 引向/var/www/test 文件夹 

```
ln –s /var/www/test test
```

创建/var/test 引向/var/www/test 文件夹 

```
ln –s  /var/www/test /var/test
```

删除软链接

和删除普通的文件是一样的，删除都是使用rm来进行操作

例：

删除test

```
rm –rf test
```

修改软链接

ln –snf  [新的源文件或目录] [目标文件或目录]

这将会修改原有的链接地址为新的地址

例如：

创建一个软链接

```
ln –s /var/www/test /var/test
```

修改指向的新路径

```
ln –snf /var/www/test1 /var/test
```

**常用参数：**

```
　　-f : 链结时先将与 dist 同档名的档案删除
　　-d : 允许系统管理者硬链结自己的目录
　　-i : 在删除与 dist 同档名的档案时先进行询问
　　-n : 在进行软连结时，将 dist 视为一般的档案
　　-s : 进行软链结(symbolic link)
　　-v : 在连结之前显示其档名
　　-b : 将在链结时会被覆写或删除的档案进行备份
　　-S SUFFIX : 将备份的档案都加上 SUFFIX 的字尾
　　-V METHOD : 指定备份的方式
　　--help : 显示辅助说明
　　--version : 显示版本
```

## 五.目录操作

**shell命令**

cd “想进的目录” //当目录名称中含有空格、中文或其它特殊字符时请用双引号包括

以下是最常用的几个目录的写法：

1、/ 代表根目录

2、. 当前目录

3、.. 上级目录

4、~ 当前用户的默认工作目录

注：目录可以省略不写， 与cd ~ 有相同的效果。

## 六.文件下载

**wget命令**

### 1.安装

`yum install wget`

### 2.使用

##### 1.使用wget下载单个文件 

以下的例子是从网络下载一个文件并保存在当前目录 

```
wget http://mirrors.163.com/.help/CentOS7-Base-163.repo
```

在下载的过程中会显示进度条，包含（下载完成百分比，已经下载的字节，当前下载速度，剩余下载时间）。

##### 2、使用wget -O下载并以不同的文件名保存 

wget默认会以最后一个符合”/”的后面的字符来命令，对于动态链接的下载通常文件名会不正确。 
错误：下面的例子会下载一个文件并以名称download.php?id=1080保存 

`wget http://www.centos.bz/download?id=1` 
即使下载的文件是zip格式，它仍然以download.php?id=1080命令。 
正确：为了解决这个问题，我们可以使用参数-O来指定一个文件名： 

`wget -O wordpress.zip http://www.centos.bz/download.php?id=1080` 

**3、使用wget –limit -rate限速下载 **
你执行wget的时候，它默认会占用全部可能的宽带下载。但是当你准备下载一个大文件，而你还需要下载其它文件时就有必要限速了。 

```
wget –limit-rate=300k http://cn.wordpress.org/wordpress-3.1-zh_CN.zip 
```

**4、使用wget -c断点续传 
**使用wget -c重新启动下载中断的文件: 

`wget -c http://cn.wordpress.org/wordpress-3.1-zh_CN.zip` 
对于我们下载大文件时突然由于网络等原因中断非常有帮助，我们可以继续接着下载而不是重新下载一个文件。需要继续中断的下载时可以使用-c参数。 

**5、使用wget -b后台下载 
**对于下载非常大的文件的时候，我们可以使用参数-b进行后台下载。 

```
wget -b http://cn.wordpress.org/wordpress-3.1-zh_CN.zip 
Continuing in background, pid 1840. 
Output will be written to `wget-log’. 
```

你可以使用以下命令来察看下载进度 

`tail -f wget-log` 

**6、伪装代理名称下载 
**有些网站能通过根据判断代理名称不是浏览器而拒绝你的下载请求。不过你可以通过–user-agent参数伪装。 

```
wget –user-agent=”Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16″ 下载链接 
```

##  七、文件树结构（实验室服务器没有）

在命令行中输入以下命令安装tree:

```
sudo apt-get install tree
```

**使用方法及参数：**

> tree -d -L 1
> 注：
> tree:显示目录树
> -d:只显示目录
> -L:选择显示的目录深度
> 1：只显示一层深度，即不递归子目录



# 中断进程

Ctrl+c 在命令行下起着终止当前执行程序的作用（**强制中断程序的执行，进程已终止**） 

Ctrl+z 中断命令，**暂停**,但是此任务并没有结束,他仍然在进程中他只是维持挂起的状态,用户可以使用fg/bg操作继续。



# 服务器配置jupyter

## 1.配置notebook



## 2.配置文件



## 3.生成密码



## 4.访问notebook



## 注意：访问失败时建立SSH通道

```text
$ ssh fengsm@192.168.20.6 -L 127.0.0.1:1234:127.0.0.1:8889
```

在本地终端输入上述命令，根据需要更改服务器地址和端口号

在浏览器输入

```
localhost:1234
```

