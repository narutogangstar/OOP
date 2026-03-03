# Parent class / super class 


class Vehicle :
    
    def __init__(self, color, wheels) :
        self.color = color
        self.wheels = wheels
        
    def honk(self) :
        print("Beep Beep!")
        
    def describe (self) :
        print(f"This vehicle is {self.color} and has {self.wheels} wheels.")
        
    def accelerate(self) :
        print("The vehicle is accelerating.")
        
    def brake(self) :
        print("The vehicle is braking.")
        
# making another Bike class which is a child class
#so it will inherit characteristics class from vehicle class
#child class / sub class

class Bike(Vehicle) :
    
    def __init__(self, color, wheels, mileage,model) :
        
        super().__init__(color, wheels)  # inheriting from parent class
        self.mileage = mileage
        self.model = model
        
    def horn(self) :
        print(" Peep Peep!")
        
    def describe_bike(self):
        print(f"This bike is a {self.model}, {self.color} in color, has {self.wheels} wheels and mileage of {self.mileage}.")
        
        
BMW = Vehicle("Black", 4)
BMW.describe()
BMW.honk()
BMW.accelerate()
BMW.brake()

royalEnfield = Bike("Red", 2, "40 km/l", "Classic 350")
royalEnfield.describe_bike()
royalEnfield.horn()

#check if this bike inherited from vehicle class
royalEnfield.accelerate()
royalEnfield.honk()
royalEnfield.brake()