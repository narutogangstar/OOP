class smartphone:
    #function/methods that is called automatically when an object is created
    def __init__(self, brand, storage, battery, color, model, price):
        
        
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage
        self.color = color
        self.battery = battery
        
        print(f"{self.brand} {self.model} has been created.")
        
    def take_photo(self):
        if self.battery >= 5:
        
            print("Taking photo...")
            self.battery = self.battery - 1
            print(f"Your battery after taking this photo {self.battery}%")
        else:
            print(f"Sorry your battery is low {self.battery}%, please charge your phone")
            
    def download_something(self,size):
        if size>= self.storage:
            print("Download not possible")
            print(f"Your available storage is {self.storage}GB")
        else:
            print("You can download it easily")
            print("downloaded successfully !")
            self.storage = self.storage - size
            print(f"Your available storage after download is {self.storage}GB")
        


#now create the actual object

Vivo = smartphone("Vivo", 512, 7300, "Black", "X200 ulta", 1000000 )



Vivo.take_photo()
Vivo.take_photo()

Vivo.download_something(100)
Vivo.download_something(450)

# You can create many objects
Vivo2 = smartphone("Vivo", 256, 5000, "Blue", "Y20", 50000 )
Vivo2.take_photo()

for i in range(7000):
    Vivo2.take_photo()





