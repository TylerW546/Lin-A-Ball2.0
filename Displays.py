import pygame
from Globals import *

def pointDisplay(screen, points):
    font = pygame.font.SysFont("Arial",50) #choose font
    text = font.render( str(points), True, BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 50) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen

   
def highScoreDisplay(screen, highScore):
    font = pygame.font.SysFont("Arial",20) #choose font
    text = font.render(  "(Max: " +str(highScore)+ ")", True, BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 90) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen


def gameTimeDisplay(screen, time, gameTime, lives):
    font = pygame.font.SysFont("Arial",20) #choose font
    text = font.render("Timer: " +str(time) +" / "+str(gameTime) + " (" + str(lives) + ")", True, BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 580) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen

def gameOver(screen, highScore, lives, time_remaining, total_points, runs_over_ten):
    pygame.draw.rect(screen, YELLOW, [0, 0, 600, 600], 0)
    font = pygame.font.SysFont("Arial",80) #choose font
    text = font.render("Game Over", True, BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 200) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen
    
    #show high score
    font = pygame.font.SysFont("Arial",40) #choose font
    text = font.render("Longest Run: " +str(highScore), True, BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 300) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen
    
    #show lives
    font = pygame.font.SysFont("Arial",40) #choose font
    text = font.render("Lives: " +str(lives), True, BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 350) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen
    
    #time remaining
    font = pygame.font.SysFont("Arial",40) #choose font
    text = font.render("Time Remaining: " +str(time_remaining) + " seconds", True, BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 400) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen
    pygame.display.update()
    
    #total points
    font = pygame.font.SysFont("Arial",40) #choose font
    text = font.render("Total Points: " +str(total_points), True, BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 450) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen
    pygame.display.update()
    
    #runs over 10
    font = pygame.font.SysFont("Arial",40) #choose font
    text = font.render("Runs over Ten: " +str(runs_over_ten), True, BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 500) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen
    pygame.display.update()
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()