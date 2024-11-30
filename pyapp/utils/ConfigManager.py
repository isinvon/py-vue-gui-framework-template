import json
import os
import sys


class ConfigManager:
    """
    load config file and return json data
    """

    def __init__(self):
        self.config_json_path = 'config.json'

    @staticmethod
    def get_resource_path(relative_path):
        """ Get the absolute path to the resource, works for dev and for PyInstaller """
        try:
            # When the program is packaged by pyInstaller will create a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except AttributeError:
            work_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            base_path = work_dir

        return os.path.join(base_path, relative_path)

    @staticmethod
    def load_and_get_json():
        """
        read and load json config file, finally return the json data(type: dict)
        """
        config_file = ConfigManager.get_resource_path('config.json')
        with open(config_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    @staticmethod
    def get_value_by_key(key: str):
        """
        get value by key
        :param key:
        :return:
        """
        data = ConfigManager.load_and_get_json()
        return data[key]
