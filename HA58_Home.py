from tkinter import *
import tkinter.messagebox as tmsg
from PIL import Image
root = Tk()
root.geometry('500x500')
root.title('Bill')
#root.iconbitmap('D:\MHA\Python\MHA.png')
#--------------------------------------------------------------------
b1 = PhotoImage(file='D:\MHA\Python\MHA1.png')
b2 = PhotoImage(file='D:\MHA\Python\Vege1.png')
b3 = PhotoImage(file="D:\MHA\Python\Grossary.png")
b4 = PhotoImage(file='D:\MHA\Python\MHA2.png')
b5 = PhotoImage(file='D:\MHA\Python\Electronics item.png')
#---------------------------------------------------------------
'''f1 = PhotoImage(file="D:\HA\Python\Image\HM1.png")
f2 = PhotoImage(file="D:\HA\Python\Image\HM2.png")
f3 = PhotoImage(file="D:\HA\Python\Image\HM3.png")
f4 = PhotoImage(file="D:\HA\Python\Image\HM4.png")
f5 = PhotoImage(file="D:\HA\Python\Image\HM5.png")
f6 = PhotoImage(file="D:\HA\Python\Image\HM6.png")
#-----------------------------------------------------------------------
v1 = PhotoImage(file="D:\HA\Python\Image\VEGETABLES\V1.png")
v2 = PhotoImage(file="D:\HA\Python\Image\VEGETABLES\V2.png")
v3 = PhotoImage(file="D:\HA\Python\Image\VEGETABLES\V3.png")
v4 = PhotoImage(file="D:\HA\Python\Image\VEGETABLES\V4.png")
v5 = PhotoImage(file="D:\HA\Python\Image\VEGETABLES\V5.png")
v6 = PhotoImage(file="D:\HA\Python\Image\VEGETABLES\V6.png")'''
#------------------------------------------------------------------
e1 = PhotoImage(file="D:\MHA\Python\com.png")
e2 = PhotoImage(file="D:\MHA\Python\lap.png")
e3 = PhotoImage(file="D:\MHA\Python\wash.png")
#------------------------------------------------------------------
ex = PhotoImage(file="D:\MHA\Python\exti.png")
ex2 = PhotoImage(file="D:\MHA\Python\exite2.png")
#-------------------------------------------------------------------
frame = Frame(root, bg="Black", borderwidth=6, relief=SUNKEN)
frame.grid(sticky=(N,W),padx=10,column=0,ipady=270)
frame1 = Frame(root, bg="black", width=1200, height=500)
frame1.grid(sticky=(N,E,S,W),row=0,column=1)
lb = Label(frame1, bg="White", fg="Orange", text="BILLING SYSTEM", font="LucidaBright 40 bold")
lb.grid(row=2, column=7, sticky=(N,E), padx=350, pady=350, ipady=60, ipadx=60)
#------------------------------------------------------------------------
frame2 = Frame(root,bg="White")
frame2.grid(sticky=S,padx=20)
#---------------------------------------------------------------------
def clear_frame():
    for widget in frame1.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
#---------------------------------------------------------------
def home():
    clear_frame()
    l1=[b2,b3,b5]
    cmd = [fruit,elec,gross]
    a=0
    for column in range(3):
        for i in range(1):
            button2 = Button(frame1,image=l1[a],command=cmd[a])
            button2.grid(row=i, column=column, padx=25, pady=40)
        a +=1
global l13
l13 = []
global l11
l11 = []
global l2
l2 = []
global l4
l4 = []
global l8
l8 = []
global l10
l10 = []
with open('ProductName.txt',"r+") as f:
        l4 = f.readlines()
with open('ProductPath.txt',"r+") as f:
        l2 = f.readlines()
with open('PriceInt.txt','r+') as f:
        l8 = f.readlines()
with open('PriceStr.txt','r+') as f:
        l10 = f.readlines()
for sub in l2:
    l11.append(sub.replace("\n",''))    
for sub1 in l8:
    l13.append(int(sub1))

