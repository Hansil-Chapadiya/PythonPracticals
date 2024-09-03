from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import  askopenfilename, asksaveasfilename
import os
#-------------------------------------------------------------------------------------------------
root = Tk()
root.geometry("750x550")
root.title('H-Notepad')
p1 = PhotoImage(file='MHA.png')
root.iconphoto(False, p1)
def new():
    global file
    root.title("untitled-notepad")
    file = None
    textarea.delete(1.0, END)
def Save():
    global file
    if file == None:
        files = [("All Files", "*.*"),('Python Files','*.py'), ("Text Document","*.txt")]
        file = asksaveasfilename(filetypes = files, defaultextension=files)
        if file == "":
            file = None
        else:
            f = open(file,"w")
            f.write(textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
    else:
        f = open(file,"w")
        f.write(textarea.get(1.0, END))
        f.close()
def Open():
    global file
    file = askopenfilename(defaultextension = ".txt", filetypes=[("All files", "*.*"), ("Text Document","*.txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        textarea.delete(1.0,END)
        f= open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()
def copy():
    textarea.event_generate(('<<Copy>>'))
def cut():
    textarea.event_generate(('<<Cut>>'))
def paste():
    textarea.event_generate(('<<Paste>>'))
def help():
    tmsg.showinfo("Help", "Hansil will help you")
#---------------------------------------------------------------------------------------------------
menubar = Menu(root, background='black', fg='white')
filemenu = Menu(menubar, tearoff=0, background='Black', fg="cyan")
filemenu.add_command(label="New",font="TimesNewRoman 12 bold", command=new)
filemenu.add_command(label="Save",font="TimesNewRoman 12 bold", command=Save)
filemenu.add_command(label="Open",font="TimesNewRoman 12 bold", command=Open)
filemenu.add_command(label="Save as",font="TimesNewRoman 12 bold", command=Save)
filemenu.add_command(label="Exit",font="TimesNewRoman 12 bold", command=quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0, background="black", foreground="cyan")
editmenu.add_command(label="Cut",font="TimesNewRoman 12 bold", command=cut)
editmenu.add_command(label="copy",font="TimesNewRoman 12 bold", command=copy)
editmenu.add_command(label="paste",font="TimesNewRoman 12 bold", command=paste)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0, background="black",foreground="cyan")
helpmenu.add_command(label="help",font="TimesNewRoman 12 bold", command=help)
menubar.add_cascade(label="Help", menu=helpmenu)
#-----------------------------------------------------------------------------------------------------------------
textarea = Text(root, fg="cyan",bg="black",font="TimesNewRoman 12 bold", height=900, width=1000)
file=None
textarea.pack(expand=True, fill=BOTH)
root.config(menu=menubar, background="black")
#---------------------------------------------------------------------------------------------------------
scroll = Scrollbar(textarea)
scroll.pack(side=RIGHT,fill="y")
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)
root.mainloop()