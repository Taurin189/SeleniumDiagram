#!/usr/bin/env python
from lib.output_blockdiag_file import OutputBlockdiagFile
from lib.read_config import ConfigReader
from lib.selenium_function import SeleniumFunction
from page_source_parser import PageSourceParser


def main():
    conf = ConfigReader('./conf/selenium_diagram.conf')
    driver_path = conf.get_config_by_key('driver', 'path')
    target_url = conf.get_config_by_key('target', 'base_url')

    selenium_func = SeleniumFunction(driver_path)
    make_url(selenium_func, target_url)
    # output_blockdiag = OutputBlockdiagFile(conf)
    # output_blockdiag.add_diagram(target_url, destination_list)

def make_url(selenium_func, target_url):
    selenium_func.access_url(target_url)
    page_source = selenium_func.get_page_source()
    parser = PageSourceParser(page_source)

    if target_url != selenium_func.get_current_url():
        parser.save_from_page_and_link(target_url, [selenium_func.get_current_url()])
        return

    destination_list = parser.get_related_netloc_list()
    parser.save_from_page_and_link(target_url, destination_list)

    for destination in destination_list:
        title = parser.get_web_page_object(destination)
        if title == '':
            print("https://" + destination)
            make_url(selenium_func, "https://" + destination)
            continue
        print(title)

if __name__ == '__main__':
    main()