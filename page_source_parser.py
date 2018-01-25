# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

from entity.web_page_entity import WebPage


class PageSourceParser:
    def __init__(self, url, page_source):
        self.page_source = page_source
        soup = BeautifulSoup(page_source, "html.parser")
        title = soup.title.string

        WebPage(
            id=url,
            title=title,
            url=url,
        ).save()
