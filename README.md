# Nuclei Poc 全网收集
NucleiPocGather，每日更新

这个项目是一个 Python 脚本，用于批量克隆 GitHub 项目，获取 Nuclei POC，并将 POC 按类别分类存放到文件夹中。同时，使用 GitHub Action 每日自动运行脚本。
# POC 详情统计

> **当前项目 POC 更新时间：**`2025-06-20 13:28`

| ID | 标签      | 数量 | 目录       | 数量 | 严重性   | 数量 |
|:---| :-------- | :--- | :--------- | :--- | :------- | :--- |
| 1 | cve | 39199 | cve | 33375 | medium | 21556 |
| 2 | wordpress | 35407 | other | 26221 | info | 20380 |
| 3 | wp-plugin | 32949 | auth | 2496 | high | 13202 |
| 4 | medium | 15696 | wordpress | 1528 | low | 9977 |
| 5 | tech | 14787 | detect | 1310 | critical | 7162 |
| 6 | detect | 13779 | remote_code_execution | 860 | unknown | 91 |
| 7 | service | 11680 | microsoft | 750 | hight | 16 |
| 8 | low | 8801 | web | 698 | informative | 10 |
| 9 | high | 6237 | sql_injection | 639 | meduim | 7 |
| 10 | http | 4356 | api | 558 | cretical | 2 |

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

