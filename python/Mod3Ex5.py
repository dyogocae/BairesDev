# -*- coding: utf-8 -*-
"""
Module 3
Ex 5) Write a Python program that reads a JSON object from a file, sorts the 
object keys in ascending order, then writes the JSON object back into the file.

file: json_test

{   "estados":[
    {"Id": 30, "estado": "São Paulo", "sigla": "SP"},
    {"Id": 10, "estado": "Minas Gerais", "sigla": "MG"},
    {"Id": 20, "estado": "Rio de Janeiro", "sigla": "RJ"}
    ]
}

@author: dyogo
"""

import json, operator

with open("json_test", "r") as read_file:
    data = json.load(read_file)

data.sort(key=operator.itemgetter('Id'))
print(json.dumps(data, indent=2))

with open('json_sorted', 'w') as f:
    json.dump(data, f)    
        