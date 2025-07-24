year=int(input("What's your year of birth?\n"))

if year>1980 and year<1994:
    print("You are a millennial.")
elif year>=1994:
    print("You are a Gen Z.")

#We can see in the elif statement -- what is someone is from 1994
#there is no condition for that
#So we will include 1994 also in Gen Z