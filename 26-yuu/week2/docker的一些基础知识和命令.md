# docker的一些基础知识和命令

首先对于`docker`我这里安装到的是 **Docker Desktop**，在学习 docker之前我们先了解几个常见名词的概念：

- **镜像（Image）**：像“安装包/模板”，比如 `nginx`
- **容器（Container）**：由镜像运行出来的实例
- **Dockerfile**：制作镜像的“配方”
- **端口映射**：`-p 电脑端口:容器端口`
- **数据卷（Volume）**：给容器保存数据，避免删容器后数据丢失

前提：先打开 **Docker Desktop**，等右下角图标稳定后再操作。

## 1.首先确认一下 docker 是否可以正常使用

```powershell
docker --version
docker info   更为详细的信息
```

```
运行第一条命令的结果：Docker version 29.9.1, build dfc520d
```

可以先使用一个简单的命令测试一下;

```powershell
docker run --rm hello-world  #--rm 表示容器运行完自动删除。
```

## 2. 最常用的容器命令

以 Nginx 网页服务为例：

```powershell
# 下载镜像（不写也会自动下载）
docker pull nginx

# 创建并启动容器：后台运行，名字叫 web，电脑 8080 端口映射到容器 80
docker run -d --name web -p 8080:80 nginx

# 查看正在运行的容器
docker ps

# 查看所有容器（包括已停止的）
docker ps -a

# 查看日志
docker logs web

# 持续查看日志，Ctrl+C 退出查看
docker logs -f web

# 进入容器内部
docker exec -it web sh
```

进入容器后可以执行：

```sh
ls
cat /etc/nginx/nginx.conf
exit
```

然后浏览器打开：

```
http://localhost:8080
```

能看到 Nginx 欢迎页就成功了。

## 3. 开启、停止、删除容器

```powershell
docker stop web       # 停止
docker start web      # 启动已有容器
docker restart web    # 重启

docker stop web
docker rm web         # 删除已停止的容器

# 容器正在运行时可强制删除
docker rm -f web
```

重点区别：

- `docker stop`：只是关机，容器还在
- `docker rm`：真正删掉容器
- `docker images`：查看镜像
- `docker rmi nginx`：删除镜像；如果还有容器使用它，需要先删容器

## 4. `docker run` 的常见参数

```powershell
docker run -d --name 容器名 -p 电脑端口:容器端口 镜像名
```

常用参数：

| 参数                       | 作用                             |
| -------------------------- | -------------------------------- |
| `-d`                       | 后台运行                         |
| `--name web`               | 给容器起名字                     |
| `-p 8080:80`               | 电脑 8080 端口映射到容器 80 端口 |
| `--rm`                     | 容器停止后自动删除               |
| `-it`                      | 交互式运行，常配合 `sh` / `bash` |
| `-v`                       | 挂载目录或数据卷                 |
| `--restart unless-stopped` | 自动重启策略                     |

例子：

```powershell
docker run -d --name web -p 8080:80 nginx
```

也可以先创建再启动：

```powershell
docker create --name web -p 8080:80 nginx
docker start web
```

## 5. 制作自己的镜像

新建一个文件夹，放进两个文件。

`index.html`：

```html
<h1>Hello Docker</h1>
```

`Dockerfile`：

```powershell
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
```

在该目录执行：docker 

```powershell
docker build -t my-web:1.0 .
docker run -d --name my-web -p 8081:80 my-web:1.0
```

打开：

```
http://localhost:8081
```

`-t my-web:1.0` 表示给镜像起名 `my-web`，版本标签是 `1.0`。

## 6. 数据挂载

把电脑目录映射进容器：

```powershell
docker run -d --name web -p 8080:80 -v "${PWD}:/usr/share/nginx/html:ro" nginx
```

- `${PWD}`：当前目录
- `/usr/share/nginx/html`：容器里的目录
- `:ro`：只读

也可以使用命名数据卷：

```powershell
docker volume create mydata
docker run -d --name web -v mydata:/data nginx
```

## 7. 清理空间

```powershell
docker system df                 # 查看 Docker 占用空间
docker container prune           # 删除所有已停止容器
docker image prune               # 删除没被使用的悬空镜像
docker system prune              # 清理未使用资源
```

`docker system prune -a` 会删得更彻底，包含所有未使用镜像，一般不建议使用。

暂且先学习这么多，剩下的慢慢补充喵！
