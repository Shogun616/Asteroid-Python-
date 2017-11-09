import sys
from matplotlib.mathtext import ship
import random
import pygame
from pygame.locals import *
from game import Game
from ship import Ship
from bullet import Bullet
from star import Star
from spacerock import Spacerock
from spacerock2 import Spacerock2
from spacerock3 import Spacerock3
from enemyship import Enemyship

class Asteroids( Game ):

    """

    Asteroids extends the base class Game to provide logic for the specifics of the game

    """

    def __init__(self, name, width, height):

        super().__init__( name, width, height )

        self.ship = Ship( 320, 240, 0)  #  TODO: should create a Ship object here


        self.asteroids=[]          # TODO: should create asteroids

        for i in range(8):

            self.asteroids.append(Spacerock(random.randrange(640), random.randrange(480),random.randrange(4,8)))

        for i in range(4):

            self.asteroids.append(Spacerock2(random.randrange(640), random.randrange(480),random.randrange(4,8)))

        for i in range(2):

            self.asteroids.append(Spacerock3(random.randrange(640), random.randrange(480),random.randrange(4,8)))

      
        self.stars=[]     # TODO: should create stars

        for i in range(30):

            self.stars.append(Star(random.randrange(640), random.randrange(480),random.randrange(1,3), 0))

        self.bullets =[]

        self.enemyship=[]

        self.enemyship = Enemyship(640, 360, 0)
        
    def handle_input(self):
        
        super().handle_input()
       
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[K_LEFT] and self.ship:
           
            self.ship.rotate(-5)
            
        if keys_pressed[K_RIGHT] and self.ship:

            self.ship.rotate(5)
            
        if keys_pressed[K_UP] and self.ship:

            self.ship.accelerate(1.0)
           
        if keys_pressed[K_DOWN] and self.ship:

            self.ship.accelerate(0)
           
        if keys_pressed[K_SPACE] and self.ship:

            self.bullets.append(Bullet(self.ship.position.x,self.ship.position.y,self.ship.rotation))

            # TODO: should create a bullet when the user fires

                 
    def update_simulation(self):

        """

        update_simulation() causes all objects in the game to update themselves

        """

        super().update_simulation()


        if self.ship:

            self.ship.update( self.width, self.height )

        for asteroid in self.asteroids:

            asteroid.update( self.width, self.height )

        for star in self.stars:

            star.update( self.width, self.height )

        for bullet in self.bullets:

            bullet.update( self.width, self.height )

        # TODO: should probably call update on our bullet/bullets here

        # TODO: should probably work out how to remove a bullet when it gets old

        self.handle_collisions()

       
        
    def render_objects(self):

        """

        render_objects() causes all objects in the game to draw themselves onto the screen

        """

        super().render_objects()

        # Render the ship:

        if self.ship:

            self.ship.draw( self.screen )

        # Render all the stars, if any:

        for star in self.stars:

            star.draw( self.screen )

        # Render all the asteroids, if any:

        for asteroid in self.asteroids:

            asteroid.draw( self.screen )

        # Render all the bullet, if any:

        for bullet in self.bullets:

            bullet.draw( self.screen )


    def handle_collisions(self):

        for bullet in self.bullets:
           for spacerock in self.asteroids:
              if spacerock.contains(bullet.position):
               print("Target Destroyed")
               self.asteroids.remove(spacerock)


        for spacerock in self.asteroids:
            if isinstance( spacerock, Spacerock ):
               
                if self.ship and self.ship.collide(spacerock):
                    print("Ship Hit")
                    self.ship.health = self.ship.health - 25
                    self.asteroids.remove(spacerock)
                  
        if self.ship and self.ship.health <= 0:
            self.ship = None
                    
        
        for spacerock2 in self.asteroids:
            if isinstance( spacerock2, Spacerock2 ):

                if self.ship and self.ship.collide(spacerock2):
                    print("Ship Critical Hit")
                    self.ship.health = self.ship.health - 50
                    self.asteroids.remove(spacerock2)

        if self.ship and self.ship.health <= 0:
             self.ship = None

              
        for spacerock3 in self.asteroids:
            if isinstance( spacerock3, Spacerock3 ):


              if self.ship and self.ship.collide(spacerock3):
                print("Ship Destroyed")
                self.ship.health = self.ship.health - 100
                self.asteroids.remove(spacerock3)

        if self.ship and self.ship.health <= 0:
            self.ship = None
                     

       
                
        """

        handle_collisions() should check:

            - if our ship has crashed into an asteroid (the ship gets destroyed - game over!)

            - if a bullet has hit an asteroid (the asteroid gets destroyed)

        :return: 

        """

        # TODO: implement collission detection,

        #       using the collission detection methods in all of the shapes

        pass


