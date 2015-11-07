import redis

from flask import Flask, request, Response
from flask_restful import Resource, Api

try:
    from flask_cors import cross_origin
    # support local usage without installed package
except:
    from flask.ext.cors import cross_origin
    # this is how you would normally import


from cortex.api.event_stream import event_stream

app = Flask(__name__)
api = Api(app)
red = redis.StrictRedis()


class DataBlock(Resource):
    def get(self, todo_id):
        return {todo_id: "None"}

    def post(self, todo_id):
        red.publish("patient1", request.data)

        timestamp_data = request.data["TimeStamps"]


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
