class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print("Hi, my name is " + self.name + " and I am in grade " + str(self.grade) + ".")

student1 = Student("Alex", 12)
student1.introduce()

student2 = Student("Sara", 11)
student2.introduce()
