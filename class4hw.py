class GameCharacter:
    
    
    health = 100
    score = 0
    lives = 3

    def take_damage(self, damage):
        self.health = self.health - damage
        print(f"Ouch! Health: {self.health}")
        
        

    def heal(self, value):
        self.health = self.health + value
        print(f"Healed! Health: {self.health}")
        
        
        

    def hit(self):
        self.score = self.score + 10
        print(f"Score: {self.score}")
        
        

    def lose_life(self):
        self.lives = self.lives - 1
        print(f"Lives left: {self.lives}")
        
        

    def show_status(self):
        print(f"Health: {self.health}, Score: {self.score}, Lives: {self.lives}")
        


player = GameCharacter()

player.show_status()

player.hit()
player.hit()

player.take_damage(25)
player.heal(10)

player.lose_life()

player.show_status()
