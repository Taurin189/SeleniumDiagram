# -*- coding:utf-8 -*-
from selenium import webdriver


class SeleniumFunction:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

    def __del__(self):
        self.driver.quit()
        self.driver.close()

    def get(self, url):
        self.driver.get(url)