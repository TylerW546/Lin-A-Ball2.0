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

# Set frame rate
FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# Initialize objects
house = House()
enemy = Enemy()
player = Player()

while running and ticks <= gameTimer and lives > 0: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if (event.type == KEYDOWN and event.key==K_ESCAPE):
            gameOver(screen,highScore, lives, startingTime//60-ticks//60, total_points, runs_over_ten)
   
    fpsClock.tick(FPS) # sets the timing of the loop in frames per second
    keys = pygame.key.get_pressed() #move the red ball with keyboard keys

    #MOVE THE RED BALL
    player.move(keys)

    enemy.move()
    enemy.bounce()

    player.testHouseSafety()
    player.testZoneSafety()
    player.testEnemySafety()

   
    #check to see if contact is made between the red circle and green ball
    if player.inEnemy:
        if (player.inZone or player.inHouse):
            None
        else:
            player.x = SCREEN_WIDTH - player.radius #send back to bottom corner
            player.y = SCREEN_HEIGHT - player.radius
            points = 0
            enemy.radius = 25
            
            targetBoxOne = True
            
            lives -= 1
            print(points)


    #erase previous drawing
    screen.fill((255, 255, 255))  # Fill the background with white
    
    #draw the safety rectangles
    zone1.draw(screen)
    zone2.draw(screen)
    
    #move the safe house
    if safe == True:
        house.move()
        safe = False
    house.draw(screen)
    
    #draw the new red circle and green ball based on the new coordinates
    player.draw(screen)
    enemy.draw(screen)

    #calculate and display points
    if player.inZone and zone1.playerIn == targetBoxOne: #top left box
        points += 1
        total_points += 1

        targetBoxOne = not(targetBoxOne)

        enemy.radius += 3
        safe = True
        if points == 10:
            runs_over_ten += 1

    if points > highScore:
        highScore = points
    
    highScoreDisplay(screen,highScore)
    pointDisplay(screen,points)
    livesDisplay(screen, lives)
    gameTimeDisplay(screen,ticks//60, gameTimer//60, lives)

    pygame.display.flip()   
    
    ticks += 1 # every 60 is one second
    #end of while loop
   
gameOver(screen,highScore, lives, startingTime//60-ticks//60, total_points, runs_over_ten)