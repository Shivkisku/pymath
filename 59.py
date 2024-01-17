class PersonalInfo:
    def __init__(self, idn, name, gender, address, contact):
        self.idn = idn
        self.name = name
        self.gender = gender
        self.address = address
        self.contact = contact

    def display_personal_info(self):
        print("Id:      ", self.idn)
        print("Name:    ", self.name)
        print("Gender:  ", self.gender)
        print("Address: ", self.address)
        print("Contact: ", self.contact)

class AcademicInfo:
    def __init__(self, stream, year):
        self.stream = stream
        self.year = year

    def display_academic_info(self):
        print("Stream: ", self.stream)
        print("Year:   ", self.year)

class Student(PersonalInfo, AcademicInfo):
    def __init__(self, idn, name, gender, address, contact, stream, year):
        # Call constructors of parent classes
        PersonalInfo.__init__(self, idn, name, gender, address, contact)
        AcademicInfo.__init__(self, stream, year)

    def display_student_details(self):
        self.display_personal_info()
        self.display_academic_info()

# Get user inputs
idn = input("Enter the ID: ")
name = input("Enter the Name: ")
gender = input("Enter the Gender: ")
address = input("Enter the Address: ")
contact = input("Enter the Contact: ")
stream = input("Enter the Stream: ")
year = int(input("Enter the Year: "))  # Assuming "Year" is an integer

# Create a Student instance
student = Student(idn, name, gender, address, contact, stream, year)

# Display student details
student.display_student_details()
