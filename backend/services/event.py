from .mongoresource import MongoResource
from flask import jsonify
from flask_restful import fields, marshal_with

event_fields = {
    'name':   fields.String,
    'description':    fields.String,
}


class Event(MongoResource): 
    def get(self):
        return jsonify(list(self.mongo.db.events.find()))

    @marshal_with(event_fields)
    def post(self, event):
        print(event)
        #self.mongo.db.events.insert_one()