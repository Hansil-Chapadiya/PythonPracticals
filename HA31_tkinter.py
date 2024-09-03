from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("444x100")
root.title('HAnsil GUI')


lable = Label(root, text="This is taskbar",background = "Cyan",foreground = "Black",font = "comicsansms 19 bold", borderwidth=4, relief= SUNKEN)
lable.pack(side=BOTTOM, anchor="s", fill=X, padx = 11, pady=11)

lable_t = Label(root, text="This is Title bar",background = "light green",foreground = "blue",font = "comicsansms 19 bold", borderwidth=4, relief= SUNKEN)
lable_t.pack(side=TOP, anchor="n", fill=X, padx = 11, pady=11)

lable_M = Label(root, text="This is Menu bar",background = "light green",foreground = "blue",font = "comicsansms 19 bold", borderwidth=4, relief= SUNKEN)
lable_M.pack(side=TOP, anchor="n", fill=X, padx = 11, pady=11)

lable_1 = Label(root, text="Button 1",background = "Black",foreground = "red",font = "comicsansms 19 bold", borderwidth=4, relief= SUNKEN)
lable_1.pack(side=LEFT, anchor="nw", fill=X, padx = 11, pady=11)

lable_2 = Label(root, text="Button 2",background = "Black",foreground = "red",font = "comicsansms 19 bold", borderwidth=4, relief= SUNKEN)
lable_2.pack(side=LEFT, anchor="n", fill=X, padx = 11, pady=11)

lable_c = Label(root, text=" This is BODY",background = "light green",foreground = "Magenta",font = "comicsansms 36 bold", borderwidth=15, relief= SUNKEN)
lable_c.pack(anchor="n", fill=X, padx = 100, pady=100)

root.mainloop()