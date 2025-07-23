#Modifying Global scope

enemies=1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function : {enemies}")#2

increase_enemies()
print(f"enemies outside function : {enemies}")#1