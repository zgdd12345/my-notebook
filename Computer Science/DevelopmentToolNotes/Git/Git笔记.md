# Git简介
目前最好的分布式版本控制系统。

## 安装
可以在多个平台上使用。安装自行百度。

安装完成后需要在命令行输入如下命令：	

```plain
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
```

<font style="color:rgb(51, 51, 51);">因为Git是分布式版本控制系统，所以，每个机器都必须自报家门：你的名字和Email地址。你也许会担心，如果有人故意冒充别人怎么办？这个不必担心，首先我们相信大家都是善良无知的群众，其次，真的有冒充的也是有办法可查的。</font>

<font style="color:rgb(51, 51, 51);">注意</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git config</font><font style="color:rgb(51, 51, 51);">命令的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">--global</font><font style="color:rgb(51, 51, 51);">参数，用了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置，当然也可以对某个仓库指定不同的用户名和Email地址。</font>

## 使用
### 创建版本库（repository）：
<font style="color:rgb(51, 51, 51);">初始化一个Git仓库，使用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git init</font><font style="color:rgb(51, 51, 51);">命令。</font>

<font style="color:rgb(51, 51, 51);">添加文件到Git仓库，分两步：</font>

使用命令git add ，注意，可反复多次使用，添加多个文件；
使用命令git commit -m <message></font><font style="color:rgb(51, 51, 51);">，完成。</font>
### 常用命令：
git status命令：git status命令可以让我们时刻掌握仓库当前的状态，查看哪里被修改过。
git diff：顾名思义就是查看difference，显示的格式正是Unix通用的diff格式，
# 高级一些的功能
## 版本回退
### <font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git log</font><font style="color:rgb(51, 51, 51);">命令显示从最近到最远的提交日志。</font>
``` bash
commit e0ee909e2ec05a74f09c9e4f6c1c525bc21e7a47 (HEAD -> main)
Author: zgdd12345 <1315660867@qq.com>
Date:   Tue Jul 18 11:42:18 2023 +0800

    test py file

commit 841820bcf3a856fd9bae027ccc3e8e1faf6833bd
Author: zgdd12345 <1315660867@qq.com>
Date:   Tue Jul 18 11:32:11 2023 +0800

    test

commit 1bfcb1df5dbaaa9607676d78d134e34d91ae0dbc (origin/main, origin/HEAD)
Author: zgdd12345 <1315660867@qq.com>
Date:   Mon Jul 17 18:16:12 2023 +0800

    change readme

commit 7a1941321f27269904aeaa2b93e3bdff45a7c723
Author: zgdd12345 <73473084+zgdd12345@users.noreply.github.com>
Date:   Mon Jul 17 12:23:21 2023 +0800

    Initial commit
```

git log --pretty=oneline 简洁显示

``` bash
fsm@fengshimingdeMacBook-Pro quantum_7_17 % git log --pretty=oneline
e0ee909e2ec05a74f09c9e4f6c1c525bc21e7a47 (HEAD -> main) test py file
841820bcf3a856fd9bae027ccc3e8e1faf6833bd test
1bfcb1df5dbaaa9607676d78d134e34d91ae0dbc (origin/main, origin/HEAD) change readme
7a1941321f27269904aeaa2b93e3bdff45a7c723 Initial commit
```

上文中的大串乱码是commit id（版本号，十六进制）。

### <font style="color:rgb(51, 51, 51);">版本回退</font>
<font style="color:rgb(51, 51, 51);">在Git中，用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">HEAD</font><font style="color:rgb(51, 51, 51);">表示当前版本，上一个版本就是</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">HEAD^</font><font style="color:rgb(51, 51, 51);">，上上一个版本就是</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">HEAD^^</font><font style="color:rgb(51, 51, 51);">，当然往上100个版本写100个</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">^</font><font style="color:rgb(51, 51, 51);">比较容易数不过来，所以写成</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">HEAD~100</font><font style="color:rgb(51, 51, 51);">。</font>

`git reset --hard HEAD^`

回到刚刚的版本： 

`git reset --hard e0ee`

<font style="color:rgb(51, 51, 51);">只要上面的命令行窗口还没有被关掉，我们可以找到指定的版本号，版本号不用写全，git会自动去找。</font>

<font style="color:rgb(51, 51, 51);">注：git的版本回退速度非常快，因为git在内部有个指向当前版本的HEAD指针，当回退版本时，git仅仅是把指针指向指定版本。然后顺便把工作区的文件更新了。所以我们让HEAD指针指向哪个版本号，就把当前版本定位在哪。</font>

        1. <font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git reflog：记录每次的命令。</font>

```plain
fsm@fengshimingdeMacBook-Pro quantum_7_17 % git reflog
e0ee909 (HEAD -> main) HEAD@{0}: reset: moving to e0ee
841820b HEAD@{1}: reset: moving to HEAD^
e0ee909 (HEAD -> main) HEAD@{2}: commit: test py file
841820b HEAD@{3}: commit: test
1bfcb1d (origin/main, origin/HEAD) HEAD@{4}: commit: change readme
7a19413 HEAD@{5}: clone: from github.com:zgdd12345/quantum_7_17.git
```

### <font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">小结</font>
* HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令git reset --hard commit_id。
* 穿梭前，用git log可以查看提交历史，以便确定要回退到哪个版本。
* 要重返未来，用git reflog查看命令历史，以便确定要回到未来的哪个版本。

