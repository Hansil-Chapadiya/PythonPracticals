from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('500x500')
root.title('Billing System')
root.iconbitmap('D:\MHA\Python\MHA.png')
root.config(bg="black")
#--------------------------------------------------------------------
Home = PhotoImage(file='D:\MHA\Python\MHA1.png')
VegeTables = PhotoImage(file='D:\MHA\Python\Vege1.png')
GrosSsary = PhotoImage(file="D:\MHA\Python\Grossary.png")
BillPay = PhotoImage(file='D:\MHA\Python\MHA2.png')
EleCtronic = PhotoImage(file='D:\MHA\Python\Electronics item.png')
#-----------------------------------------------------------------------
ex = PhotoImage(file="D:\MHA\Python\exti.png")
ex2 = PhotoImage(file="D:\MHA\Python\exite2.png")
#-------------------------------------------------------------------
e1 = PhotoImage(file="D:\MHA\Python\com.png")
e2 = PhotoImage(file="D:\MHA\Python\lap.png")
e3 = PhotoImage(file="D:\MHA\Python\wash.png")
#-------------------------------------------------------------------
MainMenuframe = Frame(root, bg="Black", borderwidth=6, relief=SUNKEN)
MainMenuframe.grid(sticky=(N,W),padx=10,column=0,ipady=270)
Homeframe = Frame(root, bg="black", width=1200, height=500)
Homeframe.grid(sticky=(N,E,S,W),row=0,column=1)
Titel_Bill_System = Label(Homeframe, bg="White", fg="Orange", text="BILLING SYSTEM", font="LucidaBright 40 bold")
Titel_Bill_System.grid(row=2, column=7, sticky=(N,E), padx=350, pady=350, ipady=60, ipadx=60)
#---------------------------------------------------------------------
def clear_frame():
    for widget in Homeframe.winfo_children():
        widget.destroy()
def home():
    clear_frame()
    CatagoryListImg=[VegeTables,GrosSsary,EleCtronic]
    cmd = [fruit,elec,gross]
    a=0
    for column in range(3):
        for i in range(1):
            CatagoryBut = Button(Homeframe,image=CatagoryListImg[a],command=cmd[a])
            CatagoryBut.grid(row=i, column=column, padx=25, pady=40)
        a += 1
#----------------------------------------------------------------------------------------------------------------------------
global ImageList, ImagePathList, ProNameList, PriceList, PriceListCopy, PriceListStr
ProNameList = []
ImagesList = []
ImagePathList = []
PriceList = []
PriceListCopy = []
PriceListStr = []
with open('ProductPath.txt',"r+") as f:
        ImagesList = f.readlines()
with open('ProductName.txt',"r+") as f:
        ProNameList = f.readlines()
with open('PriceInt.txt','r+') as f:
        PriceList = f.readlines()
with open('PriceStr.txt','r+') as f:
        PriceListStr = f.readlines()
for sub in ImagesList:
    ImagePathList.append(sub.replace("\n",'')) 
for sub1 in PriceList:
    PriceListCopy.append(int(sub1))
