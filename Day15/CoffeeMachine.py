MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
            "milk":0,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }
}

resources={
    "water":300,
    "milk":200,
    "coffee":100,
    "money":0
}

def report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")

def check_resources(type):
    if resources["water"]>=MENU[type]["ingredients"]["water"] and resources["milk"]>=MENU[type]["ingredients"]["milk"] and resources["coffee"]>=MENU[type]["ingredients"]["coffee"]:
        print("good to go")
        return True
    else:
        if resources["water"]<MENU[type]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return False
        elif resources["milk"]<MENU[type]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
        else:
            print("Sorry there is not enough coffee.")
            return False

def ask_for_money(type):
    print("Please provide money for your drink")
    quarters=float(input("quarters : "))
    dimes=float(input("Dimes : "))
    nickles=float(input("Nickles : "))
    pennies=float(input("Pennies : "))

    quarters*=0.25
    dimes*=0.10
    nickles*=0.05
    pennies*=0.01

    total=quarters+dimes+nickles+pennies

    if total<MENU[type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if total>MENU[type]["cost"]:
            change=total-MENU[type]["cost"]
            print(f"Here is ${round(change,2)} dollars in change.")
            return True
        else:
            return True

def deduct(type):
    resources["water"]-=MENU[type]["ingredients"]["water"]
    resources["milk"]-=MENU[type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[type]["ingredients"]["coffee"]
    resources["money"] += MENU[type]["cost"]

machine=True
while machine:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=="off":
        machine=False
    elif choice=="report":
        report()
    elif choice=="espresso":
        if check_resources("espresso"):
            if ask_for_money("espresso"):
                deduct("espresso")
                print("Here is your espresso. Enjoy!")
            else:
                machine=False
        else:
            machine=False

    elif choice=="latte":
        if check_resources("latte"):
            if ask_for_money("latte"):
                deduct("latte")
                print("Here is your latte. Enjoy!")
            else:
                machine=False
        else:
            machine=False

    else:
        if check_resources("cappuccino"):
            if ask_for_money("cappuccino"):
                deduct("cappuccino")
                print("Here is your cappuccino. Enjoy!")
            else:
                machine=False
        else:
            machine=False