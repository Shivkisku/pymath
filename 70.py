class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance):
        if account_number in self.accounts:
            print("Account number already exists. Please choose a different account number.")
            return
        if initial_balance < 0:
            print("Initial balance cannot be negative.")
            return
        self.accounts[account_number] = {"holder": account_holder, "balance": initial_balance}
        print(f"Account created successfully for {account_holder} with account number {account_number}.")

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            print("Account not found.")
            return
        if amount < 0:
            print("Deposit amount cannot be negative.")
            return
        self.accounts[account_number]["balance"] += amount
        print(f"Deposit successful. New balance: {self.accounts[account_number]['balance']}")

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            print("Account not found.")
            return
        if amount < 0:
            print("Withdrawal amount cannot be negative.")
            return
        if amount > self.accounts[account_number]["balance"]:
            print("Insufficient balance.")
            return
        self.accounts[account_number]["balance"] -= amount
        print(f"Withdrawal successful. New balance: {self.accounts[account_number]['balance']}")

    def check_balance(self, account_number):
        if account_number not in self.accounts:
            print("Account not found.")
            return
        account_holder = self.accounts[account_number]["holder"]
        balance = self.accounts[account_number]["balance"]
        return f"Account Holder: {account_holder}, Balance: {balance}"


def main():
    bank = Bank()

    while True:
        print("\nBank Management System Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(account_number, account_holder, initial_balance)
        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)
        elif choice == "4":
            account_number = input("Enter account number: ")
            result = bank.check_balance(account_number)
            if result:
                print(result)
        elif choice == "5":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
