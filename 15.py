def is_palindrome(number):
    return str(number) == str(number)[::-1]

def find_next_smallest_palindrome(number):
    number += 1
    while not is_palindrome(number):
        number += 1
    return number

# Input
input_number = int(input("Enter the Number = "))

# Find the next smallest palindrome
next_smallest_palindrome = find_next_smallest_palindrome(input_number)

# Display the result
print(f'The Next smallest palindrome after {input_number} is = {next_smallest_palindrome}')
