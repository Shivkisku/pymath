# Initialize a list of numbers
numbers = [10, 15, 20, 25]

# Create a tuple of pairs of numbers and their factors using a generator expression
factors = tuple((num, [x for x in range(1, num+1) if num % x == 0]) for num in numbers)

# Print the original numbers list
print(numbers)

# Print the tuple containing pairs of numbers and their factors
print(factors)
