# -*- coding: utf-8 -*-
"""
4) Write a Python program to count the number of lines in a text file.

@author: dyogo
"""

try:
  myfile = open(r'C:\Users\dyogo\BairesDev\BairesDev\file_test.txt', 'r')
  x = len(myfile.readlines())
  print('Total lines:', x)
except IOError:
    print("File not found or path is incorrect")
finally:
    print("exit") 