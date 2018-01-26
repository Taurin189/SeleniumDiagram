# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

from entity.web_page_entity import WebPage


class PageSourceParser:

    def __init__(self, page_source):
        self.soup = BeautifulSoup(page_source, "html.parser")

    def save_only_url(self, url):
        WebPage(
            id=url,
            title='',
            url=url,
        ).save()

    def save_from_page_source(self, url):
        title = self.soup.title.string

        WebPage(
            id=url,
            title=title,
            url=url,
        ).save()

    def get_link_list(self):
        link_list = self.soup.find_all("a")
        return link_list
