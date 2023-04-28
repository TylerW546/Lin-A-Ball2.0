import pygame
from Globals import *

# Set up the red circle
circle_radius = 25
circle_color = RED
circle_x = SCREEN_WIDTH - circle_radius
circle_y = SCREEN_HEIGHT - circle_radius
circle_dx = 7
circle_dy = 7

class PlayerBall:
    def __init__(self, x, y):
        self.x = x
        self.y = y