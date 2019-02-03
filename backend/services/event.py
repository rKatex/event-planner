from .mongoresource import MongoResource
from flask import jsonify

class Event(MongoResource): 
    def get(self):
        events = []
        for event in self.mongo.db.events.find():
            events.append(event)
        print("xxxxxxxxxxxxxxxx")
        print(events)
        y =  jsonify(events)
        print(y)
        return y
    def post(self):
        return "yuhu"