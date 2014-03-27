'''
#!/usr/bin/python

#Author: Suraj Patil
#Version: 2.0
#Date: 27th March 2014

does the ceaser decryption of the output of ceaser.py, the cipher and shift are taken
from the user and the plain text is printed on the console
'''
import string
cipher=raw_input('enter cipher')
key=raw_input('enter key')
letters = string.ascii_letters
dig = string.digits
for i in range(0,len(cipher)):
	if dig.find(cipher[i])!=-1:
		print "invalid input"
		exit()
for i in range(0,len(cipher)):
	a = letters.find(cipher[i])
	if a!=-1:
		print str(letters[(a-key)%26]),
