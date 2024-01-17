numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num_squares = {(x, x**2) for x in numbers if x % 2 == 0}

print("Original list of numbers: ", numbers)
print("Set of tuples containing even numbers and their squares: ", even_num_squares)
