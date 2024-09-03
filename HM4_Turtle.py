import turtle as t
import time
tt = t.Turtle()
tt.speed(6)
screen = t.Screen()
screen.bgcolor("White")
time.sleep(20)
color = ('RED','GREEN','BLUE','YELLOW','PURPLE','CYAN','MAROON','BROWN')
color2 = ('#011D8F','#FFAEC9','MAROON','BROWN','#741B7C')
t.screensize(1000, 1000)
tt.goto(0, 0)
tt.speed(0)
max_fd= 40
max_rad = 30

for i in range(25):
    for j in range(8):
        screen.bgcolor(color2[(j%5)])
        tt.color(color[j])
        tt.begin_fill()
        tt.fd(max_fd - (i))
        tt.circle(max_rad - (i), 45)
        tt.end_fill()
    tt.penup()
    tt.rt(90)
    tt.fd(2)
    tt.pendown()
tt.hideturtle()
t.exitonclick()
