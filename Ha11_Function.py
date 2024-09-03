def t(time) :
    if (time <=3 and time >= 1) :
        print("Good Midnight " + name)
    elif (time >= 4 and time <= 10) :
        print("Good morning " + name)
    elif(time >= 11 and time <= 15):
        print("Good Afternoon " + name)
    elif(time >= 16 and time <= 24) :
            print("Good night " + name)
print("Enter Your Name")
name = input()
time = int(input("Enter time\n"))
t(time)
