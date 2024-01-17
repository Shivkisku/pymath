# Generate a list of common multiples of 3 and 5 up to 100
common_multiples = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]

# Print the common_multiples list
print(common_multiples)
