# Nuclei Poc 全网收集
NucleiPocGather，每日更新

这个项目是一个 Python 脚本，用于批量克隆 GitHub 项目，获取 Nuclei POC，并将 POC 按类别分类存放到文件夹中。同时，使用 GitHub Action 每日自动运行脚本。
# POC 详情统计

> **当前项目 POC 更新时间：**`2025-10-20 13:45`

| ID | 标签      | 数量 | 目录       | 数量 | 严重性   | 数量 |
|:---| :-------- | :--- | :--------- | :--- | :------- | :--- |
| 1 | cve | 43973 | cve | 37138 | info | 25020 |
| 2 | wordpress | 38819 | other | 31851 | medium | 24324 |
| 3 | wp-plugin | 35951 | auth | 1637 | high | 14965 |
| 4 | tech | 18202 | detect | 1603 | low | 11341 |
| 5 | detect | 17534 | wordpress | 1299 | critical | 8517 |
| 6 | medium | 16803 | microsoft | 1226 | unknown | 124 |
| 7 | service | 13823 | remote_code_execution | 1105 | hight | 6 |
| 8 | low | 9970 | api | 941 | meduim | 3 |
| 9 | high | 6528 | sql_injection | 883 | none | 1 |
| 10 | http | 4566 | default | 675 | ciritical | 1 |

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

