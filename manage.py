from gevent.monkey import patch_all
patch_all()

from logging import getLogger
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.script import Manager, Server

from dendrite.blueprint import dendrite
from dendrite.views.person import person_blueprint

logger = getLogger('watson.run')

from mongo_engine import app

app.register_blueprint(dendrite,  url_prefix='/dendrite')
app.register_blueprint(person_blueprint, url_prefix='/dendrite/person')


manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0',
    port=1337,
    threaded=True))


if __name__ == '__main__':
    app.debug = True
    manager.run()
