# Python program to explain os.remove() method
	
# importing os module
import os
	
# File name
file = 'MyPlayground.playground'
	
# File location
location = "/users/shashank/"
	
# Path
path = os.path.join(location, file)
	
# Remove the file
# 'file.txt'
os.remove(path)

