class Student:
    def __init__(self):  # Constructor
        self.id = 0
        self.name = ""
        self.gender = ""
        self.total = 0  # Changed to integer (assuming it represents a total score)
        self.per = 0.0

    def __del__(self):  # Destructor
        print("Object Destroyed")

    def setData(self):
        self.id = int(input("Enter an ID: "))
        self.name = input("Enter a Name: ")
        self.gender = input("Enter a Gender: ")
        self.total = int(input("Enter a Total: "))
        self.per = float(input("Enter a Percentage: "))

    def showData(self):
        print("Id:", self.id)
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Total:", self.total)  # Fixed from "City" to "Total"
        print("Percentage:", self.per)

s = Student()  # Create an instance of the Student class
s.setData()     # Set data for the instance
s.showData()    # Display data for the instance
