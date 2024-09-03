from tkinter import *

def update_scrollregion(event):
    photoCanvas.configure(scrollregion=photoCanvas.bbox("all"))

root = Tk()   


frame1 = Frame(root, bg="#EBEBEB", width=1500, height=500)
frame1.grid(sticky=(N,E,S,W))
#frame1.rowconfigure(0, weight=1) 
#frame1.columnconfigure(0, weight=1) 

photoCanvas = Canvas(frame1, bg="#EBEBEB",width=1500, height=800)
photoCanvas.grid(row=0, column=0, sticky=(N,E,S,W))

canvasFrame = Frame(photoCanvas, bg="#EBEBEB", )
photoCanvas.create_window(0, 0, window=canvasFrame, anchor='nw')

for i in range(100):
   element = Button(canvasFrame, text='Button %i' % i, borderwidth=0, bg="#EBEBEB")
   element.grid(row=0,column=i,padx=5, pady=5, sticky="nsew")

photoScroll = Scrollbar(frame1, orient=HORIZONTAL, command=photoCanvas.xview)
#photoScroll.config(command=photoCanvas.xview)
photoCanvas.config(xscrollcommand=photoScroll.set)
photoScroll.grid(row=1, column=0, sticky="ew")

canvasFrame.bind("<Configure>", update_scrollregion)

root.mainloop()