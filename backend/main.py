import json
import datetime

from bson.objectid import ObjectId
from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from services.event import Event

def addMongoResource(api, resource, *urls):
    api.add_resource(resource, *urls,  resource_class_kwargs={ 'mongo': mongo })

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/event-board"
app.json_encoder = json.JSONEncoder
mongo = PyMongo(app)

api = Api(app)
addMongoResource(api, Event, '/event')

if __name__ == '__main__':
    app.run(debug=True) 