from polygon import Polygon
from point import Point

class Ship(Polygon):

    def __init__(self,name, width, height):
        
         super().__init__( points=[ Point(0,0), Point(-10,10), Point(15,0), Point(-10,-10) ] )

         self.name = True
         self.alive = True
         self.health = 100
         self.armor = 3
         self.shot = 1

    def __str__(self):

        if self.alive:
            return "%s (%i armor)" % (self.name)
        else:
            return "%s (Game Over)" % self.name

    def fire_at(self, spacerock):

        if self.shot >= 1:
            self.shot -= 1
            print .self.name, "Target Hit!", spacerock.name
            spacerock.hit()
        else:
            print .self.name, "Target Miss!"

    def hit(self):
        self.armor -= 2
        print .self.name, "Hit"
        if self.armor <= 0:
            print .self.armor, "Critical Hit"

        self.life -= 1
        print .self.name
        if self.name <= 0:
             self.explode()

    def explode(self):
        self.alive = False
        print .self.name, "Ship Destroyed!"
