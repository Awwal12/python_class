
'''
Project Description: Create a bank account management system that allows users to create and manage 
their bank accounts. The system should allów users to perform basic banking operations
like depositing and withdrawing money, checking balance, and viewing transaction history.

Steps to Implement:

1. Create a BankAcount class that will have the following attributes: account number, account holder name, 
account type (Savings or Checking), and balance.
2. Define a constructor method that will initialize the account attributes when a new object is created.
3. Define methods for depositing and withdrawing money from the account. These methods should update 
the balance attribute accordingly.
4. Define a method for checking the current balance of the account.
5. Define a method for displaying the transaction history of the account.
6. Create a main function that will allow users to create new accounts and perform banking 
operations on their accounts.

'''


class BankAccount:
    def __init__(self, accNum, accName, accType):
        self.accNum = accNum
        self.accName = accName
        self.accType = accType
        self.balance = 0

    def deposit(self):
        self.val = int(input('How much are depositing: '))
        self.balance += self.val
        self.addTransction(
            f'{self.accName} just deposited {self.val} NAIRA \n')

    def withdraw(self):
        print('How much do u want to withdraw')
        self.val = int(input())
        if self.val > self.balance:
            return 'Insufficient Funds'
        else:
            self.balance -= self.val
            self.addTransction(
                f'{self.accName} just withdrew {self.val} NAIRA \n')

    def checkBal(self):
        # print("What is your acct name n number: ")
        if self.accName and self.accNum:
            return f'Your balance is: {self.balance} NAIRA'
        else:
            return f'invalid credentials'

    def display_transaction_history(self):
        with open(f'transcHis.txt', "r") as file:
            result = file.read()
        return result

    def addTransction(self, message):
        with open('transcHis.txt', 'a') as file:
            file.write(message)


accounts = []


def main():
    accounts = []

    while True:
        print("Bank Management System")
        print("1. Create a new bank account")
        print("2. Deposit funds to your account")
        print("3. Withdraw funds from your account")
        print("4. Check your balance")
        print("5. Display transaction history")
        response = input("")

        if response == "1":
            name = input("Enter your name: ")
            account_type = input("Enter account type (Savings/Checking): ")
            account_number = input("Enter account number: ")
            new_account = BankAccount(account_number, name, account_type)
            accounts.append(new_account)
            print("Account created successfully.")

        elif response == "2":
            name = input("Enter your name: ")
            for account in accounts:
                if account.accName == name:
                    account.deposit()
                    break
            else:
                print("Can't find your account.")

        elif response == "3":
            name = input("Enter your name: ")
            for account in accounts:
                if account.accName == name:
                    account.withdraw()
                    break
            else:
                print("Can't find your account.")

        elif response == "4":
            name = input("Enter your name: ")
            for account in accounts:
                if account.accName == name:
                    print(account.checkBal())
                    break
            else:
                print("Can't find your account.")

        elif response == "5":
            name = input("Enter your name: ")
            for account in accounts:
                if account.accName == name:
                    print(account.display_transaction_history())
                    break
            else:
                print("Can't find your account.")


main()
