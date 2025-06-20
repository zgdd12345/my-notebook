# conda命令

#### 常用命令

 1） conda list 查看安装了哪些包。

  2） conda env list 或  conda info -e 查看当前存在哪些虚拟环境

  3） conda update conda 检查更新当前conda

  4） conda --version 查询conda版本

  5） conda -h 查询conda的命令使用

#### 创建python虚拟环境。

   使用  conda create -n your_env_name python=X.X （2.7、3.6等)命令创建python版本为X.X、名字为your_env_name的虚拟环境。your_env_name文件可以在Anaconda安装目录envs文件下找到。

#### 使用激活(或切换不同python版本)的虚拟环境。

  打开命令行输入python --version可以检查当前python的版本。

  使用如下命令即可 激活你的虚拟环境(即将python的版本改变)。

  Linux:  source activate your_env_name (虚拟环境名称)

  Windows:  activate your_env_name (虚拟环境名称)

  这是再使用 python --version 可以检查当前python版本是否为想要的。

#### 对虚拟环境中安装额外的包。

  使用命令 conda install -n your_env_name [package] 即可安装package到your_env_name中

####  关闭虚拟环境

deactivate

#### 删除虚拟环境。

  使用命令 conda remove -n your_env_name(虚拟环境名称) --all ， 即可删除。

#### 删除环境中的某个包。

  使用命令 conda remove --name your_env_name package_name 即可。

# pip命令

- **显示版本和路径**

```text
pip --version
```

- **获取帮助**

```bash
pip --help
```

- **列出已安装的包**

```cpp
pip list
```

- **查看可升级的包**

```cpp
pip list -o
```

- **升级 pip**

```bash
pip install -U pip

# 如果这个升级命令不能成功 ，可以使用以下命令：
sudo easy_install --upgrade pip
```

- **安装包**

```bash
pip install SomePackage              # 最新版本

pip install SomePackage==1.0.4       # 指定版本

pip install 'SomePackage>=1.0.4'     # 最小版本
```

- **显示安装包信息**

```text
pip show
```

- **升级包**

```text
pip install --upgrade SomePackage
```

- **卸载包**

```text
pip uninstall SomePackage
```

- **搜索包**

```text
pip search SomePackage
```

- **查看指定包的详细信息**

```text
pip show -f SomePackage
```

-
