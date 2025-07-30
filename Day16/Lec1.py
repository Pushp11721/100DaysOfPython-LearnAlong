#Importing turtle module
from turtle import Turtle, Screen

#Using module importing its library and creating object using it's class
timmy=Turtle()
print(timmy)

my_screen=Screen()
print(my_screen.canvheight)

timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
my_screen.exitonclick()
