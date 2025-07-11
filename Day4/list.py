#Basic list
fruits=["Apple","Banana"]
states_of_america=["Delaware","Pennsylvania","New York"]

#index
print(states_of_america[0])
print(states_of_america[-1])
#Updating or changing
fruits[0]="Mango"

#append() function --> adds an item at the end of the list
fruits.append("Grapes")

#extend() --> this function adds an entire list in existing list
fruits.extend(["Papaya","Tomato","Guava"])
print(fruits)
