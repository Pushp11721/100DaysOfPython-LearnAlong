rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Import random library
import random
#Create a list of rock, paper and scissors
list1=[rock,paper,scissors]

#Take user choice/input
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
#print there choice
print(list1[choice])

#select random choice for computer side
comp_choice=list1[random.randint(0,2)]
print(f"Computer chose:\n{comp_choice}")

#user choice = rock
if list1[choice]==rock and comp_choice==rock:
    print("Draw")
elif list1[choice]==rock and comp_choice==paper:
    print("You lose:(")
elif list1[choice]==rock and comp_choice==scissors:
    print("You won!!")
#user choice = paper
elif list1[choice]==paper and comp_choice==rock:
    print("You won!!")
elif list1[choice]==paper and comp_choice==paper:
    print("Draw")
elif list1[choice]==paper and comp_choice==scissors:
    print("You lose:(")
#user choice = scissors
elif list1[choice]==scissors and comp_choice==rock:
    print("You lose:(")
elif list1[choice]==scissors and comp_choice==paper:
    print("You won!!")
else:
    print("Draw")