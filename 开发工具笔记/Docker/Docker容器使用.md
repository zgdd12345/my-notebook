# Docker的使用
镜像是 Docker 的三大组件之一。

Docker 运行容器前需要本地存在对应的镜像，如果本地不存在该镜像，Docker 会从镜像仓库下载该镜像。

本章将介绍更多关于镜像的内容，包括：

- 从仓库获取镜像；

- 管理本地主机上的镜像；

- 介绍镜像实现的基本原理。
  
## 获取镜像
<a href="https://hub.docker.com/search?q=&type=image" title="超链接title">Docker镜像</a>
从 Docker 镜像仓库获取镜像的命令是 docker pull。其命令格式为：

    $ docker pull [选项] [Docker Registry 地址[:端口号]/]仓库名[:标签]
具体的选项可以通过docker pull --help命令看到，这里我们说一下镜像名称的格式。

Docker 镜像仓库地址：地址的格式一般是 <域名/IP>[:端口号]。默认地址是 Docker Hub(docker.io)。

仓库名：如之前所说，这里的仓库名是两段式名称，即 <用户名>/<软件名>。对于 Docker Hub，如果不给出用户名，则默认为 library，也就是官方镜像。

比如：

    $ docker pull ubuntu:18.04
    18.04: Pulling from library/ubuntu
    92dc2a97ff99: Pull complete
    be13a9d27eb8: Pull complete
    c8299583700a: Pull complete
    Digest: sha256:4bc3ae6596938cb0d9e5ac51a1152ec9dcac2a1c50829c74abd9c4361e321b26
    Status: Downloaded newer image for ubuntu:18.04
    docker.io/library/ubuntu:18.04
上面的命令中没有给出 Docker 镜像仓库地址，因此将会从 Docker Hub （docker.io）获取镜像。而镜像名称是 ubuntu:18.04，因此将会获取官方镜像 library/ubuntu 仓库中标签为 18.04 的镜像。docker pull 命令的输出结果最后一行给出了镜像的完整名称，即： docker.io/library/ubuntu:18.04。

从下载过程中可以看到我们之前提及的**分层存储**的概念，镜像是由多层存储所构成。下载也是一层层的去下载，并非单一文件。下载过程中给出了每一层的 ID 的前 12 位。并且下载结束后，给出该镜像完整的 sha256 的摘要，以确保下载一致性。

在使用上面命令的时候，你可能会发现，你所看到的层 ID 以及 sha256 的摘要和这里的不一样。这是因为官方镜像是一直在维护的，有任何新的 bug，或者版本更新，都会进行修复再以原来的标签发布，这样可以确保任何使用这个标签的用户可以获得更安全、更稳定的镜像。

## 运行
有了镜像后，我们就能够以这个镜像为基础启动并运行一个容器。以上面的 ubuntu:18.04 为例，如果我们打算启动里面的 bash 并且进行交互式操作的话，可以执行下面的命令。

    $ docker run -it --rm ubuntu:18.04 bash

    root@e7009c6ce357:/# cat /etc/os-release
    NAME="Ubuntu"
    VERSION="18.04.1 LTS (Bionic Beaver)"
    ID=ubuntu
    ID_LIKE=debian
    PRETTY_NAME="Ubuntu 18.04.1 LTS"
    VERSION_ID="18.04"
    HOME_URL="https://www.ubuntu.com/"
    SUPPORT_URL="https://help.ubuntu.com/"
    BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
    PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
    VERSION_CODENAME=bionic
    UBUNTU_CODENAME=bionic

docker run 就是运行容器的命令，具体格式我们会在 容器 一节进行详细讲解，我们这里简要的说明一下上面用到的参数。

-it：这是两个参数，一个是 -i：交互式操作，一个是 -t 终端。我们这里打算进入 bash 执行一些命令并查看返回结果，因此我们需要交互式终端。

--rm：这个参数是说容器退出后随之将其删除。默认情况下，为了排障需求，退出的容器并不会立即删除，除非手动 docker rm。我们这里只是随便执行个命令，看看结果，不需要排障和保留结果，因此使用 --rm 可以避免浪费空间。

ubuntu:18.04：这是指用 ubuntu:18.04 镜像为基础来启动容器。

