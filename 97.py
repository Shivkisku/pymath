# Generate a list of numbers with their squares if the number is even
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use list comprehension to calculate the square of even numbers
squared_evens = [x**2 for x in numbers if x % 2 == 0]

# Print the original numbers list
print("Original numbers list:", numbers)

# Print the list of squares for even numbers
print("Squares of even numbers:", squared_evens)
