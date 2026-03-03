# Topic: Inheritance

# Example: Animal Kingdom

# Parent class/ Superclass: Animal

# Child class/ Subclass: Dog, Cat

class Animal:
    
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    
    def speak(self):
        print(f"{self.name} makes a sound.")
    
    
    def display_age(self):
        print(f"{self.name} is {self.age} years old.")
        

class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)  
        self.breed = breed  
    
    
    def speak(self):
        print(f"{self.name} barks!")
    
    def display_breed(self):
        print(f"{self.name} is a {self.breed} breed.")


class Cat(Animal):
    def __init__(self, name, age, color, personality):
        super().__init__(name, age, color)  
        self.personality = personality  
        
    def speak(self):
        print(f"{self.name} meows!")
    
    
    def display_personality(self):
        print(f"{self.name} is a {self.personality} cat.")


dog = Dog("Buddy", 4, "brown", "Golden Retriever")
dog.speak()  
dog.display_age()  
dog.display_breed()  


cat = Cat("Whiskers", 3, "gray", "playful")
cat.speak() 
cat.display_age()  
cat.display_personality() 