## 工作区和暂存区
参考源：[工作区与暂存区](https://www.liaoxuefeng.com/wiki/896043488029600/897271968352576)

**工作区（Working Directory）：** 在电脑中看到的目录。

**版本库（Repository）：** 工作区的隐藏目录.git，这个不算工作区，是Git的版本库。

**暂存区（Stage，或者叫index）：** 存放在Repository中。同时存放在Repository中的还有Git自动创建的第一个分支main/master。以及指向main的一个指针叫HEAD。

![](https://cdn.nlark.com/yuque/0/2023/png/29307286/1689671254859-edec7b9e-19aa-4131-b7ac-31afaf974d2d.png)

在上文中我们讲到将修改后的文件添加到Git版本库中的时候分两步执行：

+ 用git add 把文件添加进去，实际上是把文件修改添加到暂存区；
+ 使用git commit提交修改，将暂存区的所有内容提交到当前分支。

我们创建repository时， Git自动创建了目前唯一一个main分支，现在git commit就是往main分支上提交更改。

我们将需要提交到修改先提交到暂存区（stage），然后一次性提交暂存区的所有修改。

## 管理修改
Git跟踪管理的是修改而不是文件。

## 撤销修改
`git checkout -- file`<font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">命令可以丢弃工作区的修改。意思是把file在工作区的修改全部撤销，此处分两种情况：</font>

+ <font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">一种是file自修改后还未放到暂存区（stage），现在撤销修改就回到和版本库一样的状态；</font>
+ <font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">一种是修改已经提交到暂存区后，又进行了修改，现在撤销修改就回到添加到暂存区后到状态。</font>

总之，file将回到最近一次 `git commit或git add`时的状态。

<font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">注：git checkout -- file</font><font style="color:rgb(51, 51, 51);">命令中的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">--</font><font style="color:rgb(51, 51, 51);">很重要，没有</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">--</font><font style="color:rgb(51, 51, 51);">，就变成了“切换到另一个分支”的命令，我们在后面的分支管理中会再次遇到</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git checkout</font><font style="color:rgb(51, 51, 51);">命令。</font>
git reset HEAD <file></font><font style="color:rgb(51, 51, 51);">可以把暂存区的修改撤销掉（unstage），重新放回工作区。</font>
git reset命令既可以回退版本，也可以把暂存区的修改回退到工作区。当我们用HEAD时，表示最新的版本。

在修改已经提交到暂存区的情况下，我们先使用 git reset HEAD撤销暂存区的修改，重新放回工作区。然后使用git checkout -- file命令可以撤销工作区的修改。

## 删除文件
删除文件分两种情况：

+ 一种是确实需要删除版本库以及暂存区中的文件，<font style="color:rgb(51, 51, 51);">那就用命令</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git rm</font><font style="color:rgb(51, 51, 51);">删掉，并且</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git commit</font><font style="color:rgb(51, 51, 51);">；</font>
+ <font style="color:rgb(51, 51, 51);">一种是删错了，用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git checkout</font><font style="color:rgb(51, 51, 51);">还原版本库中的版本。即，使用版本库里面的版本替换工作区中的版本。</font>

注：<font style="color:rgb(51, 51, 51);">命令</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git rm</font><font style="color:rgb(51, 51, 51);">用于删除一个文件。如果一个文件已经被提交到版本库，那么你永远不用担心误删，但是要小心，你只能恢复文件到最新版本，你会丢失</font>**<font style="color:rgb(51, 51, 51);">最近一次提交后你修改的内容</font>**<font style="color:rgb(51, 51, 51);">。</font>

# 远程仓库（GitHub）
## 概述
Git是分布式版本控制系统，同一个Git仓库，可以分布到不同的机器上。
本地Git仓库和GitHub仓库之间的传输上通过SSH加密的，所以需要一些设置

+ 第一步：创建SSH Key。在用户的主目录下找.ssh目录，如果有，再看.ssh目录下有没有<font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">id_rsa</font><font style="color:rgb(51, 51, 51);">和</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">id_rsa.pub</font><font style="color:rgb(51, 51, 51);">这两个文件。若有，则跳到下一步，若无，打开Shell（Windows下打开Git Bash），创建SSH Key：</font>

```plain
$ ssh-keygen -t rsa -C "youremail@example.com"
```

	将邮件地址换成自己的邮件地址，然后一路回车，使用默认值即可，由于这个Key也不是用于军事目的，所以也无需设置密码。

<font style="color:rgb(51, 51, 51);">如果一切顺利的话，可以在用户主目录里找到</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.ssh</font><font style="color:rgb(51, 51, 51);">目录，里面有</font><u><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">id_rsa</font></u><u><font style="color:rgb(51, 51, 51);">和</font></u><u><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">id_rsa.pub</font></u><u><font style="color:rgb(51, 51, 51);">两个文件，这两个就是SSH Key的秘钥对，</font></u>**<u><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">id_rsa</font></u>****<u><font style="color:rgb(51, 51, 51);">是私钥</font></u>**<u><font style="color:rgb(51, 51, 51);">，不能泄露出去，</font></u>**<u><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">id_rsa.pub</font></u>****<u><font style="color:rgb(51, 51, 51);">是公钥</font></u>**<u><font style="color:rgb(51, 51, 51);">，可以放心地告诉任何人。</font></u>

+ <font style="color:rgb(51, 51, 51);"> 第二步：登陆GitHub，打开Account settings， SSH Keys页面：1）点击Add SSH Key，填上任意Title，在文本框内粘贴</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">id_rsa.pub的内容。点击Add Key，可以看到以及添加的Key。</font>

---

<font style="color:rgb(51, 51, 51);">为什么GitHub需要SSH Key呢？因为GitHub需要识别出你推送的提交确实是你推送的，而不是别人冒充的，而Git支持SSH协议，所以，GitHub只要知道了你的公钥，就可以确认只有你自己才能推送。</font>

<font style="color:rgb(51, 51, 51);">当然，GitHub允许你添加多个Key。假定你有若干电脑，你一会儿在公司提交，一会儿在家里提交，只要把每台电脑的Key都添加到GitHub，就可以在每台电脑上往GitHub推送了。</font>

## <font style="color:rgb(51, 51, 51);">添加远程库</font>
+ 新建远程仓库（GitHub）。
+ 关联远程库：	

```plain
git remote add origin git@github.com:michaelliao/learngit.git
```

<font style="color:rgb(51, 51, 51);">添加后，远程库的名字就是</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">origin</font><font style="color:rgb(51, 51, 51);">，这是Git默认的叫法，也可以改成别的，但是</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">origin</font><font style="color:rgb(51, 51, 51);">这个名字一看就知道是远程库。</font>

+ 本地内容推送到远程：<font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git push</font><font style="color:rgb(51, 51, 51);">命令，实际上是把当前分支</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">main</font><font style="color:rgb(51, 51, 51);">推送到远程。</font>

```plain
git push -u origin main
```

由于远程库是空的，所以第一次推送main分支时加上了-u参数，Git不但会把本地的main分支内容推送到远程新的main分支，还会把本地的main分支和远程的main分支关联起来，在以后的推送或拉取时就可以简化命令。

现在只用本地提交，就可以通过命令：

```plain
git push origin main
```

把本地main分支的最新修改推送至GitHub。

+ **删除远程库：**添加的时候地址写错了，或者单纯的想删除远程库，可以使用**git remote rm <name>**命令。使用前，先用**git remote -v**查看远程库信息：

注：此处的“删除”其实是解除了本地和远程的绑定关系，并不是物理上删除了远程库。远程库本身并没有任何改动。要真正删除远程库，需要登录到GitHub，在后台页面找到删除按钮再删除。



小结：
1.要关联一个远程库，使用命令git remote add origin git@server-name:path/repo-name.git
2.关联一个远程库时必须给远程库指定一个名字，origin是默认习惯命名；
3.关联后，使用命令git push -u origin master>第一次推送master分支的所有内容；
4.此后，每次本地提交后，只要有必要，就可以使用命令git push origin master推送最新修改；
5.分布式版本系统的最大好处之一是在本地工作完全不需要考虑远程库的存在，也就是有没有联网都可以正常工作，而SVN在没有联网的时候是拒绝干活的！当有网络的时候，再把本地提交推送一下就完成了同步

## 从远程库克隆
+ 在GitHub创建一个新库。
+ </font> 用命令  <font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git clone</font>克隆一个本地库

```plain
git clone git@github.com:michaelliao/gitskills.git
```

<font style="color:rgb(51, 51, 51);">注：</font>

<font style="color:rgb(51, 51, 51);">1）GitHub给出的地址不止一个，还可以用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">https://github.com/michaelliao/gitskills.git</font><font style="color:rgb(51, 51, 51);">这样的地址。实际上，Git支持多种协议，默认的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git://</font><font style="color:rgb(51, 51, 51);">使用ssh，但也可以使用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">https</font><font style="color:rgb(51, 51, 51);">等其他协议。</font>

<font style="color:rgb(51, 51, 51);">2）使用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">https</font><font style="color:rgb(51, 51, 51);">除了速度慢以外，还有个最大的麻烦是每次推送都必须输入口令，但是在某些只开放http端口的公司内部就无法使用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">ssh</font><font style="color:rgb(51, 51, 51);">协议而只能用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">https</font><font style="color:rgb(51, 51, 51);">。</font>



# Branch管理
## 创建与合并分支
### 分析理解
<font style="color:rgb(51, 51, 51);">在上文中，我们知道，每次提交，Git都把它们串成一条时间线，这条时间线就是一个</font>**<font style="color:rgb(51, 51, 51);">分支</font>**<font style="color:rgb(51, 51, 51);">。截止到目前，只有一条时间线，在Git里，这个分支叫主分支，即</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">分支。</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">HEAD</font><font style="color:rgb(51, 51, 51);">严格来说不是指向提交，而是指向</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">，</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">才是指向提交的，所以，</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">HEAD</font><font style="color:rgb(51, 51, 51);">指向的就是当前分支。</font>

<font style="color:rgb(51, 51, 51);">一开始的时候，</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">分支是一条线，Git用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">指向最新的提交，再用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">HEAD</font><font style="color:rgb(51, 51, 51);">指向</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">，就能确定当前分支，以及当前分支的提交点：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/29307286/1689756594952-148d052d-c0d0-42f1-a34b-3d205a961b1c.png)

<font style="color:rgb(51, 51, 51);">每次提交，</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">分支都会向前移动一步，这样，随着你不断提交，</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">分支的线也越来越长。</font>

<font style="color:rgb(51, 51, 51);">当我们创建新的分支，例如</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">时，Git新建了一个指针叫</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">，指向</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">相同的提交，再把</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">HEAD</font><font style="color:rgb(51, 51, 51);">指向</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">，就表示当前分支在</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">上：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/29307286/1689756673530-d221f445-429e-4d86-ac7c-258b0a62e152.png)

