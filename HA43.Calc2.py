import math
from tkinter import *
from math import *
root = Tk()
root.geometry("850x550")
def click(event):
    global scvalue
    text = event.widget.cget('text')
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        elif True:
            value = eval(scentry.get())
        scvalue.set(value)
        scentry.update()
        
    elif text == 'C' :
       scvalue.set("")
       scentry.update()
    else:
        scvalue.set(scvalue.get() + text)
        scentry.update()
'''def trig(event):
    global scvalue
    text = event.widget.cget('text')
    if text == '=':
        scvalue = round(math.cos(math.radians(scvalue)), 5)
    scvalue.set(scvalue.get() + text)
    scentry.update()'''#
#---------------------------------------------------------------
f1 = Frame(root, borderwidth=6, relief=SUNKEN)
f1.pack(side=TOP,anchor="n", fill="x")

f2 = Frame(root,bg="Purple", borderwidth=7 ,relief=SUNKEN)
f2.pack(fill=BOTH)

f3 = Frame(root, bg="Purple", borderwidth=7, relief=SUNKEN)
f3.pack(fill="x")

f4 = Frame(root, bg="black", borderwidth=7, relief=SUNKEN)
f4.pack(fill="x")

f5 = Frame(root, bg="black", borderwidth=7, relief=SUNKEN)
f5.pack(fill=BOTH)
#---------------------------------------------------------------
scvalue = StringVar()
scvalue.set("")
scentry = Entry(f1, fg="Black", bg="White", font="lucida 40 bold", justify=RIGHT, textvar=scvalue )
scentry.pack(fill="x", ipady=13)
#---------------------------------------------------------------
for i in range(0,10):
    b = Button(f2, fg="Cyan", bg="Black", text=f"{i}", font="lucida 18 bold", padx=12, pady=12)
    b.pack(side=LEFT, anchor="n",fill=BOTH, pady=19, padx=42)
    b.bind('<Button-1>',click)
b2 = Button(f2, fg="Yellow", bg="Black", text=f"C", font="lucida 18 bold", padx=9, pady=10)
b2.pack(side=RIGHT, anchor="ne",fill=BOTH, pady=19, padx=0)
b2.bind('<Button-1>', click)
#---------------------------------------------------------------
l1 = ["+", "-", "*", "/", "%", "=","."]
for item in l1:
    b3 = Button(f3, fg="Yellow", bg="Black", text=f"{item}", font="lucida 18 bold", padx=12, pady=12)
    b3.pack(side=LEFT ,anchor="nw",fill=BOTH, pady=19, padx=42)
    b3.bind('<Button-1>', click)
#b4 = Button(f3, fg="Yellow", bg="Black", text=f"cos", font="lucida 18 bold", padx=12, pady=12)
#b4.pack(side=LEFT ,anchor="nw",fill=BOTH, pady=19, padx=42)
#b4.bind('<Button-1>', )

b8 = Button(f3, fg="Red", bg="Black", text=f"Exit", font="lucida 18 bold", command=quit ,padx=1, pady=1).pack(side=RIGHT, anchor="ne",fill=BOTH, pady=1, padx=1)
root.configure(background="Black")
root.mainloop()