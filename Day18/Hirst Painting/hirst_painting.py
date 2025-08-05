from turtle import Turtle, Screen
from main import color_list
import random

golu=Turtle()
screen=Screen()

def paint():
    golu.penup()
    golu.setposition(-100, -100)
    current_y = -100
    for i in range(10):
        for j in range(10):
            golu.dot(15, (random.choice(color_list)[0] / 255, random.choice(color_list)[0] / 255,
                          random.choice(color_list)[0] / 255))
            golu.forward(30)
        current_y += 30
        golu.sety(current_y)
        golu.setx(-100)

paint()

screen.exitonclick()