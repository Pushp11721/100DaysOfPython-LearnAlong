class Account:
    def __init__(self, name, amount, a_type):
        self.name = name
        self.amount = amount
        self.a_type = a_type

    def deposit(self, dep):
        self.amount += dep

    def withdraw(self, rem):
        self.amount -= rem

    def display(self):
        print(f"Accounts type : {self.a_type}\nBalance : {self.amount}")


pushp = Account("Pushpendra Singh", 100000, "Savings")

transaction = True

while transaction:
    ask = input(
        "Press D -> Deposit\nPress W -> Withdraw\nPress E -> Balance enquiry\nPress any other button -> Exit\n").upper()
    if ask == "D" or "W":
        amount = int(input("Enter amount : "))
        if ask == "D":
            pushp.deposit(amount)
        else:
            pushp.withdraw(amount)
    elif ask == "E":
        pushp.display()
    else:
        transaction = False

