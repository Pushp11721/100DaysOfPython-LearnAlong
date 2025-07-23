#import library
import random
import art

#Greeting
print(art.logo)
print("welcome to the Number Guessing Game!")

#Give them range
print("I'm thinking of a number between 1 and 100.")

#difficulty level
difficulty=input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
if difficulty == "easy":
    life=10
else:
    life=5

def game():
    global life
    number=random.randint(1,100)
    for i in range(0,life):
        print(f"You have {life} attempts remaining to guess the number.")
        guess=int(input("Make a guess : "))
        if guess==number:
            print("You won!!")
            break
        elif number-guess<0:
            life-=1
            if number-guess<=-20:
                print("Too high")
            else:
                print("high")
        else:
            life-=1
            if number-guess>=20:
                print("Too low")
            else:
                print("low")

game()