bash：放在镜像名后的是 命令，这里我们希望有个交互式 Shell，因此用的是 bash。

进入容器后，我们可以在 Shell 下操作，执行任何所需的命令。这里，我们执行了 cat /etc/os-release，这是 Linux 常用的查看当前系统版本的命令，从返回的结果可以看到容器内是 Ubuntu 18.04.1 LTS 系统。

最后我们通过 exit 退出了这个容器。

## 列出镜像
要想列出已经下载下来的镜像，可以使用 docker image ls 命令。

    $ docker image ls
    REPOSITORY           TAG                 IMAGE ID            CREATED             SIZE
    redis                latest              5f515359c7f8        5 days ago          183 MB
    nginx                latest              05a60462f8ba        5 days ago          181 MB
    mongo                3.2                 fe9198c04d62        5 days ago          342 MB
    <none>               <none>              00285df0df87        5 days ago          342 MB
    ubuntu               18.04               329ed837d508        3 days ago          63.3MB
    ubuntu               bionic              329ed837d508        3 days ago          63.3MB
列表包含了 仓库名、标签、镜像 ID、创建时间 以及 所占用的空间。

其中仓库名、标签在之前的基础概念章节已经介绍过了。镜像 ID 则是镜像的唯一标识，一个镜像可以对应多个 标签。因此，在上面的例子中，我们可以看到 ubuntu:18.04 和 ubuntu:bionic 拥有相同的 ID，因为它们对应的是同一个镜像。

## 镜像体积
如果仔细观察，会注意到，这里标识的所占用空间和在 Docker Hub 上看到的镜像大小不同。比如，ubuntu:18.04 镜像大小，在这里是 63.3MB，但是在 Docker Hub 显示的却是 25.47 MB。这是因为 Docker Hub 中显示的体积是压缩后的体积。在镜像下载和上传过程中镜像是保持着压缩状态的，因此 Docker Hub 所显示的大小是网络传输中更关心的流量大小。而 docker image ls 显示的是镜像下载到本地后，展开的大小，准确说，是展开后的各层所占空间的总和，因为镜像到本地后，查看空间的时候，更关心的是本地磁盘空间占用的大小。

另外一个需要注意的问题是，docker image ls 列表中的镜像体积总和并非是所有镜像实际硬盘消耗。由于 Docker 镜像是多层存储结构，并且可以继承、复用，因此不同镜像可能会因为使用相同的基础镜像，从而拥有共同的层。由于 Docker 使用 Union FS，相同的层只需要保存一份即可，因此**实际镜像硬盘占用空间很可能要比这个列表镜像大小的总和要小的多。**

你可以通过 docker system df 命令来便捷的查看镜像、容器、数据卷所占用的空间。

    $ docker system df

    TYPE                TOTAL               ACTIVE              SIZE                RECLAIMABLE
    Images              24                  0                   1.992GB             1.992GB (100%)
    Containers          1                   0                   62.82MB             62.82MB (100%)
    Local Volumes       9                   0                   652.2MB             652.2MB (100%)
    Build Cache                                                 0B                  0B

## 虚悬镜像
上面的镜像列表中，还可以看到一个特殊的镜像，这个镜像既没有仓库名，也没有标签，均为 none。：

    <none>               <none>              00285df0df87        5 days ago          342 MB
这个镜像原本是有镜像名和标签的，原来为 mongo:3.2，随着官方镜像维护，发布了新版本后，重新 docker pull mongo:3.2 时，mongo:3.2 这个镜像名被转移到了新下载的镜像身上，而旧的镜像上的这个名称则被取消，从而成为了 <none>。除了 docker pull 可能导致这种情况，docker build 也同样可以导致这种现象。由于新旧镜像同名，旧镜像名称被取消，从而出现仓库名、标签均为 <none> 的镜像。这类无标签镜像也被称为 虚悬镜像(dangling image) ，可以用下面的命令专门显示这类镜像：


    $ docker image ls -f dangling=true
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    <none>              <none>              00285df0df87        5 days ago          342 MB

一般来说，虚悬镜像已经失去了存在的价值，是可以随意删除的，可以用下面的命令删除。

    $ docker image prune

