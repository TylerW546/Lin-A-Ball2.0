# Set the height and width of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Define some basic colors in RGB format. You can create your own colors if you want more options.
BLACK = (  0,   0,   0)
GRAY =  (150, 150, 150)
WHITE = (255, 255, 255)
RED =   (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE =  (  0,   0, 255)
RED =   (255,   0,   0)
YELLOW = (255, 255, 0)
CYAN =  (  0, 255, 255)
MAGENTA = (255,  0, 255)

#GAME LOOP VARIABLES
running = True
points = 0
total_points = 0
targetBoxOne = True
ticks = 0
startingTime = 18000 #60 * 300 = 18000 for 5 minutes
gameTimer = startingTime 
highScore = 0
lives = 10
runs_over_ten = 0
safe = True