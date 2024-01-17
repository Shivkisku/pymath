class Student:
    def __init__(self, roll_number, name, percent):
        self.roll_number = roll_number
        self.name = name
        self.percent = percent

    def display_details(self):
        print(f"Roll Number: {self.roll_number}")
        print(f"Name: {self.name}")
        print(f"Percentage: {self.percent}%\n")

    def __del__(self):
        print(f"Deleting student with Roll Number {self.roll_number}")

# Creating instances of the Student class
s1 = Student(101, "Alice", 85.5)
s2 = Student(102, "Bob", 92.0)
s3 = Student(103, "Charlie", 78.8)

# Displaying details of each student
print("Student Details:")
s1.display_details()
s2.display_details()
s3.display_details()

# Deleting instances explicitly
del s1
del s2
del s3
