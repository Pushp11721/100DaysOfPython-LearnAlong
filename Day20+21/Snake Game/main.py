import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

#Setup screen
screen=Screen()
screen.setup(width=600,height=600)#size
screen.bgcolor("black")#blck background
screen.title("My Snake Game")#Giving title to screen
screen.tracer(0)

#Create snake body - we will use 3 turtle object shaped as a square
snake=Snake()
#initilize food object
food=Food()
#Initialize score
scoreboard=ScoreBoard()

#Setting controls
screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

#move snake
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #collison with food
    if snake.head.distance(food)<15:
        print("😃")
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        # game_is_on=False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            # game_is_on=False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()
    #if head collides with any segment of snake


screen.exitonclick()