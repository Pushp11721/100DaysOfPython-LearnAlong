import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen=turtle.Turtle()
pen.hideturtle()
pen.penup()

data=pandas.read_csv("50_states.csv")
states=data.state.to_list()

game_is_on=True

correct_guesses=[]
score=0
while game_is_on and score<50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                    prompt="What's another state's name?").title()

    #give exit option to exit game and give results
    if answer_state=="Exit":
        # states to learn.csv
        # missed_states = []
        # for state in states:
        #     if state not in correct_guesses:
        #         missed_states.append(state)
        missed_states=[state for state in states if state not in correct_guesses]
        missed_data = data[data.state.isin(missed_states)]
        missed_data.to_csv("missed_state.csv")

        break

    #Let's Check answer
    if answer_state in states and answer_state not in correct_guesses:
        state_data = data[data.state == answer_state]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        correct_guesses.append(answer_state)
        pen.goto(x_cor, y_cor)
        pen.write(arg=answer_state)
        correct_guesses.append(answer_state)
        score += 1

    elif answer_state in correct_guesses:
        print("You already guessed that state!")

    else:
        print("That's not a valid state name!")

screen.exitonclick()