# -*- coding: utf-8 -*-
"""
Module 4
Ex 3) Create a decorator that makes sure that all function arguments where 
it's applied will match the regex on the regex exercise above

@author: dyogo
"""

import re #Regex library

reg_expr = '^[a-z]+_[a-z]+$'

class lowercase(object):
    def __init__(self, f):
        print("decorator __init__ called")
        self.f = f
        
    def __call__(self, *args):
        self.f(args[0].lower())

@lowercase
def match_regex(text):
    if(re.search(reg_expr, text)):
        print("text: ",text," matched with regex: ",reg_expr)
    else:
        print("text: ",text," not matched with regex: ",reg_expr)

text1 = "abc_xyz"
text2 = "ABC_XYZ" 
text3 = "Wqe_iop"
text4 = "jkl_nMOp"

match_regex(text1)
match_regex(text2)
match_regex(text3)
match_regex(text4)