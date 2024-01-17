from fractions import Fraction

# Input
float_number = float(input("Enter a float number = "))

# Convert float to ratio
ratio = Fraction(float_number).limit_denominator()

# Display the result
print(f'The ratio of {float_number} is = {ratio.numerator}/{ratio.denominator}')
