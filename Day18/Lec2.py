from turtle import Turtle, Screen

#drwaing dash line
golu=Turtle()
screen=Screen()

for i in range(10):
    golu.pendown()
    golu.forward(10)
    golu.penup()
    golu.forward(10)



screen.exitonclick()