class HoursToDaysConverter:
    def __init__(self, hours):
        self.hours = hours

    def convert_to_days(self):
        return self.hours / 24

try:
    # Get the number of hours from the user
    hours_input = float(input("Enter the number of hours: "))

    # Create an instance of HoursToDaysConverter
    converter = HoursToDaysConverter(hours_input)

    # Convert hours to days
    days_result = converter.convert_to_days()

    # Display the result
    print(f"{hours_input} hours is equal to {days_result:.2f} days.")
except ValueError:
    # Handle invalid input
    print("Invalid input. Please enter a valid number of hours.")
