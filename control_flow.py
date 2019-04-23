#!/usr/local/bin/python3 
# Name: Shirley Huang
# File: wk3_ex.py
# Desc: control flow exercises
# Date: 04-21-2019

import string
# Reusing the code to create the dict of keys and values
lowercase_letters = list(string.ascii_lowercase)
lcd = {i: i.upper() for i in lowercase_letters}
the_keys = sorted(lcd.keys())


#print every other letter in the list of keys.
#print (the_keys[::2]) 

counter = 0
while counter < len(the_keys):
    if counter %2 ==0: # ==0 is even number and !=0 is odd number
        print(the_keys[counter])
    counter += 1

for k in the_keys:
    if ord(k)%11 == 0:
        print(ord(k), k, k*11, sep='\t')
    elif ord(k)%7 == 0:
        print(ord(k), k, k*7, sep='\t')
    elif ord(k) % 5 == 0:
        print(ord(k), k, k*5, sep='\t')
    elif ord(k) % 3 == 0:
        print(ord(k), k, k*3, sep='\t')
    elif ord(k) % 2 == 0:
        print(ord(k), k, k*2, sep='\t')
    elif ord(k) == 97 or ord(k) == 101 or ord(k) == 103 or ord(k) == 107 or ord(k) == 109 or ord(k) == 113:
        print(ord(k), k, k+' (P)', sep='\t')



    
