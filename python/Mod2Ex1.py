# -*- coding: utf-8 -*-
"""
Module 2
Ex 1) Write a Python program to scan a specified directory and identify the 
sub directories and files

@author: dyogo
"""

import os

#function to print a list of sub-directories
def listdir_r(dirpath):
    paths = []
    paths.append(dirpath)
    for path in os.listdir(dirpath):
        rpath = os.path.join(dirpath, path)
        if os.path.isdir(rpath):
            subdirs = listdir_r(rpath)
            if not subdirs == []:
                paths.extend(subdirs)
    return paths


print(os.getcwd())
# -- List the files on the current directory
print(os.listdir(os.getcwd()))

# print the list of sub-directories
print(listdir_r('../'))
