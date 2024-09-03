from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("600x600")
root.title("HA Document")

def get():
    print(f"Yes sir!")

def help():
    
    tmsg.showinfo("Help", "Hansil will help you")

def rate():
    print("Rate us")
    value = tmsg.askquestion("Rate us", "How was your experience good or not?")
    if value == "yes":
        msg = "Great, Thanks rate us on app store"
    else:
        msg = "What was wrong ??. "
    tmsg.showinfo("Exeperience",msg)

f1 = Frame(root, bg="green", borderwidth=6, relief=SUNKEN)
f1.pack(side=TOP, anchor="n", fill="x")

mymenu = Menu(f1, bg="cyan")
menu1 = Menu(mymenu, tearoff=0)
menu1.add_command(label="File", command=get)
menu1.add_command(label="new project", command=get)
menu1.add_command(label="New window", command=get)
menu1.add_command(label="Open", command=get)
menu1.add_command(label="Save", command=get)
mymenu.add_cascade(label='File', menu=menu1)

root.config(menu=mymenu)

menu2 = Menu(mymenu)

menu2.add_command(label="Help", command=help)
menu2.add_command(label="Rate us", command=rate)

mymenu.add_cascade(label='Help', menu=menu2)

root.config(menu=mymenu)

root.mainloop()