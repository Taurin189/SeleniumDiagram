# -*- coding:utf-8 -*-
import requests
from selenium import webdriver


class SeleniumFunction:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

    def __del__(self):
        self.driver.close()
        self.driver.quit()

    def access_url(self, url):
        self.header = requests.head(url)
        print(self.header)
        self.driver.get(url)

    def get_response_code(self):
        return self.header

    def get_current_url(self):
        return self.driver.current_url

    def login(self, account, password, account_class, password_class, submit_class):
        account_input = self.driver.find_element_by_class_name(account_class)
        password_input = self.driver.find_element_by_class_name(password_class)
        submit_button = self.driver.find_element_by_class_name(submit_class)

        account_input.send_keys(account)
        password_input.send_keys(password)

        submit_button.submit()

    def get_page_source(self):
        return self.driver.page_source
