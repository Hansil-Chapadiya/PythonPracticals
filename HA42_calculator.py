from tkinter import *

root = Tk()
root.geometry("850x550")
def click(event):
    global scvalue
    text = event.widget.cget('text')
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(scentry.get())
        scvalue.set(value)
        scentry.update()

    elif text == 'C' :
       scvalue.set("")
       scentry.update()
    else:
        scvalue.set(scvalue.get() + text)
        scentry.update()

f1 = Frame(root, borderwidth=6, relief=SUNKEN)
f1.pack(side=TOP,anchor="n", fill="x")

f2 = Frame(root,bg="Purple", borderwidth=7 ,relief=SUNKEN)
f2.pack(fill=BOTH)

f3 = Frame(root, bg="Purple", borderwidth=7, relief=SUNKEN)
f3.pack(fill="x")

f4 = Frame(root, bg="black", borderwidth=7, relief=SUNKEN)
f4.pack(fill="x")

scvalue = StringVar()
scvalue.set("")

scentry = Entry(f1, fg="Black", bg="White", font="lucida 40 bold", justify=RIGHT, textvar=scvalue )
scentry.pack(fill="x", ipady=13)

for i in range(0,10):
    b = Button(f2, fg="Cyan", bg="Black", text=f"{i}", font="lucida 18 bold", padx=12, pady=12)
    b.pack(side=LEFT, anchor="n",fill=BOTH, pady=19, padx=42)
    b.bind('<Button-1>',click)

b2 = Button(f2, fg="Yellow", bg="Black", text=f"C", font="lucida 18 bold", padx=9, pady=10)
b2.pack(side=RIGHT, anchor="ne",fill=BOTH, pady=19, padx=0)
b2.bind('<Button-1>', click)

b3 = Button(f3, fg="Yellow", bg="Black", text=f"+", font="lucida 18 bold", padx=12, pady=12)
b3.pack(side=LEFT ,anchor="nw",fill=BOTH, pady=19, padx=42)
b3.bind('<Button-1>', click)

b4 = Button(f3, fg="Yellow", bg="Black", text=f"-", font="lucida 18 bold", padx=12, pady=12)
b4.pack(side=LEFT ,anchor="nw",fill=BOTH, pady=19, padx=42)
b4.bind('<Button-1>', click)

b5 = Button(f3, fg="Yellow", bg="Black", text=f"*", font="lucida 18 bold", padx=12, pady=12)
b5.pack(side=LEFT ,anchor="nw",fill=BOTH, pady=19, padx=42)
b5.bind('<Button-1>', click)

b6 = Button(f3, fg="Yellow", bg="Black", text=f"/", font="lucida 18 bold", padx=12, pady=12)
b6.pack(side=LEFT ,anchor="nw",fill=BOTH, pady=19, padx=42)
b6.bind('<Button-1>', click)

b7 = Button(f3, fg="Yellow", bg="Black", text=f"%", font="lucida 18 bold", padx=11, pady=12)
b7.pack(side=LEFT ,anchor="nw",fill=BOTH, pady=19, padx=50)
b7.bind('<Button-1>', click)

b9 = Button(f3, fg="Yellow", bg="Black", text=f"=", font="lucida 18 bold", padx=11, pady=12)
b9.pack(side=LEFT ,anchor="nw",fill=BOTH, pady=19, padx=40)
b9.bind('<Button-1>', click)

b8 = Button(f3, fg="Red", bg="Black", text=f"Exit", font="lucida 18 bold", command=quit ,padx=1, pady=1).pack(side=RIGHT, anchor="ne",fill=BOTH, pady=1, padx=1)

root.configure(background="Black")

root.mainloop()