#----------------------------------------------------------------------------------------------------------------------------
def fruit():
    clear_frame()
    def plus():
        clear_frame()
        Label(Homeframe, text="Prodeuct name", font="TimesNewRoman 30 bold", bg="black",fg="Red").grid(row=0,column=0, pady=20, padx=20)
        Label(Homeframe, text="Image path", font="TimesNewRoman 30 bold", bg="black",fg="Red").grid(row=1,column=0, pady=20, padx=20)
        Label(Homeframe, text="Price", font="TimesNewRoman 30 bold", bg="black",fg="Red").grid(row=3,column=0, pady=20, padx=20)
        Label(Homeframe, text="Display Price", font="TimesNewRoman 30 bold",bg="black",fg="Red").grid(row=4,column=0, pady=20, padx=20)
        Label(Homeframe, text="Row", font="TimesNewRoman 30 bold", bg="black",fg="Red").grid(row=5,column=0, pady=20, padx=20)
        Label(Homeframe, text="Column", font="TimesNewRoman 30 bold", bg="black",fg="Red").grid(row=6,column=0, pady=20, padx=20)
        global Productnameen, ImgPathen, Quanten, Priceen, Columnen, Rowen,DisPlayPriceen
        Pname = StringVar()
        ImagePath = StringVar()
        Price = IntVar()
        DisPlayPrice = IntVar()
        Row= IntVar()
        Column= IntVar()
        Productnameen = Entry(Homeframe, textvariable=Pname, font="TimesNewroman 18 bold",bg="black",fg="Cyan")
        Productnameen.grid(row=0,column=1,pady=20, padx=20)
        ImgPathen = Entry(Homeframe, textvariable=ImagePath, font="TimesNewroman 18 bold",bg="black",fg="Cyan")
        ImgPathen.grid(row=1,column=1,pady=20,padx=20)
        Priceen = Entry(Homeframe, textvariable=Price, font="TimesNewroman 18 bold",bg="black",fg="Cyan")
        Priceen.grid(row=3,column=1,pady=20,padx=20)
        DisPlayPriceen = Entry(Homeframe, textvariable=DisPlayPrice, font="TimesNewroman 18 bold",bg="black",fg="Cyan")
        DisPlayPriceen.grid(row=4,column=1,pady=20,padx=20)
        Rowen = Entry(Homeframe, textvariable=Row, font="TimesNewroman 18 bold",bg="black",fg="Cyan")
        Rowen.grid(row=5,column=1,pady=20,padx=20)
        Columnen =Entry(Homeframe, textvariable=Column, font="TimesNewroman 18 bold",bg="black",fg="Cyan")
        Columnen.grid(row=6,column=1,pady=20,padx=20)
        Button(Homeframe,text="Add",command=add,font="LucidaBright 40 bold").grid(row=10,column=1,ipadx=20,pady=20, padx=20)
    def add():
        global Productnameen, ImgPathen, Priceen, Columnen, Rowen,DisPlayPriceen
        tmsg.showinfo('Bill','Prossecing Complete....Please Reopen App')
        with open('ProductName.txt',"a") as P1:
            P1.write(f"\n{Productnameen.get()}")
        with open ('ProductPath.txt',"a") as P2:
            P2.write(f"\n{ImgPathen.get()}")
        with open('PriceInt.txt','a') as P3:
            P3.write(f"\n{Priceen.get()}") 
        with open('PriceStr.txt','a') as P4:
            P4.write(f"\n{DisPlayPriceen.get()}") 
    def update_scrollregion(event):
        photoCanvas.configure(scrollregion=photoCanvas.bbox("all"))
    photoCanvas = Canvas(Homeframe, bg="black",width=1250, height=800)
    photoCanvas.grid(row=0, column=0, sticky=(N,E,S,W),padx=10,pady=10)
    canvasFrame = Frame(photoCanvas, bg="black")
    photoCanvas.create_window(0, 0, window=canvasFrame, anchor='nw', )
    global ScaleList, ImagePathListCopy
    ScaleList = []
    ImagePathListCopy = []
    for k in range(len(ImagePathList)):
        global img
        img = ImagePathList[k] 
        ImagePathListCopy.append(PhotoImage(file=img))
        ScaleList.append(Scale(canvasFrame, orient=HORIZONTAL, from_=0, to=10))
    a=0
    for column in range(10):
        row = 2
        row1 = 3
        for i in range(1,12,3):
            try:
                ItemBut = Button(canvasFrame, image=ImagePathListCopy[a])
                ItemBut.grid(row=i,column=column,pady=10,padx=78)
                Label(canvasFrame, text=f"{PriceListStr[a]}", font=" TimesNewRoman 12 bold", bg="black", fg="Light green").grid(row=row1,column=column, pady=10,padx=78, ipadx=20)
                ScaleList[a].grid(row=row,column=column,padx=78)
                if row == row:
                    row += 3
                if row1 == row1:
                    row1 += 3
                a=a+1
            except:
                break
    Button(MainMenuframe,text="Submit",command=Procedure_Bill, font="LucidaBright 12 bold", fg="cyan",  bg="black").grid(sticky=(S),row=5,column=0, pady=50, ipadx=10,ipady=10)
    Button(MainMenuframe,text="+", font="LucidaBright 12 bold", fg="cyan",  bg="black", command=plus).grid(sticky=(S),row=6,column=0, pady=50, ipadx=25,ipady=10)
    exitbutton = Button(MainMenuframe, image=ex2, command=home)
    exitbutton.grid(sticky=(S), row=7, column=0)
    photoScroll = Scrollbar(Homeframe, orient=VERTICAL,command=photoCanvas.yview)
    photoScroll1 = Scrollbar(Homeframe, orient=HORIZONTAL,command=photoCanvas.xview)
    photoCanvas.config(yscrollcommand=photoScroll.set,xscrollcommand=photoScroll1.set)
    photoScroll.grid(row=0, column=1, sticky="ns")
    photoScroll1.grid(row=1, column=0, sticky="ew")
    canvasFrame.bind("<Configure>", update_scrollregion)
