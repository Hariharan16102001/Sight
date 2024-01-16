'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Hari", 23)
person1.display_info()


class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.instance_variable = value

    def instance_method(self):
        print(f"Instance method called. Instance variable: {self.instance_variable}")

    @classmethod
    def class_method(cls):
        cls.class_variable += 1
        print(f"Class method called. Class variable: {cls.class_variable}")

    @staticmethod
    def static_method():
        print("Static method called")

obj = MyClass(42)
obj.instance_method()
MyClass.class_method()
MyClass.static_method()'''

#instance attribute
class Dog:
    def __init__(self, name):
        self.name = name

dog1 = Dog("Ruby")
dog2 = Dog("Tommy")

print(dog1.name)
print(dog2.name)

#class attribute
class Circle:
    pi = 3.14159265

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * self.radius ** 2

circle1 = Circle(2)
circle2 = Circle(3)

print(circle1.area())
print(circle2.area())

#instancemethod
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

student = Student("Hari", 23)
print(student.greet())

#class method
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1
    @classmethod
    def get_count(cls):
        return cls.count
obj1 = MyClass()
obj2 = MyClass()
print(MyClass.get_count())

#static methods
class Mathone:
    @staticmethod
    def add(x, y):
        return x + y

result = Mathone.add(3, 5)
print(result)
