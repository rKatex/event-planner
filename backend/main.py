from flask import Flask
from flask.json import JSONEncoder
from flask_restful import Api
from flask_pymongo import PyMongo
from services.event import Event
from bson import ObjectId

class MongoJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return JSONEncoder.default(self, o)

app = Flask(__name__)
app.json_encoder=MongoJSONEncoder
app.config["MONGO_URI"] = "mongodb://localhost:27017/event-board"
mongo = PyMongo(app) 

def addMongoResource(api, resource, *urls):
    api.add_resource(resource, *urls,  resource_class_kwargs={ 'mongo': mongo })

api = Api(app)
addMongoResource(api, Event, '/event')
 
if __name__ == '__main__':
    app.run(debug=True) 