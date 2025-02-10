

## 关于markdown图片相对路径
这几天在使用markdown的时候遇到的问题，没有看到对应的解决方案。在此记录总结一下

相对路径通常在表示图片、网页等位置时需要用到，相比于绝对路径更不容易出错。
如果图片与.md文件在同一目录下，那么相对路径这样表示

![avatar](buildWebsites.jpg)
其中avatar表示图片未正常加载时所显示的内容，buildWebsites.jpg为文件名

其子路径这样表示
![avatar](1/buildWebsites.jpg)
其中1为文件夹名称

其父路径用“..”表示，例如
![avatar](../buildWebsites.jpg)