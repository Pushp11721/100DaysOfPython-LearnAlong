class Car:
    #constructor
    def __init__(self,seats):
        self.seats=seats

    #change number of seats
    def enter_race_mode(self):
        self.seats=2

car1=Car(4)
print(car1.seats)
car1.enter_race_mode()
print(car1.seats)