class GameCharacter:
    health = 100
    score = 0
    
    def take_damage(self, damage_value):
        self.health =  self.health - damage_value
        print(f"Ouch!! Health: {self.health}")
        
        
        
    def hit(self):
        self.score = self.score + 10
        print(f"Current Score: {self.score}")
        
    def show_status(self):
        print(f"Current Health: {self.health}, Current Score: {self.score}")
        
        



player = GameCharacter()

player.show_status()

player.hit()
player.hit()

player.take_damage(30)


