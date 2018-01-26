#!/usr/bin/env python
from lib.read_config import ConfigReader
from lib.selenium_function import SeleniumFunction
from page_source_parser import PageSourceParser


def main():
    conf = ConfigReader('./conf/selenium_diagram.conf')
    driver_path = conf.get_config_by_key('driver', 'path')
    target_url = conf.get_config_by_key('target', 'base_url')

    selenium_func = SeleniumFunction(driver_path)
    selenium_func.access_url(target_url)
    page_source = selenium_func.get_page_source()
    parser = PageSourceParser(page_source)
    parser.save_from_page_source(target_url)




if __name__ == '__main__':
    main()