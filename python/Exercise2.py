# -*- coding: utf-8 -*-
"""
2) Write a Python program that accepts the user's first and last name and 
prints them in reverse order with a space between them.

@author: dyogo
"""

def Convert(string):
    li = list(string.split(" "))
    strFinal = ""
    for str in li[::-1]:
        if strFinal == "":
            strFinal = str
        else:    
            strFinal = strFinal + " " + str
    print(strFinal)
    
fullName = input('Type your full name: ')

Convert(fullName)