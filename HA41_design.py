import turtle

color=("red", "yellow", "green", "White", "cyan", "pink")

t = turtle.Turtle()

screen=turtle.Screen()
screen.bgcolor("Black")
t.speed(25)

for i in range(150):
    t.color(color[i%6])
    t.backward(i*1.5)
    t.left(105)
    t.width(31)