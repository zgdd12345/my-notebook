# Docker安装
<a href="https://yeasy.gitbook.io/docker_practice/install/ubuntu" title="超链接title">参考链接</a>

## Docker镜像
<a href="https://yeasy.gitbook.io/docker_practice/install/mirror" title="超链接title">参考链接</a>

## 离线安装
<a href="https://yeasy.gitbook.io/docker_practice/install/offline" title="超链接title">参考链接</a>

## 授权
将当前用户添加到 docker 组
将当前用户添加到 docker 组，这样就不需要每次运行 Docker 命令时使用 sudo。具体操作如下：

- 创建 docker 组（如果尚未创建）：

    sudo groupadd docker

- 将当前用户添加到 docker 组：

    sudo usermod -aG docker $USER
- 重新登录或重启系统

    为了使更改生效，您需要退出当前会话并重新登录，或者重启系统。

- 验证配置

    重新登录后，运行以下命令来测试是否可以正常使用 Docker：

    docker ps