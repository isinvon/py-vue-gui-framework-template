"""
@File    : build_deb.py
@Time    : 2024年11月26日13:46:44
@Author  : sinvon
@Desc    : 构建 .deb 文件 - Linux (Debian 系)
"""
import shutil
import subprocess
import os
from pyapp.utils.ConfigManager import ConfigManager

app_name = ConfigManager.get_value_by_key('app_name')

# 设置工作目录
work_dir = os.path.abspath('../..')
output_dir = os.path.join(work_dir, 'output')
main_file = os.path.join(work_dir, 'main.py')
dist_dir = os.path.join(work_dir, 'dist')

# 检查依赖命令是否存在
if not shutil.which("fpm"):
    raise EnvironmentError("请先安装 fpm 工具 (https://github.com/jordansissel/fpm)")

# 创建临时打包目录
deb_package_dir = os.path.join(output_dir, f"{app_name}_deb")
os.makedirs(deb_package_dir, exist_ok=True)

# 将文件复制到临时目录
subprocess.run(['cp', '-r', dist_dir, os.path.join(deb_package_dir, 'dist')])
subprocess.run(['cp', os.path.join(work_dir, 'config.json'), deb_package_dir])

# 使用 fpm 打包 .deb
command = [
    'fpm',
    '-s', 'dir',
    '-t', 'deb',
    '-n', app_name,
    '-v', '1.0.0',
    '--prefix', '/opt/myapp',
    '-C', deb_package_dir
]

try:
    subprocess.run(command, check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with error code: {e.returncode}")
    print(f"Command output: {e.output}")

print(f"Successfully created {os.path.join(output_dir, f'{app_name}.deb')}")
