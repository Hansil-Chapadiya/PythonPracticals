import turtle as tt
import time as tm
# from HM8_IndianFlag import IndianFlag
t = tt.turtles()
screen = tt.Screen()
tt.setup( width = 1000, height = 500, startx = None, starty = None)
color = ('E:\\Python_Programming\\Python\\SNOWIMAGES\\1 (1).png','E:\\Python_Programming\\Python\\SNOWIMAGES\\1 (3).png','E:\\Python_Programming\\Python\\SNOWIMAGES\\1 (4).png','E:\\Python_Programming\\Python\\SNOWIMAGES\\1 (5).png','E:\\Python_Programming\\Python\\SNOWIMAGES\\1 (6).png','E:\\Python_Programming\\Python\\SNOWIMAGES\\1 (7).png','E:\\Python_Programming\\Python\\SNOWIMAGES\\1 (2).png')
for i in range(7):  
    tm.sleep(0.5)
    screen.bgpic(color[i])
    if(i==0):
        tt.penup()
        tt.goto(-240,20)
        tt.fd(50)
        tt.pendown()
        tt.begin_fill()
        tt.pensize(3)
        tt.color('#A6E3CF')
        tt.circle(80)
        tt.rt(180)
        tt.circle(120)
        tt.end_fill()
        tt.penup()
        tt.lt(15)
        tt.bk(145)
        tt.pendown()
        tt.color('BROWN')
        tt.lt(60)
        tt.fd(60)
        tt.lt(125)
        tt.fd(30)
        tt.bk(30)
        tt.rt(160)
        tt.fd(39)
        tt.bk(100)
    elif(i==1):
        tt.penup()
        tt.rt(45)
        tt.fd(320)
        tt.pendown()
        tt.rt(60)
        tt.bk(60)
        tt.lt(45)
        tt.fd(70)  
        tt.bk(70)
        tt.rt(30)
        tt.bk(46) 
        tt.color('BLACK')
        tt.penup()
        tt.rt(65)
        tt.fd(160)
        tt.pendown()
        tt.begin_fill()
        tt.circle(5)
        tt.end_fill()
        tt.penup()
        tt.lt(125)
        tt.bk(50)
        tt.pendown()
        tt.begin_fill()
        tt.circle(5)
        tt.end_fill()
    elif(i==2):
        tt.penup()
        tt.lt(30)
        tt.fd(30)
        tt.pendown()
        tt.color('RED')
        tt.begin_fill()
        tt.rt(95)
        tt.bk(40)
        tt.rt(150)
        tt.bk(30)
        tt.rt(70)
        tt.bk(22)
        tt.end_fill()
    elif(i==4):
        tt.penup()
        tt.fd(30)
        tt.lt(45)
        tt.bk(20)
        tt.rt(40)
        tt.fd(30)
        tt.pendown()
        tt.color('BROWN')
        tt.circle(20,180)
    elif(i==5):
        tt.color('Purple')
        tt.penup()
        tt.goto(0,0)
        # tt.rt(5)
        tt.pendown()
        tt.begin_fill()
        tt.circle(50,105)
        tt.end_fill()
        tt.setpos(-42,4)
        tt.rt(110)
        tt.begin_fill()
        tt.circle(50,120)
        tt.end_fill()
        tt.setpos(0,0)
        tt.begin_fill()
        tt.bk(90)
        tt.rt(45)
        tt.bk(30)
        tt.rt(135)
        tt.bk(90)
        tt.end_fill()
    elif(i==6):
        tt.color('Black')
        tt.penup()
        tt.goto(-230,180)
        tt.rt(280)
        #tt.fd(150)
        tt.pendown()
        tt.fillcolor('BLACK')
        tt.begin_fill()
        tt.left(90)
        tt.fd(45)
        tt.bk(95)
        tt.lt(90)
        tt.bk(20)
        tt.rt(90)
        tt.fd(30)
        tt.rt(90)
        tt.fd(30)
        tt.lt(90)
        tt.fd(40)
        tt.rt(90)
        tt.bk(30)
        tt.lt(90)
        tt.fd(30)
        tt.rt(90)
        tt.bk(20)
        tt.end_fill()

tt.hideturtle()
tt.exitonclick()
