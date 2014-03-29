#!/usr/bin/python

#when we want to find the absolute value of any number
print abs(-1)

#when we want to find out if a object is iterable or not
a = [1,2,3,4]
print all(a) #prints True

#get the binary of number
print bin(12) #takes an int object

#returns character whose ASCII code is 97
print chr(97) #takes an int object

#classmethod

Class C:
   @classmethod
   def f(arg1, arg2):
     #some code here

#now we can call f as C.f(1,2)

#to compare two objects

print cmp(2,3)
#returns -ve if 2<3, +ve if 2>3, zero if 2==3

#creating a complex number
print complex(1,2) #creates 1+2j, both args are optional

#calculate divisor & quotient in one go
print divmod(3,2) #returns (1,1)

#evaluating expressions
x=1
print eval(`x+1`) # ` is not single quote, evaluates the expression and returns value

#executefile and return result
execfile('./type.py')

#constructor to a file
a = file('./demofile','w',3444) # creates a file demofile in write mode with buffer size 3444
#default open mode is 'r': read, and last two args are optional

#get the hexadecimal value
print hex(12) #takes a int
print float.hex(12.12)

#identification of an object
print id(a)

#converting any base into int
print int(344, 8) #converts octal 344 to decimal number, you can use '344' as well

#finding if a object is instance of a class or not
print isinstance(a,file) #prints True if a is file object

#get the length
print len('python rocks')

#list 
print list((1,2,3,4))  # returns [1,2,3,4]
print list('abcde') # returns ['a','b','c','d','e']

#converts any base to long int
long('2334',8)

#maximum
print max([1,2,3,4,5]) #prints 5

#minimum
print min([1,2,3,4,5]) #prints 1

#convert integer to octal
print oct(23)

#opening a file
a = open(name, mode, buffering)

#returns unicode character
print ord('a') #prints 67

#power
print pow(2,3) #8
print (2,3,4) #2^3%4 computed more efficiently than manual operation

#printing values
print('hello %s, %d'%(name, 34))
print('')

#range
range(12) #returns a tuple [0,1,...12]
range(23,34) #returns a tuple [23,24,25.....34]
range(1,12,3) #returns a tuple [1,4,7..]

#taking input from user
name = raw_input('enter your name')
print 'Hello %s'%(name)

#reversing a sequence

a =  reversed((2,435,1,345))
for i in a:
   print i

#will print a reverse of the given sequence

#sorting
a = sorted((23,252,1,2352)) #returns a sorted sequence of the given arg
for i in a:
  print i

#string constructor
print str(234) #returns '234'

#sum
print sum([1,2,3,4])

#construcor of tuple
a = tuple((1,2,3,4)) #creates a tuple object and links it with object a

#checking the type of object
type(12) #returns 'int'
type('a') #returns 'str'
type(12.2) #returns 'float'

