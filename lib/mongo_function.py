# -*- coding:utf-8 -*-
from pymongo import MongoClient
from pprint import pprint


class MongoFunction:
    def __init__(self, collection_name):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.selenium
        self.collection = self.db[collection_name]
        pprint(self.collection)

    def insert(self, document):
        self.collection.insert(document)

    def update(self, exist_document, document):
        self.collection.update_one({"_id": exist_document["_id"]}, {"$set": document})

    def insert_or_update(self, document):
        id = document["id"]
        exist_document = self.find_by_id(id)
        pprint(exist_document)
        if exist_document is None:
            self.insert(document)
        else:
            self.update(exist_document, document)

    def find_by_id(self, document_id):
        pprint(document_id)
        document = self.collection.find_one({"id": document_id})
        return document

    def get_one_document(self):
        one_document = self.collection.find_one()
        pprint(one_document)
