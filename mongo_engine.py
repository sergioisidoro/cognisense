from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.script import Manager, Server

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "cognisense"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)
