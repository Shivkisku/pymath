# Generate a list of numbers that are perfect squares from 1 to 100
perfect_squares = [x for x in range(1, 101) if int(x**0.5)**2 == x]

# Print the list of perfect squares
print("Perfect Squares:", perfect_squares)
