from random import randint
from turtle import Turtle, Screen

golu=Turtle()
screen1=Screen()

def triangle(side):
    golu.pencolor(randint(0,255)/255,randint(0,255)/255,randint(0,255)/255)
    for i in range(3):
        golu.forward(side)
        golu.right(120)

def square(side):
    golu.pencolor(randint(0,255)/255,randint(0,255)/255,randint(0,255)/255)
    for i in range(4):
        golu.forward(side)
        golu.right(90)

def pentagon(side):
    golu.pencolor(randint(0,255)/255,randint(0,255)/255,randint(0,255)/255)
    for i in range(5):
        golu.forward(side)
        golu.right(72)

def hexagon(side):
    golu.pencolor(randint(0,255)/255,randint(0,255)/255,randint(0,255)/255)
    for i in range(6):
        golu.forward(side)
        golu.right(60)

def heptagon(side):
    golu.pencolor(randint(0,255)/255,randint(0,255)/255,randint(0,255)/255)
    for i in range(7):
        golu.forward(side)
        golu.right(51.43)

def octagon(side):
    golu.pencolor(randint(0,255)/255,randint(0,255)/255,randint(0,255)/255)
    for i in range(8):
        golu.forward(side)
        golu.right(45)

def nonagon(side):
    golu.pencolor(randint(0,255)/255,randint(0,255)/255,randint(0,255)/255)
    for i in range(9):
        golu.forward(side)
        golu.right(40)

triangle(50)
square(50)
pentagon(50)
hexagon(50)
heptagon(50)
octagon(50)
nonagon(50)

screen1.exitonclick()