def calculate_discriminant(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant

# Input coefficients of the quadratic equation
a = float(input("Enter the A Value = "))
b = float(input("Enter the B Value = "))
c = float(input("Enter the C Value = "))

# Calculate discriminant
discriminant_value = calculate_discriminant(a, b, c)

# Determine the nature of solutions
if discriminant_value > 0:
    print("Two Solutions. Discriminant value is =", discriminant_value)
elif discriminant_value == 0:
    print("One real solution (a repeated root). Discriminant value is =", discriminant_value)
else:
    print("No real solutions (complex roots). Discriminant value is =", discriminant_value)
