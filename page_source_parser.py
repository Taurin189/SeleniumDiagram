# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urllib.parse import urlparse

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

    def save_from_page_and_link(self, url, link_list):
        title = self.soup.title.string

        WebPage(
            id=url,
            title=title,
            url=url,
            web_link=link_list
        ).save()

    def get_web_page_object(self, url):
        try:
            web_page = WebPage.objects.get({'_id': url})
        except WebPage.DoesNotExist:
            return ''
        else:
            return web_page.title

    def get_related_netloc_list(self):
        link_html_list = self.get_link_html_list()
        netloc_list = []
        for link_html in link_html_list:
            link = link_html.get("href")
            o = urlparse(link)
            if o.netloc == "":
                print("same netloc : " + str(o))
                continue
            if o.netloc not in netloc_list:
                netloc_list.append(o.netloc)

        return netloc_list

    def get_link_html_list(self):
        link_html_list = self.soup.find_all("a")
        return link_html_list
