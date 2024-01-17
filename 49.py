from fractions import Fraction

# Input from the user
float_value = float(input("Enter the Float value: "))

# Convert the float value to a ratio using Fraction
fraction_representation = Fraction(float_value).limit_denominator()

# Display the result
print(f"\nFloat value: {float_value}")
print(f"Fraction Representation = {fraction_representation.numerator}/{fraction_representation.denominator}")
