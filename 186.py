list1 = [123, 456, 789]
list2 = [234, 567, 890]

# Create a tuple of tuples with pairs of elements and the sum of their digits
digit_sum_tuples = tuple((x, y, sum(int(digit) for digit in str(x)) + sum(int(digit) for digit in str(y))) for x in list1 for y in list2)

# Print the original lists
print(list1)
print(list2)

# Print the tuple containing pairs and their digit sum
print(digit_sum_tuples)
