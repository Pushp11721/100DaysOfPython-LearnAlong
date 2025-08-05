from random import randint
from turtle import Turtle, Screen
import random

golu=Turtle()
screen=Screen()
golu.pensize(10)

angle=[0,90,180,270]
golu.speed("fastest")

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_colour=(r,g,b)
    return random_colour

def random_walk():
    golu.pencolor(random.randint(0, 255) / 255, random.randint(0, 255) / 255,
                  random.randint(0, 255) / 255)
    golu.right(random.choice(angle))
    golu.forward(20)

move=True
while move:
    random_walk()

screen.exitonclick()

