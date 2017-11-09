from polygon import Polygon
from point import Point

import random

class Spacerock3(Polygon):

    def __init__(self, x, y, rotation):

        Polygon.__init__(self, points=[Point(10,10), Point(30,-14), Point(60,0), Point(60,60), Point(60,60), Point(14,76), Point(10,60)], x=x, y=y, rotation=rotation)

        self.accelerate(0.5)

        self.rotate(random.randrange(180))

        self.angular_velocity = (random.randrange(0,120)/100)
    


