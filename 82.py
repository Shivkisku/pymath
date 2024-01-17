class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create a list of Person objects
people = [
    Person("Alice", 23),
    Person("Bob", 30),
    Person("Charlie", 28),
    Person("David", 22),
    Person("Eva", 26)
]

# Define a filtering criterion function
def is_older_than_25(person):
    return person.age > 25

# Use filter to get people older than 25
filtered_people = filter(is_older_than_25, people)

# Convert the filtered iterable to a list
filtered_people_list = list(filtered_people)

# Display the names and ages of people older than 25
print("People older than 25:")
for person in filtered_people_list:
    print(f"Name: {person.name}, Age: {person.age}")
