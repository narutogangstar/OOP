## Topic: Inheritance

# Example: Animal Kingdom

# Parent class/ Superclass: Animal

# Child class/ Subclass: Bird, Fish



class Animal:
    
    def  __init__(self, name=None,age = None ,color = None):
        self.name = name
        self.age = age
        self.color = color
    
    def eat(self):
        print(f"{self.name} is eating. nomnomnom")
    
    def sleep(self):
        print(f"{self.name} is sleeping. zzzzzzz")




class Bird(Animal):
    def __init__(self, name, color, eating_habit, bird_type):
        
        super().__init__(name, age = None, color = color)
        self.eating_habit = eating_habit
        self.bird_type = bird_type
        
    def fly(self):
        print(f"{self.name} is flying high in the sky ")
    def info(self):
        print(f"{self.name} is a {self.age} year old {self.color} {self.bird_type} bird with a {self.eating_habit}")
        


#another child class

class Fish(Animal):
    def __init__(self, name, water_type):
        super().__init__(name)
        self.water_type = water_type
        
    def swim(self):
        print(f"{self.name} is swiming in the water")
        
# making objects of any class
parrot = Bird("blue","green","hervivore","Normal")
parrot.info()
parrot.eat()
parrot.eat()

tuna = Fish("tuna","saltwater")
tuna.swim()