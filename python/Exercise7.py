# -*- coding: utf-8 -*-
"""
7) Write a Python function to remove duplicates from a list.

@author: dyogo
"""

try:
  myfile = open(r'C:\Users\dyogo\BairesDev\BairesDev\test_exercise7.txt', 'r')

  common_list = set(myfile.readlines())
  converted_list = []
  for element in common_list:
      converted_list.append(element.strip())
  unique_list = set(converted_list)
  print(unique_list)
except IOError:
    print("File not found or path is incorrect")
finally:
    print("exit") 