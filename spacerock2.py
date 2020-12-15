from polygon import Polygon
from point import Point

import random

class Spacerock2(Polygon):

    def __init__(self, x, y, rotation):

        Polygon.__init__(self, points=[Point(0,0), Point(13,-7), Point(20,0), Point(30,17), Point(30,30), Point(7,38), Point(0,20)], x=x, y=y, rotation=rotation)

        self.accelerate(0.8)
        self.rotate(random.randrange(360))
        self.angular_velocity = (random.randrange(0,190)/100)
