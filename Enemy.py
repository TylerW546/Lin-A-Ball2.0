import pygame
import random
import Global

class Enemy:
    enemies = []

    maxTailPos = 20

    def __init__(self, r=25, c=Global.GREEN, s=5):
        # Set up the green ball
        self.radius = r
        self.color = c
        self.x = random.randint(r, Global.GAME_WIDTH - r)
        self.y = random.randint(r, Global.GAME_HEIGHT - r)
        self.speed = s
        self.dx = random.choice( [-self.speed, self.speed] )
        self.dy = random.choice( [-self.speed, self.speed] )

        self.positions = []

        Enemy.enemies.append(self)
    
    def move(self):
        #MOVE THE GREEN BALL

        self.positions.insert(0, [self.x, self.y])
        if len(self.positions) > Enemy.maxTailPos:
            self.positions = self.positions[:Enemy.maxTailPos]

        self.x += self.dx
        self.y += self.dy

    def bounce(self):
        #create random bounces off of the wall
        if self.x < self.radius or self.x > Global.GAME_WIDTH - self.radius:
            self.dx = -self.dx
            if random.randint(1,2) == 1:
                self.dy = max( -18, min( self.dy + random.randint(-6,6),18) )
            self.x = max(self.radius, min(Global.GAME_WIDTH - self.radius, self.x))
        
        if self.y < self.radius or self.y > Global.GAME_WIDTH - self.radius:
            self.dy = -self.dy
            if random.randint(1,2) == 1:
                self.dx = max( -18, min( self.dx + random.randint(-6,6),18) )
                
            self.y = max(self.radius, min(Global.GAME_HEIGHT - self.radius, self.y))
    
    def draw(self, surface):
        surface2 = pygame.surface.Surface((Global.GAME_WIDTH, Global.GAME_HEIGHT), pygame.SRCALPHA)
        for i in range(len(self.positions)):
            pos = self.positions[::-1][i]
            #pygame.draw.circle(surface, self.color, (pos[0], pos[1]), 2)
            pygame.draw.circle(surface2, [self.color[0], self.color[1], self.color[2], 100*i/len(self.positions)], (pos[0], pos[1]), self.radius*(i/len(self.positions)))
        pygame.draw.circle(surface2, self.color, (self.x, self.y), self.radius)

        surface.blit(surface2, (0,0))