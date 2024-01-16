class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.__roll_number = roll_number  

    def get_roll_number(self):
        return self.__roll_number

    def set_roll_number(self, new_roll_number):
        if new_roll_number > 0:
            self.__roll_number = new_roll_number

student = Student("Hari", 12345)

print(f"Original Roll Number: {student.get_roll_number()}")
student.set_roll_number(54321)
print(f"Updated Roll Number: {student.get_roll_number()}")
