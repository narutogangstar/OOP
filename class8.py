# Topic: Encapsulation - Protecting data
# Example: 
# - vending machine - restricting direct access to inventory/cokes/sodas
# - bank account - restricting direct access to balance

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance #private attribute
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
            
        else:
            print("Deposit amount must be positive.")
            
            
    def withdraw(self, amount):
        if 0 < amount > 0 and amount < self.__balance:
            self.__balance = self.__balance - amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds or invalid amount.")
            
    # Gtter method to access private attribute
    def get_balance(self):
        print(f"Current balance: ${self.__balance}")
    
    
    # Setter method to modify private attribute
    
    def set_new_balance(self, new_balance):
        self.__balance = new_balance
            
            
            
            
            


account1 = BankAccount("Alice", 1000) 
account1.deposit(200)
account1.withdraw(150)

#try  to know th owner name
print(account1.owner)  

#try to know the balance 
# print(account1.__balance) -- this will not work bcz is private 

#now try to access the balance using getter method
account1.get_balance()

# try setter method to set new balance
account1.set_new_balance(500000000000)
# find the new balance
account1.get_balance()