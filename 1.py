import math

def degree_to_radian(degree):
    radian = degree * (math.pi / 180)
    return radian

# Sample input
degree_input = 90

# Convert degree to radian
radian_output = degree_to_radian(degree_input)

# Display the result
print(f'Degree = {degree_input}')
print(f'Degree to Radian = {radian_output}')


