import pygame
import random
from Globals import *
from Globals import BLUE

class RectArea:
    def __init__(self, x=0, y=0, s=60, c=BLUE):
        # set up random safe house
        self.x = x
        self.y = y
        self.size = s
        self.color = c

        self.playerIn = False
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.size, self.size], 0)

class House(RectArea):
    houses = []

    def __init__(self, x=0, y=0, s=60, c=BLUE, append=True):
        super().__init__(x,y,s,c)

        if append:
            House.houses.append(self)
        
    def move(self):
        self.x = random.randint(5,595-self.size)
        if self.x <= 105:
            self.y = random.randint(105,595-self.size)
        elif self.x >= 435:
            self.y = random.randint(5,495-self.size)


class Zone(RectArea):
    def __init__(self, x=0, y=0, s=60, c=BLUE):
        super().__init__(x, y, s, c)
    
    def draw(self, screen):
        if self.playerIn:
            pygame.draw.rect(screen, BLUE, [self.x-1, self.y-1, self.size+2, self.size+2], 0)
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.size, self.size], 0)

    

zone1 = Zone(0,0,100,(255, 255, 167))
zone2 = Zone(SCREEN_WIDTH-100,SCREEN_HEIGHT-100,100,(255, 255, 167))