<font style="color:rgb(51, 51, 51);">Git创建一个分支</font>**<font style="color:rgb(51, 51, 51);">很快</font>**<font style="color:rgb(51, 51, 51);">，因为除了增加一个</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">指针，改改</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">HEAD</font><font style="color:rgb(51, 51, 51);">的指向，工作区的文件都没有任何变化！不过，从现在开始，对工作区的修改和提交就是针对</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支了，比如新提交一次后，</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">指针往前移动一步，而</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">指针不变：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/29307286/1689756787694-0715dfe9-bf77-4351-b462-18c6b4fcc142.png)

<font style="color:rgb(51, 51, 51);">假如我们在</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">上的工作完成了，就可以把</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">合并到</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">上。Git怎么合并呢？最简单的方法，就是直接把</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">指向</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">的当前提交，就完成了合并：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/29307286/1689756877489-e49e9ba8-e174-4580-b806-0232209b642f.png)

<font style="color:rgb(51, 51, 51);">所以Git合并分支也很快！就改改指针，工作区内容也不变！</font>

<font style="color:rgb(51, 51, 51);">合并完分支后，甚至可以删除</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支。删除</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支就是把</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">指针给删掉，删掉后，我们就剩下了一条</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">分支：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/29307286/1689756954061-e2201116-8622-44dd-b67c-85dc3cd9b880.png)

### 实验
+ 首先创建dev分支并切换到dev分支。

```plain
git checkout -b dev
```

<font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git checkout</font><font style="color:rgb(51, 51, 51);">命令加上</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">-b</font><font style="color:rgb(51, 51, 51);">参数表示创建并切换，相当于以下两条命令：</font>

```plain
git branch dev
git checkout dev
```

<font style="color:rgb(51, 51, 51);">然后，用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git branch</font><font style="color:rgb(51, 51, 51);">命令查看当前分支:</font>

```plain
$ git branch
* dev
  master
```

<font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git branch</font><font style="color:rgb(51, 51, 51);">命令会列出所有分支，当前分支前面会标一个</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">*</font><font style="color:rgb(51, 51, 51);">号。然后，我们就可以在</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支上正常提交。</font>

<font style="color:rgb(51, 51, 51);"></font>

+ 查看当前分支：<font style="color:rgb(51, 51, 51);">用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git branch</font><font style="color:rgb(51, 51, 51);">命令查看当前分支:</font>

```plain
$ git branch
* dev
  master
```

<font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git branch</font><font style="color:rgb(51, 51, 51);">命令会列出所有分支，当前分支前面会标一个</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">*</font><font style="color:rgb(51, 51, 51);">号。然后，我们就可以在</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支上正常提交。</font>

+ 提交
+ 切换回main分支

```plain
git checkout master
```

<font style="color:rgb(51, 51, 51);">切换回</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">分支后，再查看一个</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">readme.txt</font><font style="color:rgb(51, 51, 51);">文件，刚才添加的内容不见了！因为那个提交是在</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支上，而</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">分支此刻的提交点并没有变：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/29307286/1689758255011-71d91fec-0c89-4108-addf-9266cedfeab4.png)

+ 将dev分支的内容合并到main分支

```plain
git merge dev
```

<font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git merge</font><font style="color:rgb(51, 51, 51);">命令用于合并指定分支到当前分支。合并后，再查看</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">readme.txt</font><font style="color:rgb(51, 51, 51);">的内容，就可以看到，和</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支的最新提交是完全一样的。</font>

<font style="color:rgb(51, 51, 51);">注意</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">Fast-forward</font><font style="color:rgb(51, 51, 51);">信息，Git告诉我们，这次合并是“快进模式”，也就是直接把</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">指向</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">的当前提交，所以合并速度非常快。当然，也不是每次合并都能</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">Fast-forward</font><font style="color:rgb(51, 51, 51);">，我们后面会讲其他方式的合并。</font>

<font style="color:rgb(51, 51, 51);">合并完成后，就可以放心地删除</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支了：</font>

```plain
$ git branch -d dev
Deleted branch dev (was b17d20e).
```

删除后，只剩main分支。

<font style="color:rgb(51, 51, 51);">因为创建、合并和删除分支非常快，所以Git鼓励你使用分支完成某个任务，合并后再删掉分支，这和直接在</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">分支上工作效果是一样的，但过程更安全。</font>

+ switch操作

我们在上面切换分支使用<font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git checkout <branch>，</font><font style="color:rgb(51, 51, 51);">而前面讲过的撤销修改则是</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git checkout -- <file></font><font style="color:rgb(51, 51, 51);">，同一个命令，有两种作用，确实有点令人迷惑。实际上，切换分支这个动作，用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">switch</font><font style="color:rgb(51, 51, 51);">更科学。因此，最新版本的Git提供了新的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git switch</font><font style="color:rgb(51, 51, 51);">命令来切换分支，创建并切换到新的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支，可以使用：</font>

```plain
git switch -c dev
```

<font style="color:rgb(51, 51, 51);">直接切换到已有的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">分支，可以使用：</font>

```plain
git switch master
```

<font style="color:rgb(51, 51, 51);">使用新的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git switch</font><font style="color:rgb(51, 51, 51);">命令，比</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git checkout</font><font style="color:rgb(51, 51, 51);">要更容易理解。</font>

### <font style="color:rgb(68, 68, 68);">小结</font>
<font style="color:rgb(51, 51, 51);">Git鼓励大量使用分支：</font>

<font style="color:rgb(51, 51, 51);">查看分支：</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git branch</font>

<font style="color:rgb(51, 51, 51);">创建分支：</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git branch <name></font>

<font style="color:rgb(51, 51, 51);">切换分支：</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git checkout <name></font><font style="color:rgb(51, 51, 51);">或者</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git switch <name></font>

<font style="color:rgb(51, 51, 51);">创建+切换分支：</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git checkout -b <name></font><font style="color:rgb(51, 51, 51);">或者</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git switch -c <name></font>

<font style="color:rgb(51, 51, 51);">合并某分支到当前分支：</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git merge <name></font>

<font style="color:rgb(51, 51, 51);">删除分支：</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git branch -d <name></font>

## 解决冲突
两个分支同一个文件都被修改之后，Git无法执行快速合并，这样就可能有冲突。

```plain
git merge feature1
```

可以用git status查看冲突文件。

<font style="color:rgb(51, 51, 51);">我们可以直接查看readme.txt的内容：</font>

```plain
Git is a distributed version control system.
Git is free software distributed under the GPL.
Git has a mutable index called stage.
Git tracks changes of files.
<<<<<<< HEAD
Creating a new branch is quick & simple.
=======
Creating a new branch is quick AND simple.
>>>>>>> feature1
```

