#import library
import random
import art

#list for cards
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
#Ask the user to play
print(art.logo)
ask=input("Do you want to play a game of Blackjack? Type 'Y' or 'N' : ").lower()

#Create a function to return your starting cards
def your_card():
    '''returns 2 random cards from a deck for user'''
    user_cards=[]
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    return  user_cards

#Create a function to return Computers starting cards
def comp_cards():
    '''returns 2 random cards from a deck for computer'''
    computer_cards=[]
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    return computer_cards

def add_card():
    '''Provide single random card'''
    value=random.choice(cards)
    return value

if ask=="y":
    #provide user cards
    starting_cards=your_card()
    #current user score
    current_score=sum(starting_cards)
    if 11 in starting_cards and current_score>21:
        starting_cards.remove(11)
        starting_cards.append(1)
    print(f"Your cards : {starting_cards}, current score : {current_score}")
    #provide computers first card
    comp_starting_cards=comp_cards()
    comp_score=sum(comp_starting_cards)
    if 11 in comp_starting_cards and comp_score>21:
        comp_starting_cards.remove(11)
        comp_starting_cards.append(1)
    print(f"Computer's first card : {comp_starting_cards[0]}")

    #ask user if he wants to draw another card
    ask_2=input("Type 'Y' to get another card, type 'N' to pass : ").lower()
    if ask_2=="y":
        #add one random card in user cards
        starting_cards.append(add_card())
        current_score=sum(starting_cards)
        if 11 in starting_cards and current_score > 21:
            starting_cards.remove(11)
            starting_cards.append(1)
        #again print computers first card
        print(f"Computer's first card : {comp_starting_cards[0]}")
        #print user cards
        print(f"Your final hand : {starting_cards}, final score : {current_score}")
        #print computer final hand
        while sum(comp_starting_cards)<17:
            comp_starting_cards.append(add_card())
            if 11 in comp_starting_cards and comp_score > 21:
                comp_starting_cards.remove(11)
                comp_starting_cards.append(1)
        comp_score = sum(comp_starting_cards)
        print(f"Computer's final hand : {comp_starting_cards}, final score : {comp_score}")
        if current_score>21:
            print("You went over. You lose :(")
        elif current_score<=21 and comp_score>21:
            print("You won!!")
        elif current_score and comp_score <=21:
            if current_score>comp_score:
                print("You won!!")
            elif current_score<comp_score:
                print("You lose :(")
            else:
                print("It's a =draw=")
    else:
        print(f"Your final hand : {starting_cards}, final score : {current_score}")
        while sum(comp_starting_cards) < 17:
            comp_starting_cards.append(add_card())
        comp_score = sum(comp_starting_cards)
        print(f"Computer's final hand : {comp_starting_cards}, final score : {comp_score}")
        if current_score>21:
            print("You went over. You lose :(")
        elif current_score<=21 and comp_score>21:
            print("You won!!")
        elif current_score and comp_score <=21:
            if current_score>comp_score:
                print("You won!!")
            elif current_score<comp_score:
                print("You lose :(")
            else:
                print("It's a =draw=")
