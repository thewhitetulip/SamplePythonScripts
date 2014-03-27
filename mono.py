'''
#!/usr/bin/python

#Author: Suraj Patil
#Version: 2.0
#Date: 27th March 2014

implements the monoalphabetic algorithm
every alphabet in a..z is replaced by a unique character
'''
import string
#import random
letters = string.ascii_letters
small=[]
cap=[]
mapping={}
for i in range(0,51):
    if i<26:
        small.append(letters[i])
    else:
        cap.append(letters[i])
#for i in range(0,25):
#    mapping[small[i]] = chr(random.randint(33,96))
mapping = {'a': '.', 'c': 'I', 'b': '4', 'e': 'T', 'd': ')', 'g': 'V', 'f': 'W', 'i': ':',
           'h': 'U', 'k': 'Q', 'j': ',', 'm': '[', 'l': 'R', 'o': '$', 'n': 'T', 'q': '<', 'p': 'L',
           's': 'P', 'r': '@', 'u': '0', 't': 'I', 'w': '*', 'v': 'Y', 'y': '6', 'x': ':'}
cleartext = raw_input('enter cleartext:')
for i in range(0,len(cleartext)):
    print mapping[cleartext[i]],
