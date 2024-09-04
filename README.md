# Nuclei Poc 全网收集

<a href="https://github.com/2897087026/NucleiPocGather/stargazers"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/2897087026/NucleiPocGather?color=yellow&logo=riseup&logoColor=yellow&style=flat-square"></a>
<a href="https://github.com/2897087026/NucleiPocGather/network/members"><img alt="GitHub forks" src="https://img.shields.io/github/forks/2897087026/NucleiPocGather?color=orange&style=flat-square"></a>
<a href="https://github.com/2897087026/NucleiPocGather/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/2897087026/NucleiPocGather?color=red&style=flat-square"></a>

NucleiPocGather，每日更新

这个项目是一个 Python 脚本，用于批量克隆 GitHub 项目，获取 Nuclei POC，并将 POC 按类别分类存放到文件夹中。同时，使用 GitHub
Action 每日自动运行脚本。

## 如何使用

### 克隆项目

克隆这个项目到本地：

```bash
git clone https://github.com/2897087026/NucleiPocGather.git
```

进入项目目录：

```bash
cd NucleiPocGather
```

### 配置

在 `repo.csv` 文件中配置监控 GitHub 项目信息。

### 运行脚本

运行 Python 脚本：

```bash
python NucleiPocGather.py
```

### GitHub Action

在 GitHub 仓库中设置 Action，以便每日自动运行脚本。

> 需要配置`Workflow permissions`为`Read and write`权限

## 文件结构

- `NucleiPocGather.py`: 收集全网 Nuclei POC 的脚本文件。
- `repo.csv`: Nuclei POC 仓库列表。
- `poc.txt`: 已存档 POC 列表。
- `poc/`: 存放分类后的 Nuclei POC 文件夹。

