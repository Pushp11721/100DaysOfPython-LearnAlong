game_level=3
enemies=["Skeleton","Zombie","Alien"]

def create_enemy():
    if game_level<5:
        new_enemy=enemies[0]

print(new_enemy)#Gives error because new_enemy is a local variable within the function create_enemy()

