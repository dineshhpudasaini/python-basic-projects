class car:
    wheels = 4
    company = "Toyata"

    def __init__(self,color):
        self.color = color

    # @classmethod
    def hello(hi):
        print(f"car company : {hi.company}")

car1 = car("Red")
print(car1.color)
car1.hello()