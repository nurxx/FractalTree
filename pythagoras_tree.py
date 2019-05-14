import turtle
import tkinter
from turtle import *
from random import randint

MIN_DEPTH = 1
height = 280

color_palette= ['#fad089','#ff9c5b','#f8ed62','#3b8183','#2b696b']

turtle.title('Pythagoras Tree')
window = turtle.Screen().bgcolor('#000000')
turtle.screensize()
turtle.setup(width=1.0,height=0.9)
turtle.Turtle()

turtle.hideturtle()
turtle.speed(0)

levels = int(turtle.numinput("Pythagoras Tree", "Въведете брой итерации: ", 10, minval=2, maxval=19))
if levels > 15:
    height+=100

turtle.pensize(levels)
turtle.sety(-300)

turtle.color(color_palette[-1])

turtle.left(90)
turtle.penup()
turtle.backward(height)
turtle.pendown()
turtle.forward(height)
angle = 30

def draw(height,iterations):
    width=turtle.pensize()

    turtle.pensize(3/4*width)
    height = 3/4*height

    turtle.left(angle)
    turtle.forward(height)
    turtle.color(color_palette[randint(0,4)])
    if iterations < levels:
        draw(height, iterations + 1)
    turtle.backward(height)
    turtle.right(2*angle)
    turtle.forward(height)

    turtle.color(color_palette[randint(0,4)])
    if iterations < levels:
        draw(height, iterations + 1)
    turtle.backward(height)
    turtle.left(angle)
    turtle.pensize(width)

if __name__=='__main__':
    draw(height,2)
    done()
