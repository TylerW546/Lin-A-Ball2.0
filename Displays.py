import pygame
import Global

def zeroPad(num, target):
    num = str(num)
    return "0" * (target-len(num)) + num

def formatTimeMinSec(secs):
    min = secs//60
    sec = secs%60

    return str(min) + ":" + zeroPad(sec,2)

def pointDisplay(surface, points):
    rect = surface.get_rect()

    font = pygame.font.SysFont("Arial",50) #choose font
    text = font.render( str(points), True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (rect.width/2, 50) #positions bounding box at surface coordinates
    surface.blit(text, text_rect) #writes the text to the surface

   
def highScoreDisplay(surface, highScore):
    rect = surface.get_rect()
    
    font = pygame.font.SysFont("Arial",20) #choose font
    text = font.render(  "(Max: " +str(highScore)+ ")", True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (rect.width/2, 90) #positions bounding box at surface coordinates
    surface.blit(text, text_rect) #writes the text to the surface

def livesDisplay(surface, lives):
    for i in range(lives):
        pygame.draw.rect(surface, Global.RED, ([10+14*i, Global.GAME_HEIGHT-25,15,15]), 0)
        pygame.draw.rect(surface, Global.BLACK, ([10+14*i, Global.GAME_HEIGHT-25,15,15]), 1)

def gameTimeDisplay(surface, time, gameTime):
    rect = surface.get_rect()
    
    font = pygame.font.SysFont("Arial",20) #choose font


    text = font.render("Timer: %s / %s" % (formatTimeMinSec(time), formatTimeMinSec(gameTime)), True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (rect.width/2, rect.height-20) #positions bounding box at surface coordinates
    surface.blit(text, text_rect) #writes the text to the surface

def gameOver(surface, highScore, lives, time_remaining, total_points, runs_over_ten):
    rect = surface.get_rect()
    
    pygame.draw.rect(surface, Global.YELLOW, [0, 0, rect.width, rect.height], 0)

    font = pygame.font.SysFont("Arial",80) #choose font
    text = font.render("Game Over", True, Global.BLACK, None) #text that you want to display
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (rect.width/2, rect.height/4) #positions bounding box at surface coordinates
    surface.blit(text, text_rect) #writes the text to the surface
    
    #show high score
    font = pygame.font.SysFont("Arial",40) #choose font
    text = font.render("Longest Run: " +str(highScore), True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (rect.width/2, rect.height/2) #positions bounding box at surface coordinates
    surface.blit(text, text_rect) #writes the text to the surface
    
    #show lives
    font = pygame.font.SysFont("Arial",40) #choose font
    text = font.render("Lives Remaining: " +str(lives), True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (rect.width/2, rect.height/2+50) #positions bounding box at surface coordinates
    surface.blit(text, text_rect) #writes the text to the surface
    
    #time remaining
    font = pygame.font.SysFont("Arial",40) #choose font
    text = font.render("Time Remaining: " +str(formatTimeMinSec(time_remaining)), True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (rect.width/2, rect.height/2+100) #positions bounding box at surface coordinates
    surface.blit(text, text_rect) #writes the text to the surface
    
    #total points
    font = pygame.font.SysFont("Arial",40) #choose font
    text = font.render("Total Points: " +str(total_points), True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (rect.width/2, rect.height/2+150) #positions bounding box at surface coordinates
    surface.blit(text, text_rect) #writes the text to the surface
    
    #runs over 10
    font = pygame.font.SysFont("Arial",40) #choose font
    text = font.render("Runs over Ten: " +str(runs_over_ten), True, Global.BLACK, None) #text that you want to display
        
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (rect.width/2, rect.height/2+200) #positions bounding box at surface coordinates
    surface.blit(text, text_rect) #writes the text to the surface
    pygame.display.update()
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                pygame.quit()
                exit()