from tkinter import *
def get(event):
    print(f"You clicked on {event.x} & {event.y}")

root = Tk()
root.geometry("500x500")

button = Button(root, text="Click here" , bg="black", fg="cyan")
button.pack()

button.bind('<Button-1>',get)


root.mainloop()