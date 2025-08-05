from turtle import Turtle
from random import randint
tim=Turtle()

def draw_shape(num_sides):
    tim.pencolor(randint(0,255)/255,randint(0,255)/255,randint(0,255)/255)
    angle=360/num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for i in range(3,10):
    draw_shape(i)