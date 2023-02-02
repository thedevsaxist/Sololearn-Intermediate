"""Classes can have their own attributes that belong to that class and not the instances"""

class Student:
    count = 0
    def __init__(self, name) -> None:
        self.name = name
        Student.count += 1

print(Student.count, "students")
mark = Student('Mark')
print(Student.count, "students")
ann = Student('Ann')
print(Student.count, "students")