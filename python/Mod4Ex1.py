# -*- coding: utf-8 -*-
"""
Module 4
Ex 1) Write a Python regex function to find sequences of lowercase letters 
joined with an underscore.

@author: dyogo
"""

import re #Regex library

reg_expr = '^[a-z]+_[a-z]+$'

def match_regex(text):
    if(re.search(reg_expr, text)):
        print("text: ",text," matched with regex: ",reg_expr)
    else:
        print("text: ",text," not matched with regex: ",reg_expr)

text1 = "abc_xyz"
text2 = "cDf_juy" 
text3 = "Wqe_iop"
text4 = "jkl_nmop"

match_regex(text1)
match_regex(text2)
match_regex(text3)
match_regex(text4)