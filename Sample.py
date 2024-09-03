import turtle as tt
t = tt.Turtle()
screen = tt.Screen()
tt.screensize(1000,1000)
screen.bgcolor("Black")
x = 0
y = 110
class IronMan:
    def Face():
        t.pencolor("Aqua")
        t.pensize(3)

        t.penup()
        t.goto(-55,110)
        t.pendown()

        t.fd(100)
        t.lt(85)
        t.fd(150)

        t.rt(80)
        t.fd(50)
        t.rt(15)
        t.fd(90)

        t.rt(95)
        t.fd(180)

        # print(t.pos())

        t.rt(25)
        t.fd(30)
        t.lt(35)
        t.fd(110)


        t.rt(35)
        t.fd(130)
        t.rt(46)
        t.fd(55)

    Face()

tt.hideturtle()
tt.exitonclick()