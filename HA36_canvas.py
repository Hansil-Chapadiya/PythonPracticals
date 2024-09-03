from tkinter import *



root = Tk()

canvas_width = 800
canvas_hight = 400

root.geometry(f"{canvas_width}x{canvas_hight}")

canvas_widget=Canvas(root, height=canvas_hight, width=canvas_width)
canvas_widget.pack()


#canvas_widget.create_oval(10,80,80,10, fil="cyan")
#canvas_widget.create_polygon(30,120,50,100,60,150, fill="red")
#canvas_widget.create_rectangle(12,400,400,12, fill="red")
canvas_widget.create_text(30,120, text="Hansil", fill="Blue", font=97)
 

root.mainloop()