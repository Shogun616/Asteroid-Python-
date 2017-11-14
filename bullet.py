from circle import Circle
from polygon import Polygon

class Bullet(Circle):

    def __init__(self, x, y, rotation):
        super().__init__(x, y, r=2,rotation=rotation)

        self.accelerate(5.0)

    def update_bullet(self, width, height):


       # Update the position and orientation of the shape

       #  position is modified by "pull" - how much it should move each frame

       #  rotation is modified by "angular_velocity" - how much it should rotate each frame

       self.position += self.pull

       self.rotation += self.angular_velocity
                        
                        
   






        


    


