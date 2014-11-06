import os

def rename_files():
	#Get a list of file names.
	file_list=os.listdir(r"C:\Users\xxdpavelxx\Pictures\Anatomy\Injuries")  #lists files in specified directory
	print file_list
	current_path=os.getcwd()
	os.chdir(r"C:\Users\xxdpavelxx\Pictures\Anatomy\Injuries") # can change directory who's files you want to rename.
	#For each file change its name.
	for file_name in file_list:
		print "old name of file: " +file_name
		os.rename(file_name,file_name.translate(None,"abc")) # will take out the characters 'a','b','c' from file names and replace it with ''.
		print "new name of file: " +file_name
	os.chdir(current_path)
	
rename_files()