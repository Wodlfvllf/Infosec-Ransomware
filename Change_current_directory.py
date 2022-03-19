# Python program to change the
# current working directory


import os

# Function to Get the current
# working directory
def current_path():
	print("Current working directory before")
	print(os.getcwd())
	print()


# Driver's code
# Printing CWD before
current_path()

# Changing the CWD
os.chdir('../')

# Printing CWD after
current_path()

