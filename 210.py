string = "Hello, world!"
non_alphanumeric = {char for char in string if not char.isalnum()}

print("Original String:", string)
print("Non-Alphanumeric Set:", non_alphanumeric)
