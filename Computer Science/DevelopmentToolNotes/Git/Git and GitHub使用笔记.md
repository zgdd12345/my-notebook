# Git and GitHub使用笔记

## 0.简单使用

配置好git和github之后简单使用。

### 初始化

使用当前目录作为Git仓库，我们只需使它初始化。

```bush
git init  # 将当前目录设置为git可管理的目录
```

使用指定目录作为Git仓库。

```
git init newrepo  # 将指定目录设置为git可管理的目录
```

### 添加到暂存区

第一步：使用命令 git add readme.txt添加到暂存区里面去。如下：

```
git add readme.txt  # 添加指定文件
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

### 关联远程库

```
git remote add origin git@github.com:zgdd12345/quantum_project.git   # github下code处地址
```

把本地库的内容推送到远程，使用 `git push`命令，实际上是把**当前分支master**推送到远程。**第一次推送master分支时，加上了 –u参数**，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令。

第一次推送命令如下：

```
git push -u origin master
```

词汇推送命令如下：

```
git push origin master
```

将远程的项目与本地合并

```
git pull --reabase origin master
```

### 获取远程最新版本

#### `git pull`



#### `git fetch`
`git fetch` 是 Git 中用于从远程仓库同步最新数据的核心命令，其核心特点是 ‌**安全获取远程变更而不自动合并**‌。

**核心功能**
1. ‌**获取远程更新**‌
    - 下载远程仓库的最新提交历史、分支和标签信息，但不会修改本地工作目录或当前分支状态34
    - 更新本地仓库中的 ‌**远程跟踪分支**‌（如 `origin/main`），使其与远程仓库保持同步
2. ‌**非破坏性操作**‌
    - 与 `git pull` 不同，`fetch` 仅获取数据，需手动执行 `merge` 或 `rebase` 才会合并变更
    