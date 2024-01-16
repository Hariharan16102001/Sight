class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
dog = Dog("Ruby")
cat = Cat("Teddy")
print(dog.speak())
print(cat.speak())
