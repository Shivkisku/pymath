class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __gt__(self, other):
        return self.value > other.value

# Creating two Number objects
number1 = Number(5)
number2 = Number(3)

# Comparing the two numbers using the > operator
result = number1 > number2

# Displaying the result
if result:
    print(f"{number1} is greater than {number2}")
else:
    print(f"{number1} is not greater than {number2}")
