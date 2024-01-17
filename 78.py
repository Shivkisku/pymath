class MyClass:
    def __init__(self, value):
        self.value = value

def process_object(obj):
    obj.value *= 2
    return obj

# Creating an instance of MyClass
my_obj = MyClass(10)

# Calling the process_object function
result_obj = process_object(my_obj)

# Displaying the values of the original and modified objects
print("Original Object Value:", my_obj.value)
print("Modified Object Value:", result_obj.value)
