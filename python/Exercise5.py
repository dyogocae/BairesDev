# -*- coding: utf-8 -*-
"""
5) Write a Python program to count the frequency of words in a text file.

@author: dyogo
"""

def freq(strfile):
    str_list = strfile.split()
    unique_words = set(str_list)
    
    for words in unique_words:
        print('Frequency of ', words, ' is: ', str_list.count(words))

try:
  myfile = open(r'C:\Users\dyogo\BairesDev\BairesDev\test_exercise5.txt', 'r')
  string = myfile.read().replace('\n',' ')
  freq(string)
except IOError:
    print("File not found or path is incorrect")
finally:
    print("exit") 