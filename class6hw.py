# Parent class / super class

class Cat:
    
    def __init__(self, color, age, breed):
        self.color = color
        self.age = age
        self.breed = breed
        
    def sound(self):
        print("Meow!")
        
    def describe(self):
        print(f"This cat is {self.color}, {self.age} years old, and of {self.breed} breed.")
        
    def eat(self):
        print("The cat is eating.")
        

# Child class / sub class
# Tiger will inherit properties from Cat

class Tiger(Cat):
    
    def __init__(self, color, age, breed, weight, length):
        
        super().__init__(color, age, breed)  # inheriting from Cat class
        self.weight = weight
        self.length = length
        
    def roar(self):
        print("ROARRR!")
        
    def describe_tiger(self):
        print(
            f"This tiger is {self.color}, {self.age} years old, "
            f"weighs {self.weight}, is {self.length} long, "
            f"and belongs to the {self.breed} breed."
        )


# Creating objects

kitty = Cat("White", 2, "Persian")
kitty.describe()
kitty.sound()
kitty.eat()

print()

sheru = Tiger("Orange", 5, "Bengal", "220 kg", "3 meters")
sheru.describe_tiger()
sheru.roar()

# Checking inherited methods
sheru.sound()
sheru.eat()
