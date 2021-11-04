# -*- coding: utf-8 -*-
"""
Module 3
Ex 1) Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are the same from a 
given list of strings. 

@author: dyogo
"""


li = ['abc', 'xyz', 'aba', '1221']

count = 0
    
for word in li:
    if (len(word)) < 2: 
        continue
    firstCh = word[0]
    lastCh = word[len(word)-1]
    if (firstCh == lastCh):
        count += 1
    
print("Sample List: ",li)
print("Result: ",count)    
    