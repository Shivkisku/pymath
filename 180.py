from itertools import chain

# Initialize two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Create a tuple of unique elements from both lists while preserving order
unique_ordered_elements_tuple = tuple(set(chain(list1, list2)))

# Print the original lists
print(list1)
print(list2)

# Print the tuple containing unique elements while preserving order
print(unique_ordered_elements_tuple)
