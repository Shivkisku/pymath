class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def find_elder(person1, person2):
    if person1.age > person2.age:
        return person1
    elif person2.age > person1.age:
        return person2
    else:
        return None

# Create two Person objects
person1 = Person("John", 25)
person2 = Person("Alice", 30)

# Find the elder person
elder = find_elder(person1, person2)

# Display the result
if elder is None:
    print("Both persons are of the same age.")
else:
    print(f"The elder person is {elder.name} with age {elder.age}.")
