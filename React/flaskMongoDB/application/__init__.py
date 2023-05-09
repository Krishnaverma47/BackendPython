from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["SECRET_KEY"] = "58775dcbdf03595db8e52d79e94f2690fce305a7"
app.config['MONGO_URI'] = "mongodb://localhost:27017"

mongodb_client = PyMongo(app)
myDatabase = mongodb_client.db

from application import routes

