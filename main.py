import sys
import os
import tkinter
from tkinter import *




# create root window
root = Tk()
 
# root window title and dimension
root.title("Twilio APP - Call + SMS")
# Set geometry(widthxheight)
root.geometry('350x200')
 
# adding a label to the root window
lbl = Label(root, text = "Message To Send ")
lbl.grid()
 
# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =0)



 
# function to display user text when
# button is clicked
def clicked():
 global your_msg
 your_msg = txt.get()
   # res = "You wrote" + txt.get()
    #lbl.configure(text = res)
os.system(' python send_sms.py')
 
# button widget with red color text inside
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)
btn.place(x= 80 , y = 120)

lbl = Label(root, text = "Mobile Number ")
lbl.grid()
lbl.place(x=10, y=50)
txt1 = Entry(root, width=10)
txt1.grid(column =1, row =5)
txt1.place(y=50 , x =130)





# Execute Tkinter
root.mainloop()
