
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
        self.transcHistory = []

    def deposit(self):
        self.val = int(input('How much are depositing: '))
        self.balance += self.val
        print(f'You just deposited {self.val} ')
        self.transcHistory.append(f'You deposited {self.val} today')

    def withdraw(self):
        print('How much do u want to withdraw')
        self.val = int(input())
        if self.val > self.balance:
            print('Insufficient Funds')
        else:
            self.balance -= self.val
            print(f'You just withdrew: {self.balance} NAIRA')
            self.transcHistory.append(f'You withdrew {self.val} today')

    def checkBal(self):
        # print("What is your acct name n number: ")
        if self.accName and self.accNum:
            print(f'Your balance is: {self.balance} NAIRA')
        else:
            print(f'invalid credentials')

    def transHisto(self):
        print(self.transcHistory)


accounts = []


def main():
    while True:
        response = input
