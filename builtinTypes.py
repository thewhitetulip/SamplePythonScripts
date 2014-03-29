#The principal built-in types are numerics, sequences, mappings, files, classes, instances and exceptions.

#boolean operators

print 23 or False #prints 23
print 23 and False #print False
print not 23 #prints False

#comparisons operators

print 4>3 #prints True
print 4<3 #prints False
print 4==3 #prints False
print 4<=3 #prints False
print 4>=3 #prints True
print 4!=2 #prints True

print type(3) is int #prints True
print type('3') is not int # prints True

#operations
#x=23, =24
print x + y
print x - y
print x * y
print x / y
print x // y
print x % y
print -x
print +x
print abs(x)
print int(x)
print long(x)
print float(x)
print complex(re,im)
print c.conjugate()
print divmod(x, y)
print pow(x, y)
print x ** y

#bitwise operations on int
print x | y
print x ^ y
print x & y
print x << n
print x >> n
print ~x

#methods on Integer types

n = 30
print n.bit_length() #returns the length of binary of 30

#same with long

#additional methods on float
a = 4.5
a.as_integer_ratio() #returns a tuple as humans write fractions

a=2.0
print a.is_integer() # true

print a.hex() #prints hex of a

print a.fromhex('0x004') #returns float of hex value



