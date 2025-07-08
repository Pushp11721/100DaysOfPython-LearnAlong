#Greetings
print("Welcome to the tip calculator!")

#Total bill amount
total_bill=float(input("What was the total bill? $"))

#ask for tip percentage
tip=int(input("How much tip would you like to give : "))

#people to split
people=int(input("How many people to split the bill : "))

#calculations
new_total=((tip*total_bill)/100)+total_bill
per_person=round(new_total/people,2)

#Give output
print(f"Each person should pay : ${per_person}")
