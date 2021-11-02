"""
3) Write a Python program that accepts a filename from the user and prints 
the filename’s extension.

@author: dyogo
"""

def Convert(filename):
    li = list(filename.split("."))
    for str in li[::-1]:
      extension = str
      break
    return(extension)

filename = input('Type your file name: ')
print('Te extension of file is: '+Convert(filename))