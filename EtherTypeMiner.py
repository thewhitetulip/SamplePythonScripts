'''http://standards.ieee.org/develop/regauth/ethertype/eth.txt
this is the etherType text file we are going to use
there are 43 lines, each one has a hex number, I have to convert
all those hex numbers into decimal, and then print them back to the text file

NO way I am going to do that by hand. simple, use python!
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

#the next thing we need to do is to write this to our file, remmember in the actual code we have 'printed' the results,
#in reality we have to save them to python variables to work with them, but it is a good practice to see them first
#and then do the actual programming


