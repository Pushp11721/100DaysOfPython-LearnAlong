from turtle import Turtle, Screen
import random

screen=Screen()

#setting screen size
screen.setup(width=500,height=400)

#Taking their bet by using textinput() function
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color : ")

#setting turtle position
#Create turtles
colors=["red","orange","yellow","green","blue","purple"]
y_pos=[-70,-40,-10,20,50,80]
turtle_list=[]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    new_turtle.color(colors[turtle_index])
    turtle_list.append(new_turtle)
is_race_on=False

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_dist=random.randint(0,10)
        turtle.forward(random_dist)

screen.exitonclick()