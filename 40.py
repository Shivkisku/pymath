def find_perfect_squares(start, end):
    perfect_squares = [x**2 for x in range(int(start**0.5), int(end**0.5) + 1)]
    return perfect_squares

# Sample input
start_number = 1
end_number = 49

# Display the input
print(f"Start Number = {start_number}")
print(f"End Number = {end_number}")

# Find and display the perfect squares
perfect_squares = find_perfect_squares(start_number, end_number)
print(f"Perfect Squares = {perfect_squares}")