## 中间层镜像
为了加速镜像构建、重复利用资源，Docker会利用中间层镜像。所以在使用一段时间后，可能会看到一些依赖的中间层镜像。默认的 docker image ls 列表中只会显示顶层镜像，如果希望显示包括中间层镜像在内的所有镜像的话，需要加 -a 参数。

    $ docker image ls -a

这样会看到很多无标签的镜像，与之前的虚悬镜像不同，这些无标签的镜像很多都是中间层镜像，是其它镜像所依赖的镜像。这些无标签镜像不应该删除，否则会导致上层镜像因为依赖丢失而出错。实际上，这些镜像也没必要删除，因为之前说过，相同的层只会存一遍，而这些镜像是别的镜像的依赖，因此并不会因为它们被列出来而多存了一份，无论如何你也会需要它们。只要删除那些依赖它们的镜像后，这些依赖的中间层镜像也会被连带删除。

列出部分镜像
不加任何参数的情况下，docker image ls 会列出所有顶层镜像，但是有时候我们只希望列出部分镜像。docker image ls 有好几个参数可以帮助做到这个事情。

## 根据仓库名列出镜像

    $ docker image ls ubuntu
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    ubuntu              18.04               329ed837d508        3 days ago          63.3MB
    ubuntu              bionic              329ed837d508        3 days ago          63.3MB
列出特定的某个镜像，也就是说指定仓库名和标签

    $ docker image ls ubuntu:18.04
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    ubuntu              18.04               329ed837d508        3 days ago          63.3MB
除此以外，docker image ls 还支持强大的过滤器参数 --filter，或者简写 -f。之前我们已经看到了使用过滤器来列出虚悬镜像的用法，它还有更多的用法。比如，我们希望看到在 mongo:3.2 之后建立的镜像，可以用下面的命令：

    $ docker image ls -f since=mongo:3.2
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    redis               latest              5f515359c7f8        5 days ago          183 MB
    nginx               latest              05a60462f8ba        5 days ago          181 MB
想查看某个位置之前的镜像也可以，只需要把 since 换成 before 即可。

此外，如果镜像构建时，定义了 LABEL，还可以通过 LABEL 来过滤。

    $ docker image ls -f label=com.example.version=0.1


## 以特定格式显示
默认情况下，docker image ls 会输出一个完整的表格，但是我们并非所有时候都会需要这些内容。比如，刚才删除虚悬镜像的时候，我们需要利用 docker image ls 把所有的虚悬镜像的 ID 列出来，然后才可以交给 docker image rm 命令作为参数来删除指定的这些镜像，这个时候就用到了 -q 参数。

    $ docker image ls -q
    5f515359c7f8
    05a60462f8ba
    fe9198c04d62
    00285df0df87
    329ed837d508
    329ed837d508
--filter 配合 -q 产生出指定范围的 ID 列表，然后送给另一个 docker 命令作为参数，从而针对这组实体成批的进行某种操作的做法在 Docker 命令行使用过程中非常常见，不仅仅是镜像，将来我们会在各个命令中看到这类搭配以完成很强大的功能。因此每次在文档看到过滤器后，可以多注意一下它们的用法。

另外一些时候，我们可能只是对表格的结构不满意，希望自己组织列；或者不希望有标题，这样方便其它程序解析结果等，这就用到了 Go 的模板语法。

比如，下面的命令会直接列出镜像结果，并且只包含镜像ID和仓库名：

    $ docker image ls --format "{{.ID}}: {{.Repository}}"
    5f515359c7f8: redis
    05a60462f8ba: nginx
    fe9198c04d62: mongo
    00285df0df87: <none>
    329ed837d508: ubuntu
    329ed837d508: ubuntu
或者打算以表格等距显示，并且有标题行，和默认一样，不过自己定义列：

    $ docker image ls --format "table {{.ID}}\t{{.Repository}}\t{{.Tag}}"
    IMAGE ID            REPOSITORY          TAG
    5f515359c7f8        redis               latest
    05a60462f8ba        nginx               latest
    fe9198c04d62        mongo               3.2
    00285df0df87        <none>              <none>
    329ed837d508        ubuntu              18.04
    329ed837d508        ubuntu              bionic