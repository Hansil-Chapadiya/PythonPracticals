from tkinter import *

root = Tk()
root.title("Window Resizer")
canvas_width = 800
canvas_hieght = 800
def get():
    canvas_hieght = HeEn.get()
    canvas_width  = wiEn.get()
    root.geometry(f"{canvas_hieght}x{canvas_width}") 

f1=Frame(root, bg="Red", borderwidth=4, relief=SUNKEN)
f1.pack(side=TOP, anchor="n", fill="x")
f2=Frame(root, bg="Black", borderwidth=4, relief=SUNKEN)
f2.pack(side=LEFT, anchor="n", fill="y")

Label(f1, text="Window resizer", fg="White", bg="Black", font=36).pack(side=TOP, anchor="n")
Label(f2, text="Height :", fg="Cyan", bg="black", font=30 ).grid(row=3, column=4, padx=120, pady=100)
Label(f2, text="Width  :", fg="Cyan", bg="black", font=30 ).grid(row=5, column=4, padx=120, pady=100)

HeVal = StringVar()
wiVal = StringVar()

HeEn = Entry(f2,textvariable=HeVal, font=30)
wiEn = Entry(f2,textvariable=wiVal, font=30)

HeEn.grid(row=3, column=6, padx=100)
wiEn.grid(row=5, column=6, padx=100)

button = Button(f2, fg="Red", bg="Black", text="Submit", font=40, command=get)
button.grid(row=7, column=6, padx=100)

root.mainloop()