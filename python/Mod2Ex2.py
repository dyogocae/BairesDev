# -*- coding: utf-8 -*-
"""
2) Write a Python program to get the size, permissions, owner, device, 
created, last modified, and last accessed date time of a specified path.

@author: dyogo
"""

import os
import time
from pathlib import Path
from stat import *
             
#-- get the current path
print('Path: ',os.getcwd())

#-- get the size of the path
print('Size path: ',os.path.getsize(os.getcwd()))

#-- get the permissions of the path
path = Path(os.getcwd())
print('path permissions: ')
if(os.access(path, os.R_OK)):
    print('Read')
if(os.access(path, os.W_OK)):
    print('Write')
if(os.access(path, os.X_OK)):
    print('Execute')
if not (os.access(path, os.R_OK) and 
        os.access(path, os.W_OK) and 
        os.access(path, os.X_OK)):
    print('none')

#-- get the device of the path  
#-- get the owner of the path 
system = os.listdir(os.getcwd())
for element in system:
    if os.path.isfile(os.path.join(os.getcwd(),element)):
        print("Device: ", os.stat(os.path.join(os.getcwd(),element)).st_dev)
        print("Owner: ", os.stat(os.path.join(os.getcwd(),element)).st_uid) 
        break
            
#-- get the date of creation of the path
dtc =  time.strftime('%Y-%m-%d', 
                    time.localtime(os.path.getctime(os.getcwd())))
print('Date of creation: ', dtc)

#-- get the date of last modified of path
dtm =  time.strftime('%Y-%m-%d %H:%M:%S', 
                    time.localtime(os.path.getmtime(os.getcwd())))
print('Last modified: ', dtm)

#-- get the datetime of last access of path
dta =  time.strftime('%Y-%m-%d %H:%M:%S', 
                    time.localtime(os.path.getatime(os.getcwd())))
print('Last Access: ', dta)

