import requests
import json

from flask import Flask, render_template, jsonify
from flask_restplus import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

@api.route('/todos')
class TodoList(Resource):
    def get(self, ):
        response = requests.get("https://jsonplaceholder.typicode.com/todos/")
        return response.json()

@api.route('/todos_name')
class TodoName(Resource):
    def get(self, ):
        response = requests.get("https://jsonplaceholder.typicode.com/todos/")
        text = json.dumps(response.json())
        input_dict = json.loads(text)
        output_dict = [x for x in input_dict if x['title'] == 'fugiat veniam minus']
        return output_dict

@api.route('/todos_completed')
class TodoCompleted(Resource):
    def get(self, ):
        response = requests.get("https://jsonplaceholder.typicode.com/todos/")
        text = json.dumps(response.json())
        input_dict = json.loads(text)
        output_dict = [x for x in input_dict if x['completed'] == False]
        return output_dict             