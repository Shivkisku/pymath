def cap_number(num, lower_bound, upper_bound):
    if num < lower_bound:
        return lower_bound
    elif num > upper_bound:
        return upper_bound
    else:
        return num

# Input from the user
num = float(input("Enter a number: "))
lower_bound = float(input("Enter the lower bound: "))
upper_bound = float(input("Enter the upper bound: "))

# Cap the number within the specified range
capped_num = cap_number(num, lower_bound, upper_bound)

# Display the result
print(f"The capped number is: {capped_num}")
