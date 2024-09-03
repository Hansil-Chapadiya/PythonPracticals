import turtle as tt
t = tt.Turtle()
screen = tt.Screen()
tt.screensize(1200,1100)
screen.bgcolor("Black")
x = 0
y = 110
t.speed(0)
class IronMan:
    def Face():
        t.pencolor("Aqua")
        t.pensize(3)

        t.penup()
        t.goto(-55,110)
        t.pendown()

        t.fd(100)
        t.lt(75)
        t.fd(150)

        # print(t.pos())
        t.rt(80)
        t.fd(50)

        t.penup()
        t.rt(15)
        t.fd(90)
        # print(t.pos())
        t.rt(85)
        t.fd(180)
        t.pendown()

        # print(t.pos())

        t.rt(25)
        t.fd(30)
        t.lt(35)
        t.fd(110)


        t.rt(35)
        t.fd(130)
        t.rt(46)
        t.fd(55)
# ---------------------------------------------------------------------------------------------------------

        t.penup()
        t.goto(-55,110)
        t.pendown()

        t.rt(75)
        t.fd(150)

        t.penup()
        t.lt(80)
        t.fd(50)
        t.lt(15)
        t.fd(90)
        
        
        t.lt(85)
        t.fd(180)
        t.pendown()

        # print(t.pos())

        t.lt(25)
        t.fd(30)
        t.rt(35)
        t.fd(110)

        t.lt(35)
        t.fd(130)
        t.lt(43)
        t.fd(55)
#-----------------------------------------------------------------------------------------------------------------
    def Double():
        t.penup()
        t.lt(40)
        t.fd(60)
        t.rt(36)
        t.pendown()
        t.fd(30)
        t.penup()
        t.bk(30)
        t.pendown()
        t.lt(90)
        t.fd(30)
        t.lt(90)
        t.fd(100)
        t.lt(90)
        t.fd(30)
        t.rt(90)
        t.fd(30)


        t.penup()
        t.bk(30)
        t.lt(90)
        t.bk(30)
        t.rt(90)

        t.rt(45)
        t.fd(20)
        # print(t.pos())
        t.pendown()

        t.rt(90)
        t.fd(25)
        t.rt(45)
        t.fd(95)
        t.rt(45)
        t.fd(25)
        # t.hideturtle()

        t.lt(80)
        t.fd(40)
        t.lt(40)
        t.fd(60)
        t.rt(30)
        t.fd(50)

        # print(t.pos())

        t.penup()
        t.goto(-60.54,-111.16)
        t.pendown()

        t.lt(103)
        t.fd(40)
        t.rt(38)
        t.fd(60)
        t.lt(30)
        t.fd(49)

    def LineDouble():
       

        t.penup()
        t.goto(-110,80)
        t.rt(165)
        t.pendown()

        t.circle(250,50)
        t.color("White")
        t.begin_fill()
       
        t.rt(65)
        t.fd(30)
        t.rt(90)
        t.fd(40)
       
        t.rt(60)
        t.fd(50)
        t.rt(75)
        t.fd(28)
        t.end_fill()
        
        t.pencolor('Aqua')
        t.bk(28)
        t.rt(103)
        t.fd(50)
        t.lt(59)
        t.fd(40)
        t.lt(90)
        t.fd(30)
        t.lt(58)
        t.fd(60)

        t.penup()
        t.goto(-110,80)
        t.pendown()

        t.color("White")
        t.begin_fill()
        t.lt(20)
        t.fd(30)
        t.lt(90)
        t.fd(40)

        t.lt(60)
        t.fd(50)
        t.lt(75)
        t.fd(28)
        t.end_fill()

        t.pencolor(
            'Aqua'
        )
        t.lt(81)
        t.fd(58)

        t.lt(60)
        t.fd(30)
        t.lt(86)
        t.fd(40)

        t.lt(60)
        t.fd(50)
        t.lt(75)
        t.fd(28)

        t.penup()
        t.goto(171.62,45.88)
        t.pendown()

        t.lt(25)
        t.fd(50)
        t.rt(35)
        t.fd(90)
        t.lt(10)
        t.fd(57)

        print(t.pos())
        # t.fd(40)
        # t.rt(68)
        # t.fd(90)
        # t.lt(5)
        # t.fd(80)

        t.penup()
        t.goto(-176.84,37.21)
        t.pendown()

        t.rt(15)
        t.fd(50)
        t.lt(35)
        t.fd(90)
        t.rt(10)
        t.fd(57)
        # t.lt(75)
        # t.fd(90)
        # t.rt(5)
        # t.fd(80)

        t.penup()
        t.goto(83.82,254.89)
        t.pendown()
        t.lt(68)
        t.circle(342,33)
        # t.fd(50)
        # t.lt(5)
        # t.fd(50)
        t.rt(8)
        t.fd(40)
        t.lt(8)
        t.fd(50)

        t.penup()
        t.goto(176.12,236.85)
        t.pendown()
        t.rt(43)
        t.fd(30)
        t.lt(15)
        t.fd(15)
        t.penup()
        t.goto(171.62,45.88)
        t.pendown()
        t.rt(56)
        t.fd(17)
        t.rt(35)
        t.fd(90)
        t.lt(10)
        t.fd(70)
        t.lt(18)
        t.fd(19)

        t.penup()
        t.goto(-176.84,37.21)
        t.pendown()

        t.rt(29)
        t.fd(17)
        t.lt(25)
        t.fd(90)
        t.rt(7.0)
        t.fd(65)
        t.rt(18)
        t.fd(23)

    def Last():
        t.penup()
        t.goto(218.20,219.75)
        t.pendown()
        t.lt(65)
        t.fd(300)
        t.rt(15)
        t.fd(100)
       

    def Font():
        t.penup()
        t.goto(0,-254)
        t.pendown()
        t.write("One thing you can't take away - I am Iron man", align="center", 
        font=("TimesNewRoman",25,"bold","italic"))
        t.goto(0,-290)
        t.write("- Tony Stark", align="center", font=("Rockwell",25,"bold"))





        


    Face()
    Double()
    LineDouble()
    # Font()



