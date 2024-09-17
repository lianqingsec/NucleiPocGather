import os
import yaml
import concurrent.futures
from collections import defaultdict, Counter
from datetime import datetime
from tqdm import tqdm


def process_yaml_file(file_path):
    """处理单个 YAML 文件，返回 tags 列表和 severity 值."""
    tags = []
    severity = None
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)  # 读取 YAML 文件
            if 'info' in data:
                # 获取 tags 字符串并分割成列表
                tags = [tag.strip() for tag in data['info'].get('tags', '').split(',')] if 'tags' in data[
                    'info'] else []
                # 获取 severity 值并转换为小写
                severity = data['info'].get('severity', None)
                if severity:
                    severity = severity.lower()
    except Exception:
        pass
    return tags, severity


def count_tags_and_severity_in_yaml_files(directory):
    """递归遍历目录，统计所有 YAML 文件中的 info.tags 和 info.severity 字段."""
    all_tags = []  # 存储所有标签
    severities = []  # 存储所有 severity 值

    # 递归遍历目录，收集所有 YAML 文件
    yaml_files = [os.path.join(root, filename) for root, _, files in os.walk(directory)
                  for filename in files if filename.endswith(('.yaml', '.yml'))]

    # 使用多线程处理文件
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for tags, severity in tqdm(executor.map(process_yaml_file, yaml_files), total=len(yaml_files),
                                   desc="处理 YAML 文件"):
            all_tags.extend(tags)
            if severity:
                severities.append(severity)

    return all_tags, severities


def get_top_n_items(items_list, n=10):
    """获取计数的前 N 名."""
    counter = Counter(items_list)
    return counter.most_common(n)


def get_current_time():
    """获取当前时间并按指定格式返回."""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M")


def count_yaml_files_in_subdirectories(directory):
    """计算每个子目录中的 YAML 文件数量，并返回前 10 个目录及其数量."""
    yaml_counts = defaultdict(int)

    # 获取目录下的所有条目
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            yaml_counts[item] = sum(1 for subitem in os.listdir(item_path)
                                    if subitem.endswith(('.yaml', '.yml')))

    # 按数量排序，并获取前 10 个
    return sorted(yaml_counts.items(), key=lambda x: x[1], reverse=True)[:10]


def update_table(content, new_data):
    """更新表格内容."""
    for i, (index, label, count, directory, dir_count, severity, sev_count) in enumerate(new_data):
        line_index = 10 + i  # 假设表格从第二行开始
        content[
            line_index] = f"| {index} | {label} | {count} | {directory} | {dir_count} | {severity} | {sev_count} |\n"
    return content


def update_readme(poc_directory_count, yaml_file_count, new_table_data):
    """更新 README.md 文件."""
    current_time = get_current_time()

    # 读取 README.md 文件
    with open('README.md', 'r', encoding='utf-8') as file:
        content = file.readlines()

    for i, line in enumerate(content):
        if "当前项目 POC 更新时间：" in line:
            content[i] = f"> **当前项目 POC 更新时间：**`{current_time}`\n"
        if "个目录" in line and "个文件" in line:
            content[i] = f"{poc_directory_count} 个目录，{yaml_file_count} 个文件\n"
        if "| ID | 标签      | 数量 | 目录       | 数量 | 严重性   | 数量 |" in line:
            content = update_table(content, new_table_data)
            break

    with open('README.md', 'w', encoding='utf-8') as file:
        file.writelines(content)


