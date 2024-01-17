# Initialize two lists of numbers
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Create a tuple of triples of numbers and their products using a nested generator expression
product_tuples = tuple((x, y, x * y) for x in list1 for y in list2)

# Print the original lists
print(list1)
print(list2)

# Print the tuple containing triples of numbers and their products
print(product_tuples)
