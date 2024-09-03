import math
from tkinter import RIGHT
from tkinter.font import BOLD
import turtle as tt
t = tt.Turtle()
screen = tt.Screen()
tt.screensize(1000,1000)
# screen.bgcolor("#ffff66")
t.speed(10)
class IndianFlag:
    # draw pole
    def Pole():
        t.penup()
        t.goto(-170,-300)
        t.pendown()
        t.color("Brown")
        #t.pencolor("Black")
        t.begin_fill()
        t.pensize(2)
        t.fd(100)
        t.lt(90)
        t.fd(30)
        t.lt(90)
        t.fd(100)
        t.lt(90)
        t.fd(30)
        t.end_fill()
        t.penup()
        t.goto(-130,-270)
        t.pendown()
        t.begin_fill()
        t.bk(500)  
        t.lt(90)
        t.fd(20)
        t.rt(90)
        t.fd(500)
        t.end_fill()
        t.begin_fill()
        t.bk(500)
        t.lt(90)
        t.bk(10)
        t.circle(10)
        t.end_fill()
    #---------------------------------------------------------------
    # draw flag
    def Flag():
        # Orange Color
        def orange():
            t.color("orange")
            #t.pencolor("Black")
            t.pensize(3)
            t.penup()
            t.fd(10)
            t.down()
            t.begin_fill()
            for x in range(-110,120):
                y = math.sin(math.radians((x))) #generate angle
                t.goto(x,(y*(-20)+210))
            
            t.rt(90)
            t.fd(30)
            #print("Orange Part ",t.pos())
            t.rt(90)
            for x in range(120,-110,-1):
                y = math.sin(math.radians((x)))
                t.goto(x,(y*(-20)+180))

            #t.rt(90)
            #t.fd(30)
            #t.goto(-110,230)
            t.end_fill() # end of orange region

        #White Region Start
        def white():
            
            t.pensize(3)
            # Don't Draw
            t.penup()
            #t.goto(119,162.51) # for start white part
            # Start Draw
            t.pendown()

            t.color("White")
            t.begin_fill()
            #t.pencolor("Black")
            
            # Repeating White Part Border
            for x in range(-110,120):
                y = math.sin(math.radians((x)))
                #print(y*10)
                t.goto(x,(y*(-20)+180))
            
            t.rt(90)
            t.bk(30)
            print("White Part = ", t.pos())
            t.rt(90)

            for x in range(120,-110,-1):
                y = math.sin(math.radians((x)))
                #print(y*10)
                t.goto(x,(y*(-20)+150))
            t.end_fill()
            


        def green():
            t.pensize(3)
            t.color("Green")
            #t.pencolor("Black")
            t.begin_fill()
            # Repeating White Part Border
            for x in range(-110,120):
                y = math.sin(math.radians((x)))
                #print(y*10)
                t.goto(x,(y*(-20)+150))
            
            #t.goto(119,132.51)
            
            t.rt(90)
            t.fd(30)
            t.rt(90)

            #Green Part
            for x in range(120,-110,-1):
                y = math.sin(math.radians((x)))
                #print(y*10)
                t.goto(x,(y*(-20)+120))

            t.end_fill()

        def Ashoka():
            t.pensize(4)

            #don't draw
            t.penup()
            t.goto(0,179)
            t.pendown()

            t.pencolor("navy")
            #start draw
            t.circle(14)

            t.penup()
            t.rt(90)
            t.bk(14)
            t.pendown()

            t.pensize(1)
            for i in range(24):
                t.fd(15)
                t.bk(15)
                t.lt(15)

        def SevenFive():
            t.hideturtle()
            tt.delay(15)
            t.penup()
            t.setpos(250,-185)
            t.pendown()
            t.write("75",font=("Castellar",120,"bold"),align='right')

            t.showturtle()
            t.penup()
            t.goto(220,-105)
            t.pendown()

            t.pensize(7)
            t.circle(35)

            t.rt(90)
            t.pensize(2)
            t.bk(35)
            for i in range(24):
                t.fd(33)
                t.bk(33)
                t.lt(15)

            t.hideturtle()
            t.penup()
            t.setpos(8,-185)
            t.pendown()
            t.write("Years of Independence",font=("TimesNewRoman",25))
        
        orange()
        white() 
        green()
        Ashoka()
        SevenFive()
    
    Pole() 
    Flag()       

# draw rectangle
t.pensize(5)
t.pencolor('Red')
t.penup()
t.goto(-350,300)
t.pendown()
t.fd(690)
t.rt(90)
t.fd(600)
t.rt(90)
t.fd(690)
t.rt(90)
t.fd(600)
IndianFlag()
tt.hideturtle()
tt.exitonclick()