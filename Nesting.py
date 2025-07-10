#TODO : Ticket counter with age based pricing after checking age their age

#Inputs
height=int(input("Enter your height : "))
age=int(input("Enter your age : "))
bill=0

if height>=170:
    if age<=12:
        bill+=5
    elif age<=18:
        bill+=7
    elif 45 <= age <= 55:
        bill+=0
    else:
        bill+=12
    photo=input("Do you want to take a photo? type 'Y' or 'N' : ")
    if photo=="Y":
        bill+=3
        print(f"Your total bill will be : ${bill}")
    else:
        print(f"Your total bill will be : ${bill}")

else:
    print("Sorry, you can't ride :(")


