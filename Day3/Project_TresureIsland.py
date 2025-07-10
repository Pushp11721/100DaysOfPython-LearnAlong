#Greetings and objective
print("Welcome to Treasure Island.\nYour mission is yo find the treasure.\n")

#Road selection
road=input("You're at a cross road. Where do you want to go?\nType 'left' or 'right' : ")
if road=="left":
    #correct choice arrived at lake
    print("\nYou've come to a lake. There is an island in the middle of the lake.")
    #wait or swim
    lake=input("Type 'wait' to wait for boat. Type 'swim' to swim across : ")
    if lake=="wait":
        #correct choice, now we are at island
        print("\nYou arrive at the island unharmed. There is a house with 3 doors.")
        #choose a door
        door=input("One red, one yellow and one blue. Which colour do you choose : ")
        if door=="yellow":
            print("YOU WON!!!\nYOU FOUND THE TREASURE!!!")
        else:
            print("GAME OVER:(")
            if door=="red":
                print("You got burned to death!")
            else:
                print("You got drowned in a river")
    else:
        print("GAME OVER:(\nYou got eaten by a Crocodile.")
else:
    print("GAME OVER:(\nYou got smashed by a speeding car.")
