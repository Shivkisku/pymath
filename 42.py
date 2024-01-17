def check_absolute_difference(number):
    digits = [int(digit) for digit in str(number)]

    for i in range(len(digits) - 1):
        if abs(digits[i] - digits[i + 1]) != 2:
            return False
    
    return True

# Input from the user
user_input = int(input("Enter a number: "))

# Check and display the result
if check_absolute_difference(user_input):
    print("The absolute difference between consecutive digits is two")
else:
    print("The absolute difference between consecutive digits is not two")
