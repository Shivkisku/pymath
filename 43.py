def is_disarium_number(number):
    str_num = str(number)
    length = len(str_num)
    total = sum(int(digit) ** (i + 1) for i, digit in enumerate(str_num))
    return total == number

def is_unhappy_number(number):
    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))
    return number != 1

# Input from the user
user_input = int(input("Enter the Number = "))

# Check and display the result
if is_disarium_number(user_input):
    print(f"{user_input} is a Disarium Number")
else:
    print(f"{user_input} is Not a Disarium Number")

if is_unhappy_number(user_input):
    print(f"{user_input} is an Unhappy Number")
else:
    print(f"{user_input} is Not an Unhappy Number")
