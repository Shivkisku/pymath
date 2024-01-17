class Student:
    def __init__(self):  # Constructor
        self.name = ""
        self.total = 0  # Initialize as 0 instead of an empty string
        self.per = 0.0

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setTotal(self, total):
        self.total = total

    def getTotal(self):
        return self.total

    def setPercentage(self, per):
        self.per = per

    def getPercentage(self):
        return self.per

# Get user input for name, total, and percentage with input validation
name = input("Enter a Name: ")
while True:
    try:
        total = int(input("Enter a Total: "))
        break  # Break the loop if the input is an integer
    except ValueError:
        print("Invalid input! Please enter a valid integer for Total.")

while True:
    try:
        per = float(input("Enter a Percentage: "))
        break  # Break the loop if the input is a float
    except ValueError:
        print("Invalid input! Please enter a valid float for Percentage.")

# Create an instance of the Student class
s = Student()

# Set the attributes using setter methods
s.setName(name)
s.setTotal(total)
s.setPercentage(per)

# Get the attributes using getter methods
n = s.getName()
t = s.getTotal()
p = s.getPercentage()

# Display student details
print("\nDisplaying Student Details")
print("Name:", n)
print("Total:", t)
print("Percentage:", p)
