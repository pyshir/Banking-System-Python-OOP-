from abc import ABC, abstractmethod

class Account (ABC):
    
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    def get_balance(self):
        return self._balance
    
    def set_balance(self, balance):
        if balance < 0:
            self._balance = 0
        else:
            self._balance = balance

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    def __add__(self, other):
        return self._balance + other._balance



class SavingsAccount(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance)

    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self._balance + amount)
            return True
        
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance + self.interest():
            self.set_balance(self._balance - amount)            
            return True        
        
        return False
        
    def interest(self):
        interest = self._balance * 0.1
        return interest



        
class CurrentAccount(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance)
    
    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self._balance + amount)
            return True
        
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance + self.interest():
            self.set_balance(self._balance - amount)
            return True
        
        return False
        
    def interest(self):
        interest = self._balance * 0.04
        return interest


class Bank:

    def  __init__(self):
        self.accounts = {
            Customer(1): SavingsAccount('name1', 100),
            Customer(2): SavingsAccount('name2', 200),
            Customer(3): CurrentAccount('name3', 300),
            Customer(4): CurrentAccount('name4', 400)
            
            }
        self.main_account = SavingsAccount('Bank', 0)

    def __len__(self):
        return len(self.accounts.keys())

    def get_net_balance(self):
        total  = 0
        for i, j in self.accounts.items():
            x = j + self.main_account
            total += x
        return total


class Customer:

    def __init__(self, account_no):
        self.account_no = account_no

    def __eq__(self, other):
        return self.account_no == other.account_no

    def __hash__(self):
        return hash(self.account_no)
       

class Transaction:

    def __init__(self):
        self.transactions = {}

    def add_statement(self, account_no, action):
        if account_no not in self.transactions:
            self.transactions[account_no] = []
        
        self.transactions[account_no].append(action)

    def get_statement(self, account_no):
        for i, j in self.transactions.items():
            if i == account_no:
                print(f'Statement of Account No: {account_no}')
                for x in j:
                    print(x)


if __name__ == '__main__':
    
    bank = Bank()
    transaction = Transaction()

    while True:

        print(f"""
1.Deposit
2.Withdraw
3.Transfer
4.Interest & check Balance
5.Statement
6.Bank Statement
""")
        choice = input('Choose one: = ')
        if choice == '6':
            print(f'Number of account in this bank is, {len(bank)}')
            print(f'Total Bank Balance is, {bank.get_net_balance()}')

            break

        account_no = int(input('Account Id: '))
        customer = Customer(account_no)
        for i, j in bank.accounts.items():
            if i == customer:

                if choice == '1':
                    amount = int(input('Amount: '))
                    if j.deposit(amount):
                        print('Successful')
                        action = f'Deposit: {amount}'
                        transaction.add_statement(account_no, action)    
                        break                    
                    else:
                        print('Failed')                    
                    break

                elif choice == '2':
                    amount = int(input('Amount: '))
                    if j.withdraw(amount):
                        print('Successful')
                        action = f'Withdraw: {amount}'
                        transaction.add_statement(account_no, action)
                        break
                    else:
                        print('Failed')
                    break

                elif choice == '3':
                    amount = int(input('Amount: '))
                    second_account = int(input('Second Account Id: '))
                    customer2 = Customer(second_account)
                    for x, y in bank.accounts.items():
                        if x == customer2:
                            if j.withdraw(amount):
                                if y.deposit(amount):
                                    action_1 = f'Transferred: {amount}'
                                    action_2 = f'Recieved: {amount}'
                                    transaction.add_statement(account_no, action_1)
                                    transaction.add_statement(second_account, action_2)
                                    print('Transfer Successful')
                                break
                    else:
                        print('Invalid second Account')
                        break

                    break

                elif choice == '4':
                    print(f'Total balance: {j.get_balance():.2f} BDT\nTotal Interest: {j.interest():.2f} BDT')
                    break

                elif choice == '5':
                    transaction.get_statement(account_no)
                    break

        else:
            print('Account not found')

        if choice == '6':
            print(len(bank))

            
                
                    