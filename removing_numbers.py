"""

#!/usr/bin/python

#Author: Suraj Patil
#Version: 2.0
#Date: 27th March 2014


input:
1. this is a dummy text
2. another dummy text
3. this is dummy
4. this is also dummy
output:
   this is a dummy text
   another dummy text
   this is dummy
   this is also dummy
"""
f = open('text', 'r')
f1= open('textModified', 'w')
i=0
lines = f.readlines()

for i in lines:
	lines[i] = lines[1:]
	f1.write(lines[i])
  
f.close()
f1.close()
