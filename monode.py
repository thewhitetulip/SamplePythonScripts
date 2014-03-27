'''
#!/usr/bin/python

#Author: Suraj Patil
#Version: 2.0
#Date: 27th March 2014

decrypts the output of the mono.py, i.e. reverse monoalphabetic algorithm
'''
mapping = {'$': 'o', ')': 'd', '*': 'w', ',': 'j', '.': 'a', '0': 'u', '4': 'b', '6': 'y', ':': 'x', '<': 'q', '@': 'r', 'I': 't', 'L': 'p', 'Q': 'k', 'P': 's', 'R': 'l', 'U': 'h', 'T': 'n', 'W': 'f', 'V': 'g', 'Y': 'v', '[': 'm'}
cipher = raw_input('enter cipher text')
for i in range(0, len(cipher)):
    print mapping[cipher[i]],
