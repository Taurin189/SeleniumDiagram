#!/usr/bin/env python
from lib.read_config import ConfigReader
from lib.selenium_function import SeleniumFunction


def main():
    conf = ConfigReader('./conf/selenium_diagram')
    driver_path = conf.get_config_by_key('driver', 'path')
    target_url = conf.get_config_by_key('target', 'base_url')
    selenium_func = SeleniumFunction(driver_path)


    print('hoge')

if __name__ == '__main__':
    main()