import pygame
import random
import Global

class RectArea:
    def __init__(self, x=0, y=0, s=60, c=Global.BLUE):
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

    def __init__(self, x=0, y=0, s=60, c=Global.BLUE, append=True):
        super().__init__(x,y,s,c)

        if append:
            House.houses.append(self)
        
    def move(self):
        self.x = random.randint(5,Global.SCREEN_WIDTH-5-self.size)
        if self.x <= 105:
            self.y = random.randint(105,Global.SCREEN_HEIGHT-5-self.size)
        elif self.x >= Global.SCREEN_WIDTH-105:
            self.y = random.randint(5,Global.SCREEN_HEIGHT-105-self.size)
        else:
            self.y = random.randint(5,Global.SCREEN_HEIGHT-5-self.size)


class Zone(RectArea):
    def __init__(self, x=0, y=0, s=60, c=Global.BLUE, zone=1):
        super().__init__(x, y, s, c)
        self.zone = zone
    
    def draw(self, screen):
        if self.playerIn:
            pygame.draw.rect(screen, Global.BLUE, [self.x-1, self.y-1, self.size+2, self.size+2], 0)
        if (self.zone==1) == Global.targetBoxOne:
            pygame.draw.rect(screen, Global.RED, [self.x-1, self.y-1, self.size+2, self.size+2], 0)
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.size, self.size], 0)

    

zone1 = Zone(0,0,100,(255, 255, 167),1)
zone2 = Zone(Global.SCREEN_WIDTH-100,Global.SCREEN_HEIGHT-100,100,(255, 255, 167),2)