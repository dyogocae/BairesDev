# -*- coding: utf-8 -*-
"""
8) Write a Python function to remove an item from a tuple.

@author: dyogo
"""

import numpy as np
import random

tp = np.random.randint(1,100,size=10)
print(tp)

myList = list(tp)

n = int(input('Type the number you want to remove: '))

myList.remove(n)

print(myList)

idx = int(input('Now, type de index you want to remove: '))

myList.pop(idx)

print(myList)