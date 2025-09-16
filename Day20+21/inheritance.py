class Animal:
    def __init__(self):
        self.num_eyes=2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()#getting  animal breath method
        print("doing this underwater")#adding more info

    def swim(self):
        print("moving in water.")

nemo=Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)