#-------------------------------------------------------------------------------------------------
IndexList = []
ProNameListCopy = []
ScaleListValue = [] 
TotalAmount = []
global Procedure_Bill
def Procedure_Bill():
    def help():
        value = tmsg.askquestion("Confirm","Are you sure for bill pay?")
        if value == "yes":
            msg = "Thanks for choose our app & go to bill pay"
            tmsg.showinfo("Response",msg)
            #with open("Bill_Data.txt", "a") as f:
            #    f.Write(f"Name : {nameen.get()} - Ph-No. - {Phoneen.get()}\n")
            for j in range(12):
                with open( "Bill_data.txt","a") as f:
                    global l3
                    if ScaleList[j].get() > 0:
                        f.write(f"{ProNameList[j]} = {ScaleList[j].get()}\n")
                        IndexList.append(j)
                        ProNameListCopy.append(ProNameList[j])
                        ScaleListValue.append(ScaleList[j].get())
                        TotalAmount.append(ScaleList[j].get()*PriceListCopy[j])  
    help()
global TableCmd
def TableCmd():
    row = 6
    i = 0
    while i < len(IndexList):
        Indexbut = Button(Homeframe, text=i+1)
        Indexbut.grid(row=row,column=0,ipadx=20)
        ProductNameBut = Button(Homeframe, text=ProNameListCopy[i])
        ProductNameBut.grid(row=row, column=1, ipadx=40)
        ScaleListValueBut = Button(Homeframe, text=ScaleListValue[i])
        ScaleListValueBut.grid(row=row, column=5, ipadx=20)
        TotalAmountBut = Button(Homeframe, text=TotalAmount[i])
        TotalAmountBut.grid(row=row,column=6, ipadx=20)
        row += 1
        i += 1
    Label(Homeframe, text="Total",font=40, bg="black",fg="white").grid(row=row,column=0, padx=30,pady=30, ipadx=30)
    PaymentValue = Button(Homeframe, text=sum(TotalAmount), bg="Purple", fg="white", font="TimesNewRoman 16 bold")
    PaymentValue.grid(row=row+1,column=0, ipadx=20)
def ListClear():
    def ok():
        if nameen.get() != StringVar() or Phoneen.get() != IntVar(): 
            tmsg.showinfo("Warning","Please enter your name/phone")
        else:
            IndexList.clear()
            ProNameListCopy.clear()
            ScaleListValue.clear()
            TotalAmount.clear()
            tmsg.showinfo("Bill","Bill is ready")
    ok()  
def elec():
    clear_frame()
    ItemList2 = [e1,e2,e3]
    a=0
    for column in range(1):
        for i in range(3):
            button3 = Button(Homeframe, image=ItemList2[a])
            button3.grid(row=i,column=column,pady=60,padx=80)
            a=a+1 
    exitbutton = Button(Homeframe, image=ex2, command=home)
    exitbutton.grid(sticky=S,row=1,column=2)
def gross():
    clear_frame()
    ItemList3 = [e1,e2,e3]
    a=0
    for column in range(1):
        for i in range(3):
            button3 = Button(Homeframe, image=ItemList3[a])
            button3.grid(row=i,column=column,pady=60,padx=80)
            a=a+1 
    exitbutton = Button(Homeframe, image=ex2, command=home)
    exitbutton.grid(sticky=S, row=1, column=3)
#---------------------------------------------------------------------------------------------------------------
def bill():
    clear_frame()
    Label(Homeframe, text="Name  : ", font=30).grid(row=0,column=0, pady=20)
    Label(Homeframe, text="Ph no : ",font=30).grid(row=1,column=0, pady=20)
    name = StringVar()
    Phone = IntVar()
    global nameen,Phoneen
    nameen = Entry(Homeframe, textvariable=name, font="TimesNewroman 18 bold")
    nameen.grid(row=0,column=1,pady=20)
    Phoneen= Entry(Homeframe,textvariable=Phone, font="Timesnewroman 18 bold", bg="black" , fg="white")
    Phoneen.grid(row=1,column=1,pady=20)
    Label(Homeframe, text="Sr.No",font=40, bg="black",fg="white").grid(row=5, column=0, padx=3,pady=30, ipadx=30)
    Label(Homeframe,text="Product name",bg="Black",font=40,fg="White").grid(row=5,column=1, padx=3,pady=30, ipadx=30)
    Label(Homeframe, text="Quantity",font=40, bg="black",fg="white").grid(row=5,column=5, padx=3,pady=30, ipadx=30)
    Label(Homeframe, text="Price",font=40, bg="black",fg="white").grid(row=5,column=6, padx=30,pady=30, ipadx=30)
    TableCmd()
    but0k =Button(Homeframe,text=" Ok ",command=ListClear, fg="Cyan", bg="black",font="TimesNewRoman 20 bold" )
    but0k.grid(row=20,column=0,ipadx=30, pady=30)
ExitButMainFrame = Button(MainMenuframe, image=ex, command=exit)
ExitButMainFrame.grid(row=0,column=0,pady=4, sticky=NW)
HomeBut = Button(MainMenuframe, image=Home, command=home)
HomeBut.grid(row=2,column=0,pady=20)
BillBut = Button(MainMenuframe, image=BillPay, command=bill)
BillBut.grid(row=4,column=0,pady=20)
root.mainloop()