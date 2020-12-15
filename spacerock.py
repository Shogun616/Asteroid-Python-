from polygon import Polygon
from point import Point

import random

class Spacerock(Polygon):

    def __init__(self, x, y, rotation):

        Polygon.__init__(self, points=[Point(-10,-10), Point(7,-4), Point(15,-15), Point(15,8), Point(15,15), Point(7,9), Point(0,7)], x=x, y=y, rotation=rotation)

        self.accelerate(1.5)
        self.rotate(random.randrange(720))
        self.angular_velocity = (random.randrange(0,300)/100)
