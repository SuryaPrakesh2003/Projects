class Bank:
    def __init__(self,name):
        self.name=name
        self.accounts=[]
    def add_account(self,account):
        self.accounts.append(account)
class Account:
    def __init__(self,number,owner,balance,password):
        self.number=number
        self.owner=owner
        self.balance=balance
        self.password=password
        self.transactions=[]
    def deposit(self,amount):
            self.balance+=amount
            self.transactions.append(Transaction(amount,'Deposit'))
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            self.transactions.append(Transaction(amount,'Deposit'))
        else:
            print("Insufficient Funds")
            
class Transaction:
    def __init__(self,amount,type):
        self.amount=amount
        self.type=type
def fAccount(accounts, number):
    for account in accounts:
        if account.number == number:
            return account
    return None
bankname=input("Enter bank name:")
bank=Bank(bankname)
while True:
    print("1.create account")
    print("2.Deposit")
    print('3.Withdraw')
    print("4.check balance")
    print('5.Exit')
    choice=int(input("Enter your choice"))
    if choice==1:
        number=input("enter account number:")
        owner=input("enter account owner name:")
        balance=float(input("enter opening balance"))
        password=input("Enter your password")
        account=Account(number,owner,balance,password)
        bank.add_account(account)
        print("Account created successfully")
    elif choice==2:
        number=input("Enter account number:")
        amount=float(input("Enter amount to deposit:"))
        password=input("enter your password")
        account=fAccount(bank.accounts,number)
        if account:
            if account.password==password:
                account.deposit(amount)
                print("Deposit Successful")
                break
            else:
                print("password is incorrect")
                break
        else:
            print("Account not found")
    elif choice==3:
        number=input("Enter account number:")
        amount=float(input("Enter amount to withdraw:"))
        password=input("enter your password")
        account=fAccount(bank.accounts,number)
        if account:
            account.withdraw(amount)
            print("withdrawal is Successful")
        else:
            print("Account not found")
    elif choice==4:
        number=input("enter account number:")
        password=input("enter your password:")
        for i in bank.accounts:
            if i.number==number:
                if i.password==password:
                    print("your balance is :"+str(i.balance))
                    break
                else:
                    print("password is incorrect")
                    break
            else:
                print("There is no bank account")
            
    elif choice==5:
        print('Thank you for using the Bank Management System')
        break
    else:
        print('Invalid choice')
    