# Input
number = int(input("Number = "))

# Format number with commas as thousands separators
formatted_number = '{:,}'.format(number)

# Display the result
print(f'Formatted Number = {formatted_number}')
