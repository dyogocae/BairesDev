# -*- coding: utf-8 -*-
"""
Module 3
Ex 6) Write a python file with two functions: a function that receives a 
number and appends to a global variable list, and another function that 
returns this list ordered.

@author: dyogo
"""

numb_aleatory = []

def ins_numb(n):
    numb_aleatory.append(n)

def sort_numb():
    print("sorted list: ",sorted(numb_aleatory))

ins_numb(10)

ins_numb(90)

ins_numb(60)

ins_numb(70)

ins_numb(30)

print("list: ",numb_aleatory)
sort_numb()