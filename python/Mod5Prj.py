# -*- coding: utf-8 -*-
"""
Module 5
Project: 

    Create a simple function that fetches and parses the JSON from this API:
        https://jsonplaceholder.typicode.com/todos/ and then print all the 
        completed TODOs in the screen.

        Create a simple local web server with an API endpoint that proxies 
        the TODOs API used above and accepts the "completed" and the "name" 
        filtering. You can use any web framework you prefer.


@author: dyogo
"""

import requests
import json

def get_json_data():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    if (response.status_code == 200):
        text = json.dumps(response.json())
        input_dict = json.loads(text)
        output_dict = [x for x in input_dict if x['completed'] == True]
        output_json = json.dumps(output_dict, indent=2)
        print(output_json)

get_json_data()        