<font style="color:rgb(51, 51, 51);">Git用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);"><<<<<<<</font><font style="color:rgb(51, 51, 51);">，</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">=======</font><font style="color:rgb(51, 51, 51);">，</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">>>>>>>></font><font style="color:rgb(51, 51, 51);">标记出不同分支的内容，我们修改如下后保存：</font>

```plain
Creating a new branch is quick and simple.
```

<font style="color:rgb(51, 51, 51);">再提交：</font>

```plain
$ git add readme.txt 
$ git commit -m "conflict fixed"
[master cf810e4] conflict fixed
```

<font style="color:rgb(51, 51, 51);">用带参数的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git log</font><font style="color:rgb(51, 51, 51);">也可以看到分支的合并情况：</font>

```plain
$ git log --graph --pretty=oneline --abbrev-commit
*   cf810e4 (HEAD -> master) conflict fixed
|\  
| * 14096d0 (feature1) AND simple
* | 5dc6824 & simple
|/  
* b17d20e branch test
* d46f35e (origin/master) remove test.txt
* b84166e add test.txt
* 519219b git tracks changes
* e43a48b understand how stage works
* 1094adb append GPL
* e475afc add distributed
* eaadf4e wrote a readme file
```

<font style="color:rgb(51, 51, 51);">最后，删除</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">feature1</font><font style="color:rgb(51, 51, 51);">分支：</font>

```plain
$ git branch -d feature1
Deleted branch feature1 (was 14096d0).
```

小结：

<font style="color:rgb(51, 51, 51);">当Git无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成。</font>

<font style="color:rgb(51, 51, 51);">解决冲突就是把Git合并失败的文件手动编辑为我们希望的内容，再提交。</font>

<font style="color:rgb(51, 51, 51);">用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git log --graph</font><font style="color:rgb(51, 51, 51);">命令可以看到分支合并图。</font>

## 分支管理策略
<font style="color:rgb(51, 51, 51);">通常，合并分支时，如果可能，Git会用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">Fast forward</font><font style="color:rgb(51, 51, 51);">模式，但这种模式下，删除分支后，会丢掉分支信息。</font>

<font style="color:rgb(51, 51, 51);">如果要强制禁用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">Fast forward</font><font style="color:rgb(51, 51, 51);">模式，Git就会在merge时生成一个新的commit，这样，从分支历史上就可以看出分支信息。</font>

<font style="color:rgb(51, 51, 51);">下面我们实战一下</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">--no-ff</font><font style="color:rgb(51, 51, 51);">方式的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git merge</font><font style="color:rgb(51, 51, 51);">：</font>

**<font style="color:rgb(51, 51, 51);">实验前准备：</font>**

<font style="color:rgb(51, 51, 51);">首先，仍然创建并切换</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支：</font>

```plain
$ git switch -c dev
Switched to a new branch 'dev'
```

<font style="color:rgb(51, 51, 51);">修改readme.txt文件，并提交一个新的commit：</font>

<font style="color:rgb(51, 51, 51);">切换回main分支</font>

### 实验
<font style="color:rgb(51, 51, 51);">准备合并</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支，请注意</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">--no-ff</font><font style="color:rgb(51, 51, 51);">参数，表示禁用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">Fast forward</font><font style="color:rgb(51, 51, 51);">：</font>

```plain
$ git merge --no-ff -m "merge with no-ff" dev
Merge made by the 'recursive' strategy.
 readme.txt | 1 +
 1 file changed, 1 insertion(+)
```

<font style="color:rgb(51, 51, 51);">因为本次合并要创建一个新的commit，所以加上</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">-m</font><font style="color:rgb(51, 51, 51);">参数，把commit描述写进去。</font>

<font style="color:rgb(51, 51, 51);">合并后，我们用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git log</font><font style="color:rgb(51, 51, 51);">看看分支历史：</font>

```plain
$ git log --graph --pretty=oneline --abbrev-commit
*   e1e9c68 (HEAD -> master) merge with no-ff
|\  
| * f52c633 (dev) add merge
|/  
*   cf810e4 conflict fixed
...
```

<font style="color:rgb(51, 51, 51);">可以看到，不使用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">Fast forward</font><font style="color:rgb(51, 51, 51);">模式，merge后就像这样：</font>

### 分支策略：
<font style="color:rgb(51, 51, 51);">在实际开发中，我们应该按照几个基本原则进行分支管理：</font>

+ <font style="color:rgb(51, 51, 51);">首先，</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">分支应该是非常稳定的，也就是仅用来发布新版本，平时不能在上面干活；</font>
+ <font style="color:rgb(51, 51, 51);">那在哪干活呢？干活都在</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支上，也就是说，</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支是不稳定的，到某个时候，比如1.0版本发布时，再把</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支合并到</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">上，在</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">分支发布1.0版本；</font>
+ <font style="color:rgb(51, 51, 51);">你和你的小伙伴们每个人都在</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支上干活，每个人都有自己的分支，时不时地往</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支上合并就可以了。</font>

<font style="color:rgb(51, 51, 51);">所以，团队合作的分支看起来就像这样：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/29307286/1689823682190-b15cdb94-01ee-48e6-b281-ca5f818e80f9.png)

### 小结
<font style="color:rgb(51, 51, 51);">Git分支十分强大，在团队开发中应该充分应用。</font>

<font style="color:rgb(51, 51, 51);">合并分支时，加上</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">--no-ff</font><font style="color:rgb(51, 51, 51);">参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">fast forward</font><font style="color:rgb(51, 51, 51);">合并就看不出来曾经做过合并。</font>

## Bug分支
使用临时分支修复bug，修复后合并分支，再删除临时分支可以有效提升开发效率。

### stash功能
<font style="color:rgb(51, 51, 51);">Git还提供了一个</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">stash</font><font style="color:rgb(51, 51, 51);">功能，可以把当前工作现场“储藏”起来，等以后恢复现场后继续工作：</font>

```plain
$ git stash
Saved working directory and index state WIP on dev: f52c633 add merge
```

<font style="color:rgb(51, 51, 51);">用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git stash list</font><font style="color:rgb(51, 51, 51);">命令查看保存到现场：</font>

```plain
$ git stash list
stash@{0}: WIP on dev: f52c633 add merge
```

<font style="color:rgb(51, 51, 51);">工作现场还在，Git把stash内容存在某个地方了，但是需要恢复一下，有两个办法：</font>

    - <font style="color:rgb(51, 51, 51);">一是用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git stash apply</font><font style="color:rgb(51, 51, 51);">恢复，但是恢复后，stash内容并不删除，你需要用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git stash drop</font><font style="color:rgb(51, 51, 51);">来删除；</font>
    - <font style="color:rgb(51, 51, 51);">另一种方式是用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git stash pop</font><font style="color:rgb(51, 51, 51);">，恢复的同时把stash内容也删了：</font>

```plain
$ git stash pop
On branch dev
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   hello.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   readme.txt

Dropped refs/stash@{0} (5d677e2ee266f39ea296182fb2354265b91b3b2a)
```

### bug分支
+ 保存现场；
+ 创建bug分支；
+ 修复bug然后提交；
+ 切换到main分支、合并、删除bug分支；
+ 恢复现场。



### 复制特定提交到当前分支
main分支存在bug，dev分支当然也有bug。重新修改一遍过于繁琐，下文讲述快捷操作。

<font style="color:rgb(51, 51, 51);">为了方便操作，Git专门提供了一个</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">cherry-pick</font><font style="color:rgb(51, 51, 51);">命令，让我们能复制一个特定的提交到当前分支：</font>

```plain
$ git branch
* dev
  master
$ git cherry-pick 4c805e2
[master 1d4b803] fix bug 101
 1 file changed, 1 insertion(+), 1 deletion(-)
```

