"""
@File    : build_app.py
@Time    : 2024年11月26日13:46:44
@Author  : sinvon
@Desc    : 构建 .app 文件 - macOS
"""
import subprocess
import os
from pyapp.utils.ConfigManager import ConfigManager

app_name = ConfigManager.get_value_by_key('app_name')

# 设置工作目录
work_dir = os.path.abspath('../..')
output_dir = os.path.join(work_dir, 'output')
main_file = os.path.join(work_dir, 'main.py')
dist_dir = os.path.join(work_dir, 'dist')

command = [
    'pyinstaller',
    '--onefile',
    '--noconsole',
    f'--add-data={os.path.join(work_dir, "config.json")}:.',  # macOS 分隔符为 ":"
    f'--add-data={os.path.join(work_dir, "assets")}:assets',
    f'--add-data={dist_dir}:dist',
    '--name', f'{app_name}',
    '--workpath', os.path.join(work_dir, 'build'),
    '--distpath', output_dir,
    '--windowed',  # macOS 窗口应用
    # '--target-arch=x86_64',  # 可选，指定架构
    main_file
]

try:
    subprocess.run(command, check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with error code: {e.returncode}")
    print(f"Command output: {e.output}")

print(f"Successfully created {os.path.join(output_dir, f'{app_name}.app')}")
