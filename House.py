import pygame
from Globals import *

# set up random safe house
safe_size = 60
safe_color = BLUE
safe_x = 0
safe_y = 0

def safeHouse(screen, safe_x, safe_y):
    pygame.draw.rect(screen, BLUE, [safe_x, safe_y, safe_size, safe_size], 0)