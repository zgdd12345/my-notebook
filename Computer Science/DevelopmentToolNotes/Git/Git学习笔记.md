# Git学习笔记

## 0.简介

Git 是一个开源的分布式版本控制系统，用于敏捷高效地处理任何或小或大的项目。

Git 是 Linus Torvalds 为了帮助管理 Linux 内核开发而开发的一个开放源码的版本控制软件。

Git 与常用的版本控制工具 CVS, Subversion 等不同，它采用了分布式版本库的方式，不必服务器端软件支持。

## 1.入门

### 1.1将文件添加到版本库

使用Git前，需要先建立一个仓库(repository)。您可以使用一个已经存在的目录作为Git仓库或创建一个空目录。

使用您当前目录作为Git仓库，我们只需使它初始化。

```bush
git init  # 将当前目录设置为git可管理的目录
```

使用指定目录作为Git仓库。

```
git init newrepo  # 将指定目录设置为git可管理的目录
```

所有的版本控制系统，**只能跟踪文本文件的改动**，比如txt文件，网页，所有程序的代码等，Git也不列外，版本控制系统可以告诉你每次的改动，但是图片，视频这些二进制文件，虽能也能由版本控制系统管理，但没法跟踪文件的变化，只能把二进制文件每次改动串起来，也就是知道图片从1kb变成2kb，但是到底改了啥，版本控制也不知道。

第一步：使用命令 git add readme.txt添加到暂存区里面去。如下：

```
git add readme.txt
```

```
git add .  # 将全部文件添加到暂存区
```

第二步：用命令 git commit告诉Git，把文件提交到仓库。

```  
git commit -m "说明信息"   # 必须添加注释信息
```

可以通过命令git status来查看是否还有文件未提交

```
git status
```

可以通过命令git diff 文件名来查看文件修改内容

```
git diff readme.txt
```

### 1.2版本回滚

查看历史记录。

```
git log  # 查看提交日志
```

git log命令显示从最近到最远的提交日志。

简洁显示日志信息：`git log –pretty=oneline`

版本回退：

第一种：

```
git reset --hard HEAD^   # 如果要回退到上上个版本只需把HEAD^ 改成 HEAD^^ 以此类推
```

如果要回退到前100个版本的话，使用上面的方法肯定不方便，我们可以使用下面的简便命令操作。

第二种：

```
git reset --hard HEAD~100  # 
```

可以通过版本号回退，使用命令方法如下：

```
git reset --hard  # 版本号 
```

可以通过如下命令即可获取到版本号：

```
git reflog
```

使用得到的版本号恢复

```
git reset --hard 6fcfc89
```

## 2.工作区与暂存区的区别

**工作区：**在电脑上看到的目录。

**版本库(Repository)：**工作区有一个隐藏目录`.git`,这个不属于工作区，这是版本库。

其中版本库里面存了很多东西，其中最重要的就是**stage(暂存区)**，还有Git为我们自动创建了**第一个分支master**,以及指向master的一个指针**HEAD**。

使用Git提交文件到版本库有两步：

第一步：是使用 `git add` 把文件添加进去，实际上就是把文件添加到暂存区。

第二步：使用`git commit`提交更改，就是把暂存区的所有内容提交到当前分支上。

## 3.撤销修改和删除文件

**撤销修改**是在不做版本回退的情况下撤销之前的修改返回原本状态。

`git checkout -- file` 可以丢弃工作区的修改，如下命令：

```
git checkout -- readme.txt  # 把readme.txt文件在工作区做的修改全部撤销
```

两种情况：

1. readme.txt自动修改后，还没有放到暂存区，使用撤销修改回到和版本库一样的状态。
2. 另外一种是readme.txt已经放入暂存区了，接着又作了修改，撤销修改就回到添加暂存区后的状态。

注意：命令`git checkout -- readme.txt` 中的 -- 很重要，如果没有 -- 的话，那么命令变成创建分支了。

**删除文件**

可以直接在文件目录中把文件删了，或者使用如上rm命令：rm b.txt ，如果我想彻底从版本库中删掉了此文件的话，可以再执行commit命令提交。

## 4.远程仓库（GitHub）

### 4.1设置SSH Keys

本地Git仓库和github仓库之间的传输是通过SSH加密，所以需要设置SSH Keys。

1. 创建SSH Keys.

   在用户主目录下，看看有没有.ssh目录，如果有，再看看这个目录下有没有id_rsa和id_rsa.pub这两个文件，如果有的话，直接跳过此如下命令，如果没有的话，打开命令行，输入如下命令：

   ```
   ssh-keygen -t rsa –C “youremail@example.com”
   ```

   id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥

2. 在Github设置SSH Keys.

   登录github,打开” settings”中的SSH Keys页面，然后点击“Add SSH Key”,填上任意title，在Key文本框里黏贴id_rsa.pub文件的内容。

### 4.2添加远程库

1. 在Github上创建repository。

   可以从这个仓库克隆出新的仓库，也可以把一个已有的本地仓库与之关联，然后，把本地仓库的内容推送到GitHub仓库。

2. 在本地的testgit仓库下运行命令：

   关联远程库

```
git remote add origin git@github.com:zgdd12345/quantum_project.git   # github下code处地址
```

把本地库的内容推送到远程，使用 `git push`命令，实际上是把**当前分支master**推送到远程。

由于远程库是空的，我们**第一次推送master分支时，加上了 –u参数**，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令。

从现在起，只要本地作了提交，就可以通过如下命令：

```
git push origin master
```

把本地master分支的最新修改推送到github上了，现在你就拥有了真正的**分布式版本库**了。

### 4.3从远程库clone

```
git clone 远程库地址  
```

## 5.创建与合并分支

### 5.1创建与合并

每次提交，Git都把它们串成一条时间线，这条时间线就是一个分支。截止到目前，只有一条时间线，在Git里，这个分支叫**主分支**，即**master分支**。HEAD严格来说不是指向提交，而是指向master，master才是指向提交的，所以，HEAD指向的就是当前分支。

我们来创建dev分支，然后切换到dev分支上。

```
git checkout 命令加上 –b参数表示创建并切换，相当于如下2条命令

git branch dev

git checkout dev

git branch  # 查看分支，会列出所有的分支，当前分支前面会添加一个星号。
```

把dev分支上的内容合并到分支master上，可以在master分支上，使用如下命令 `git merge dev`

`git merge`命令用于合并指定分支到当前分支上，

总结创建与合并分支命令如下：

查看分支：`git branch`

创建分支：`git branch name`

切换分支：`git checkout name`

创建+切换分支：`git checkout –b name`

合并某分支到当前分支：`git merge name`

删除分支：`git branch –d name`

### 5.2冲突解决



### 5.3分支管理策略



### 5.4bug分支



## 6.多人协作

当你从远程库克隆时候，实际上Git自动把本地的master分支和远程的master分支对应起来了，并且**远程库的默认名称是origin。**

要查看远程库的信息 使用 `git remote`
要查看远程库的详细信息 使用 `git remote –v`


