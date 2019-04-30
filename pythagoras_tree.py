import turtle
import tkinter
from turtle import *
from random_colors_generator import *

MIN_DEPTH = 1
turtle.title('Pythagoras Tree')
window = turtle.Screen().bgcolor('#000000')
tree = turtle.Turtle()
tree.speed(200)


recursion_depth = int(turtle.numinput("Fractal tree", "Input fractal tree's max leaves count:", 10, minval=1, maxval=20))

if recursion_depth in list(range(1,10)):
    tree.pensize(1)
else:
    tree.pensize(2)

tree.sety(-300)

tree.color(generate_random_color())

tree.left(90)

tree.shape('turtle')

def draw(leaves):
    if leaves < recursion_depth:
        return
    else:
        tree.color(generate_random_color())
        tree.forward(leaves)
        tree.left(30)
        draw(leaves*3/4)
        tree.color(generate_random_color())
        tree.right(60)
        draw(leaves*3/4)
        tree.color(generate_random_color())
        tree.left(30)
        tree.backward(leaves)

if __name__=='__main__':
    draw(200)
    turtle.bye()
    done()
