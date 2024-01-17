# Initialize two lists of numbers
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Create a tuple of triplets of numbers and their sums using nested loops in a generator expression
sum_tuples = tuple((x, y, x + y) for x in list1 for y in list2)

# Print the original lists
print(list1)
print(list2)

# Print the tuple containing triplets of numbers and their sums
print(sum_tuples)