#--------------------------------------------------------------------------------
def fruit():
    clear_frame()
    global plus
    global l11
    def plus():
        clear_frame()
        Label(frame1, text="Prodeuct name", font="TimesNewRoman 30 bold", bg="black",fg="Red").grid(row=0,column=0, pady=20, padx=20)
        Label(frame1, text="Image path", font="TimesNewRoman 30 bold",bg="black",fg="Red").grid(row=1,column=0, pady=20, padx=20)
        Label(frame1, text="Price", font="TimesNewRoman 30 bold",bg="black",fg="Red").grid(row=3,column=0, pady=20, padx=20)
        Label(frame1, text="Display Price", font="TimesNewRoman 30 bold",bg="black",fg="Red").grid(row=4,column=0, pady=20, padx=20)
        Label(frame1, text="Row", font="TimesNewRoman 30 bold",bg="black",fg="Red").grid(row=5,column=0, pady=20, padx=20)
        Label(frame1, text="Column", font="TimesNewRoman 30 bold",bg="black",fg="Red").grid(row=6,column=0, pady=20, padx=20)
        global Productnameen, ImgPathen, Quanten, Priceen, Columnen, Rowen, DisPlayPriceen
        Pname = StringVar()
        ImagePath = StringVar()
        Price = IntVar()
        DisPlayPrice = IntVar()
        Row= IntVar()
        Column= IntVar()
        Productnameen = Entry(frame1, textvariable=Pname, font="TimesNewroman 18 bold",bg="black",fg="Cyan")
        Productnameen.grid(row=0,column=1,pady=20, padx=20)
        ImgPathen = Entry(frame1, textvariable=ImagePath, font="TimesNewroman 18 bold",bg="black",fg="Cyan")
        ImgPathen.grid(row=1,column=1,pady=20,padx=20)
        Priceen = Entry(frame1, textvariable=Price, font="TimesNewroman 18 bold",bg="black",fg="Cyan")
        Priceen.grid(row=3,column=1,pady=20,padx=20)
        DisPlayPriceen = Entry(frame1, textvariable=DisPlayPrice, font="TimesNewroman 18 bold",bg="black",fg="Cyan")
        DisPlayPriceen.grid(row=4,column=1,pady=20,padx=20)
        Rowen = Entry(frame1, textvariable=Row, font="TimesNewroman 18 bold",bg="black",fg="Cyan")
        Rowen.grid(row=5,column=1,pady=20,padx=20)
        Columnen =Entry(frame1, textvariable=Column, font="TimesNewroman 18 bold",bg="black",fg="Cyan")
        Columnen.grid(row=6,column=1,pady=20,padx=20)
        Button(frame1,text="Add",command=add,bg="black",fg="Red", font="LucidaBright 40 bold").grid(row=10,column=1,ipadx=20,pady=20, padx=20)
    def add():
        tmsg.showinfo('Bill','Prossecing Complete....Please Reopen App')
        global Productnameen, ImgPathen, Priceen, Columnen, Rowen, DisPlayPriceen
        with open('ProductName.txt',"a") as P1:
            P1.write(f"\n{Productnameen.get()}")
        with open ('ProductPath.txt',"a") as P2:
            P2.write(f"\n{ImgPathen.get()}")
        with open('PriceInt.txt','a') as P3:
            P3.write(f"\n{Priceen.get()}") 
        with open('PriceStr.txt','a') as P4:
            P4.write(f"\n{DisPlayPriceen.get()}") 
        #l2.append(PhotoImage(file=ImgPathen.get()))
    def update_scrollregion(event):
        photoCanvas.configure(scrollregion=photoCanvas.bbox("all"))
    photoCanvas = Canvas(frame1, bg="black",width=1250, height=800)
    photoCanvas.grid(row=0, column=0, sticky=(N,E,S,W),padx=10,pady=10)
    canvasFrame = Frame(photoCanvas, bg="black")
    photoCanvas.create_window(0, 0, window=canvasFrame, anchor='nw', )
    
    '''global s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12
    s1 = Scale(canvasFrame, orient=HORIZONTAL, from_=0, to=10)
    s2 = Scale(canvasFrame, orient=HORIZONTAL, from_=0, to=10)
    s3 = Scale(canvasFrame, orient=HORIZONTAL, from_=0, to=10)
    s4 = Scale(canvasFrame, orient=HORIZONTAL, from_=0, to=10)
    s5 = Scale(canvasFrame, orient=HORIZONTAL, from_=0, to=10)
    s6 = Scale(canvasFrame, orient=HORIZONTAL, from_=0, to=10)
    s7 = Scale(canvasFrame, orient=HORIZONTAL, from_=0, to=10)
    s8 = Scale(canvasFrame, orient=HORIZONTAL, from_=0, to=10)
    s9 = Scale(canvasFrame, orient=HORIZONTAL, from_=0, to=10)
    s10 = Scale(canvasFrame, orient=HORIZONTAL, from_=0, to=10)
    s11 = Scale(canvasFrame, orient=HORIZONTAL, from_=0, to=10)
    s12 = Scale(canvasFrame, orient=HORIZONTAL, from_=0, to=10)
    s13 = Scale(canvasFrame, orient=HORIZONTAL, from_=0, to=10)'''
    global l3
    l3 = []
    #print(l4)
    global l12
    l12 = []
    for k in range(len(l11)):
        global img1
        img1 = l11[k] 
        l12.append(PhotoImage(file=img1))
        l3.append(Scale(canvasFrame, orient=HORIZONTAL, from_=0, to=10))
    #print(l11)
    #print(l12)
    a=0
    for column in range(10):
        row = 2
        row1 = 3
        for i in range(1,15,3):
            try:
                button3 = Button(canvasFrame, image=l12[a])
                button3.grid(row=i,column=column,pady=10,padx=78)
                Label(canvasFrame, text=f"{l10[a]}", font=" TimesNewRoman 12 bold", bg="black", fg="Light green").grid(row=row1,column=column, pady=10,padx=78, ipadx=20)
                l3[a].grid(row=row,column=column,padx=78)
                if row == row:
                    row += 3
                if row1 == row1:
                    row1 += 3
                a=a+1
            except:
                break
    Button(frame,text="Submit",command=t, font="LucidaBright 12 bold", fg="cyan",  bg="black").grid(sticky=(S),row=5,column=0, pady=30, ipadx=10,ipady=10)
    Button(frame,text="+", font="LucidaBright 12 bold", fg="cyan",  bg="black", command=plus).grid(sticky=(S),row=6,column=0, pady=20, ipadx=25,ipady=10)
    exitbutton = Button(frame, image=ex2, command=home)
    exitbutton.grid(sticky=(S), row=7, column=0)
    photoScroll = Scrollbar(frame1, orient=VERTICAL,command=photoCanvas.yview)
    photoScroll1 = Scrollbar(frame1, orient=HORIZONTAL,command=photoCanvas.xview)
    photoCanvas.config(yscrollcommand=photoScroll.set,xscrollcommand=photoScroll1.set)
    photoScroll.grid(row=0, column=1, sticky="ns")
    photoScroll1.grid(row=1, column=0, sticky="ew")
    canvasFrame.bind("<Configure>", update_scrollregion)
