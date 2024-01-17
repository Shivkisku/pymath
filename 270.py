numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_greater_than_5 = {x: x ** 2 for x in numbers if x > 5}

print("Original Numbers:", numbers)
print("Squares Greater Than 5 Dictionary:", squares_greater_than_5)
