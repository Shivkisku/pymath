import random

def generate_random_numbers():
    # Create a list of numbers from 0 to 49
    numbers = list(range(50))
    
    # Shuffle the list
    random.shuffle(numbers)
    
    # Generate and display random numbers
    while True:
        random_number = numbers.pop()
        print(f"\nRandom Number = {random_number}")
        
        # Ask if the user wants another random number
        user_input = input("Do You Want Another Random Number? (Y/N) = ").upper()
        if user_input != 'Y':
            break

# Call the function to generate random numbers
generate_random_numbers()
