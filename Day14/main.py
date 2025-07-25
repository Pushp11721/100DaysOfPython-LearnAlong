import random

#Create a dictionary of popular things or people with their follower count
from game_data import data
list_of_chosen=[]
score=0

#Game algorithm
game=True
while game:
    # Pick any 2 from them to compare
    a = data[random.randint(0, 48)]
    list_of_chosen.append(a)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")

    b = data[random.randint(0, 48)]
    b_distinct = False
    while not b_distinct:
        if b in list_of_chosen:
            b = data[random.randint(0, 48)]
        else:
            b_distinct = True
    list_of_chosen.append(b)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")

    ask = input("Who has more followers? Type 'A' or 'B' : ").lower()

    if ask == "a":
        if a['follower_count'] > b['follower_count']:
            score += 1
            print("\n" * 20)
            print(f"You're right! Current score : {score}")
            print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
            c = data[random.randint(0, 48)]
            c_distinct = False
            while not c_distinct:
                if c in list_of_chosen:
                    c = data[random.randint(0, 48)]
                else:
                    c_distinct = True
            list_of_chosen.append(c)
            print(f"Compare B: {c['name']}, a {c['description']}, from {c['country']}")
            ask2 = input("Who has more followers? Type 'A' or 'B' : ").lower()
            if ask2 == "a":
                if a['follower_count'] > c['follower_count']:
                    score += 1
                    print("\n" * 20)
                else:
                    print(f"Sorry, that's wrong. Final score : {score}")
                    game=False
            else:
                if a['follower_count'] < c['follower_count']:
                    score += 1
                    print("\n" * 20)
                else:
                    print(f"Sorry, that's wrong. Final score : {score}")
                    game=False
        else:
            print(f"Sorry, that's wrong. Final score : {score}")
            game=False
    else:
        if a['follower_count'] < b['follower_count']:
            score += 1
            print("\n" * 20)
            print(f"You're right! Current score : {score}")
            print(f"Compare A: {b['name']}, a {b['description']}, from {b['country']}")
            d = data[random.randint(0, 48)]
            d_distinct = False
            while not d_distinct:
                if d in list_of_chosen:
                    d = data[random.randint(0, 48)]
                else:
                    d_distinct = True
            list_of_chosen.append(d)
            print(f"Compare B: {d['name']}, a {d['description']}, from {d['country']}")
            ask3 = input("Who has more followers? Type 'A' or 'B' : ").lower()
            if ask3 == "a":
                if a['follower_count'] > d['follower_count']:
                    score += 1
                    print("\n" * 20)
                    print(f"You're right! Current score : {score}")
                else:
                    print(f"Sorry, that's wrong. Final score : {score}")
                    game=False
            else:
                if a['follower_count'] < d['follower_count']:
                    score += 1
                    print("\n" * 20)
                    print(f"You're right! Current score : {score}")
                else:
                    print(f"Sorry, that's wrong. Final score : {score}")
                    game=False
        else:
            print(f"Sorry, that's wrong. Final score : {score}")
            game=False


