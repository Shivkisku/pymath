class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Roll Number: {self.roll_number}, Name: {self.name}, Marks: {self.marks}"

# Create a list of students
students = [
    Student(101, "Alice", 85),
    Student(102, "Bob", 92),
    Student(103, "Charlie", 78)
]

# Print details of all students
print("Details of all students:")
for student in students:
    print(student)

# Access and modify attributes of a specific student
selected_student = students[0]
print("\nDetails of the selected student before modification:")
print(selected_student)

# Modify attributes
selected_student.name = "Alicia"
selected_student.marks = 90

print("\nDetails of the selected student after modification:")
print(selected_student)
