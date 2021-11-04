# -*- coding: utf-8 -*-
"""
Module 2
Ex 4) Create a Python function that accepts any number of numbers as 
positional arguments and prints the sum of those numbers.

@author: dyogo
"""

def sum_numb(*numb):
    summ = 0.00
    for n in numb:
        summ += n
    print('Sum of numbers is: ',summ)
  
print('Type the numbers (type any letter to escape):')    
try:
    my_list = []
     
    while True:
        my_list.append(int(input()))
         
# if the input is not-integer, just print the list
except:
    print('Please, type a number!')    
    
sum_numb(*my_list)    