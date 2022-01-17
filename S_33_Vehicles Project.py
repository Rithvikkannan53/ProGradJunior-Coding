class Vehicle:
    def __init__(self,model_name,color,price):
        self.model_name = model_name
        self.color = color
        self.price = price

    def show(self):
        print("Details:",self.model_name,self.color,self.price)

    def max_speed(self):
        print("Maximum speed of any vehicle is 180km/hr")

    def change_gear(self):
        print("Vehicle can change upto 6 gears")

class Car(Vehicle):
    def max_speed(self):
        print("Maximum speed of car is 240km/hr")

    def change_gear(self):
        print("Cars can change upto 6 gears")

car = Car("Renault Kwid","Olive Brown",322500)
car.show()
car.max_speed()
car.change_gear()
print("\n")
vehicle = Vehicle("Yamaha R15","Blue",232000)
vehicle.show()
vehicle.max_speed()
vehicle.change_gear()
