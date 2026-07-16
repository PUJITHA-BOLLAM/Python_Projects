from datetime import datetime
# Parent Class
class Account:
    def __init__(self, acc_no, name, balance=1000):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return

        self.balance += amount

        time = datetime.now().strftime("%d-%m-%Y %H:%M")
        self.transactions.append(f"{time} - Deposited ₹{amount}")

        print(f"Deposit Successful")
        print(f"Current Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")

        elif amount <= self.balance:
            self.balance -= amount

            time = datetime.now().strftime("%d-%m-%Y %H:%M")
            self.transactions.append(f"{time} - Withdrawn ₹{amount}")

            print(f"Withdrawal Successful")
            print(f"Current Balance: ₹{self.balance}")

        else:
            print("Insufficient Balance")

    def show_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet")
        else:
            print("\nTransaction History")
            for t in self.transactions:
                print(t)

    def display(self):
        print("\n------ ACCOUNT DETAILS ------")
        print("Account Number:", self.acc_no)
        print("Name:", self.name)
        print("Balance:", self.balance)


# Child Class - Savings Account
class SavingsAccount(Account):

    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest

        print(f"Interest Added: ₹{interest}")
        print(f"New Balance: ₹{self.balance}")


# Child Class - Current Account
class CurrentAccount(Account):

    def withdraw(self, amount):

        overdraft_limit = 500

        if amount <= 0:
            print("Invalid amount")

        elif amount <= self.balance + overdraft_limit:
            self.balance -= amount

            time = datetime.now().strftime("%d-%m-%Y %H:%M")
            self.transactions.append(f"{time} - Withdrawn ₹{amount}")

            print("Withdrawal Successful")
            print(f"Current Balance: ₹{self.balance}")

        else:
            print("Overdraft Limit Exceeded")


# Composition
class Bank:

    def __init__(self):
        self.accounts = []

    def create_account(self):

        acc_no = int(input("Enter Account Number: "))
        name = input("Enter Name: ")

        print("\n1. Savings Account")
        print("2. Current Account")
        print("3. Normal Account")

        choice = int(input("Choose Account Type: "))

        if choice == 1:
            account = SavingsAccount(acc_no, name)

        elif choice == 2:
            account = CurrentAccount(acc_no, name)

        else:
            account = Account(acc_no, name)

        self.accounts.append(account)

        print("Account Created Successfully!")

    def show_accounts(self):

        if not self.accounts:
            print("No Accounts Found")
            return

        print("\n------ ALL ACCOUNTS ------")

        for acc in self.accounts:
            print(
                f"Acc No: {acc.acc_no} | "
                f"Name: {acc.name} | "
                f"Balance: ₹{acc.balance}"
            )

    def find_account(self, acc_no):

        for acc in self.accounts:

            if acc.acc_no == acc_no:
                return acc

        return None

    def delete_account(self):

        acc_no = int(input("Enter Account Number to Delete: "))

        account = self.find_account(acc_no)

        if account:
            self.accounts.remove(account)
            print("Account Deleted Successfully")
        else:
            print("Account Not Found")


# Main Program
bank = Bank()

while True:

    print("\n========== BANK MANAGEMENT ==========")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Account Details")
    print("6. Transaction History")
    print("7. Show All Accounts")
    print("8. Add Interest (Savings)")
    print("9. Delete Account")
    print("10. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        bank.create_account()

    elif choice in [2, 3, 4, 5, 6, 8]:

        acc_no = int(input("Enter Account Number: "))

        account = bank.find_account(acc_no)

        if not account:
            print("Account Not Found")
            continue

        if choice == 2:
            amount = int(input("Enter Amount: "))
            account.deposit(amount)

        elif choice == 3:
            amount = int(input("Enter Amount: "))
            account.withdraw(amount)

        elif choice == 4:
            account.show_balance()

        elif choice == 5:
            account.display()

        elif choice == 6:
            account.show_transactions()

        elif choice == 8:

            if isinstance(account, SavingsAccount):
                account.add_interest()
            else:
                print("Interest available only for Savings Accounts")

    elif choice == 7:
        bank.show_accounts()

    elif choice == 9:
        bank.delete_account()

    elif choice == 10:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
```
