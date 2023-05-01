import pygame
import Global

def zeroPad(num, target):
    num = str(num)
    return "0" * (target-len(num)) + num

def pointDisplay(screen, points):
    font = pygame.font.SysFont("Arial",50) #choose font
    text = font.render( str(points), True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 50) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen

   
def highScoreDisplay(screen, highScore):
    font = pygame.font.SysFont("Arial",20) #choose font
    text = font.render(  "(Max: " +str(highScore)+ ")", True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 90) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen

def livesDisplay(screen, lives):
    for i in range(lives):
        pygame.draw.rect(screen, Global.RED, ([10+14*i, Global.SCREEN_HEIGHT-25,15,15]), 0)
        pygame.draw.rect(screen, Global.BLACK, ([10+14*i, Global.SCREEN_HEIGHT-25,15,15]), 1)

def gameTimeDisplay(screen, time, gameTime, lives):
    font = pygame.font.SysFont("Arial",20) #choose font

    tMin = time//60
    tSec = time%60

    gTMin = gameTime//60
    gtSec = gameTime%60

    text = font.render("Timer: %s:%s / %s:%s" % (tMin, zeroPad(tSec, 2), gTMin, zeroPad(gtSec, 2)), True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 580) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen

def gameOver(screen, highScore, lives, time_remaining, total_points, runs_over_ten):
    pygame.draw.rect(screen, Global.YELLOW, [0, 0, 600, 600], 0)
    font = pygame.font.SysFont("Arial",80) #choose font
    text = font.render("Game Over", True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 200) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen
    
    #show high score
    font = pygame.font.SysFont("Arial",40) #choose font
    text = font.render("Longest Run: " +str(highScore), True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 300) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen
    
    #show lives
    font = pygame.font.SysFont("Arial",40) #choose font
    text = font.render("Lives Remaining: " +str(lives), True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 350) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen
    
    #time remaining
    font = pygame.font.SysFont("Arial",40) #choose font
    text = font.render("Time Remaining: " +str(time_remaining) + " seconds", True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 400) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen
    pygame.display.update()
    
    #total points
    font = pygame.font.SysFont("Arial",40) #choose font
    text = font.render("Total Points: " +str(total_points), True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 450) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen
    pygame.display.update()
    
    #runs over 10
    font = pygame.font.SysFont("Arial",40) #choose font
    text = font.render("Runs over Ten: " +str(runs_over_ten), True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (300, 500) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen
    pygame.display.update()
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                pygame.quit()
                exit()