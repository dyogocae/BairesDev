"""
1) Program to test whether a passed letter is a vowel or not
"""
import random
import string

letter = random.choice(string.ascii_letters)
if (letter.upper() == "A" or 
    letter.upper() == "E" or 
    letter.upper() == "I" or 
    letter.upper() == "O" or
    letter.upper() == "U"):
    print('Letter '+letter+' is a vowel!' )
else:
    print('Letter '+letter+' isn''t a vowel!' )
