class SchoolHeightRecords:
    def __init__(self):
        self.student_records = {}

    def add_student(self, name, height):
        self.student_records[name] = height
        print(f"Height record added for {name}")

    def remove_student(self, name):
        if name in self.student_records:
            del self.student_records[name]
            print(f"Height record removed for {name}")
        else:
            print(f"{name} not found in records")

    def find_student_height(self, name):
        height = self.student_records.get(name)
        if height is not None:
            print(f"{name}'s height is {height}")
        else:
            print(f"{name} not found in records")

    def display_records(self):
        print("Student Height Records:")
        for name, height in self.student_records.items():
            print(f"{name}: {height} cm")

# Create an instance of SchoolHeightRecords
school_records = SchoolHeightRecords()

while True:
    print("\nMenu:")
    print("1. Add Student Height")
    print("2. Remove Student Height")
    print("3. Find Student Height")
    print("4. Display All Records")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter student name: ")
        height = input("Enter student height (in cm): ")
        school_records.add_student(name, height)

    elif choice == "2":
        name = input("Enter student name to remove: ")
        school_records.remove_student(name)

    elif choice == "3":
        name = input("Enter student name to find height: ")
        school_records.find_student_height(name)

    elif choice == "4":
        school_records.display_records()

    elif choice == "5":
        print("Quitting the program.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