tt.hideturtle()
tt.exitonclick()



# t.rt(85)
        # t.fd(170)
        # t.lt(70)
        # t.fd(38)
        # t.rt(89)
        # t.penup()
        # t.fd(30)
        # t.pendown()
        # t.lt(4)
        # t.fd(70)
        # t.lt(29)
        # t.fd(30)
        # t.rt(35)
        # t.fd(45)
        # t.rt(75)
        # t.fd(30)
        # t.lt(23)
        # t.fd(80)

# -------------------------------------------------------------------------------------------------------
        # t.penup()
        # t.goto(0,110)
        # t.fd(50)
        # t.rt(75)
        # t.fd(150)
        # t.lt(80)
        # t.fd(50)
        # t.lt(15)
        # t.fd(35)
        # t.pendown()

        # t.lt(23)
        # t.fd(30)
        # t.rt(75)
        # t.fd(45)
        # t.rt(35)
        # t.fd(30)
        # t.lt(29)
        # t.fd(70)
       

        # t.rt(15)
        # t.fd(55)
        # t.rt(35)
        # t.fd(130)

        # t.rt(35)
        # t.fd(110)
        # t.lt(35)
        # t.fd(30)
        # t.rt(35)
        # t.fd(190)

        # t.rt(80)
        # t.fd(50)
        # t.rt(15)
        # t.fd(90)

        # t.rt(75)
        # t.fd(80)
        # t.fd(80)
        # t.hideturtle()
 # t.rt(35)
# t.fd(70)

# t.rt(35)
# t.fd(70)
# t.rt(15)
# t.fd(90)















# subface
# t.rt(90)
        # t.fd(40)
        # t.rt(45)
        # t.fd(100)
        # t.rt(45)
        # t.fd(40)

        # t.lt(90)
        # t.fd(35)
        # t.lt(10)
        # t.fd(50)
        # t.rt(15)
        # t.fd(16)

        # t.penup()
        # t.lt(43)
        # t.fd(40)
        # t.rt(40)
        # t.fd(29)
        # t.pendown()

        # t.lt(90)
        # t.fd(40)
        # t.rt(60)
        # t.fd(100)
        # t.lt(5)
        # t.fd(63)

        # t.penup()
        # t.goto(-74.92,-97.27)
        # t.pendown()

        # t.lt(55)
        # t.fd(38)
        # t.rt(35)
        # t.fd(40)
        # t.lt(45)
        # t.fd(25)
    