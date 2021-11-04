# -*- coding: utf-8 -*-
"""
Module 2
Ex 3) Write a Python program that takes user input and runs it as a command 
using the os module.

@author: dyogo
"""
import os
cmd = input('Input a cmd command to run: ') # ipconfig
stream = os.popen(cmd)
output = stream.read()
print(output)

import subprocess
process = subprocess.Popen(['ping', 'python.org'], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

while True:
    output = process.stdout.readline()
    print(output.strip())
    # Do something else
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        # Process has finished, read rest of the output 
        for output in process.stdout.readlines():
            print(output.strip())
        break


