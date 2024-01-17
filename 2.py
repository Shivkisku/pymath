import math

def radian_to_degree(radian):
    degree = radian * (180 / math.pi)
    return degree

# Sample input
radian_input = 2

# Convert radian to degree
degree_output = radian_to_degree(radian_input)

# Display the result
print(f'Radian = {radian_input}')
print(f'Radian to Degree = {degree_output}')
