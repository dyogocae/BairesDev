# -*- coding: utf-8 -*-
"""
Module 3
Ex 2) Write a Python program to display the current date and time.

@author: dyogo
"""

from datetime import datetime

print("Current date and time: ",datetime.now().strftime("%Y-%M-%d %H:%M:%S"))