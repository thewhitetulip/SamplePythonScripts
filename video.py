#!/usr/bin/python
import os
import subprocess
import random

path=""
video_list=[]

def set_path():
	if not os.path.exists("./path.txt"):
		path = raw_input("Enter the path where videos are stored")
		if path !="":
			try:
				f=open("./path.txt","w")
			except(IOError):
				print "Something is wrong with the file"
				exit
			f.write(path)
			f.close()

def play():	
	try:
		f = open("./path.txt")
	except(IOError):
		print "Path invalid, please try again"
		exit
	path = f.readline()
	f.close()
	
	video_list = os.listdir(path)
	os.chdir(path)
	
	subprocess.Popen(["vlc", video_list[random.randint(0,len(video_list)-1)]])

if __name__=="__main__":
	set_path()
	play()
