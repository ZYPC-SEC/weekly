# 学习 GitHub 与 Markdown 代码 Writeup

## 目录

1. Git 与 GitHub 的关系
2. 环境配置与账号准备
3. 核心概念：三个区域
4. 本地工作流：add → commit → push
5. 远程操作：clone、pull、branch
6. 团队协作：Fork + Pull Request
7. Markdown 基础语法

---

## 1. Git 与 GitHub 的关系

Git 是分布式版本控制系统，GitHub 是基于 Git 的远程托管与协作平台。

两者的分工：

- **Git**：在本地记录每一次修改，支持版本回退、分支切换。
- **GitHub**：把本地仓库托管到远程，让多人可以围绕同一个仓库协作。

常见误区：`commit` 之后别人并不会立刻看到。`commit` 只保存到本地仓库，还需要 `push` 到 GitHub。

---

## 2. 环境配置与账号准备

### 2.1 安装 Git 与验证

从 [git-scm.com](https://git-scm.com) 下载安装包，安装后终端执行：

    git --version

输出版本号即安装成功。

### 2.2 配置用户信息（必做）

    git config --global user.name "YourGitHubUsername"
    git config --global user.email "your_email@example.com"

用户名和邮箱应与 GitHub 账号一致，否则提交记录无法正确关联。

### 2.3 SSH 密钥（推荐）

SSH 方式推送代码不需要每次输入密码。生成密钥并添加到 GitHub：

    ssh-keygen -t ed25519 -C "your_email@example.com"

将 `~/.ssh/id_ed25519.pub` 的内容复制到 GitHub → Settings → SSH and GPG keys → New SSH key。

---

## 3. 核心概念：三个区域

Git 的工作围绕三个区域展开：

| 区域 | 含义 |
| --- | --- |
| **工作区** | 你实际编辑文件的目录 |
| **暂存区** | 临时存放“准备提交”的修改 |
| **本地仓库** | Git 保存版本历史的地方（`.git` 目录） |

三个区域之间由三条命令驱动：

    工作区  --git add-->  暂存区  --git commit-->  本地仓库  --git push-->  GitHub

`git status` 用于随时查看当前处于哪一步、哪些文件已被暂存。

---

## 4. 本地工作流：add → commit → push

这是最基础、使用频率最高的流程。

### 4.1 初始化仓库

    git init

将当前目录变成 Git 仓库，生成 `.git` 目录。

### 4.2 暂存修改

    git add .              # 暂存所有修改
    git add README.md      # 只暂存指定文件

### 4.3 提交

    git commit -m "docs: update readme"

`-m` 后面是提交信息，应简短说明本次改动内容。

### 4.4 推送到 GitHub

    git push

将本地提交上传到远程仓库。第一次推送需要指定远程地址和分支：

    git push -u origin main

### 4.5 完整示例

    git status
    git add .
    git commit -m "feat: add login page"
    git push

建议养成每次提交前先看 `git status` 的习惯。

---

## 5. 远程操作：clone、pull、branch

### 5.1 克隆远程仓库

    git clone git@github.com:用户名/仓库名.git

或使用 HTTPS：

    git clone https://github.com/用户名/仓库名.git

SSH 方式需要在 GitHub 配置公钥；HTTPS 方式需要输入账号和 Personal Access Token。

### 5.2 拉取远程更新

    git pull

将 GitHub 上的最新改动下载并合并到本地。多人协作时，开始工作前先 `pull` 可以减少冲突。

### 5.3 分支

分支让不同功能或修复互相隔离，避免直接改动 `main`。

    git branch                 # 查看分支
    git switch -c new-feature  # 创建并切换到新分支
    git switch main            # 切回主分支

在新分支上完成修改并 `commit`、`push` 后，再通过 Pull Request 合并到 `main`，是团队协作的标准做法。

---

## 6. 团队协作：Fork + Pull Request

参与别人的开源项目，或没有仓库直接写入权限时，使用 Fork + Pull Request 流程。

### 6.1 流程

    1. Fork 对方仓库 → 到自己账号下
    2. Clone 自己的 Fork 到本地
    3. 创建功能分支
    4. 修改、commit、push 到自己的 Fork
    5. 在 GitHub 页面向原仓库发起 Pull Request
    6. 对方 Review 后合并

### 6.2 Fork 与直接 Push 的区别

| 方式 | 适用场景 |
| --- | --- |
| **直接 Push**（被邀请为 collaborator） | 你有仓库的写入权限 |
| **Fork + Pull Request** | 公开项目、外部贡献者、无直接写入权限 |

PR（Pull Request）不仅是“提交代码”，也是讨论、审查和记录决策的场所。

---

## 7. Markdown 基础语法

Markdown 是纯文本标记语言，用少量符号完成排版，可直接在 GitHub 的 README、Issue、PR 描述中渲染。

### 7.1 标题

    # 一级标题
    ## 二级标题
    ### 三级标题

`#` 的数量对应标题级别，1–6 级。

### 7.2 强调

    **加粗**
    *斜体*
    ~~删除线~~

### 7.3 列表

无序列表：

    - 项目一
    - 项目二

有序列表：

    1. 第一步
    2. 第二步

任务列表：

    - [x] 已完成
    - [ ] 未完成

### 7.4 代码

行内代码用反引号：

    执行 `git status` 查看状态。

代码块用三个反引号，并标注语言以获得语法高亮：

    ```python
    print("Hello")
    ```

如果要在 Markdown 中展示代码块标记本身，用四个反引号包裹三个反引号即可。

### 7.5 链接与图片

    [链接文字](https://example.com)
    ![替代文本](image.png)

图片语法比链接多一个 `!`。

### 7.6 表格

    | 命令 | 作用 |
    | --- | --- |
    | `git add` | 暂存修改 |
    | `git commit` | 提交到本地 |

用 `|` 分隔单元格，第二行 `---` 分隔表头与表体。冒号可控制对齐：`:---` 左对齐，`---:` 右对齐，`:---:` 居中。

### 7.7 引用与分隔线

    > 这是一段引用。

    ---

三个或更多 `-` 或 `*` 生成分隔线。

### 7.8 在 GitHub 上的实际用途

- **README.md**：仓库首页展示，用 Markdown 写项目说明、安装步骤、用法示例。
- **Issue / PR 描述**：用列表、代码块、任务列表清晰描述问题和改动。
- **个人 Profile README**：创建与用户名同名的仓库，其中的 `README.md` 会显示在 GitHub 个人主页上。

---

