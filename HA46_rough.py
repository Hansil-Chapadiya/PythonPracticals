from tkinter import *
import math
class calculator:
    def __init__(self) :
        root = Tk()
        root.title('MHA')
        root.configure(background="white")
        self.string = StringVar()
        entry = Entry(root, textvariable=self.string)
        entry.grid(row=0,column=0,columnspan=6)
        entry.configure(background="white")
        entry.focus()

        values = ['7','8','9','/','%','clear','AC',
                  '4','5','6','*','(",")','**',
                  '1','2','3','-','=',',','0','.','min','+','sin','asin','cos', 'acos','tan()',
                  'pow','log10','max','abs','floor','pi','e','log','ceil','degrees','radians']
        
        text = 1
        i = 0
        row = 1
        col = 0
        for txt in values:
            padx = 10
            pady = 10
            if(i==7):
                row=2
                col=0
            if(i==14):
                row=3
                col=0
            if(i==19):
                row=4
                col=0
            if(i==26):
                row=5
                col=0
            if(i==33):
                row=6
                col=0
            if txt == '=':
                btn = Button(root,height=2,width=4,padx=70,pady=pady,text=txt, command=lambda txt=txt:self.equals())
                btn.grid(row=row,column=col,columnspan=3,padx=2,pady=2)
                btn.configure(background="yellow")
            elif txt == "clear":
                btn = Button(root,height=2,width=4,padx=padx,pady=pady,text=txt, command=lambda txt=txt:self.delete())
                btn.grid(row=row,column=col,padx=1,pady=1)
                btn.configure(background="grey")
            elif txt == "AC":
                btn = Button(root,height=2,width=4,padx=padx,pady=pady,text=txt, command=lambda txt=txt:self.clearall())
                btn.grid(row=row,column=col,padx=1,pady=1)
                btn.configure(background="red")
            else:
                btn = Button(root,height=2,width=4,padx=padx,pady=pady,text=txt, command=lambda txt=txt:self.addChar(txt))
                btn.grid(row=row,column=col,padx=1,pady=1)
                btn.configure(background="cyan")

            col = col+1
            i = i+1
        root.mainloop()

    def clearall(self):
        self.string.set('')
    
    def equals(self):
        result = ""

        try:
            result = eval(self.string.get())
            self.string.set(result)
        except:
            result = "Invalid Input"
        self.string.set(result)

    def addChar(self,char):
        self.string.set(self.string.get()+(str(char)))

    def delete(self):
        self.string.set(self.string.get()[0:-1])

calculator()
