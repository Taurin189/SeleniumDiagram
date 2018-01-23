# -*- coding:utf-8 -*-

import configparser


class ConfigReader:
    def __init__(self, path):
        self.config = configparser.ConfigParser()
        self.config.read(path)

    def get_config_by_key(self, category, key):
        val = self.config[category][key]
        return val

