import math

# Initialize a list of numbers
numbers = [1, 2, 3, 4, 5]

# Create a tuple of pairs of numbers and their factorials using a generator expression
factorial_tuples = tuple((x, math.factorial(x)) for x in numbers)

# Print the original numbers list
print(numbers)

# Print the tuple containing pairs of numbers and their factorials
print(factorial_tuples)
