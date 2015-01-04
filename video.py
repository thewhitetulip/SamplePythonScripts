import os
import subprocess
import random

path=""
video_list=[]

def set_path():
	if not os.path.exists("./path.txt"):
		path = raw_input("Enter the path where videos are stored")
		path=path.lstrip().rstrip()
		if os.path.exists(path):
			if path !="":
				try:
					f=open("./path.txt","w")
				except(IOError):
					print "Something is wrong with the file"
					exit()
				finally:
					print "file created on this path: "+path
				f.write(path)
				f.write("\n")
				f.close()
		else:
			print "That path is invalid"
	else:
		return

def listing():	
#this function invokes the vlc media player to actually play a video
	try:
		f = open("./path.txt")
	except(IOError):
		print "Path invalid, please try again"
		exit()
	
	path = f.readline()
	f.close()
	
	path=path.lstrip().rstrip()
	video_list = os.listdir(path)
	total_videos = len(video_list)
	
	if not os.path.exists("./list.txt"):
		f=open("./list.txt","w")
		num=random.randint(0,len(video_list)-1)
		f.write("%s,"%(num))
		f.close()
	else:
		f = open("./list.txt","r")
		line = f.readline()
		line = line.split(",")
		num=0
		if len(line)==total_videos: #when all the videos have been watched, truncate the file
			print "all videos finished"
			f=open("./list.txt","w")
			f.close()
		while True:
			num=random.randint(0,len(video_list)-1)
			if str(num) not in line:
				break
		f=open("./list.txt","a")
		f.write("%s,"%(num))
		print "written to file"
		f.close()					

	play(path, video_list, num)

def play(path, video_list, num):
	os.chdir(path)
	subprocess.Popen(["vlc", video_list[num]])


if __name__=="__main__":
	set_path()
	listing()
