# Nuclei Poc 全网收集
NucleiPocGather，每日更新

这个项目是一个 Python 脚本，用于批量克隆 GitHub 项目，获取 Nuclei POC，并将 POC 按类别分类存放到文件夹中。同时，使用 GitHub Action 每日自动运行脚本。
# POC 详情统计

> **当前项目 POC 更新时间：**`2024-10-04 12:58`

| ID | 标签      | 数量 | 目录       | 数量 | 严重性   | 数量 |
|:---| :-------- | :--- | :--------- | :--- | :------- | :--- |
| 1 | cve | 29267 | cve | 19871 | medium | 15589 |
| 2 | wordpress | 26140 | other | 12857 | high | 10639 |
| 3 | wp-plugin | 24165 | auth | 1623 | info | 8257 |
| 4 | medium | 12093 | wordpress | 1239 | low | 6030 |
| 5 | high | 5614 | remote_code_execution | 955 | critical | 4771 |
| 6 | low | 4974 | detect | 934 | unknown | 67 |
| 7 | tech | 3641 | sql | 687 | meduim | 5 |
| 8 | detect | 2821 | microsoft | 685 | informative | 4 |
| 9 | critical | 1994 | sql_injection | 644 | hight | 3 |
| 10 | panel | 1708 | default | 612 | unknnown | 1 |

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

