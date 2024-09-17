import os
import yaml
import hashlib
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor


def hash_content(content):
    """计算内容的哈希值."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def read_fields_from_yaml(file_path):
    """读取 YAML 文件中的指定字段并返回哈希值和文件名."""
    fields_to_read = ['requests', 'tcp', 'http', 'file', 'fingerprint', 'request', 'workflows', 'rules', 'network']
    found_fields = []  # 存储找到的字段内容

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

            # 查找指定字段
            for field in fields_to_read:
                value = data.get(field)
                if value is not None:
                    found_fields.append(str(value))  # 将找到的值转换为字符串并加入列表

            # 如果找到字段，则计算哈希值
            if found_fields:
                combined_content = "\n".join(found_fields)
                return hash_content(combined_content), file_path

    except Exception:
        pass
    return None, None  # 未找到任何字段


def process_file(file_path):
    """处理文件并返回其哈希值和路径."""
    return read_fields_from_yaml(file_path)


def traverse_directory_and_read_fields(dir_path):
    """递归遍历目录并读取所有 YAML 文件中的指定字段."""
    hash_dict = {}  # 存储哈希值和文件名的字典
    yaml_files = []

    # 收集所有 YAML 文件
    for root, _, files in os.walk(dir_path):
        for filename in files:
            if filename.endswith('.yaml') or filename.endswith('.yml'):
                yaml_files.append(os.path.join(root, filename))

    # 使用多线程处理文件并打印进度条
    with ThreadPoolExecutor() as executor:
        results = list(tqdm(executor.map(process_file, yaml_files), total=len(yaml_files), desc="进度条: "))

    for file_hash, valid_file_path in results:
        if file_hash and valid_file_path:
            # 如果哈希值已经存在，添加到列表中
            if file_hash in hash_dict:
                hash_dict[file_hash].append(valid_file_path)
            else:
                hash_dict[file_hash] = [valid_file_path]

    # 打印具有相同哈希值的文件名，并删除多余的文件
    same_file_count = 0  # 记录相同文件的数量
    for file_hash, file_paths in hash_dict.items():
        if len(file_paths) > 1:
            # 找到文件名最短的文件
            shortest_file = min(file_paths, key=len)
            print(f"[+] 文件哈希值: {file_hash} -> 相同的文件: {', '.join(file_paths)}")
            print(f"[+] 保留文件: [{shortest_file}]")

            # 删除其他文件
            for file_path in file_paths:
                if file_path != shortest_file:
                    os.remove(file_path)
                    print(f"[-] 已删除文件: {file_path}")

            same_file_count += len(file_paths)

    print(f"\n[+] 总共有 {same_file_count} 个相同的文件。")


def deWeight():
    poc_directory = "poc"  # 替换为你的 POC 目录路径
    traverse_directory_and_read_fields(poc_directory)


if __name__ == "__main__":
    poc_directory = "poc"  # 替换为你的 POC 目录路径
    traverse_directory_and_read_fields(poc_directory)