<font style="color:rgb(51, 51, 51);">Git自动给dev分支做了一次提交，注意这次提交的commit是</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">1d4b803</font><font style="color:rgb(51, 51, 51);">，它并不同于master的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">4c805e2</font><font style="color:rgb(51, 51, 51);">，因为这两个commit只是改动相同，但确实是两个不同的commit。用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git cherry-pick</font><font style="color:rgb(51, 51, 51);">，我们就不需要在dev分支上手动再把修bug的过程重复一遍。</font>

### 小结
+ 我们通过新建bug分支修复bug
+ 现有工作未完成时，git stash现场工作，再去修复bug，修复完git stash pop回到工作现场。
+ <font style="color:rgb(51, 51, 51);">在master分支上修复的bug，想要合并到当前dev分支，可以用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git cherry-pick <commit></font><font style="color:rgb(51, 51, 51);">命令，把bug提交的修改“复制”到当前分支，避免重复劳动。</font>

## Feature分支
添加新功能时，使用**Feature分支**可以避免实验性质的代码搞乱主分支。

正常新建分支、开发、合并、删除分支。

删除分支：

未合并的分支强行删除会被Git警告。需要使用下述命令：

```plain
git branch -D feature-vulcan
```

## 多人协作
### 远程仓库信息
<font style="color:rgb(51, 51, 51);">当你从远程仓库克隆时，实际上Git自动把本地的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">分支和远程的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">分支对应起来了，并且，远程仓库的默认名称是</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">origin</font><font style="color:rgb(51, 51, 51);">。</font>

<font style="color:rgb(51, 51, 51);">要查看远程库的信息，用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git remote</font><font style="color:rgb(51, 51, 51);">：</font>

```plain
$ git remote
origin
```

<font style="color:rgb(51, 51, 51);">或者，用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git remote -v</font><font style="color:rgb(51, 51, 51);">显示更详细的信息：</font>

```plain
$ git remote -v
origin  git@github.com:michaelliao/learngit.git (fetch)
origin  git@github.com:michaelliao/learngit.git (push)
```

<font style="color:rgb(51, 51, 51);">上面显示了可以抓取和推送的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">origin</font><font style="color:rgb(51, 51, 51);">的地址。如果没有推送权限，就看不到push的地址。</font>



### 推送分支
<font style="color:rgb(51, 51, 51);">推送分支，就是把该分支上的所有本地提交推送到远程库。推送时，要指定本地分支，这样，Git就会把该分支推送到远程库对应的远程分支上：</font>

```plain
$ git push origin master
```

<font style="color:rgb(51, 51, 51);">如果要推送其他分支，比如</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">，就改成：</font>

```plain
$ git push origin dev
```

<font style="color:rgb(51, 51, 51);">但是，并不是一定要把本地分支往远程推送，那么，哪些分支需要推送，哪些不需要呢？</font>

+ **<font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font>****<font style="color:rgb(51, 51, 51);">分支是主分支，因此要时刻与远程同步；</font>**
+ **<font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font>****<font style="color:rgb(51, 51, 51);">分支是开发分支，团队所有成员都需要在上面工作，所以也需要与远程同步；</font>**
+ <font style="color:rgb(51, 51, 51);">bug分支只用于在本地修复bug，就没必要推到远程了，除非老板要看看你每周到底修复了几个bug；</font>
+ <font style="color:rgb(51, 51, 51);">feature分支是否推到远程，取决于你是否和你的小伙伴合作在上面开发。</font>

<font style="color:rgb(51, 51, 51);">总之，就是在Git中，分支完全可以在本地自己藏着玩，是否推送，视你的心情而定！</font>

### 抓取分支
<font style="color:rgb(51, 51, 51);">当新的合作者从远程库clone时，默认情况下，他只能看到本地的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">master</font><font style="color:rgb(51, 51, 51);">分支。要在</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支上开发，就必须创建远程</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">origin</font><font style="color:rgb(51, 51, 51);">的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支到本地，于是他用这个命令创建本地</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支：</font>

```plain
$ git checkout -b dev origin/dev
```

<font style="color:rgb(51, 51, 51);">现在，他就可以在</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">上继续修改，然后，时不时地把</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">push</font><font style="color:rgb(51, 51, 51);">到远程。</font>

<font style="color:rgb(51, 51, 51);">小伙伴已经向</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">origin/dev</font><font style="color:rgb(51, 51, 51);">分支推送了他的提交，而碰巧你也对同样的文件作了修改，并试图推送。推送失败，因为你的小伙伴的最新提交和你试图推送的提交有冲突，解决办法也很简单，Git已经提示我们，先用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git pull</font><font style="color:rgb(51, 51, 51);">把最新的提交从</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">origin/dev</font><font style="color:rgb(51, 51, 51);">抓下来，然后，在本地合并，解决冲突，再推送：</font>

```plain
$ git pull
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> dev
```

<font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git pull</font><font style="color:rgb(51, 51, 51);">也失败了，原因是没有指定本地</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">分支与远程</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">origin/dev</font><font style="color:rgb(51, 51, 51);">分支的链接，根据提示，设置</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dev</font><font style="color:rgb(51, 51, 51);">和</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">origin/dev</font><font style="color:rgb(51, 51, 51);">的链接：</font>

```plain
$ git branch --set-upstream-to=origin/dev dev
Branch 'dev' set up to track remote branch 'dev' from 'origin'.
```

<font style="color:rgb(51, 51, 51);">再pull：</font>

```plain
$ git pull
Auto-merging env.txt
CONFLICT (add/add): Merge conflict in env.txt
Automatic merge failed; fix conflicts and then commit the result.
```

