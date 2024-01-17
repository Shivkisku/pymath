# Create a tuple of odd numbers from 1 to 20 using a generator expression with a condition
odds = tuple(x for x in range(1, 21) if x % 2 != 0)

# Print the tuple containing odd numbers
print(odds)
