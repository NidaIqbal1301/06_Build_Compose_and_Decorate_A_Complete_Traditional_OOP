class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_student_info(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
        
student1 = Student("Nida", 85)
student1.display_student_info()
