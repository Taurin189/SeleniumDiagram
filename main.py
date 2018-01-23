#!/usr/bin/env python
from lib.read_config import ConfigReader


def main():
    conf = ConfigReader('./conf/selenium_diagram')
    driver_path = conf.get_config_by_key('driver', 'path')

    print('hoge')

if __name__ == '__main__':
    main()