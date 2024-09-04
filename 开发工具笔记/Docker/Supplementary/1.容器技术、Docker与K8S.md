# 容器技术、Docker与K8S
与虚拟机通过操作系统实现隔离不同，容器技术只隔离应用程序的运行时环境但容器之间可以共享同一个操作系统，这里的运行时环境指的是程序运行依赖的各种库以及配置。

容器更加的轻量级且占用的资源更少，与操作系统动辄几G的内存占用相比，容器技术只需数M空间，因此我们可以在同样规格的硬件上大量部署容器，这是虚拟机所不能比拟的，而且不同于操作系统数分钟的启动时间容器几乎瞬时启动，容器技术为打包服务栈提供了一种更加高效的方式。

容器是一种通用技术，docker只是其中的一种实现。Docker本身并不是容器，它是创建容器的工具，是应用容器引擎。

K8S是基于容器的集群管理平台，它的全称，是kubernetes。

## Docker

docker是一个用Go语言实现的开源项目，可以让我们方便的创建和使用容器，docker将程序以及程序所有的依赖都打包到docker container，这样你的程序可以在任何环境都会有**一致的表现并且可以快速部署。**

Docker技术的三大核心概念，分别是：

- 镜像（Image）
- 容器（Container）
- 仓库（Repository）

### Docker的使用

docker中有这样几个概念：

- dockerfile：dockerfile就是image的源代码
- image：理解为可执行程序，
- container：运行起来的进程。

我们只需要在dockerfile中指定需要哪些程序、依赖什么样的配置，之后把dockerfile交给“编译器”docker进行“编译”，也就是**docker build命令**，生成的可执行程序就是image，之后就可以运行这个image了，这就是**docker run命令**，image运行起来后就是docker container。

### Docker如何工作？

docker使用了常见的CS架构，也就是client-server模式，docker client负责处理用户输入的各种命令，比如docker build、docker run，真正工作的其实是server，也就是docker demon，值得注意的是，docker client和docker demon可以运行在同一台机器上。
<img src="img/docker_struct.jpg" alt="图片alt" title="Docker">

1. docker build：
   当我们写完dockerfile交给docker“编译”时使用这个命令，那么client在接收到请求后转发给docker daemon，接着docker daemon根据dockerfile创建出“可执行程序”image。
2. docker run
    有了“可执行程序”image后就可以运行程序了，接下来使用命令docker run，docker daemon接收到该命令后找到具体的image，然后加载到内存开始执行，image执行起来就是所谓的container。
3. docker pull
    docker中image的概念就类似于“可执行程序”。Docker Hub，docker官方的“应用商店”，可以使用docker pull命令下载到别人编写好的image，这样你就不用自己编写dockerfile了。docker registry可以用来存放各种image，公共的可以供任何人下载image的仓库就是docker Hub。

    这个命令的实现也很简单，那就是用户通过docker client发送命令，docker daemon接收到命令后向docker registry发送image下载请求，下载后存放在本地，这样我们就可以使用image了。

### Docker的底层
docker基于Linux内核提供这样几项功能实现的：
- **NameSpace**:Linux中的PID、IPC、网络等资源是全局的，而NameSpace机制是一种资源隔离方案，在该机制下这些资源就不再是全局的了，而是属于某个特定的NameSpace，各个NameSpace下的资源互不干扰，这就使得每个NameSpace看上去就像一个独立的操作系统一样，但是只有NameSpace是不够。
- **Control groups**:虽然有了NameSpace技术可以实现资源隔离，但进程还是可以不受控的访问系统资源，比如CPU、内存、磁盘、网络等，为了控制容器中进程对资源的访问，Docker采用control groups技术(也就是cgroup)，有了cgroup就可以控制容器中进程对系统资源的消耗了，比如你可以限制某个容器使用内存的上限、可以在哪些CPU上运行等等。

## K8S
