'''from matplotlib import pyplot as plt
x = [100,200,300]
y = [50,80,100]
plt.plot(x,y)
plt.title('Sample')
plt.show()'''
import math
import turtle as tt
t = tt.Turtle()
screen = tt.Screen()
tt.screensize(1000,1000)
screen.bgcolor("white")

'''
a = 30
b,c,d = 50,60,60
tt.penup()
for x in range(-10,50):
    y=  a * math.sin((2*math.pi/b)+(x + c)) + d
    tt.goto(x,y)
    tt.pendown()

import turtle
dan = turtle.Turtle()
dan.shape('turtle')
# needed for the sin() function
import math

dan.penup()
dan.goto(-200, 28)
dan.color('blue')
dan.pensize(3)
dan.pendown()
for x in range(-200, 200):
    y = math.cos(math.radians(x))
    #print(y)
    dan.goto(x, y * 80)
'''
# t.setpos(-350,300)
# t.fd(690)
# t.rt(90)
# t.fd(600)
# # t.rt(90)
# # t.fd(690)
# # t.rt(90)
# # t.fd(600)

# tt.circle(250,70)
# tt.exitonclick()



