#TODO : **kwargs - Many keyword arguments
#we can pass in any keyword argument in this - it will return us dictionary
def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3,multiply=5)

#let's create our own class like this
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan",model="GTR")

