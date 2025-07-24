# age=int(input("How old are you?\n"))
#
# if age>18:
# #print("You can drive at age {age}.")
#     print(f"You can drive at age {age}.")

#We will use try except block to prevent error
try:
    age = int(input("How old are you?\n"))
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical response, such as 15.")
    age = int(input("How old are you?\n"))

if age>=18:
    print(f"You can drive at age {age}.")