#change filenames of all files in the given path to something you put there, You can name them in some order,
# like Photo001, Photo002 etc, of great help when you have a lot of files with contextual names
import os

path = raw_input('Enter path: ')
tempate_name=raw_input('Enter the name you want in the bulk rename: ')
template_extension = raw_input('Enter the extension: ')

j=0
os.chdir(path)
for i in os.listdir(path):
	os.rename(i,template_name+ str(j)+template_extension')
	j+=1
