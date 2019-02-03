from flask_restful import Api
from flask_pymongo import PyMongo


class Router():
    def __init__(self, api: Api, mongo: PyMongo):
        self.api = api
        self.mongo = mongo

    def addResource(self, resource, *urls):
        self.api.add_resource(resource, *urls, resource_class_kwargs={'mongo': self.mongo})
