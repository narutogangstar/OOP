# Topic: Encapsulation - Protecting data
# Example:
# - Vending Machine: users cannot directly access item stock

class VendingMachine:
    def __init__(self, machine_name, stock):
        self.machine_name = machine_name
        self.__stock = stock   # private attribute

    def add_items(self, amount):
        if amount > 0:
            self.__stock += amount
            print(f"Added {amount} items to the machine.")
        else:
            print("Amount must be positive.")

    def dispense_item(self, amount):
        if amount > 0 and amount <= self.__stock:
            self.__stock -= amount
            print(f"Dispensed {amount} item(s).")
        else:
            print("Not enough items or invalid amount.")

    # Getter method to access private stock
    def get_stock(self):
        print(f"Current stock: {self.__stock}")

    # Setter method to update stock safely
    def set_stock(self, new_stock):
        if new_stock >= 0:
            self.__stock = new_stock
        else:
            print("Stock cannot be negative.")


# Creating object
machine1 = VendingMachine("Coke Machine", 50)

# Adding and dispensing items
machine1.add_items(20)
machine1.dispense_item(10)

# Accessing public attribute
print(machine1.machine_name)

# Trying to access private attribute directly (will not work)
# print(machine1.__stock)

# Accessing stock using getter
machine1.get_stock()

# Changing stock using setter
machine1.set_stock(100)
machine1.get_stock()
