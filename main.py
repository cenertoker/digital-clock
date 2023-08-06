from tkinter import *
from time import *
import datetime

root = Tk()
root.title('CT SAAT')

def clock():
    text = strftime('%H:%M:%S')
    label.config(text=text)
    label.after(1000,clock)


label = Label(root,font=("ds-digital",150),background="green",foreground="yellow")
label.pack(anchor="center")

clock()

mainloop()