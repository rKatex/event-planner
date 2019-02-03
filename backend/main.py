from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from services.event import Event
from helper.jsonencoder import MongoJSONEncoder
from routing.router import Router

app = Flask(__name__)
app.json_encoder = MongoJSONEncoder
app.config["MONGO_URI"] = "mongodb://localhost:27017/event-board"
mongo = PyMongo(app)
api = Api(app)
router = Router(api, mongo)

router.addResource(api, Event, '/event')

if __name__ == '__main__':
    app.run(debug=True)
