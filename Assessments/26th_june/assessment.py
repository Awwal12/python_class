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
        users_resp = input(
            "Select from the options \n Select 1 to create account \n select 2 to deposit \n select 3 to withdraw \n select 4 to  ")


john = BankAccount(1012, 'dio', 'savings')
john.deposit()
john.checkBal()
