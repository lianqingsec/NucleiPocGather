# Nuclei Poc 全网收集
NucleiPocGather，每日更新

这个项目是一个 Python 脚本，用于批量克隆 GitHub 项目，获取 Nuclei POC，并将 POC 按类别分类存放到文件夹中。同时，使用 GitHub Action 每日自动运行脚本。
# POC 详情统计

> **当前项目 POC 更新时间：**`2026-05-07 15:28`

| ID | 标签      | 数量 | 目录       | 数量 | 严重性   | 数量 |
|:---| :-------- | :--- | :--------- | :--- | :------- | :--- |
| 1 | cve | 73208 | cve | 49538 | medium | 32324 |
| 2 | wordpress | 67197 | other | 41533 | info | 25044 |
| 3 | wp-plugin | 62103 | auth | 3527 | low | 24399 |
| 4 | medium | 24892 | remote_code_execution | 2840 | high | 19766 |
| 5 | low | 23016 | sql | 2506 | critical | 11822 |
| 6 | tech | 18291 | wordpress | 1998 | unknown | 101 |
| 7 | detect | 17522 | microsoft | 1660 | hight | 15 |
| 8 | production | 16107 | detect | 1404 | meduim | 14 |
| 9 | service | 13827 | sql_injection | 1034 | informative | 8 |
| 10 | candidate | 13705 | social | 733 | cretical | 2 |

**81 个目录，44572 个文件**
## 如何使用

### 克隆项目

克隆这个项目到本地：

```bash
git clone https://github.com/lianqingsec/NucleiPocGather.git
```

进入项目目录：

```bash
cd NucleiPocGather
```

### 配置

在 `repo.txt` 文件中配置监控 GitHub 项目信息。

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
- `DeWeight.py`: 对现有的 Nuclei POC 进行进一步去重的脚本文件。
- `WirteREADME.py`: 统计现有的 POC 并更新 README.md 文件。
- `repo.txt`: Nuclei POC 仓库列表。
- `poc.txt`: 已存档 POC 列表。
- `poc/`: 存放分类后的 Nuclei POC 文件夹。

