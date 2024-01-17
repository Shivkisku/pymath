# Generate a list of squares of even numbers and cubes of odd numbers from -5 to 5
result = [x**2 if x % 2 == 0 else x**3 for x in range(-5, 6)]

# Print the result list
print(result)
