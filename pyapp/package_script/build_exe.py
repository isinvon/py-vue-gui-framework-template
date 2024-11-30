"""
@File    : build_exe.py
@Time    : 2024年11月26日13:46:44
@Author  : sinvon
@Desc    : 构建 .exe 文件 - Windows
"""
import os
import subprocess
import sys

work_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
pyapp_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
current_dir = os.path.dirname(os.path.abspath(__file__))

# 一次性向系统中添加多个路径(extend是append的列表形式)
sys.path.extend([work_dir, pyapp_dir, current_dir])

from pyapp.utils.ConfigManager import ConfigManager

app_name = ConfigManager.get_value_by_key('app_name')

# 设置工作目录
output_dir = os.path.join(work_dir, 'output')  # 修改输出目录名称
main_file = os.path.join(work_dir, 'main.py')
dist_dir = os.path.join(work_dir, 'dist')  # 前端项目 dist 目录

command = [
    'pyinstaller',
    '--onefile',
    '--noconsole',
    f'--add-data={os.path.join(work_dir, "config.json")};.',  # 添加配置文件到exe中的根目录
    f'--add-data={os.path.join(work_dir, "assets")};assets',  # 添加资源目录到exe中根目录下的assets中
    f'--add-data={dist_dir};dist',  # 添加 dist 目录及其内容到exe中根目录下的dist中
    '--name', f'{app_name}',  # 可执行文件名称
    '--workpath', os.path.join(work_dir, 'build'),  # 指定临时文件目录
    '--distpath', output_dir,  # 指定输出目录
    main_file  # 主入口文件
]

# 执行 PyInstaller 命令
subprocess.run(command)

print(f"Successfully created {os.path.join(output_dir, f'{app_name}.exe')}")
