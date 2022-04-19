import socket 
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


class GU:
    def __init__(self,chat):
        self.chat=chat
        self.root=tk.Tk()
        self.root.geometry("1000x750")
        self.passw_var=tk.StringVar()
        self.root.title('User Interface')
        bg = PhotoImage(file = "hg1.png")
        
        # Show image using label
        label1 = Label(self.root, image = bg)
        label1.place(x = 0, y = 0)
        
        # Create Frame
        frame1 = Frame(self.root)
        frame1.pack(pady = 20 )

        chat1 = tk.Label(self.root, text = self.chat, fg='red', font = ('calibre',10,'bold'))
        chat1.config(text=self.chat)
        passw_label = tk.Label(self.root, text = 'Press to start Cryptomining', fg='red', font = ('calibre',10,'bold'))  
        sub_btn=tk.Button(self.root,text = 'Submit',relief=RAISED,font=('Arial Bold', 18), command = self.submit)
        chat1.place(relx=0.01,rely=0,relheight=0.05,relwidth=1)
        passw_label.place(relx=0.3,rely=0.4,relheight=0.05,relwidth=0.2)
        sub_btn.place(relx=0.3,rely=0.7,relheight=0.1,relwidth=0.2)
        self.root.mainloop()

    def submit(self):
        #c.send('start'.encode())
        self.passw_var.set("")

s = socket.socket()       
print ("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345               

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))        
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)    
print ("socket is listening")           

c, addr = s.accept()    
print ('Got connection from', addr )
# a forever loop until we interrupt it or
# an error occurs
# send a thank you message to the client. encoding to send byte type.
print("Shashank")
key=c.recv(1024)
print(key.decode())
print("Shashank2")
g=GU(key.decode())
print("Shashank3")
# Close the connection with the client
print("gore ho tum")
c.close()
