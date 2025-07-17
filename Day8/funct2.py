#functions with more than 1 input
def greet(name,location):
    print(f"Hello {name}!!")
    print(f"How's the weather in {location}.")

#calling out function normally
greet("World","Your area")
#calling out function with assigning there position specifically
greet(location="Amazon",name="Python")#here we can change its position also if provided with parameter
