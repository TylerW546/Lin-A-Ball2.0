# Program--Line-A-Ball
# Version Number: 1
# Date Last Updated: 04/26/23

# Import some libraries
import pygame
import random
import time
import math
import os
from pygame.locals import *  #don't need on home computer
 
from Globals import *
from Displays import *
from House import *
from Enemy import *
from Player import *

# Initialize the game engine
pygame.init()

#this code will right justify the screen in the top right
RIGHT_JUSTIFY_X = 1920 - SCREEN_WIDTH - 50 #1600 for laptop, 1920 for desktop
RIGHT_JUSTIFY_Y = 50
RIGHT_JUSTIFY_STRING = str(RIGHT_JUSTIFY_X) + "," +  str(RIGHT_JUSTIFY_Y)
os.environ['SDL_VIDEO_WINDOW_POS'] = RIGHT_JUSTIFY_STRING

#sets the variable name for the display
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

# this function will draw guidelines on the screen
def drawGridLines():
    for i in range(100):
        pygame.draw.line(screen, (200,200,200), [0 + i*10, 0], [0 + i*10,800], 1)
        pygame.draw.line(screen, (200,200,200), [0, 0 + i*10], [1000,0 + i*10], 1)
    for i in range(10):
        pygame.draw.line(screen, (100,100,100), [0 + i*100, 0], [0 + i*100,800], 1)
        pygame.draw.line(screen, (100,100,100), [0, 0 + i*100], [1000,0 + i*100], 1)
      
# this function prints the current mouse coordinates on bottom right of screen
def print_coordinates_on_screen():
    fontObj = pygame.font.Font("C:\Windows\Fonts\cour.ttf",15)
    mousex, mousey = pygame.mouse.get_pos()
    mouse_position = "({:3d}, {:3d})".format(mousex,mousey) #converts mouse coords to a formatted string
    timer_text = fontObj.render( mouse_position, True, BLUE, WHITE)
    timer_rect = timer_text.get_rect()
    timer_rect.bottomright = (SCREEN_WIDTH-5, SCREEN_HEIGHT-5) 
    screen.blit(timer_text, timer_rect)


# Set frame rate
FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()


#GAME LOOP VARIABLES
running = True
points = 0
total_points = 0
bottom_box = False
top_box = True
ticks = 0
gameTimer = 18000 #60 * 300 = 18000 for 5 minutes
highScore = 0
safe = True
lives = 10
runs_over_ten = 0

while running and ticks <= gameTimer and lives > 0: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
   
    fpsClock.tick(FPS) # sets the timing of the loop in frames per second
   
    #MOVE THE RED BALL
    keys = pygame.key.get_pressed() #move the red ball with keyboard keys
    if keys[K_w] or keys[K_UP]:
        circle_y -= circle_dy
    if keys[K_a] or keys[K_LEFT]:
        circle_x -= circle_dx
    if keys[K_s] or keys[K_DOWN]:
        circle_y += circle_dy
    if keys[K_d] or keys[K_RIGHT]:
        circle_x += circle_dx
   
    if keys[K_r]:
        ball_x = random.randint(ball_radius, SCREEN_WIDTH - ball_radius)
        ball_y = random.randint(ball_radius, SCREEN_HEIGHT - ball_radius)
    
    #this limits the x and y coordinates of the red circle
    circle_x = max(circle_radius, min(circle_x, SCREEN_WIDTH - circle_radius))
    circle_y = max(circle_radius, min(circle_y, SCREEN_WIDTH - circle_radius))
    
    #MOVE THE GREEN BALL
    ball_x += ball_dx
    ball_y += ball_dy
   
    #create random bounces off of the wall
    if ball_x <= ball_radius or ball_x >= SCREEN_WIDTH - ball_radius:
        ball_dx = -ball_dx
        if random.randint(1,2) == 1:
            ball_dy = max( -18, min( ball_dy + random.randint(-6,6),18) )
        else:
            ball_dy = ball_dy
    
    if ball_y <= ball_radius or ball_y >= SCREEN_WIDTH - ball_radius:
        ball_dy = -ball_dy
        if random.randint(1,2) == 1:
            ball_dx = ball_dx
        else:
            ball_dx = max( -18, min( ball_dx + random.randint(-6,6),18) )
   
    #check to see if contact is made between the red circle and green ball
    if math.dist( [ball_x, ball_y], [circle_x, circle_y] ) <= (ball_radius + circle_radius):
        if ( (circle_x <= 100-circle_radius and circle_y <= 100-circle_radius) \
        or (circle_x >= SCREEN_WIDTH-100+circle_radius and circle_y >= SCREEN_HEIGHT-100+circle_radius) \
        or ( circle_x + circle_radius >= safe_x and circle_x - circle_radius <= safe_x + safe_size and circle_y + circle_radius >= safe_y and circle_y - circle_radius <= safe_y + safe_size) ):
            None
        else:
            circle_x = SCREEN_WIDTH - circle_radius #send back to bottom corner
            circle_y = SCREEN_HEIGHT - circle_radius
            points = 0
            ball_radius = 25
            top_box = True
            bottom_box = False
            lives -= 1
            print(points)
    
    #erase previous drawing
    screen.fill((255, 255, 255))  # Fill the background with white
    
    #draw the safety rectangles
    pygame.draw.rect(screen, (255, 255, 167), [0, 0, 100, 100], 0)
    pygame.draw.rect(screen, (255, 255, 167), [SCREEN_WIDTH-100, SCREEN_HEIGHT-100, 100, 100], 0)
    
    #draw the safe house
    if safe == True:
        safe_x = random.randint(5,595-safe_size)
        if safe_x <= 105:
            safe_y = random.randint(105,595-safe_size)
        elif safe_x >= 435:
            safe_y = random.randint(5,495-safe_size)
        safe = False
        #print(safe_x, safe_y)
    safeHouse(screen,safe_x,safe_y)
    
    #draw the new red circle and green ball based on the new coordinates
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    #calculate and display points
    if circle_x <= 100 and circle_y <= 100 and top_box == True: #top left box
        points += 1
        total_points += 1
        top_box = False
        bottom_box = True
        print(points)
        ball_radius += 3
        safe = True
        if points == 10:
            runs_over_ten += 1
        
    if circle_x >= SCREEN_WIDTH-100 and circle_y >= SCREEN_HEIGHT-100 and bottom_box == True: #bottom right box
        points += 1
        total_points += 1
        top_box = True
        bottom_box = False
        print(points)
        ball_radius += 3
        safe = True
        if points == 10:
            runs_over_ten += 1
    
    if points > highScore:
        highScore = points
    
    
    highScoreDisplay(screen,highScore)
    pointDisplay(screen,points)
    gameTimeDisplay(screen,ticks//60, gameTimer//60, lives)
    #print_coordinates_on_screen()
    #update the screen
    #pygame.display.update() 
    pygame.display.flip()   
    
    ticks += 1 # every 60 is one second
    #end of while loop
   
gameOver(screen,highScore, lives, 300-ticks//60, total_points, runs_over_ten)