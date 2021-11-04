# -*- coding: utf-8 -*-
"""
Module 3
Ex 3) Write a Python program that asks the user for their birth date and 
prints the user’s current age in years, months, and days.

@author: dyogo
"""

from datetime import datetime, date

dt_format_str = "%d/%m/%Y"

#get strings 
dtBirth_str = input("enter your birthday in this format dd/mm/yyyy: ")
dtBirth = datetime.strptime(dtBirth_str,dt_format_str)

#transform strings to date
dtCurrent = datetime.today().strftime(dt_format_str)
dtCurrent = datetime.strptime(dtCurrent,dt_format_str)

#years
years = dtCurrent.year - dtBirth.year
#months
if (dtCurrent.month < dtBirth.month):
    years -= 1
    months = dtCurrent.month
elif (dtCurrent.month >= dtBirth.month):    
    months = dtCurrent.month - dtBirth.month
#days  
if (dtCurrent.day < dtBirth.day):
    months -= 1
    days = dtBirth.day - dtCurrent.day
elif (dtCurrent.day >= dtBirth.day):    
    days = dtCurrent.day - dtBirth.day        

print('You are {0} years, {1} months, and {2} days old'.format(years, months, days))
