from polygon import Polygon
from point import Point

class Enemyship(Polygon):
    
     def __init__(self,name, width, height):

        
         super().__init__( points=[ Point(20,20), Point(-10,10), Point(30,15), Point(-20,-20) ] )


