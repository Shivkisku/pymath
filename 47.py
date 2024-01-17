def tetrahedral_number(n):
    # Calculate the nth tetrahedral number using the formula (n * (n + 1) * (n + 2)) / 6
    tetrahedral_num = (n * (n + 1) * (n + 2)) / 6
    return tetrahedral_num

# Input from the user
n_value = int(input("Enter the Number: "))

# Calculate and display the nth tetrahedral number
result = tetrahedral_number(n_value)
print(f"Tetrahedral Number = {result}")
