# -*- coding: utf-8 -*-
"""
Module 3
Ex 4) Write a Python function using list comprehension that receives a list of 
words and returns a list that contains:
 a. The number of characters in each word if the word has 3 or more characters
 b. The string “x” if the word has fewer than 3 characters

@author: dyogo
"""

li = ["teste", "itens", "ab", "aba", "baires", "dev", "us"]

final_li = ["x" if (len(word) < 3) else len(word) for word in li]

print(li)
print(final_li)