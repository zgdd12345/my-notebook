<font style="color:rgb(77, 77, 77);">首先本地要有一个项目文件夹，同时远程也有一个项目文件夹，然后通过配置文件来同步二者。</font>

<font style="color:rgb(255, 0, 0);">SFTP可以查看远程项目所有文件，但不能直接操作，必须操作本地项目文件，再同步到远程项目。</font>

<font style="color:rgb(255, 0, 0);"></font>

<font style="color:rgb(77, 77, 77);">现在我们本地和远程均有一个文件夹“sftpFolder”，用VsCode打开本地文件夹“sftpFolder”，然后执行 </font><font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">ctrl+shift+p</font><font style="color:rgb(77, 77, 77);"> ，搜索 </font><font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">SFTP:Config</font><font style="color:rgb(77, 77, 77);"> ，回车后，会生成一个“.vscode/sftp.json”，这个就是配置文件。</font>

```powershell
{
    "name": "tiger6",
    "host": "192.168.20.6",
    "protocol": "sftp",
    "port": 22,
    "username": "fengsm",
    "password": "fengsm2021",
    "remotePath": "/home/fengsm/road_baseline/",
    "context": "D:/Experiments/road_connectivity-master/",
    "uploadOnSave": true,
    "useTempFile": false,
    "openSsh": false,
    "syncMode": "update",
    "ignore": [            
        "**/.vscode/**",
        "**/.git/**",
        "**/.DS_Store"
    ]
}
```



# <font style="color:rgb(79, 79, 79);">上传本地代码到服务器</font>
<font style="color:rgb(77, 77, 77);">使用 ctrl+shift+p 快捷键调出输入框，选择 SFTP:Upload 回车  
</font><font style="color:rgb(77, 77, 77);">本地的项目代码就可以上传到服务器了  
</font><font style="color:rgb(77, 77, 77);">现在修改本地代码 </font>**<font style="color:rgb(77, 77, 77);">ctrl+s</font>**<font style="color:rgb(77, 77, 77);"> 保存，即可同步到服务器了</font>

