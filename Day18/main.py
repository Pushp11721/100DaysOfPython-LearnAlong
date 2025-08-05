from turtle import Turtle, Screen

#Create object timmy using Turtle() class
timmy=Turtle()
screen=Screen()

#change shape of turtle
timmy.shape("turtle")

#change color of turtle
timmy.color("red")

#move timmy
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
for i in range(4):
    timmy.forward(100)
    timmy.right(90)


screen.exitonclick()