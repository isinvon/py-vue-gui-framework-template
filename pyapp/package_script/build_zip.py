"""
@File    : build_zip.py
@Time    : 2024年11月26日13:46:44
@Author  : sinvon
@Desc    : 构建 .zip 文件
"""
import zipfile
import os
from pyapp.utils.ConfigManager import ConfigManager

app_name = ConfigManager.get_value_by_key('app_name')

# 设置工作目录
work_dir = os.path.abspath('../..')
output_dir = os.path.join(work_dir, 'output')
archive_name = os.path.join(output_dir, f"{app_name}.zip")
files_to_include = [os.path.join(work_dir, 'config.json'), os.path.join(work_dir, 'dist')]

os.makedirs(output_dir, exist_ok=True)

# 创建 zip 压缩包
with zipfile.ZipFile(archive_name, 'w') as zipf:
    for file in files_to_include:
        zipf.write(file, arcname=os.path.basename(file))

print(f"Successfully created {archive_name}")
