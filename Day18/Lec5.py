from turtle import Turtle, Screen
import random
from numpy.ma.core import shape

golu=Turtle()
screen=Screen()
current_heading=golu.heading()
golu.speed("fastest")
while current_heading!=360:
    golu.pencolor(random.randint(0, 255) / 255, random.randint(0, 255) / 255,
                  random.randint(0, 255) / 255)
    golu.circle(100.0)
    current_heading+=5
    golu.setheading(current_heading)
screen.exitonclick()