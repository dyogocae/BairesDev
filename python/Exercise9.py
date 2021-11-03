# -*- coding: utf-8 -*-
"""
9) Write a Python function to merge two dictionaries.

@author: dyogo
"""

dict1 = {'dc_a': 10, 'dc_b': 20, 'dc_c': 30}

dict2 = {'dc_a': 10, 'dc_b': 30, 'dc_c': 60}

dict3 = {'dc_a': 10, 'dc_b': 50, 'dc_c': 100}

# -- method update -- the dictionary passed as argument will override
dict1.update(dict2)
print('Updated dictionary 1: ')
print(dict1)

# -- method **kwargs -- the last argument will override the other ones
dictk = {**dict1, **dict3}
print('Dictionary kwargs:')
print(dictk)


