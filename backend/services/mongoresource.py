from flask_restful import Resource
from flask_pymongo import PyMongo

class MongoResource(Resource):
    def __init__(self, **kwargs):
        self.mongo:PyMongo = kwargs["mongo"]