import os
fd = "Copy of Sales quote.txt"

# popen() is similar to open()
file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

os.rename(fd,'New.txt')
size = os.path.getsize("Os_Module")
 
print("Size of the file is", size," bytes.")
os.remove('New.txt')
# File not closed, shown in next function.

