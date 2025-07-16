import random

stages=[r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',r'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

word_list=["aardvark","baboon","camel"]#You can take words of your choice or in the future come back and use some API's for it:)

#Randomly choose a word from the world_list and assign it to a variable called chosen_word.
chosen_word=random.choice(word_list)
# print(chosen_word)
display=""
for i in range(0,len(chosen_word)):
    display+="_"
print(display)

#Check for the guess in chosen_word

life=6
correct_letters=[]
while life>0:
    word = ""
    # Ask the user to guess the letter
    guess = input("Guess a letter : ").lower()
    a = 0
    for i in chosen_word:
        if i==guess:
            #if guess is correct replace the correct letter
            word+=i
            correct_letters.append(i)
            a+=1
        elif i in correct_letters:
            word+=i
        else:
            #else just leave it blank
            word+="_"
    if guess not in chosen_word:
        life-=1
    print(word)
    if life==0:
        print(stages[0])
        print("Game Over!!")
    elif "_" not in word:
        print(stages[life])
        print("You Won!!")
    elif a==1:
        print(stages[life])
        print("Correct")
    elif a==0:
        print(stages[life])
        print("wrong")