<font style="color:rgb(51, 51, 51);">这回</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git pull</font><font style="color:rgb(51, 51, 51);">成功，但是合并有冲突，需要手动解决，解决的方法和分支管理中的</font>[解决冲突](http://www.liaoxuefeng.com/wiki/896043488029600/900004111093344)<font style="color:rgb(51, 51, 51);">完全一样。解决后，提交，再push：</font>

```plain
$ git commit -m "fix env conflict"
[dev 57c53ab] fix env conflict

$ git push origin dev
Counting objects: 6, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 621 bytes | 621.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To github.com:michaelliao/learngit.git
   7a5e5dd..57c53ab  dev -> dev
```

### 多人协作流程
1. <font style="color:rgb(51, 51, 51);">首先，可以试图用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git push origin <branch-name></font><font style="color:rgb(51, 51, 51);">推送自己的修改；</font>
2. <font style="color:rgb(51, 51, 51);">如果推送失败，则因为远程分支比你的本地更新，需要先用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git pull</font><font style="color:rgb(51, 51, 51);">试图合并；</font>
3. <font style="color:rgb(51, 51, 51);">如果合并有冲突，则解决冲突，并在本地提交；</font>
4. <font style="color:rgb(51, 51, 51);">没有冲突或者解决掉冲突后，再用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git push origin <branch-name></font><font style="color:rgb(51, 51, 51);">推送就能成功！</font>

<font style="color:rgb(51, 51, 51);">如果</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git pull</font><font style="color:rgb(51, 51, 51);">提示</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">no tracking information</font><font style="color:rgb(51, 51, 51);">，则说明本地分支和远程分支的链接关系没有创建，用命令</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git branch --set-upstream-to <branch-name> origin/<branch-name></font><font style="color:rgb(51, 51, 51);">。</font>

### 小结
+ <font style="color:rgb(51, 51, 51);">查看远程库信息，使用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git remote -v</font><font style="color:rgb(51, 51, 51);">；</font>
+ <font style="color:rgb(51, 51, 51);">本地新建的分支如果不推送到远程，对其他人就是不可见的；</font>
+ <font style="color:rgb(51, 51, 51);">从本地推送分支，使用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git push origin branch-name</font><font style="color:rgb(51, 51, 51);">，如果推送失败，先用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git pull</font><font style="color:rgb(51, 51, 51);">抓取远程的新提交；</font>
+ <font style="color:rgb(51, 51, 51);">在本地创建和远程分支对应的分支，使用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git checkout -b branch-name origin/branch-name</font><font style="color:rgb(51, 51, 51);">，本地和远程分支的名称最好一致；</font>
+ <font style="color:rgb(51, 51, 51);">建立本地分支和远程分支的关联，使用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git branch --set-upstream branch-name origin/branch-name</font><font style="color:rgb(51, 51, 51);">；</font>
+ <font style="color:rgb(51, 51, 51);">从远程抓取分支，使用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git pull</font><font style="color:rgb(51, 51, 51);">，如果有冲突，要先处理冲突。</font>

## Rebase
将提交历史变成干净的一条线。<font style="color:rgb(51, 51, 51);"></font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git rebase命令</font>

```plain
$ git rebase
First, rewinding head to replay your work on top of it...
Applying: add comment
Using index info to reconstruct a base tree...
M	hello.py
Falling back to patching base and 3-way merge...
Auto-merging hello.py
Applying: add author
Using index info to reconstruct a base tree...
M	hello.py
Falling back to patching base and 3-way merge...
Auto-merging hello.py
```

<font style="color:rgb(51, 51, 51);">输出了一大堆操作，到底是啥效果？再用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git log</font><font style="color:rgb(51, 51, 51);">看看：</font>

```plain
$ git log --graph --pretty=oneline --abbrev-commit
* 7e61ed4 (HEAD -> master) add author
* 3611cfe add comment
* f005ed4 (origin/master) set exit=1
* d1be385 init hello
...
```

<font style="color:rgb(51, 51, 51);">原本分叉的提交现在变成一条直线了！这种神奇的操作是怎么实现的？其实原理非常简单。我们注意观察，发现Git把我们本地的提交“挪动”了位置，放到了</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">f005ed4 (origin/master) set exit=1</font><font style="color:rgb(51, 51, 51);">之后，这样，整个提交历史就成了一条直线。rebase操作前后，最终的提交内容是一致的，但是，我们本地的commit修改内容已经变化了，它们的修改不再基于</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">d1be385 init hello</font><font style="color:rgb(51, 51, 51);">，而是基于</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">f005ed4 (origin/master) set exit=1</font><font style="color:rgb(51, 51, 51);">，但最后的提交</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">7e61ed4</font><font style="color:rgb(51, 51, 51);">内容是一致的。</font>

<font style="color:rgb(51, 51, 51);">这就是rebase操作的特点：把分叉的提交历史“整理”成一条直线，看上去更直观。</font>

# 标签管理
<font style="color:rgb(51, 51, 51);">发布一个版本时，我们通常先在版本库中打一个</font>**<font style="color:rgb(51, 51, 51);">标签（tag）</font>**<font style="color:rgb(51, 51, 51);">，这样，就唯一确定了打标签时刻的版本。将来无论什么时候，取某个标签的版本，就是把那个打标签的时刻的历史版本取出来。所以，标签也是版本库的一个快照。</font>

<font style="color:rgb(51, 51, 51);">Git的标签虽然是版本库的快照，但其实它就是指向某个commit的指针（跟分支很像对不对？但是分支可以移动，标签不能移动），所以，创建和删除标签都是瞬间完成的。</font>

<font style="color:rgb(51, 51, 51);">Git有commit，为什么还要引入tag？</font>

<font style="color:rgb(51, 51, 51);">“请把上周一的那个版本打包发布，commit号是6a5819e...”</font>

<font style="color:rgb(51, 51, 51);">“一串乱七八糟的数字不好找！”</font>

<font style="color:rgb(51, 51, 51);">如果换一个办法：</font>

<font style="color:rgb(51, 51, 51);">“请把上周一的那个版本打包发布，版本号是v1.2”</font>

<font style="color:rgb(51, 51, 51);">“好的，按照tag v1.2查找commit就行！”</font>

<font style="color:rgb(51, 51, 51);">所以，tag就是一个让人容易记住的有意义的名字，它跟某个commit绑在一起。</font>

## <font style="color:rgb(51, 51, 51);">创建标签</font>
<font style="color:rgb(51, 51, 51);">在Git中打标签非常简单，首先，切换到需要打标签的分支上：</font>

```plain
$ git branch
* dev
  master
$ git checkout master
Switched to branch 'master'
```

<font style="color:rgb(51, 51, 51);">然后，敲命令</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git tag <name></font><font style="color:rgb(51, 51, 51);">就可以打一个新标签：</font>

```plain
$ git tag v1.0
```

<font style="color:rgb(51, 51, 51);">可以用命令</font><code style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git tag</code><font style="color:rgb(51, 51, 51);">查看所有标签：</font>

```plain
$ git tag
v1.0
```

<font style="color:rgb(51, 51, 51);">默认标签是打在最新提交的commit上的。有时候，如果忘了打标签，比如，现在已经是周五了，但应该在周一打的标签没有打，怎么办？方法是找到历史提交的commit id，然后打上就可以了。</font>

```plain
$ git log --pretty=oneline --abbrev-commit
12a631b (HEAD -> master, tag: v1.0, origin/master) merged bug fix 101
4c805e2 fix bug 101
e1e9c68 merge with no-ff
f52c633 add merge
cf810e4 conflict fixed
5dc6824 & simple
14096d0 AND simple
b17d20e branch test
d46f35e remove test.txt
b84166e add test.txt
519219b git tracks changes
e43a48b understand how stage works
1094adb append GPL
e475afc add distributed
eaadf4e wrote a readme file
```

<font style="color:rgb(51, 51, 51);">比方说要对</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">add merge</font><font style="color:rgb(51, 51, 51);">这次提交打标签，它对应的commit id是</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">f52c633</font><font style="color:rgb(51, 51, 51);">，敲入命令：</font>

```plain
$ git tag v0.9 f52c633
```

<font style="color:rgb(51, 51, 51);">再用命令</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git tag</font><font style="color:rgb(51, 51, 51);">查看标签：	</font>

```plain
$ git tag
v0.9
v1.0
```

<font style="color:rgb(51, 51, 51);">注意，标签不是按时间顺序列出，而是按字母排序的。可以用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git show <tagname></font><font style="color:rgb(51, 51, 51);">查看标签信息：</font>

```plain
$ git show v0.9
commit f52c63349bc3c1593499807e5c8e972b82c8f286 (tag: v0.9)
Author: Michael Liao <askxuefeng@gmail.com>
Date:   Fri May 18 21:56:54 2018 +0800

    add merge

diff --git a/readme.txt b/readme.txt
...
```

<font style="color:rgb(51, 51, 51);">可以看到，</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">v0.9</font><font style="color:rgb(51, 51, 51);">确实打在</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">add merge</font><font style="color:rgb(51, 51, 51);">这次提交上。</font>

<font style="color:rgb(51, 51, 51);">还可以创建带有说明的标签，用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">-a</font><font style="color:rgb(51, 51, 51);">指定标签名，</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">-m</font><font style="color:rgb(51, 51, 51);">指定说明文字：</font>

```plain
$ git tag -a v0.1 -m "version 0.1 released" 1094adb
```

<font style="color:rgb(51, 51, 51);">用命令</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git show <tagname></font><font style="color:rgb(51, 51, 51);">可以看到说明文字：</font>

```plain
$ git show v0.1
tag v0.1
Tagger: Michael Liao <askxuefeng@gmail.com>
Date:   Fri May 18 22:48:43 2018 +0800

version 0.1 released

commit 1094adb7b9b3807259d8cb349e7df1d4d6477073 (tag: v0.1)
Author: Michael Liao <askxuefeng@gmail.com>
Date:   Fri May 18 21:06:15 2018 +0800

    append GPL

diff --git a/readme.txt b/readme.txt
...
```

<font style="color:rgb(216, 80, 48);background-color:rgb(255, 241, 240);">注意：标签总是和某个commit挂钩。如果这个commit既出现在master分支，又出现在dev分支，那么在这两个分支上都可以看到这个标签。</font>

<font style="color:rgb(68, 68, 68);">小结：</font>

+ <font style="color:rgb(51, 51, 51);">命令</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git tag <tagname></font><font style="color:rgb(51, 51, 51);">用于新建一个标签，默认为</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">HEAD</font><font style="color:rgb(51, 51, 51);">，也可以指定一个commit id；</font>
+ <font style="color:rgb(51, 51, 51);">命令</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git tag -a <tagname> -m "blablabla..."</font><font style="color:rgb(51, 51, 51);">可以指定标签信息；</font>
+ <font style="color:rgb(51, 51, 51);">命令</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git tag</font><font style="color:rgb(51, 51, 51);">可以查看所有标签。</font>

## 操作标签
<font style="color:rgb(51, 51, 51);">如果标签打错了，也可以删除：</font>

```plain
$ git tag -d v0.1
Deleted tag 'v0.1' (was f15b0dd)
```

<font style="color:rgb(51, 51, 51);">因为创建的标签都只存储在本地，不会自动推送到远程。所以，打错的标签可以在本地安全删除。</font>

<font style="color:rgb(51, 51, 51);">如果要推送某个标签到远程，使用命令</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git push origin <tagname></font><font style="color:rgb(51, 51, 51);">：</font>

```plain
$ git push origin v1.0
Total 0 (delta 0), reused 0 (delta 0)
To github.com:michaelliao/learngit.git
 * [new tag]         v1.0 -> v1.0
```

<font style="color:rgb(51, 51, 51);">或者，一次性推送全部尚未推送到远程的本地标签：</font>

```plain
$ git push origin --tags
Total 0 (delta 0), reused 0 (delta 0)
To github.com:michaelliao/learngit.git
 * [new tag]         v0.9 -> v0.9
```

<font style="color:rgb(51, 51, 51);">如果标签已经推送到远程，要删除远程标签就麻烦一点，先从本地删除：</font>

```plain
$ git tag -d v0.9
Deleted tag 'v0.9' (was f52c633)
```

<font style="color:rgb(51, 51, 51);">然后，从远程删除。删除命令也是push，但是格式如下：</font>

```plain
$ git push origin :refs/tags/v0.9
To github.com:michaelliao/learngit.git
 - [deleted]         v0.9
```

<font style="color:rgb(51, 51, 51);">要看看是否真的从远程库删除了标签，可以登陆GitHub查看。</font>

<font style="color:rgb(51, 51, 51);">小结：</font>

+ <font style="color:rgb(51, 51, 51);">命令</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git push origin <tagname></font><font style="color:rgb(51, 51, 51);">可以推送一个本地标签；</font>
+ <font style="color:rgb(51, 51, 51);">命令</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git push origin --tags</font><font style="color:rgb(51, 51, 51);">可以推送全部未推送过的本地标签；</font>
+ <font style="color:rgb(51, 51, 51);">命令</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git tag -d <tagname></font><font style="color:rgb(51, 51, 51);">可以删除一个本地标签；</font>
+ <font style="color:rgb(51, 51, 51);">命令</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git push origin :refs/tags/<tagname></font><font style="color:rgb(51, 51, 51);">可以删除一个远程标签。</font>

# 自定义Git
## 忽略特殊文件
部分文件我们需要保存着Git工作目录中，但是有不能提交它们，我们可以在Git工作区的根目录下创建一个特殊的<font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore文件。然后把要忽略的文件名填进去，Git会自动忽略这些文件。</font>

<font style="color:rgb(51, 51, 51);">不需要从头写</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore</font><font style="color:rgb(51, 51, 51);">文件，GitHub已经为我们准备了各种配置文件，只需要组合一下就可以使用了。所有配置文件可以直接在线浏览：</font>[GitHub - github/gitignore: A collection of useful .gitignore templates](https://github.com/github/gitignore)

<font style="color:rgb(51, 51, 51);">忽略文件的原则是： </font>

1. <font style="color:rgb(51, 51, 51);">忽略操作系统自动生成的文件，比如缩略图等；</font>
2. <font style="color:rgb(51, 51, 51);">忽略编译生成的中间文件、可执行文件等，也就是如果一个文件是通过另一个文件自动生成的，那自动生成的文件就没必要放进版本库，比如Java编译产生的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.class</font><font style="color:rgb(51, 51, 51);">文件；</font>
3. <font style="color:rgb(51, 51, 51);">忽略你自己的带有敏感信息的配置文件，比如存放口令的配置文件。</font>

<font style="color:rgb(51, 51, 51);">举个例子：</font>

<font style="color:rgb(51, 51, 51);">假设你在Windows下进行Python开发，Windows会自动在有图片的目录下生成隐藏的缩略图文件，如果有自定义目录，目录下就会有</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">Desktop.ini</font><font style="color:rgb(51, 51, 51);">文件，因此你需要忽略Windows自动生成的垃圾文件：</font>

```plain
# Windows:
Thumbs.db
ehthumbs.db
Desktop.ini
```

<font style="color:rgb(51, 51, 51);">然后，继续忽略Python编译产生的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.pyc</font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.pyo</font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">dist</font><font style="color:rgb(51, 51, 51);">等文件或目录：</font>

```plain
# Python:
*.py[cod]
*.so
*.egg
*.egg-info
dist
build
```

<font style="color:rgb(51, 51, 51);">加上你自己定义的文件，最终得到一个完整的</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore</font><font style="color:rgb(51, 51, 51);">文件，内容如下：</font>

```plain
# Windows:
Thumbs.db
ehthumbs.db
Desktop.ini

# Python:
*.py[cod]
*.so
*.egg
*.egg-info
dist
build

# My configurations:
db.ini
deploy_key_rsa
```

<font style="color:rgb(51, 51, 51);">最后一步就是把</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore</font><font style="color:rgb(51, 51, 51);">也提交到Git，就完成了！当然检验</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore</font><font style="color:rgb(51, 51, 51);">的标准是</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git status</font><font style="color:rgb(51, 51, 51);">命令是不是说</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">working directory clean</font><font style="color:rgb(51, 51, 51);">。</font>

<font style="color:rgb(51, 51, 51);">使用Windows的童鞋注意了，如果你在资源管理器里新建一个</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore</font><font style="color:rgb(51, 51, 51);">文件，它会非常弱智地提示你必须输入文件名，但是在文本编辑器里“保存”或者“另存为”就可以把文件保存为</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore</font><font style="color:rgb(51, 51, 51);">了。</font>

<font style="color:rgb(51, 51, 51);">有些时候，你想添加一个文件到Git，但发现添加不了，原因是这个文件被</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore</font><font style="color:rgb(51, 51, 51);">忽略了：</font>

```plain
$ git add App.class
The following paths are ignored by one of your .gitignore files:
App.class
Use -f if you really want to add them.
```

<font style="color:rgb(51, 51, 51);">如果你确实想添加该文件，可以用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">-f</font><font style="color:rgb(51, 51, 51);">强制添加到Git：</font>

```plain
$ git add -f App.class
```

<font style="color:rgb(51, 51, 51);">或者你发现，可能是</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore</font><font style="color:rgb(51, 51, 51);">写得有问题，需要找出来到底哪个规则写错了，可以用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git check-ignore</font><font style="color:rgb(51, 51, 51);">命令检查：</font>

```plain
$ git check-ignore -v App.class
.gitignore:3:*.class	App.class
```

<font style="color:rgb(51, 51, 51);">Git会告诉我们，</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore</font><font style="color:rgb(51, 51, 51);">的第3行规则忽略了该文件，于是我们就可以知道应该修订哪个规则。</font>

<font style="color:rgb(51, 51, 51);">还有些时候，当我们编写了规则排除了部分文件时：</font>

```plain
# 排除所有.开头的隐藏文件:
.*
# 排除所有.class文件:
*.class
```

<font style="color:rgb(51, 51, 51);">但是我们发现</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.*</font><font style="color:rgb(51, 51, 51);">这个规则把</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore</font><font style="color:rgb(51, 51, 51);">也排除了，并且</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">App.class</font><font style="color:rgb(51, 51, 51);">需要被添加到版本库，但是被</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">*.class</font><font style="color:rgb(51, 51, 51);">规则排除了。</font>

<font style="color:rgb(51, 51, 51);">虽然可以用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git add -f</font><font style="color:rgb(51, 51, 51);">强制添加进去，但有强迫症的童鞋还是希望不要破坏</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore</font><font style="color:rgb(51, 51, 51);">规则，这个时候，可以添加两条例外规则：</font>

```plain
# 排除所有.开头的隐藏文件:
.*
# 排除所有.class文件:
*.class

# 不排除.gitignore和App.class:
!.gitignore
!App.class
```

<font style="color:rgb(51, 51, 51);">把指定文件排除在</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore</font><font style="color:rgb(51, 51, 51);">规则外的写法就是</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">!</font><font style="color:rgb(51, 51, 51);">+文件名，所以，只需把例外文件添加进去即可。</font>

<font style="color:rgb(51, 51, 51);">可以通过</font>[https://gitignore.itranswarp.com](https://gitignore.itranswarp.com/)<font style="color:rgb(51, 51, 51);">在线生成</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore</font><font style="color:rgb(51, 51, 51);">文件。</font>

<font style="color:rgb(68, 68, 68);">小结</font>

+ <font style="color:rgb(51, 51, 51);">忽略某些文件时，需要编写</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore</font><font style="color:rgb(51, 51, 51);">；</font>
+ <font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore</font><font style="color:rgb(51, 51, 51);">文件本身要放到版本库里，并且可以对</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitignore</font><font style="color:rgb(51, 51, 51);">做版本管理！</font>

## 配置别名
### motivation
偷懒用

### 配置别名
<font style="color:rgb(51, 51, 51);">有没有经常敲错命令？比如</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git status</font><font style="color:rgb(51, 51, 51);">？</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">status</font><font style="color:rgb(51, 51, 51);">这个单词真心不好记。如果敲</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git st</font><font style="color:rgb(51, 51, 51);">就表示</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git status</font><font style="color:rgb(51, 51, 51);">那就简单多了，当然这种偷懒的办法我们是极力赞成的。我们只需要敲一行命令，告诉Git，以后</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">st</font><font style="color:rgb(51, 51, 51);">就表示</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">status</font><font style="color:rgb(51, 51, 51);">：</font>

```plain
$ git config --global alias.st status
```

<font style="color:rgb(51, 51, 51);">当然还有别的命令可以简写，很多人都用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">co</font><font style="color:rgb(51, 51, 51);">表示</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">checkout</font><font style="color:rgb(51, 51, 51);">，</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">ci</font><font style="color:rgb(51, 51, 51);">表示</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">commit</font><font style="color:rgb(51, 51, 51);">，</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">br</font><font style="color:rgb(51, 51, 51);">表示</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">branch</font><font style="color:rgb(51, 51, 51);">：</font>

```plain
$ git config --global alias.co checkout
$ git config --global alias.ci commit
$ git config --global alias.br branch
```

<font style="color:rgb(51, 51, 51);">以后提交就可以简写成：</font>

```plain
$ git ci -m "bala bala bala..."
```

**<font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">--global</font>****<font style="color:rgb(51, 51, 51);">参数是全局参数，</font>**<font style="color:rgb(51, 51, 51);">也就是这些命令在这台电脑的所有Git仓库下都有用。</font>

<font style="color:rgb(51, 51, 51);">在撤销修改一节中，我们知道，命令</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git reset HEAD file</font><font style="color:rgb(51, 51, 51);">可以把暂存区的修改撤销掉（unstage），重新放回工作区。既然是一个unstage操作，就可以配置一个</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">unstage</font><font style="color:rgb(51, 51, 51);">别名：</font>

```plain
$ git config --global alias.unstage 'reset HEAD'
```

<font style="color:rgb(51, 51, 51);">当你敲入命令：</font>

```plain
$ git unstage test.py
```

<font style="color:rgb(51, 51, 51);">实际上Git执行的是：</font>

```plain
$ git reset HEAD test.py
```

<font style="color:rgb(51, 51, 51);">配置一个</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git last</font><font style="color:rgb(51, 51, 51);">，让其显示最后一次提交信息：</font>

```plain
$ git config --global alias.last 'log -1'
```

<font style="color:rgb(51, 51, 51);">这样，用</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git last</font><font style="color:rgb(51, 51, 51);">就能显示最近一次的提交：</font>

```plain
$ git last
commit adca45d317e6d8a4b23f9811c3d7b7f0f180bfe2
Merge: bd6ae48 291bea8
Author: Michael Liao <askxuefeng@gmail.com>
Date:   Thu Aug 22 22:49:22 2013 +0800

    merge & fix hello.py
```

<font style="color:rgb(51, 51, 51);">甚至还有人丧心病狂地把</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">lg</font><font style="color:rgb(51, 51, 51);">配置成了：</font>

```plain
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

<font style="color:rgb(51, 51, 51);">来看看</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">git lg</font><font style="color:rgb(51, 51, 51);">的效果：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/29307286/1689842750206-8e202c35-6490-4051-8bbd-3093f3226c31.png)

### 配置文件
<font style="color:rgb(51, 51, 51);">配置Git的时候，加上</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">--global</font><font style="color:rgb(51, 51, 51);">是针对当前用户起作用的，如果不加，那只针对当前的仓库起作用。每个仓库的Git配置文件都放在</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.git/config</font><font style="color:rgb(51, 51, 51);">文件中：</font>

```plain
$ cat .git/config 
[core]
    repositoryformatversion = 0
    filemode = true
    bare = false
    logallrefupdates = true
    ignorecase = true
    precomposeunicode = true
[remote "origin"]
    url = git@github.com:michaelliao/learngit.git
    fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
    remote = origin
    merge = refs/heads/master
[alias]
    last = log -1
```

<font style="color:rgb(51, 51, 51);">别名就在</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">[alias]</font><font style="color:rgb(51, 51, 51);">后面，要删除别名，直接把对应的行删掉即可。</font>

<font style="color:rgb(51, 51, 51);">而当前用户的Git配置文件放在用户主目录下的一个隐藏文件</font><font style="color:rgb(51, 51, 51);background-color:rgb(250, 250, 250);">.gitconfig</font><font style="color:rgb(51, 51, 51);">中：</font>

```plain
$ cat .gitconfig
[alias]
    co = checkout
    ci = commit
    br = branch
    st = status
[user]
    name = Your Name
    email = your@email.com
```

<font style="color:rgb(51, 51, 51);">配置别名也可以直接修改这个文件，如果改错了，可以删掉文件重新通过命令配置。</font>



#  .git目录文件分析










