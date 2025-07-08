Mac的终端操作和Linux基本一致。

# 常用命令
参考[链接](https://blog.51cto.com/u_15501625/5013236)

cd：进入指定文件夹路径

pwd：显示当前的目录路径

ls：显示当前目录下的内容

ls -la：显示当前目录下的详细内容

ls -a：显示当前目录下的内容，包含隐藏文件

mkdir：创建目录

touch file.format：创建指定格式的文件

mvdir：移动目录，或重命名

rm：删除文件 或 空目录

rm -rf dir：删除一个 非空 目录

cp f1 f2：复制文件或目录

file：显示文件类型

find：使用匹配表达式查找文件,如find *.gradle

open file_name：使用默认的程序打开文件

cat：显示或连接文件内容

ln：为文件创建联接

head：显示文件的最初几行

tail：显示文件的最后几行

paste：横向拼接文件内容

diff：比较并显示两个文件的内容差异

wc：统计文件的字符数、词数和行数

uniq：去掉文件中的重复行

grep：通过简单正则表达式搜索文件

sudo：获取root权限

clear：清除屏幕或窗口内容

which：查看指定程序的路径

history：列出最近执行过的命令及编号

env：显示当前所有设置过的环境变量

date：显示系统的当前日期和时间

cal：显示日历

# cat命令
参考[链接](https://blog.csdn.net/Robin_Pi/article/details/108727283)

cat主要有三个方面的作用：



1. 查看文件

`cat file_name`一次性、整个查看文件

2. 创建文件

`cat new_file_name`只能是新建一个不存在的文件！

3. 合并文件

`cat file_name1 file_name2 > target_file_name`完成将文件1 和 文件2合并为目标文件。

或者合并当前目录下，所有包含某些名称（xxx）的文件：

`cat xxx* > target_file_name`

又或者是以xxx结尾的文件：

