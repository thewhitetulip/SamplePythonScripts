import os
#creates file on the go on the entries of a tuple

ports=[20,21,23,25,43,49,53,69,70,79,80,109,110,115,137,139,143,161,194,389,443,444,458,546,547,1080]

path=raw_input('Enter the path you want to create the files: ')

try:
   os.chdir(path)
except:
   print "Invalid Path"

try:
   for i in ports:
      for i in ports:
         file = open('./'+str(i),'w')
         file.close()
except:
   print "Could not create files, please check if you have the appropriate read/write permissions
