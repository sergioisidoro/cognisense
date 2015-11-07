import redis
import json
import datetime

from flask import Flask, request, Response
from flask_restful import Resource, Api

try:
    from flask_cors import cross_origin
    # support local usage without installed package
except:
    from flask.ext.cors import cross_origin
    # this is how you would normally import


from cortex.api.event_stream import event_stream
from cortex.core.models import DataBlock as DataBlockModel

app = Flask(__name__)
api = Api(app)
red = redis.StrictRedis()

app.config['MONGODB_SETTINGS'] = {'db': 'cognisense', 'alias': 'default'}

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_to_datetime(x):
    return datetime.datetime.fromtimestamp(int(x))

class DataBlock(Resource):
    def get(self, todo_id):
        return {todo_id: "None"}

    def post(self, todo_id):
        if request.data:
            red.publish("patient1", request.data)
            print request.data
            data = json.loads(request.data)

            timestamp_data = data.pop("timestamps", None)
            data_type = data.pop("type", None)

            for key, value in data.iteritems():
                d = DataBlockModel(
                    #source_timestamp=map(unix_to_datetime, timestamp_data),
                    channel_name=key,
                    channel_type=data_type,
                    data=value)
                #d.save()

        return "cool, thanks bro!", 201


@app.route('/event_listener/<tagID>')
@cross_origin(origins='*', methods=['GET', 'POST', 'OPTIONS'],
              headers=[
                'X-Requested-With', 'Content-Type', 'Origin',
                'withCredentials', 'Access-Control-Allow-Credentials',
                'token'])
def stream(tagID):
    resp = Response(event_stream(tagID), mimetype="text/event-stream")
    return resp

api.add_resource(DataBlock, '/<string:todo_id>')
