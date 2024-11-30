"""
@File    : build_tar_gz.py
@Time    : 2024年11月26日13:46:44
@Author  : sinvon
@Desc    : 构建 .tar.gz 文件
"""
import tarfile
import os
from pyapp.utils.ConfigManager import ConfigManager

app_name = ConfigManager.get_value_by_key('app_name')

# 设置工作目录
work_dir = os.path.abspath('../..')
output_dir = os.path.join(work_dir, 'output')
archive_name = os.path.join(output_dir, f"{app_name}.tar.gz")
files_to_include = [os.path.join(work_dir, 'config.json'), os.path.join(work_dir, 'dist')]

os.makedirs(output_dir, exist_ok=True)

# 创建 tar.gz 压缩包
with tarfile.open(archive_name, "w:gz") as tar:
    for file in files_to_include:
        tar.add(file, arcname=os.path.basename(file))

print(f"Successfully created {archive_name}")
