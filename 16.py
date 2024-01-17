def is_palindrome(number):
    return str(number) == str(number)[::-1]

def find_previous_palindrome(number):
    number -= 1
    while not is_palindrome(number):
        number -= 1
    return number

# Input
input_number = int(input("Enter the Number = "))

# Find the previous palindrome
previous_palindrome = find_previous_palindrome(input_number)

# Display the result
print(f'Previous Palindrome = {previous_palindrome}')
