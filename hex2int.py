#!/usr/bin/python

#Author: Suraj Patil
#Version: 1.0
#Date: 26th March 2014

'''
this file won't execute, you will have to type this all into the python prompt, which is the appropriate way of 
doing programming, as it allows the programmer to have an interactive output

output: 
0x0800 2048	Internet Protocol version 4 (IPv4)
0x0806 2054	Address Resolution Protocol (ARP)
0x0842 2114	Wake-on-LAN[3]
... any number of entries

input:
0x0800     Internet Protocol version 4 (IPv4)
0x0806     Address Resolution Protocol (ARP)
0x0842     Wake-on-LAN[3]
...any number of entries

0x0800 = hexadecimal of 2048
'''



>>> f = open('/root/Desktop/project/EtherType','r')
>>> lines = f.readlines()
>>> lines
['0x0800 \t2048 Internet Protocol version 4 (IPv4)\n', '0x0806 \t2054 Address Resolution Protocol (ARP)\n', ......

'''now we get the content of the file in python's tuple, the next thing we want to do is extract only the hex numbers'''

>>> for i in lines:
...    print i[:7]
... 
0x0800 
0x0806 
0x0842 
0x22F3 
0x6003 
0x8035 
0x809B 
0x80F3 
0x8100 
0x8137 
0x8138 
0x8204 
0x86DD 
0x8808 
0x8809 
0x8819 
0x8847 
0x8848 
0x8863 
0x8864 
0x8870 
0x887B 
0x888E 
0x8892 
0x889A 
0x88A2 
0x88A4 
0x88A8 
0x88AB 
0x88CC 
0x88CD 
0x88E1 
0x88E3 
0x88E5 
0x88F7 
0x8902 
0x8906 
0x8914 
0x8915 
0x892F 
0x9000 
0x9100 
0xCAFE 
#the next thing we need to do is convert them into integer

for i in lines:
...   print int(str(i[:7]),16)
... 
2048
2054
2114
8947
24579
32821
32923
33011
33024
33079
33080
33284
34525
34824
34825
34841
34887
34888
34915
34916
34928
34939
34958
34962
34970
34978
34980
34984
34987
35020
35021
35041
35043
35045
35063
35074
35078
35092
35093
35119
36864
37120
51966

the next thing we need to do is to write this to our file, remmember in the actual code we have 'printed' the results,
in reality we have to save them to python variables to work with them, but it is a good practice to see them first
and then do the actual programming

you will now notice that we already have the file read in python, so the pointer is now in the last position. We have to
in a way create a new file with one extra column after the hex number

>>> a=[]  #create a new tuple

>>> for i in lines:
...  a.append( int(str(i[:7]),16))
... 
>>> a
[2048, 2054, 2114, 8947, 24579, 32821, 32923, 33011, 33024, 33079, 33080, 33284, 34525, 34824, 34825, 34841,
34887, 34888, 34915, 34916, 34928, 34939, 34958, 34962, 34970, 34978, 34980, 34984, 34987, 35020, 35021, 35041, 
35043, 35045, 35063, 35074, 35078, 35092, 35093, 35119, 36864, 37120, 51966]


>>> lines[0]
'0x0800 \tInternet Protocol version 4 (IPv4)\n'

>>> lines[:7]+str(2048)+lines[7:]
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: can only concatenate list (not "str") to list

>>> lines[0]
'0x0800 \tInternet Protocol version 4 (IPv4)\n'

>>> type(lines[0])
<type 'str'>

>>> lines[:7]
['0x0800 \tInternet Protocol version 4 (IPv4)\n', .....

>>> lines[0][:7]+str(2048)+lines[0][7:]
'0x0800 2048\tInternet Protocol version 4 (IPv4)\n'

# now we got the answer for the first line, we need to do this for a;; the other lines as well

>>> file = open('/root/Desktop/project/EtherType2','a')

>>> dir(file)
['__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__',
'__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'closed', 'encoding', 
'errors', 'fileno', 'flush', 'isatty', 'mode', 'name', 'newlines', 'next', 'read', 'readinto', 'readline', 
'readlines', 'seek', 'softspace', 'tell', 'truncate', 'write', 'writelines', 'xreadlines']

>>> for i in range(43):
...   final_print =  lines[i][:7]+str(a[i])+lines[i][7:]
...   file.write(final_print)
... 

>>> file.close()


[root@localhost ~]# cat /root/Desktop/project/EtherType2
0x0800 2048	Internet Protocol version 4 (IPv4)
0x0806 2054	Address Resolution Protocol (ARP)
0x0842 2114	Wake-on-LAN[3]
---
this is the result that we wanted!
