numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {x: x ** 2 for x in numbers if x % 2 == 0}

print("Original Numbers:", numbers)
print("Even Squares Dictionary:", even_squares)
