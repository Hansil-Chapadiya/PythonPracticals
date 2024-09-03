from HA58_Home import *
from HA59_Bill import *
button4 = Button(frame, image=ex, command=exit)
button4.grid(row=0,column=0,pady=4, sticky=NW)
button1 = Button(frame, image=b1, command=home)
button1.grid(row=2,column=0,pady=20)
button2 = Button(frame, image=b4, command=bill)
button2.grid(row=4,column=0,pady=20)

root.mainloop()