import pygame
import math
from Globals import *
from House import *
from Enemy import Enemy

def testArea(player, area):
    return player.x + player.radius >= area.x and player.x - player.radius <= area.x + area.size and player.y + player.radius >= area.y and player.y - player.radius <= area.y + area.size

class Player:
    def __init__(self, r=25, c=RED):
        self.x = SCREEN_WIDTH - r
        self.y = SCREEN_HEIGHT - r
        self.radius = r
        self.color = c
        self.dx = 0
        self.dy = 0
        self.ax = 0
        self.ay = 0
        self.speed = 7

        self.inHouse = False

        self.inZone = True
        self.zoneOne = False

        self.inEnemy = False
    
    def move(self, keys):
        self.ax = 0
        self.ay = 0
        
        a = 2
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.ay -= a
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.ax -= a
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.ay += a
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.ax += a
        
        self.dx *= .8
        self.dy *= .8

        self.dx += self.ax
        self.dy += self.ay
        
        maxVel = 7
        self.dx = max(-maxVel, min(self.dx, maxVel))
        self.dy = max(-maxVel, min(self.dy, maxVel))
        
        self.x += self.dx
        self.y += self.dy
    
        #this limits the x and y coordinates of the red circle
        self.x = max(self.radius, min(self.x, SCREEN_WIDTH - self.radius))
        self.y = max(self.radius, min(self.y, SCREEN_WIDTH - self.radius))

    def testHouseSafety(self):
        for house in House.houses:
            if testArea(self, house):
                self.inHouse = True
                house.playerIn = True
                return
        self.inHouse = False
        house.playerIn = False
    
    def testZoneSafety(self):
        self.inZone = False
        for zone in [zone1, zone2]:
            if testArea(self, zone):
                self.inZone = True
                zone.playerIn = True
            else:
                zone.playerIn = False

    def testEnemySafety(self):
        for enemy in Enemy.enemies:
            if math.dist( [enemy.x, enemy.y], [self.x, self.y] ) <= (enemy.radius + self.radius):
                self.inEnemy = True
                return
        self.inEnemy = False


    
    def draw(self, screen):
        if self.inHouse:
            pygame.draw.circle(screen, BLUE, (self.x, self.y), self.radius+2)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        