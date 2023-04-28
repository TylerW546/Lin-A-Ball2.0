import pygame
import random
from Globals import *

# Set up the green ball
ball_radius = 25
ball_color = GREEN
ball_x = random.randint(ball_radius, SCREEN_WIDTH - ball_radius)
ball_y = random.randint(ball_radius, SCREEN_HEIGHT - ball_radius)
ball_speed = 5
ball_dx = random.choice( [-ball_speed, ball_speed] )
ball_dy = random.choice( [-ball_speed, ball_speed] )