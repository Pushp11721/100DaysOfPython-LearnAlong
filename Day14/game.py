#Display art
import random
import game_data
import art
print(art.logo)

#function
def format_data(account):
    return f"Compare A: {account["name"]}, a {account["description"]}, from {account["country"]}."

def check_answer(user_guess,a_following,b_following):
    if user_guess=="a":
        if a_following>b_following:
            return True
        else:
            return False
    else:
        if b_following>a_following:
            return True
        else:
            return False

#Generate a random account from the game data
account_a=random.choice(game_data.data)
account_b=random.choice(game_data.data)

score=0

if account_a==account_b:
    account_b=random.choice(game_data.data)

#format it into printable data
print(format_data(account_a))
print(art.vs)
print(format_data(account_b))

#ask user for a guess
guess=input("Who has more followers? Type 'A' or 'B': ").lower()

#Check if user is correct
a_follower_count=account_a["follower_count"]
b_follower_count=account_a["follower_count"]

is_correct=check_answer(guess,a_follower_count,b_follower_count)

#Give user feedback
if is_correct:
    score+=1
    print(f"You're right! Current score {score}")
else:
    print(f"Sorry, that's wrong. Final score {score}")