numbers = [10, -5, 20, -15, 30]

# Create a tuple of positive numbers
positive = tuple(x for x in numbers if x >= 0)

# Create a tuple of negative numbers
negative = tuple(x for x in numbers if x < 0)

print(numbers)
print(positive)
print(negative)
