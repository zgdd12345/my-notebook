[适用于Linux的windows子系统](https://learn.microsoft.com/zh-cn/windows/wsl/about "适用于Linux的windows子系统")

适用于 Linux 的 Windows 子系统（WSL）是 Windows 的一项功能，可用于在 Windows 计算机上运行 Linux 环境，而无需单独的虚拟机或双重启动。 WSL 旨在为想要同时使用 Windows 和 Linux 的开发人员提供无缝高效的体验。

- 使用 WSL 安装和运行各种 Linux 分发版，例如 Ubuntu、Debian、Kali 等。 [安装 Linux 分发版](https://learn.microsoft.com/zh-cn/windows/wsl/install) 并从 [Microsoft 应用商店](https://learn.microsoft.com/zh-cn/windows/wsl/compare-versions#wsl-in-the-microsoft-store)接收自动更新， [导入 Microsoft 应用商店中不可用的 Linux 分发版](https://learn.microsoft.com/zh-cn/windows/wsl/use-custom-distro)，或 [生成自己的自定义 Linux 分发版](https://learn.microsoft.com/zh-cn/windows/wsl/build-custom-distro)。
- 将文件存储在独立的 Linux 文件系统中，特定于已安装的分发版。
- 运行命令行工具，例如 BASH。
- 运行常见的 BASH 命令行工具，例如`grep`，`sed``awk`或其他 ELF-64 二进制文件。
- 运行 Bash 脚本和 GNU/Linux 命令行应用程序，包括：
    - 工具：vim、emacs、tmux
    - 语言： [NodeJS](https://learn.microsoft.com/zh-cn/windows/nodejs/setup-on-wsl2)、JavaScript、 [Python](https://learn.microsoft.com/zh-cn/windows/python/web-frameworks)、Ruby、C/C++、C# & F#、Rust、Go 等。
    - 服务：SSHD、 [MySQL](https://learn.microsoft.com/zh-cn/windows/wsl/tutorials/wsl-database)、Apache、lighttpd、 [MongoDB](https://learn.microsoft.com/zh-cn/windows/wsl/tutorials/wsl-database)、 [PostgreSQL](https://learn.microsoft.com/zh-cn/windows/wsl/tutorials/wsl-database)。
- 使用自己的 GNU/Linux 分发包管理器安装其他软件。
- 使用类似 Unix 的命令行 shell 调用 Windows 应用程序。
- 在 Windows 上调用 GNU/Linux 应用程序。
- 运行直接集成到 Windows 桌面的 [GNU/Linux 图形应用程序](https://learn.microsoft.com/zh-cn/windows/wsl/tutorials/gui-apps)
- 使用设备 [GPU 加速 Linux 上运行的机器学习工作负载。](https://learn.microsoft.com/zh-cn/windows/wsl/tutorials/gpu-compute)

## WSL2
安装 Linux 分发版时，WSL 2 是默认发行版类型。 WSL 2 使用虚拟化技术在轻型实用工具虚拟机（VM）内运行 Linux 内核。 Linux 分发版作为 WSL 2 托管 VM 内的独立容器运行。 通过 WSL 2 运行的 Linux 分发版将共享同一网络命名空间、设备树（而非 `/dev/pts`）、CPU/内核/内存/交换、 `/init` 二进制文件，但有自己的 PID 命名空间、装载命名空间、用户命名空间、Cgroup 命名空间和 `init` 进程。

WSL 2 **提高了文件系统性能** ，并且与 WSL 1 体系结构相比增加了 **完整的系统调用兼容性** 。 详细了解 [WSL 1 和 WSL 2 的比较](https://learn.microsoft.com/zh-cn/windows/wsl/compare-versions)方式。

可以使用 WSL 1 或 WSL 2 体系结构运行单个 Linux 分发版。 可以随时升级或降级每个分发，并且可以并行运行 WSL 1 和 WSL 2 分发版。 请参阅 [“设置 WSL 版本”命令](https://learn.microsoft.com/zh-cn/windows/wsl/basic-commands#set-default-wsl-version)。