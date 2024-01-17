mixed_data = [1, 'apple', 2.5, 'banana', 3, 'cherry']

# Create a tuple of distinct elements from the mixed_data list
distinct_mixed_elements_tuple = tuple(set(item for item in mixed_data))

# Print the original mixed_data list
print(mixed_data)

# Print the tuple containing distinct elements from the mixed_data list
print(distinct_mixed_elements_tuple)