l5 = []
l6 = []
l7 = [] 
l9 = []
global t
def t():
    def help():
        value = tmsg.askquestion("Confirm","Are you sure for bill pay?")
        if value == "yes":
            msg = "Thanks for choose our app & go to bill pay"
            tmsg.showinfo("Response",msg)
    
            for j in range(len(l12)):
                with open("ProductName.txt") as R:
                    l4 = R.readlines()
                    with open( "Bill_data.txt","a") as f:
                        global l3
                        if l3[j].get() > 0:
                            f.write(f"{l4[j]} = {l3[j].get()}\n")
                            l5.append(j)
                            l6.append(l4[j])
                            l7.append(l3[j].get())
                            l9.append(l3[j].get()*l13[j])  
    help()
global l
def l():
    row = 6
    i = 0
    while i < len(l5):
        butt1 = Button(frame1, text=i+1)
        butt1.grid(row=row,column=0,ipadx=20)
        butt2 = Button(frame1, text=l6[i])
        butt2.grid(row=row, column=1, ipadx=40)
        #global l3
        butt3 = Button(frame1, text=l7[i])
        butt3.grid(row=row, column=5, ipadx=20)

        butt4 = Button(frame1, text=l9[i])
        butt4.grid(row=row,column=6, ipadx=20)

        row += 1
        i += 1
    Label(frame1, text="Total",font=40, bg="black",fg="white").grid(row=row,column=0, padx=30,pady=30, ipadx=30)
    butt = Button(frame1, text=sum(l9), bg="Purple", fg="white", font="TimesNewRoman 16 bold")
    butt.grid(row=row+1,column=0, ipadx=20)
def c():
    def ok():
        tmsg.showinfo("Bill","Bill is ready")
    l5.clear()
    l6.clear()
    l7.clear()
    l9.clear()
    ok()  


    

   
#------------------------------------------------------------------
def elec():
    clear_frame()
    l2 = [e1,e2,e3]
    a=0
    for column in range(1):
        for i in range(3):
            button3 = Button(frame1, image=l2[a])
            button3.grid(row=i,column=column,pady=60,padx=80)
            a=a+1 
    exitbutton = Button(frame1, image=ex2, command=home)
    exitbutton.grid(sticky=S,row=1,column=2)


def gross():
    clear_frame()
    l2 = [e1,e2,e3]
    a=0
    for column in range(1):
        for i in range(3):
            button3 = Button(frame1, image=l2[a])
            button3.grid(row=i,column=column,pady=60,padx=80)
            a=a+1 
    exitbutton = Button(frame1, image=ex2, command=home)
    exitbutton.grid(sticky=S, row=1, column=3)

root.config(bg="black")