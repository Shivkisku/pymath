class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand.capitalize()
        self.model = model.capitalize()
        self.price = price

class PhoneStore:
    def __init__(self):
        self.inventory = []

    def add_phone(self, brand, model, price):
        phone = Phone(brand, model, price)
        self.inventory.append(phone)
        print(f"Phone {brand} {model} added to inventory")

    def remove_phone(self, brand, model):
        brand = brand.capitalize()
        model = model.capitalize()
        for phone in self.inventory:
            if phone.brand == brand and phone.model == model:
                self.inventory.remove(phone)
                print(f"Phone {brand} {model} removed from inventory")
                return
        print(f"Phone {brand} {model} not found in inventory")

    def find_phone(self, brand, model):
        brand = brand.capitalize()
        model = model.capitalize()
        for phone in self.inventory:
            if phone.brand == brand and phone.model == model:
                return phone
        return None

    def display_inventory(self):
        print("Phone Inventory:")
        for phone in self.inventory:
            print(f"{phone.brand} {phone.model} - Price: {phone.price}")

# Create an instance of PhoneStore
phone_store = PhoneStore()

while True:
    print("\nMenu:")
    print("1. Add Phone to Inventory")
    print("2. Remove Phone from Inventory")
    print("3. Find Phone in Inventory")
    print("4. Display Inventory")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        brand = input("Enter phone brand: ")
        model = input("Enter phone model: ")
        price = float(input("Enter phone price: "))
        phone_store.add_phone(brand, model, price)

    elif choice == "2":
        brand = input("Enter phone brand to remove: ")
        model = input("Enter phone model to remove: ")
        phone_store.remove_phone(brand, model)

    elif choice == "3":
        brand = input("Enter phone brand to find: ")
        model = input("Enter phone model to find: ")
        found_phone = phone_store.find_phone(brand, model)
        if found_phone:
            print(f"Phone found: {found_phone.brand} {found_phone.model} - Price: {found_phone.price}")
        else:
            print(f"Phone {brand} {model} not found in inventory")

    elif choice == "4":
        phone_store.display_inventory()

    elif choice == "5":
        print("Quitting the program.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
