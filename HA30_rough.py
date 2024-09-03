from tkinter import *
from tkinter.ttk import *
from tkinter.tix import *

from time import strftime

root = Tk()
root.title("Addition")

def Addition():
    string = f"18 + 30 = {18 + 30}"  
    lable.config(text = string )
    lable.after(1000, Addition)



lable = Label(root, font =("C:\\Users\\Admin\\Downloads\\ds_digital", 80), background= "black", foreground = "cyan")
lable.pack(anchor = 'center')
Addition()

mainloop()
