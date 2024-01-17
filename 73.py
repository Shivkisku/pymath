class Student:
    def __init__(self, student_id, name, per):
        self.student_id = student_id
        self.name = name
        self.per = per

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Percentage: {self.per}"

# Array of Student objects
students = [
    Student(101, "Alice", 85),
    Student(102, "Bob", 92),
    Student(103, "Charlie", 78)
]

# Function to search for a student by ID
def search_student_by_id(student_id):
    for student in students:
        if student.student_id == student_id:
            return student
    return None

# Print all student IDs
print("Student IDs:")
for student in students:
    print(student.student_id)

# User input to search for a student by ID
search_id = int(input("Enter the student ID to search: "))

# Search for the student by ID
found_student = search_student_by_id(search_id)

# Display the result
if found_student:
    print("\nStudent Found:")
    print(found_student)
else:
    print("\nStudent Not Found")
