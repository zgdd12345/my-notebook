# Imagenet

## 1.Tiny-imagenet

### 1.1简介

Tiny Imagenet 有 200 个类。 每个类有 500 张训练图像、50 张验证图像和 50 张测试图像。官方发布了带有图像和注释的训练和验证集。 官方提供类标签和边界框作为注释； 但是，用户只需要预测每个图像的类别标签，而无需定位对象。 测试集无标签发布。

### 1.2下载数据

  点击官方链接，即可直接下载（http://cs231n.stanford.edu/tiny-imagenet-200.zip。下载完成后会得到大约236MB的压缩包。

### 1.3数据形式

首先解压完文件夹会得到以下内容

$ tree data
tiny-imagenet-200
├── train
│   ├── class1
│   │   ├── images
│   │   │   ├── img1.JPEG
│   │   │   ├── img2.JPEG
│   │   │   └── ...
│   │   └── class1_boxes.txt
│   ├── class2
│   │   ├── images
│   │   │   ├── img3.JPEG
│   │   │   ├── img4.JPEG
│   │   │   └── ...
│   │   └── class2_boxes.txt
│   └── ...
├── val
│   ├── images
│   │   ├── img5.JPEG
│   │   ├── img6.JPEG
│   │   └── ...
│   └── val_annotations.txt
├── test
│   └── images
│       ├── img7.JPEG
│       ├── img8.JPEG
│       └── ...
├── wnids.txt
└── words.txt

如官方所说，测试集（test）是没有标注的，因此一般我们自己也不会用到。主要就是训练集（train）和验证集（val）。从上述tree可以看出，train和val的结构是不一样的，因此不能简单的使用pytorch自带的

`torchvision.datasets.ImageFolder(‘/data_dir’)`

### 1.4自定义数据加载

```python
from torch.utils.data import Dataset, DataLoader
from torchvision import models, utils, datasets, transforms
import numpy as np
import sys
import os
from PIL import Image


class TinyImageNet(Dataset):
    def __init__(self, root, train=True, transform=None):
        self.Train = train
        self.root_dir = root
        self.transform = transform
        self.train_dir = os.path.join(self.root_dir, "train")
        self.val_dir = os.path.join(self.root_dir, "val")

        if (self.Train):
            self._create_class_idx_dict_train()
        else:
            self._create_class_idx_dict_val()

        self._make_dataset(self.Train)

        words_file = os.path.join(self.root_dir, "words.txt")
        wnids_file = os.path.join(self.root_dir, "wnids.txt")

        self.set_nids = set()

        with open(wnids_file, 'r') as fo:
            data = fo.readlines()
            for entry in data:
                self.set_nids.add(entry.strip("\n"))

        self.class_to_label = {}
        with open(words_file, 'r') as fo:
            data = fo.readlines()
            for entry in data:
                words = entry.split("\t")
                if words[0] in self.set_nids:
                    self.class_to_label[words[0]] = (words[1].strip("\n").split(","))[0]

    def _create_class_idx_dict_train(self):
        if sys.version_info >= (3, 5):
            classes = [d.name for d in os.scandir(self.train_dir) if d.is_dir()]
        else:
            classes = [d for d in os.listdir(self.train_dir) if os.path.isdir(os.path.join(train_dir, d))]
        classes = sorted(classes)
        num_images = 0
        for root, dirs, files in os.walk(self.train_dir):
            for f in files:
                if f.endswith(".JPEG"):
                    num_images = num_images + 1

        self.len_dataset = num_images;

        self.tgt_idx_to_class = {i: classes[i] for i in range(len(classes))}
        self.class_to_tgt_idx = {classes[i]: i for i in range(len(classes))}

    def _create_class_idx_dict_val(self):
        val_image_dir = os.path.join(self.val_dir, "images")
        if sys.version_info >= (3, 5):
            images = [d.name for d in os.scandir(val_image_dir) if d.is_file()]
        else:
            images = [d for d in os.listdir(val_image_dir) if os.path.isfile(os.path.join(train_dir, d))]
        val_annotations_file = os.path.join(self.val_dir, "val_annotations.txt")
        self.val_img_to_class = {}
        set_of_classes = set()
        with open(val_annotations_file, 'r') as fo:
            entry = fo.readlines()
            for data in entry:
                words = data.split("\t")
                self.val_img_to_class[words[0]] = words[1]
                set_of_classes.add(words[1])

        self.len_dataset = len(list(self.val_img_to_class.keys()))
        classes = sorted(list(set_of_classes))
        # self.idx_to_class = {i:self.val_img_to_class[images[i]] for i in range(len(images))}
        self.class_to_tgt_idx = {classes[i]: i for i in range(len(classes))}
        self.tgt_idx_to_class = {i: classes[i] for i in range(len(classes))}

    def _make_dataset(self, Train=True):
        self.images = []
        if Train:
            img_root_dir = self.train_dir
            list_of_dirs = [target for target in self.class_to_tgt_idx.keys()]
        else:
            img_root_dir = self.val_dir
            list_of_dirs = ["images"]

        for tgt in list_of_dirs:
            dirs = os.path.join(img_root_dir, tgt)
            if not os.path.isdir(dirs):
                continue

            for root, _, files in sorted(os.walk(dirs)):
                for fname in sorted(files):
                    if (fname.endswith(".JPEG")):
                        path = os.path.join(root, fname)
                        if Train:
                            item = (path, self.class_to_tgt_idx[tgt])
                        else:
                            item = (path, self.class_to_tgt_idx[self.val_img_to_class[fname]])
                        self.images.append(item)

    def return_label(self, idx):
        return [self.class_to_label[self.tgt_idx_to_class[i.item()]] for i in idx]

    def __len__(self):
        return self.len_dataset

    def __getitem__(self, idx):
        img_path, tgt = self.images[idx]
        with open(img_path, 'rb') as f:
            sample = Image.open(img_path)
            sample = sample.convert('RGB')
        if self.transform is not None:
            sample = self.transform(sample)

        return sample, tgt
```

然后就可以直接加载数据了：

```python
from * import TinyImageNet
data_dir = './tiny-imagenet-200/'
dataset_train = TinyImageNet(data_dir, train=True)
dataset_val = TinyImageNet(data_dir, train=False)

#  "*"为你的文件名，transform中的均值与标准差可以参考标准的imagenet
```

