from tkinter import *

root = Tk()

#scrollbar = Scrollbar(root)
#scrollbar.pack(side=LEFT, fill="y")
myslider = Scale(root, orient=HORIZONTAL, from_=0, to=10)
#myslider.set(23)
myslider.grid()

#text = Text(root, yscrollcommand=myslider.set)
#text.pack(fill=BOTH)
def submit():
    print(myslider.get())
#myslider.config(command=text.yview)
submit = Button(root, text="Submit",command=submit)
submit.grid()


root.mainloop()