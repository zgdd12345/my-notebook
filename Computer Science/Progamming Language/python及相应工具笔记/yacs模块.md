# yacs模块

### 0.Introduction

yacs的作者是faster-rcnn的作者Ross Girshick。github地址：https://github.com/rbgirshick/yacs

yacs是一个轻量级用于定义和管理系统配置的开源库，是科学实验软件中常用的参数配置库。这些“配置”通常涵盖概念，例如用于训练机器学习模型的超参数或可配置的模型超参数（例如卷积神经网络的深度）。**YACS使用YAML**作为一种简单的，人类可读的序列化格式。范例是：你的代码+实验E的yacs配置(+外部依赖+硬件+其他讨厌的术语…)=可重复的实验E。尽管您可能无法控制所有内容，但至少可以控制代码和实验性配置。YACS在这里为您提供帮助。

YACS 源自py-faster-rcnn和 Detectron中使用的实验配置系统 。

### 1.安装

`pip install yacs`

### 2.用法

YACS可以多种灵活方式使用。主要有两种范例：

1. 配置为**局部变量 (local variable)**
2. 配置为**全局单例(global singleton)**

尽管建议使用local variable，但要由自己决定。

要在项目中使用YACS，**首先要创建一个项目配置文件**，通常称为config.py或defaults.py。该文件是所有可配置选项的一站式参考点。它应该有很好的文档记录，并为所有选项提供合理的默认值。


```python
# my_project/config.py

from yacs.config import CfgNode as CN


_C = CN()

_C.SYSTEM = CN()
# Number of GPUS to use in the experiment
_C.SYSTEM.NUM_GPUS = 8
# Number of workers for doing things
_C.SYSTEM.NUM_WORKERS = 4

_C.TRAIN = CN()
# A very important hyperparameter
_C.TRAIN.HYPERPARAMETER_1 = 0.1
# The all important scales for the stuff
_C.TRAIN.SCALES = (2, 4, 8, 16)


def get_cfg_defaults():
  """Get a yacs CfgNode object with default values for my_project."""
  # Return a clone so that the defaults will not be altered
  # This is for the "local variable" use pattern
  return _C.clone()

# Alternatively, provide a way to import the defaults as
# a global singleton:
# cfg = _C  # users can `from config import cfg`
```

接下来，创建YAML配置文件。通常为每个实验做一个。每个配置文件仅覆盖该实验中正在更改的选项。

```python
# my_project/experiment.yaml

SYSTEM:
  NUM_GPUS: 2
TRAIN:
  SCALES: (1, 2)
```

最后，您将拥有使用config系统的实际项目代码。进行任何初始设置后，最好冻结它，以防止通过调用freeze()方法进行进一步修改。如下所示，通过cfg直接导入和访问config选项，可以将其用作全局选项集，也可以将config选项cfg复制并作为参数传递。

```python 
# my_project/main.py

import my_project
from config import get_cfg_defaults  # local variable usage pattern, or:
# from config import cfg  # global singleton usage pattern


if __name__ == "__main__":
  cfg = get_cfg_defaults()
  cfg.merge_from_file("experiment.yaml")
  cfg.freeze()
  print(cfg)

  # Example of using the cfg as global access to options
  if cfg.SYSTEM.NUM_GPUS > 0:
    my_project.setup_multi_gpu_support()

  model = my_project.create_model(cfg)
```

命令行替代

您可以CfgNode使用完全限定的键值对列表来更新。这样可以很容易地从命令行使用替代选项。例如：

```python 
cfg.merge_from_file("experiment.yaml")
# Now override from a list (opts could come from the command line)
opts = ["SYSTEM.NUM_GPUS", 8, "TRAIN.SCALES", "(1, 2, 3, 4)"]
cfg.merge_from_list(opts)
```

建议采用以下原则：“相同的配置选项只使用一种方法。” 这个原则意味着如果在YACS配置对象中定义了一个选项，那么你的程序应该使用cfg.merge_from_list（opts）设置该配置选项，而不是通过定义–train-scales作为命令行参数来实现。 然后用来设置cfg.TRAIN.SCALES。

### 3.API reference

use `__C` as created config file

##### 1. clone()

return a copy config file, so the defaults will not be altered

```text
def get_cfg_defaults():
	return __C.clone()
```

##### 2. clear()

clear your config file, you will get `None` as the result

```text
print(__C.clear())  # None
```

##### 3. merge_from_file()

对于不同的实验，你有不同的超参设置，所以你可以使用yaml文件来管理不同的configs，然后使用`merge_from_file()`这个方法，这个会比较每个experiments特有的config和默认参数的区别，会将默认参数与特定参数不同的部分，用特定参数覆盖。

```text
__C.merge_from_file("./test_config.yaml")
```

Addition:

- 你需要merge的yaml文件中，**不能有default参数中不存在的参数**，不然会报错，但是可以比default中设定的参数少，比如default文件中有name参数，这是不需要特定改动的，你可以在yaml中不设置name这个key。

```python
from yacs.config import CfgNode as CN
# default cfgs
__C = CN()
__C.name = 'test'
__C.model = CN()
__C.model.backbone = 'resnet'
__C.model.depth = 18

# yaml cfgs
# 不报错的情况1：参数和default中一样多，并且层级关系一致
name: test
model:
    backbone: resnet
    depth: 18

# 不报错的情况2：参数可以比default中少，以下例子就不包含name和model.backbone
model: 
    depth: 34

# 报错的情况1：以下多了model.batch_normalization这个额外的key，这在default中是不存在的
name: test
model:
    backbone: resnet
    depth: 29
    batch_normalization: True

# 报错的情况2：关键词不一致，这里的关键词是na_me，而default中是name
na_me: test
```

##### 4. merge_from_list()

可以用`list`来传递参数

```python
from yacs.config import CfgNode as CN
__C = CN()
__C.name = 'test'
__C.model = CN()
__C.model.backbone = 'resnet'
__C.model.depth = 18
print(__C)
'''
model:
  backbone: resnet
  depth: 18
name: test
'''

opts = ["name", 'test_name', "model.backbone", "vgg"]
__C.merge_from_list(opts)
print(__C)
'''
model:
  backbone: vgg
  depth: 18
name: test_name
'''
```

other details are the same as `merge_from_file`

##### 5. merge_from_other_cfg()

the same as `merge_from_file` and `merge_from_list`, the only difference is that the merged file is also a `CfgNode` class

##### 6. freeze()

freeze the configs, and you can not change the value after this operation

```text
from yacs.config import CfgNode as CN
__C = CN()
__C.name = 'test'
__C.model = CN()
__C.model.backbone = 'resnet'
__C.model.depth = 18

# freeze the config
__C.freeze()
# try to change the name's value, raise an error
__C.name = 'test2'  # error
```

##### 7. defrost()

reverse operation of `freeze()`

```text
from yacs.config import CfgNode as CN
__C = CN()
__C.name = 'test'
__C.model = CN()
__C.model.backbone = 'resnet'
__C.model.depth = 18

# freeze the config
__C.freeze()
# try to change the name's value, raise an error
__C.name = 'test2'  # error

__C.defrost()  # not freeze cfgs, after this operation you can change the value
__C.name = 'test2'  # work
```

