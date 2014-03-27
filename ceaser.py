'''
#!/usr/bin/python

#Author: Suraj Patil
#Version: 2.0
#Date: 27th March 2014

this program implement the ceaser cipher shift algorithm, it takes the plain text
and the shift from the user and prints the cipher

usage: python ceaser.py
'''
import string

plaintext=raw_input("enter clear text")
key=raw_input('input key')
letters = string.ascii_letters #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
dig = string.digits
for i in range(0,len(plaintext)):
	if not plaintext[i].isalpha: #dig.find(plaintext[i])!=-1:
		print "enter alphabet only"
		exit()
for i in range(0,len(plaintext)):
	a = letters.find(plaintext[i])
	if a!=-1:
		print str(letters[(a+key)%26]),
