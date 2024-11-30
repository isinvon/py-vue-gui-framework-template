"""
@File    : build_rpm.py
@Time    : 2024年11月26日13:46:44
@Author  : sinvon
@Desc    : 构建 .rpm 文件 - Linux (RedHat 系)
"""
import shutil
import subprocess
import os
from pyapp.utils.ConfigManager import ConfigManager

app_name = ConfigManager.get_value_by_key('app_name')

# 设置工作目录
work_dir = os.path.abspath('../..')
output_dir = os.path.join(work_dir, 'output')

# 检查依赖命令是否存在
if not shutil.which("fpm"):
    raise EnvironmentError("请先安装 fpm 工具 (https://github.com/jordansissel/fpm)")

# 创建打包命令
command = [
    'fpm',
    '-s', 'dir',
    '-t', 'rpm',
    '-n', app_name,
    '-v', '1.0.0',
    '--prefix', '/opt/myapp',
    '-C', work_dir
]

subprocess.run(command)

print(f"Successfully created {os.path.join(output_dir, f'{app_name}.rpm')}")
