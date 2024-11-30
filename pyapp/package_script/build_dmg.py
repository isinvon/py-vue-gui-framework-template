"""
@File    : build_macos.py
@Time    : 2024年11月29日
@Author  : sinvon
@Desc    : 构建 .app ,然后通过 .app 构建 .dmg 文件 - macOS
"""
import subprocess
import os
from pyapp.utils.ConfigManager import ConfigManager

# 获取应用程序名称
app_name = ConfigManager.get_value_by_key('app_name')

# 设置工作目录
work_dir = os.path.abspath('../..')
output_dir = os.path.join(work_dir, 'output')
main_file = os.path.join(work_dir, 'main.py')
dist_dir = os.path.join(work_dir, 'dist')
app_path = os.path.join(output_dir, f'{app_name}.app')
dmg_path = os.path.join(output_dir, f'{app_name}.dmg')


def build_app():
    """构建 .app 文件"""
    print("=== Building .app file ===")
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
        main_file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Successfully created {app_path}")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error code: {e.returncode}")
        print(f"Command output: {e.output}")
        exit(1)


def build_dmg():
    """构建 .dmg 文件"""
    print("=== Building .dmg file ===")
    dmg_command = [
        'hdiutil', 'create',
        '-volname', app_name,
        '-fs', 'HFS+',
        '-srcfolder', app_path,
        '-format', 'UDBZ',
        dmg_path
    ]

    try:
        subprocess.run(dmg_command, check=True)
        print(f"Successfully created {dmg_path}")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error code: {e.returncode}")
        print(f"Command output: {e.output}")
        exit(1)


if __name__ == "__main__":
    build_app()
    build_dmg()
