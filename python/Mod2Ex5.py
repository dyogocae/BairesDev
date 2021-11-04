# -*- coding: utf-8 -*-
"""
Module 2
Ex 5) Create a Python function that accepts any number of positional and 
keyword arguments, and that prints them back to the user. Your output should 
indicate which values were provided as positional arguments, and which were 
provided as keyword arguments. 

@author: dyogo
"""

def myFun(*args,**kwargs):
    print("args (positional): ", args)
    print("kwargs (keywords): ", kwargs)
 
myFun('first pos argument',
      'second pos argument',
      'third pos argument',
      first="any argument",
      mid="any argument to",
      last="same thing")