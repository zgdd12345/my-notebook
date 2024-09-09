# Docker 跨平台的一些问题
## Docker for Mac
是运行在 Hypervisor 上的 一个 HyperKit 实现，毕竟还是虚拟化加容器的实现方式，而不是内核级别的实现。(虚拟机) Docker for Mac不使用VirtualBox，而是使用HyperKit，一个轻量级的macOS虚拟化解决方案，它在MacOS 10.10 Yosemite及更高版本中的Hypervisor.framework中编译。
docker是如何跨平台的 -> 在mac下运行docker实际上是先开启了一个linux虚拟机，然后在虚拟机上运行docker。

## docker是如何实现应用隔离的
 -> docker是容器，它将所有的访问文件和操作系统的api重新定向了，让应用内感觉自己在一个独立的操作系统上运行，而docker拦截了api调用，并且把那些全局的对操作系统的访问进行了包装，使得程序不会真的访问它们。

## 宿主如果和容器系统不同的话，那不是和虚拟机一样，一层层的调用，那么 Docker 和虚拟机还有什么差别？

要把 Windows 和 Linux 分清楚，更要把内核(kernel)和用户空间(userland)分清楚。

容器内的进程是直接运行于宿主内核的，这点和宿主进程一致，只是容器的 userland 不同，容器的 userland 由容器镜像提供，也就是说镜像提供了 rootfs。

假设宿主是 Ubuntu，容器是 CentOS。CentOS 容器中的进程会直接向 Ubuntu 宿主内核发送 syscall，而不会直接或间接的使用任何 Ubuntu 的 userland 的库。

这点和虚拟机有本质的不同，虚拟机是虚拟环境，在现有系统上虚拟一套物理设备，然后在虚拟环境内运行一个虚拟环境的操作系统内核，在内核之上再跑完整系统，并在里面调用进程。

还以上面的例子去考虑，虚拟机中，CentOS 的进程发送 syscall 内核调用，该请求会被虚拟机内的 CentOS 的内核接到，然后 CentOS 内核访问虚拟硬件时，由虚拟机的服务软件截获，并使用宿主系统，也就是 Ubuntu 的内核及 userland 的库去执行。

而且，Linux 和 Windows 在这点上非常不同。Linux 的进程是直接发 syscall 的，而 Windows 则把 syscall 隐藏于一层层的 DLL 服务之后，因此 Windows 的任何一个进程如果要执行，不仅仅需要 Windows 内核，还需要一群服务来支撑，所以如果 Windows 要实现类似的机制，容器内将不会像 Linux 这样轻量级，而是非常臃肿。看一下微软移植的 Docker 就非常清楚了。

所以不要把 Docker 和虚拟机弄混，Docker 容器只是一个进程而已，只不过利用镜像提供的 rootfs 提供了调用所需的 userland 库支持，使得进程可以在受控环境下运行而已，它并没有虚拟出一个机器出来。