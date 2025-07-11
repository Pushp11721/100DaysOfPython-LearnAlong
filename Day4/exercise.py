#Select who is going to pay the bill by using list and random function
import random

friends=["Alice","Bob","Charlie","David","Emanuel"]

#selecting random person from list
bill=friends[random.randint(0,4)]
print(bill)

#Another of doing this is by using choice() function
print(random.choice(friends))#choice(x) returns random item from list x

