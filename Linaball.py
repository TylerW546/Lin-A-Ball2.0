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
 
import Global
from Displays import *
from Areas import *
from Enemy import *
from Player import *

# Initialize the game engine
pygame.init()

#this code will right justify the screen in the top right
RIGHT_JUSTIFY_X = 1920 - Global.SCREEN_WIDTH - 50 #1600 for laptop, 1920 for desktop
RIGHT_JUSTIFY_Y = 50
RIGHT_JUSTIFY_STRING = str(RIGHT_JUSTIFY_X) + "," +  str(RIGHT_JUSTIFY_Y)
os.environ['SDL_VIDEO_WINDOW_POS'] = RIGHT_JUSTIFY_STRING

#sets the variable name for the display
screen = pygame.display.set_mode( (Global.SCREEN_WIDTH, Global.SCREEN_HEIGHT))
gameWindow = pygame.surface.Surface((Global.GAME_WIDTH, Global.GAME_HEIGHT))

# Set frame rate
FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# Initialize objects
house = House()
enemy = Enemy()
player = Player()

while Global.running and Global.ticks <= Global.gameTimer and Global.lives > 0: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if (event.type == KEYDOWN and event.key==K_ESCAPE):
            gameOver(screen,Global.highScore, Global.lives, Global.startingTime//60-Global.ticks//60, Global.total_points, Global.runs_over_ten)
   
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
            player.x = Global.GAME_WIDTH - player.radius #send back to bottom corner
            player.y = Global.GAME_HEIGHT - player.radius
            Global.points = 0
            enemy.radius = 25
            
            Global.targetBoxOne = True
            
            Global.lives -= 1
            print(Global.points)


    #erase previous drawing
    gameWindow.fill((255, 255, 255))  # Fill the background with white
    
    #draw the safety rectangles
    zone1.draw(gameWindow)
    zone2.draw(gameWindow)
    
    #move the safe house
    if Global.safe == True:
        house.move()
        Global.safe = False
    house.draw(gameWindow)
    
    #draw the new red circle and green ball based on the new coordinates
    player.draw(gameWindow)
    enemy.draw(gameWindow)

    #calculate and display points
    if True in [zone1.playerIn, zone2.playerIn] and zone1.playerIn == Global.targetBoxOne: #top left box
        Global.points += 1
        Global.total_points += 1

        Global.targetBoxOne = not(Global.targetBoxOne)

        enemy.radius += 3
        Global.safe = True
        if Global.points == 10:
            Global.runs_over_ten += 1

    Global.highScore = max(Global.points, Global.highScore)
    
    highScoreDisplay(gameWindow,Global.highScore)
    pointDisplay(gameWindow,Global.points)
    livesDisplay(gameWindow, Global.lives)
    gameTimeDisplay(gameWindow,Global.ticks//60, Global.gameTimer//60)

    screen.blit(gameWindow, (Global.BORDER_WIDTH, Global.BORDER_HEIGHT))

    pygame.display.flip()   
    
    Global.ticks += 1 # every 60 is one second
    #end of while loop
   
gameOver(screen,Global.highScore, Global.lives, Global.startingTime//60-Global.ticks//60, Global.total_points, Global.runs_over_ten)