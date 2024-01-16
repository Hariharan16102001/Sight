
class Vehicle:
    def display_info(self):
        return "This is a generic vehicle."
class Car(Vehicle):
    def display_info(self):
        return "This is a car."
class Bicycle(Vehicle):
    def display_info(self):
        return "This is a bicycle."
vehicle = Vehicle()
car = Car()
bicycle = Bicycle()
print(vehicle.display_info())
print(car.display_info())
print(bicycle.display_info())


#method overloading
class Calculator:
    def add(self, x, y, z=0):
        return x + y + z
calc = Calculator()
result1 = calc.add(1, 2)
result2 = calc.add(1, 2, 3)
print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
