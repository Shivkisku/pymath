list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [5, 6, 7, 8]

# Create a tuple of distinct elements using set symmetric difference
distinct_elements_symmetric_diff = tuple(set(list1) ^ set(list2) ^ set(list3))

# Print the original lists
print(list1)
print(list2)
print(list3)

# Print the tuple containing distinct elements using set symmetric difference
print(distinct_elements_symmetric_diff)
