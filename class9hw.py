# Base class Thing
class Thing:
    def __init__(self):
        print(f"{self.__class__.__name__} created")
    
    def speak(self):
        print(f"{self.__class__.__name__} makes a sound")

# A Car class that inherits from Thing
class Car(Thing):
    def __init__(self):
        super().__init__()
    
    def speak(self):
        print("Car goes Vroom Vroom")

# A Robot class that inherits from Thing
class Robot(Thing):
    def __init__(self):
        super().__init__()
    
    def speak(self):
        print("Robot says Beep Boop")

# A Phone class that inherits from Thing
class Phone(Thing):
    def __init__(self):
        super().__init__()
    
    def speak(self):
        print("Phone rings: Ring Ring")

# A Human class that inherits from Thing
class Human(Thing):
    def __init__(self):
        super().__init__()
    
    def speak(self):
        print("Human says Hello!")

# A Book class that inherits from Thing
class Book(Thing):
    def __init__(self):
        super().__init__()
    
    def speak(self):
        print("Book rustles as pages turn")

# Create objects of different types
car = Car()
robot = Robot()
phone = Phone()
human = Human()
book = Book()

# Create a list of these objects
things = [car, robot, phone, human, book]

# Use a loop to call the `speak()` method for each object
for thing in things:
    thing.speak()
