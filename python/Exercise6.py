# -*- coding: utf-8 -*-
"""
6) Write a Python program that takes an input string from the user and counts 
the frequency of characters in the string.
Sample String : google.com
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

@author: dyogo
"""


string = input('Type something: ')
li = list(string)

unique_ch = set(li)

for ch in unique_ch:
    print(ch,':',li.count(ch))
