import os
#creates file on the go on the entries of a tuple

#change the ports tuple to whatever name you want to create files for, suppose you want to create 1000 files all of student names then
#have the tuple as, ports=['name1, 'name2', 1000 times]
ports=[20,21,23,25,43,49,53,69,70,79,80,109,110,115,137,139,143,161,194,389,443,444,458,546,547,1080]

#take the path to where we want to create files
#raw_input takes the input in the string format

folder_name = raw_input("Enter the folder name you want to create: ")
path=raw_input('Enter the path you want to create the files: ')
ask = raw_input('Do you want to enable verbose mode? y/n')

try:
   os.chdir(path)
   os.mkdir(folder_name)
   os.chdir('./'+folder_name)
   print 
except:
   print "Invalid Path"
   #will execute if you do not have write permission to the folder

try:
   for i in ports:
      for i in ports:
         file = open('./'+str(i),'w') #opens the files in write mode, and python creates a file when you open it in wr
         file.close()
         if ask==y:
			 print "created file "+ str(i)
except:
   print "Could not create files, please check if you have the appropriate read/write permissions"
