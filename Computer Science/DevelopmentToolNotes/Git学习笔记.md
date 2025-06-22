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

 



## 7.Git命令总结整理

### 一、新建代码库

\# 在当前目录新建一个Git代码库

```
git init
```

\# 新建一个目录，将其初始化为Git代码库

```
git init [project-name] # 下载一个项目和它的整个代码历史
```

```
 git clone [url]
```

### 二、配置

\# 显示当前的Git配置

```
git config --list
```

\# 编辑Git配置文件

```
 git config -e [--global] # 设置提交代码时的用户信息
```

```
git config [--global] user.name "[name]"
git config [--global] user.email "[email address]"
```

### 三、增加/删除文件

```
 
# 添加指定文件到暂存区
git add [file1] [file2] ... # 添加指定目录到暂存区，包括子目录
git add [dir] # 添加当前目录的所有文件到暂存区
git add . # 添加每个变化前，都会要求确认 # 对于同一个文件的多处变化，可以实现分次提交
git add -p

# 删除工作区文件，并且将这次删除放入暂存区
git rm [file1] [file2] ... # 停止追踪指定文件，但该文件会保留在工作区
git rm --cached [file] # 改名文件，并且将这个改名放入暂存区
git mv [file-original] [file-renamed]
```

### 四、代码提交

提交暂存区到仓库区

```
git commit -m [message] # 提交暂存区的指定文件到仓库区
git commit [file1] [file2] ... -m [message] # 提交工作区自上次commit之后的变化，直接到仓库区
git commit -a
```

提交时显示所有diff信息

```
git commit -v
```

使用一次新的commit，替代上一次提交 # 如果代码没有任何新变化，则用来改写上一次commit的提交信息

```
git commit --amend -m [message] # 重做上一次commit，并包括指定文件的新变化
git commit --amend [file1] [file2] ...
```

### 五、分支

列出所有本地分支

```
git branch
```

列出所有远程分支

```
git branch -r
```

列出所有本地分支和远程分支

```
git branch -a
```

新建一个分支，但依然停留在当前分支

```
git branch [branch-name] # 新建一个分支，并切换到该分支
git checkout -b [branch] # 新建一个分支，指向指定commit
git branch [branch] [commit] # 新建一个分支，与指定的远程分支建立追踪关系
git branch --track [branch] [remote-branch] # 切换到指定分支，并更新工作区
git checkout [branch-name] # 切换到上一个分支
git checkout - # 建立追踪关系，在现有分支与指定的远程分支之间
git branch --set-upstream [branch] [remote-branch] # 合并指定分支到当前分支
git merge [branch] # 选择一个commit，合并进当前分支
git cherry-pick [commit] # 删除分支
git branch -d [branch-name] # 删除远程分支
git push origin --delete [branch-name]
git branch -dr [remote/branch]
```

### 六、标签

列出所有tag

```
git tag
```

新建一个tag在当前commit

```
git tag [tag] [commit] # 删除本地tag
git tag -d [tag] # 删除远程tag
git push origin :refs/tags/[tagName] # 查看tag信息
git show [tag] # 提交指定tag
git push [remote] --tags
```

新建一个分支，指向某个tag

```
git checkout -b [branch] [tag]
```



### 七、查看信息

显示有变更的文件

```
git status
```

显示当前分支的版本历史

```
git log
```

显示commit历史，以及每次commit发生变更的文件

```
git log --stat
```

搜索提交历史，根据关键词

```
git log -S [keyword] # 显示某个commit之后的所有变动，每个commit占据一行
git log [tag] HEAD --pretty=format:%s
```

显示某个commit之后的所有变动，其"提交说明"必须符合搜索条件

```
git log [tag] HEAD --grep feature
```

显示某个文件的版本历史，包括文件改名

```
git log --follow [file]
git whatchanged [file] # 显示指定文件相关的每一次diff
git log -5 --pretty --oneline
```

显示所有提交过的用户，按提交次数排序

```
git shortlog -sn
```

显示指定文件是什么人在什么时间修改过

```
git blame [file] # 显示暂存区和工作区的差异
git diff
```

显示暂存区和上一个commit的差异

```
git diff --cached [file] # 显示工作区与当前分支最新commit之间的差异
git diff HEAD
```

\# 显示两次提交之间的差异

```
git diff [first-branch]...[second-branch] # 显示今天你写了多少行代码
git diff --shortstat "@{0 day ago}" # 显示某次提交的元数据和内容变化
git show [commit] # 显示某次提交发生变化的文件
git show --name-only [commit] # 显示某次提交时，某个文件的内容
git show [commit]:[filename] # 显示当前分支的最近几次提交
git reflog
```



### 八、远程同步

下载远程仓库的所有变动

```
git fetch [remote] # 显示所有远程仓库
git remote -v
```

显示某个远程仓库的信息

```
git remote show [remote] # 增加一个新的远程仓库，并命名
git remote add [shortname] [url] # 取回远程仓库的变化，并与本地分支合并
git pull [remote] [branch] # 上传本地指定分支到远程仓库
git push [remote] --force
```

推送所有分支到远程仓库

```
git push [remote] --all
```



### 九、撤销

恢复暂存区的指定文件到工作区

```
git checkout [commit] [file] # 恢复暂存区的所有文件到工作区
git checkout . # 重置暂存区的指定文件，与上一次commit保持一致，但工作区不变
git reset [file] # 重置暂存区与工作区，与上一次commit保持一致
git reset --hard
```

重置当前分支的指针为指定commit，同时重置暂存区，但工作区不变

```
git reset [commit] # 重置当前分支的HEAD为指定commit，同时重置暂存区和工作区，与指定commit一致
git reset --hard [commit] # 重置当前HEAD为指定commit，但保持暂存区和工作区不变
git reset --keep [commit] # 新建一个commit，用来撤销指定commit # 后者的所有变化都将被前者抵消，并且应用到当前分支
git revert [commit] # 暂时将未提交的变化移除，稍后再移入
git stash
git stash pop
```
