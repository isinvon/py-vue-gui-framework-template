import sys
import webview

from pyapp.utils.GradientPrinter import GradientPrinter
from pyapp.utils.ConfigManager import ConfigManager


def start_webview():
    """ 
    - Detects environment (development or production) and starts the WebView accordingly.
    - When using PyInstaller to package Python, it creates a temporary folder and stores the path in sys._MEIPASS.
    - This allows detection of whether the app is in production or development mode.
    """
    # prod mode
    if hasattr(sys, '_MEIPASS'):
        vue_dist_path = ConfigManager.get_resource_path('dist')
        vue_dist_path = vue_dist_path.replace("\\", "/")
        print(f"Vue dist path: {vue_dist_path}")  # debug
        webview_url = f'file://{vue_dist_path}/index.html'
    # dev mode
    else:
        app_gui_port = ConfigManager.get_value_by_key(key='gui_port')
        webview_url = f'http://localhost:{app_gui_port}'

    app_name = ConfigManager.get_value_by_key(key='app_name')
    app_width = ConfigManager.get_value_by_key(key='width')
    app_height = ConfigManager.get_value_by_key(key='height')

    # Start WebView
    webview.create_window(
        title=app_name,
        url=webview_url,
        width=app_width,
        height=app_height
    )
    webview.start()


if __name__ == '__main__':
    GradientPrinter.gradient_text(">>>> ======== Python is running ======== >>>>", start_color=(64, 169, 255),
                                  end_color=(255, 218, 53))
    start_webview()
