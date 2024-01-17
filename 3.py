def trapezoid_area(base1, base2, height):
    area = ((base1 + base2) / 2) * height
    return area

# Sample input
height_input = 2
base1_input = 3
base2_input = 2

# Calculate the area of the trapezoid
area_output = trapezoid_area(base1_input, base2_input, height_input)

# Display the result
print(f'Height of Trapezoid = {height_input}')
print(f'Base 1 = {base1_input}')
print(f'Base 2 = {base2_input}')
print(f'Area = {area_output}')
