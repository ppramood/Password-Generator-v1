import random 
import tkinter as tk
from tkinter import BOTH, END, LEFT

# ---------- Fuction Area ---------#
def call_fuc():
	return lambda :Pass_Generator()

def Pass_Generator():
	
	alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	my_pw = ""
	pw_length=passcompare()
	for i in range(pw_length):
		next_index = random.randrange(len(alphabet))
		my_pw+=alphabet[next_index]
	out=box_clear()
	output_box.insert(END,my_pw)

def passlength(length):
	password_length = length
	return password_length

def box_clear():
	output_box.delete("1.0",END)

def passcompare():
	if pass_len.get():
		return passlength(int(pass_len.get()))
	else:
		return passlength(length=8)


#-----------End Of Fuction Area ------------#
#----------------GUI Area-------------------#

gui = tk.Tk()
gui.title("Password Generator")
message = tk.Label(gui,text="GENERATED PASSWORD",fg="red",bg="black")
message.pack()

#display = StringVar() # is not defined 
#display='Click Generate'

button = tk.Button(gui,text="Generate",bg="black",fg="red")
button.config(command=call_fuc())
button.pack()

pass_len=tk.Entry(gui)
pass_len.pack()

output_box = tk.Text(gui,width =30,height=5)
output_box.insert(END,"Your Password Generated Here ")
output_box.pack()

button1 = tk.Button(gui,text="info")
button1.config(bg="black",fg="red",font=1,height=1,width=3)
button1.config()
button1.pack()
gui.mainloop()
#---------------End Of GUI------------------#

