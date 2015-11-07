from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class DataBlock(Resource):
    def get(self, todo_id):
        return {todo_id: todos}

    def post(self, todo_id):
        print request.data
        return "cool, thanks bro!", 201

api.add_resource(DataBlock, '/<string:todo_id>')
