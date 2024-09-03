from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('500x500')
root.title('Bill')

main_frame = Frame(root)
main_frame.pack(side=LEFT,anchor="nw",fill=BOTH)

my_canvas = Canvas(main_frame)
my_canvas.pack()

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill="y")

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

sframe = Frame(my_canvas)
my_canvas.create_window((0,0), window=sframe)

for i in range(100):
    b1 = Button(sframe,text=f"b{i}")
    b1.pack(pady=20)


root.mainloop()