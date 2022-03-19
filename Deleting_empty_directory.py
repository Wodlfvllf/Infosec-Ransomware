# Python program to explain os.rmdir() method
	
# importing os module
import os
	
# Directory name
directory = "Create"
	
# Parent Directory
parent = "/Users/shashank/python/"
	
# Path
path = os.path.join(parent, directory)
	
# Remove the Directory
# "Geeks"
os.rmdir(path)

