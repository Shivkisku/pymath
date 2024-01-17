from itertools import permutations

# Input
input_string = input("Enter the Values = ")

# Generate all permutations
perms = [''.join(p) for p in permutations(input_string)]

# Display the result
print(perms)
