from .mongoresource import MongoResource
from flask import jsonify
from flask_restful import reqparse


eventParser = reqparse.RequestParser()
eventParser.add_argument('name', required=True)
eventParser.add_argument('description')


class Event(MongoResource):
    def get(self):
        return jsonify(list(self.mongo.db.events.find()))

    def post(self):
        event = eventParser.parse_args()
        inserted_id = self.mongo.db.events.insert_one(event).inserted_id
        return jsonify({"_id": inserted_id})
