import tkinter as tk
import decrypt

class GUi:
	def __init__(self,Key):
		self.root=tk.Tk()
		self.root.geometry("600x400")
		self.passw_var=tk.StringVar()
		self.Key=Key
		passw_label = tk.Label(self.root, text = 'Password', font = ('calibre',10,'bold'))
		passw_entry=tk.Entry(self.root, textvariable = self.passw_var, font = ('calibre',10,'normal'), show = '*')   
		sub_btn=tk.Button(self.root,text = 'Submit', command = self.submit)
		passw_label.grid(row=1,column=0)
		passw_entry.grid(row=1,column=1)
		sub_btn.grid(row=2,column=1)
		self.root.mainloop()

	def submit(self):
		password=self.passw_var.get()
		if password == self.Key:
			decrypt.decryption(self.Key)
			self.root.destroy()
		else:
			passw_lab = tk.Label(self.root, text = 'WrongPassword', font = ('calibre',10,'bold'))
			passw_lab.grid(row=1,column=0)  
		self.passw_var.set("")
