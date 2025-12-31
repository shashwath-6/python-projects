import sqlite3
from datetime import datetime


class BankSystem:
    def __init__(self):
        self.connection = sqlite3.connect("abcbank.db")
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        # Create account table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_number INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                balance REAL NOT NULL
            )
        ''')

        # Create transfer history table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transfers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                from_account INTEGER,
                to_account INTEGER,
                amount REAL,
                timestamp TEXT NOT NULL,
                FOREIGN KEY (from_account) REFERENCES accounts(account_number),
                FOREIGN KEY (to_account) REFERENCES accounts(account_number)
            )
        ''')
        self.connection.commit()

    def create_account(self):
        try:
            account_number = int(input("Enter account number: "))
            name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial balance: "))

            self.cursor.execute('''INSERT INTO accounts (account_number, name, balance) VALUES (?, ?, ?)''',
                                (account_number, name, initial_balance))
            self.connection.commit()
            print("Account created successfully.")
        except sqlite3.IntegrityError:
            print("Account number already exists.")
        except ValueError:
            print("Invalid input. Please try again.")

    def deposit(self):
        try:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))

            if amount <= 0:
                print("Invalid deposit amount.")
                return

            self.cursor.execute('''SELECT balance FROM accounts WHERE account_number = ?''', (account_number,))
            account = self.cursor.fetchone()

            if account:
                new_balance = account[0] + amount
                self.cursor.execute('''UPDATE accounts SET balance = ? WHERE account_number = ?''',
                                    (new_balance, account_number))
                self.connection.commit()
                print(f"Deposited {amount}. New balance: {new_balance}")
            else:
                print("Account not found.")
        except ValueError:
            print("Invalid input. Please try again.")

    def withdraw(self):
        try:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Invalid withdrawal amount.")
                return

            self.cursor.execute('''SELECT balance FROM accounts WHERE account_number = ?''', (account_number,))
            account = self.cursor.fetchone()

            if account:
                if account[0] >= amount:
                    new_balance = account[0] - amount
                    self.cursor.execute('''UPDATE accounts SET balance = ? WHERE account_number = ?''',
                                        (new_balance, account_number))
                    self.connection.commit()
                    print(f"Withdrew {amount}. New balance: {new_balance}")
                else:
                    print("Insufficient balance.")
            else:
                print("Account not found.")
        except ValueError:
            print("Invalid input. Please try again.")

    def show_balance(self):
        try:
            account_number = int(input("Enter account number: "))

            self.cursor.execute('''SELECT name, balance FROM accounts WHERE account_number = ?''', (account_number,))
            account = self.cursor.fetchone()

            if account:
                print(f"Account Holder: {account[0]}\nBalance: {account[1]}")
            else:
                print("Account not found.")
        except ValueError:
            print("Invalid input. Please try again.")

    def transfer(self):
        try:
            from_account = int(input("Enter sender's account number: "))
            to_account = int(input("Enter receiver's account number: "))
            amount = float(input("Enter amount to transfer: "))

            if amount <= 0:
                print("Invalid transfer amount.")
                return

            self.cursor.execute('''SELECT balance FROM accounts WHERE account_number = ?''', (from_account,))
            sender = self.cursor.fetchone()

            self.cursor.execute('''SELECT balance FROM accounts WHERE account_number = ?''', (to_account,))
            receiver = self.cursor.fetchone()

            if sender and receiver:
                if sender[0] >= amount:
                    new_sender_balance = sender[0] - amount
                    new_receiver_balance = receiver[0] + amount

                    self.cursor.execute('''UPDATE accounts SET balance = ? WHERE account_number = ?''',
                                        (new_sender_balance, from_account))
                    self.cursor.execute('''UPDATE accounts SET balance = ? WHERE account_number = ?''',
                                        (new_receiver_balance, to_account))

                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.cursor.execute(
                        '''INSERT INTO transfers (from_account, to_account, amount, timestamp) VALUES (?, ?, ?, ?)''',
                        (from_account, to_account, amount, timestamp))
                    self.connection.commit()
                    print(f"Transferred {amount} from account {from_account} to account {to_account} at {timestamp}.")
                else:
                    print("Insufficient balance in the sender's account.")
            else:
                print("One or both accounts not found.")
        except ValueError:
            print("Invalid input. Please try again.")

    def close(self):
        self.connection.close()


# Example usage
if __name__ == "__main__":
    bank = BankSystem()

    while True:
        print("\n--- Bank System Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Show Balance")
        print("5. Transfer")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.deposit()
        elif choice == "3":
            bank.withdraw()
        elif choice == "4":
            bank.show_balance()
        elif choice == "5":
            bank.transfer()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            bank.close()
            break
        else:
            print("Invalid choice. Please try again.")