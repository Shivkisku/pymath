class Student:
    def __init__(self):
        self.student_details = {}

    @property
    def input_student_details(self):
        roll_number = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))
        self.student_details[roll_number] = {"Name": name, "Marks": marks}
        print("Student details added successfully!")

    def update_student_marks(self):
        roll_number = input("Enter Roll Number to update marks: ")
        if roll_number in self.student_details:
            new_marks = float(input("Enter New Marks: "))
            self.student_details[roll_number]["Marks"] = new_marks
            print("Marks updated successfully!")
        else:
            print("Student not found.")

    def print_student_details(self):
        roll_number = input("Enter Roll Number to print details: ")
        if roll_number in self.student_details:
            details = self.student_details[roll_number]
            print(f"Roll Number: {roll_number}, Name: {details['Name']}, Marks: {details['Marks']}")
        else:
            print("Student not found.")

def main():
    obj = Student()

    while True:
        print("\nStudent Management System Menu:")
        print("1. Input Student Details")
        print("2. Update Student Marks")
        print("3. Print Student Details")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            obj.input_student_details
        elif choice == "2":
            obj.update_student_marks()
        elif choice == "3":
            obj.print_student_details()
        elif choice == "4":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
