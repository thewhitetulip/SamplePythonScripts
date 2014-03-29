'''
#!/usr/bin/python

#Author: Suraj Patil
#Version: 2.0
#Date: 27th March 2014


this program prints all the tables from 13 to 50 to a file
this script prints it on the console
for i in range(13,51):
  for j in range(1,11):
    print i*j,
  print ''
'''

#the below program has been modified to print the output to a text file
path = raw_input("Enter the file in which you want to save tables: ")

try:
	f=open(path, 'w')
	for i in range(1,11):
	  f.write( "%3d%s"%(i, ' '))
	f.write('\n'
	for i in range(1,11):
	  f.write('----')
	f.write('\n')
	for i in range(13,51):
	  for j in range(1,11):
		f.write( "%3d%s"%(i*j, ' '))
	  f.write('\n')
          f.close()
except:
	print 'Some error occured'
