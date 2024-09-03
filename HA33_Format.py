from tkinter import *
root = Tk()

def get():
    with open("record.txt", "a") as f:
        f.write(f"{nameEn.get()} -- {SurnameEn.get()} -- {RollEn.get()} -- {Attenden.get()}\n")

f1 = Frame(root, bg="Black", borderwidth=6, relief=SUNKEN)
f1.pack(side=TOP,anchor="n", fill="x")

f3 = Frame(root, bg="White", borderwidth=6, relief=SUNKEN)
f3.pack(side=BOTTOM,anchor="w", fill="x")

f2 = Frame(root, bg="Black", borderwidth=6, relief=SUNKEN)
f2.pack(side=LEFT,anchor="w",fill="y", pady=1)

f4 = Frame(root, bg="Black", borderwidth=6, relief=SUNKEN)
f4.pack(side=LEFT,anchor="n",fill="y", pady=1)



Label(f1, fg="cyan", bg="black", text="Form",font=("C:\\Users\\Admin\\Downloads\\ds_digital\\DS-DIGI ", 20)).pack(side=TOP,anchor="n")
Label(f3, fg="White", bg="black", text="Filling form").pack( anchor="s")
Button(f2, fg="Red", bg="White", text="Menubar",font=("C:\\Users\\Admin\\Downloads\\ds_digital\\DS-DIGI ", 10)).pack(side=LEFT,anchor="nw",padx=30)
Label(f4, fg="Red", text="Name:", font=20).grid(row=0, column=2, pady=20, padx=20)
Label(f4, fg="Red", text="Surname:", font=20).grid(row=1, column=2, pady=20, padx=20)
Label(f4, fg="Red", text="RollNo:", font=20).grid(row=2, column=2, pady=20, padx=20)
Label(f4, fg="Red", text="Attendence:", font=20).grid(row=3, column=2, pady=20, padx=20)

name = StringVar()
Surname = StringVar()
RollNo = StringVar()
Attend = StringVar()

nameEn = Entry(f4, textvariable=name, font=30)
SurnameEn = Entry(f4, textvariable=Surname, font=30)
RollEn = Entry(f4, textvariable=RollNo, font=30)
Attenden = Entry(f4, textvariable=Attend, font=30)

nameEn.grid(row=0, column=4, padx=500)
SurnameEn.grid(row=1, column=4, padx=500)
RollEn.grid(row=2, column=4, padx=500)
Attenden.grid(row=3, column=4, padx=500)

Button(f4, text="Submit", fg="cyan", bg="Black", font=57, command=get).grid(row=6, column=4, padx=50, pady=10)
root.mainloop()