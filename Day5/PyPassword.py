#importing random module
import random


#lists
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['i','#','$','%','&','(',')','*','+']

#Greetings
print("Welcome to the PyPassword Generator!")

#Ask for letters count in password
letters_count=int(input("How many letters would you like in your password?\n"))

#Ask for symbols count in password
symbols_count=int(input("How many symbols would you like?\n"))

#Ask for number counts in password
number_count=int(input("How many numbers would you like?\n"))

list_pass=[]

#select letters at random
for i in range(0,letters_count):
    list_pass.append(random.choice(letters))
#select symbols
for i in range(0,symbols_count):
    list_pass.append(random.choice(symbols))
#select numbers
for i in range(0,number_count):
    list_pass.append(random.choice(numbers))

print(list_pass)
#using shuffle() function to randomize list elements
random.shuffle(list_pass)
print(list_pass)
#using join function to convert list into a string
# final_pass=''.join(list_pass)
print(''.join(list_pass))

#We can use for loop also by creating an empty string and adding elements of list one by one into it