def wirte_readme():
    poc_directory = "poc"  # 替换为你的 poc 目录路径

    # 统计所有 YAML 文件数量
    yaml_file_count = sum(1 for root, _, files in os.walk(poc_directory)
                          for filename in files if filename.endswith(('.yaml', '.yml')))
    print(f"在 '{poc_directory}' 目录中找到 {yaml_file_count} 个 YAML 文件.")

    # 统计每个子目录中的 YAML 文件数量并获取前 10 个
    top_yaml_counts = count_yaml_files_in_subdirectories(poc_directory)
    print("\n前 10 个目录及其 YAML 文件数量:")
    for subdir, count in top_yaml_counts:
        print(f"{subdir}: {count} 个 YAML 文件")

    # 提取前 10 个目录名和次数
    top_dirs, top_dirs_number = zip(*top_yaml_counts)

    # 统计所有 YAML 文件中的 info.tags 和 info.severity 字段
    all_tags, severities = count_tags_and_severity_in_yaml_files(poc_directory)

    # 获取前 10 名标签和 severity
    top_tags = get_top_n_items(all_tags, n=10)
    top_severities = get_top_n_items(severities, n=10)

    print("\n前 10 个标签及其出现次数:")
    for tag, count in top_tags:
        print(f"{tag}: {count} 次")

    print("\n前 10 个 severity 及其出现次数:")
    for severity, count in top_severities:
        print(f"{severity}: {count} 次")

    # 提取标签和 severity 名称与数量
    top_tag = [tag for tag, _ in top_tags]
    top_tags_number = [count for _, count in top_tags]
    top_severitie = [severity for severity, _ in top_severities]
    top_severities_number = [count for _, count in top_severities]

    # 设置数据
    new_table_data = [
        (i + 1, f'{top_tag[i]}', int(top_tags_number[i]), f'{top_dirs[i]}', int(top_dirs_number[i]),
         f'{top_severitie[i] if i < len(top_severitie) else ""}',
         int(top_severities_number[i] if i < len(top_severities_number) else 0))
        for i in range(10)
    ]

    # 更新 README.md 文件
    update_readme(len(top_yaml_counts), yaml_file_count, new_table_data)


if __name__ == "__main__":
    poc_directory = "poc"  # 替换为你的 poc 目录路径

    # 统计所有 YAML 文件数量
    yaml_file_count = sum(1 for root, _, files in os.walk(poc_directory)
                          for filename in files if filename.endswith(('.yaml', '.yml')))
    print(f"在 '{poc_directory}' 目录中找到 {yaml_file_count} 个 YAML 文件.")

    # 统计每个子目录中的 YAML 文件数量并获取前 10 个
    top_yaml_counts = count_yaml_files_in_subdirectories(poc_directory)
    print("\n前 10 个目录及其 YAML 文件数量:")
    for subdir, count in top_yaml_counts:
        print(f"{subdir}: {count} 个 YAML 文件")

    # 提取前 10 个目录名和次数
    top_dirs, top_dirs_number = zip(*top_yaml_counts)

    # 统计所有 YAML 文件中的 info.tags 和 info.severity 字段
    all_tags, severities = count_tags_and_severity_in_yaml_files(poc_directory)

    # 获取前 10 名标签和 severity
    top_tags = get_top_n_items(all_tags, n=10)
    top_severities = get_top_n_items(severities, n=10)

    print("\n前 10 个标签及其出现次数:")
    for tag, count in top_tags:
        print(f"{tag}: {count} 次")

    print("\n前 10 个 severity 及其出现次数:")
    for severity, count in top_severities:
        print(f"{severity}: {count} 次")

    # 提取标签和 severity 名称与数量
    top_tag = [tag for tag, _ in top_tags]
    top_tags_number = [count for _, count in top_tags]
    top_severitie = [severity for severity, _ in top_severities]
    top_severities_number = [count for _, count in top_severities]

    # 设置数据
    new_table_data = [
        (i + 1, f'{top_tag[i]}', int(top_tags_number[i]), f'{top_dirs[i]}', int(top_dirs_number[i]),
         f'{top_severitie[i] if i < len(top_severitie) else ""}',
         int(top_severities_number[i] if i < len(top_severities_number) else 0))
        for i in range(10)
    ]

    # 更新 README.md 文件
    update_readme(len(top_yaml_counts), yaml_file_count, new_table_data)
