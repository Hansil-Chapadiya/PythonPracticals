from tkinter import *
root = Tk()
root.geometry("450x450")
root.title("Text Document")
frame = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
frame.pack()

frame2 = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
frame2.pack()

frame5 = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
frame5.pack(side=BOTTOM, anchor="s", fill="x")

frame3 = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
frame3.pack(side=LEFT, anchor="w", fill="y", pady=1)

frame4 = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
frame4.pack(fill="both")

button = Button(frame, fg="White", bg="grey", text="   File   ")
button.pack(side=LEFT, anchor="nw", padx=8)

button2 = Button(frame, fg="White", bg="grey", text="  Edit   ")
button2.pack(side=LEFT, anchor="nw", padx=8)

button3 = Button(frame, fg="White", bg="grey", text="Selection")
button3.pack(side=LEFT, anchor="nw", padx=8)

button4 = Button(frame, fg="White", bg="grey", text="  View   ")
button4.pack(side=LEFT, anchor="nw", padx=8)

button5 = Button(frame2, fg="white", bg="grey", text=" Doc1   ")
button5.pack(side=LEFT, anchor="nw", padx=8)

button6 = Button(frame3, fg="white", bg="grey", text=" Menubar")
button6.pack(side=LEFT, anchor="nw", padx=8)

button7 = Text(frame4, fg="Cyan", bg="black", font=20, height=50, width=170)
button7.pack(fill=BOTH)


button8 = Button(frame5, fg="white", bg="grey", text="Last Portion")
button8.pack( anchor="sw")

lable = Label(frame, fg="white", bg="black",text='''Document                                                                  ''')
lable.pack(side=TOP, anchor="n", padx=500, fill=X)

lable2 = Label(frame2, fg="White" ,bg="Black")
lable2.pack(padx=800)

root.mainloop()