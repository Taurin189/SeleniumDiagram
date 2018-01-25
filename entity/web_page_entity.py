# -*- coding:utf-8 -*-
from pymodm import connect, fields, MongoModel, EmbeddedMongoModel


connect('mongodb://localhost:27017/service')


class WebPage(MongoModel):
    id = fields.CharField(primary_key=True)
    url = fields.CharField()
    title = fields.CharField()
    web_link_ids = fields.ListField(fields.CharField())