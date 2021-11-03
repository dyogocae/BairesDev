# -*- coding: utf-8 -*-
"""
10) Write a Python program that iterates through integers from 1 to 100 and 
prints them. For integers that are multiples of three, print "Fizz" instead 
of the number. For integers that are multiples of five, print "Buzz". 
For integers which are multiples of both three and five print, "FizzBuzz".

@author: dyogo
"""

for number in range(1,101):
    if(number%3 == 0 and number%5 == 0):
        print('FizzBuzz')
        continue
    if(number%3 == 0):
        print('Fizz')
        continue
    if(number%5 == 0):
        print('Buzz')
        continue
    print(number)