from circle import Circle
from polygon import Polygon

class Bullet(Circle):

    def __init__(self, x, y, rotation):
        super().__init__(x, y, r=2,rotation=rotation)

        self.accelerate(10.0)
                        
                        
   






        


    


