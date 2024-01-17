# Generate a list of positive numbers from another list
numbers = [1, -2, 3, -4, 5, -6]
positive_numbers = [x for x in numbers if x > 0]

# Print the original numbers list and the list of positive numbers
print("Original numbers:", numbers)
print("Positive numbers:", positive_numbers)
