## 静态库
<font style="color:rgb(77, 77, 77);">之所以称为【静态库】，是因为</font>**<font style="color:rgb(77, 77, 77);">在链接阶段，会将汇编生成的目标文件.o与引用到的库一起链接打包到可执行文件中。</font>**<font style="color:rgb(77, 77, 77);">因此对应的链接方式称为静态链接。</font>

<font style="color:rgb(77, 77, 77);">静态库可以简单看成是一组目标文件（.o/.obj文件）的集合，即很多目标文件经过压缩打包后形成的一个文件。</font>

<font style="color:rgb(77, 77, 77);">静态库特点总结：</font>

+ <font style="color:rgba(0, 0, 0, 0.75);">静态库对函数库的链接是放在</font>**<font style="color:rgba(0, 0, 0, 0.75);">编译时期完成</font>**<font style="color:rgba(0, 0, 0, 0.75);">的。</font>
+ <font style="color:rgba(0, 0, 0, 0.75);">程序在运行时与函数库再无瓜葛，</font>**<font style="color:rgba(0, 0, 0, 0.75);">移植方便。</font>**
+ **<font style="color:rgba(0, 0, 0, 0.75);">浪费空间和资源</font>**<font style="color:rgba(0, 0, 0, 0.75);">，因为所有相关的目标文件与牵涉到的函数库被链接合成一个可执行文件。</font>

<font style="color:rgb(77, 77, 77);">  
</font>

## 动态库
