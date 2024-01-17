import math

def sphere_surface_area(radius):
    surface_area = 4 * math.pi * radius**2
    return surface_area

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

# Sample input
radius_input = 2.3

# Calculate surface area and volume
surface_area_output = sphere_surface_area(radius_input)
volume_output = sphere_volume(radius_input)

# Display the result
print(f'Radius of Sphere = {radius_input}')
print(f'Surface Area of the Sphere = {surface_area_output}')
print(f'Volume of the Sphere = {volume_output}')
