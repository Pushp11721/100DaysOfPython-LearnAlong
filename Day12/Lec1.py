enemies=1#Global scope

def increase_enemies():
    enemies=2#Local Scope
    print(f"enemies inside function : {enemies}")#2

increase_enemies()

print(f"enemies outside function : {enemies}")#1