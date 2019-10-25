import pygame
import random
 
WIDTH = 360
HEIGHT = 480
FPS = 30
 
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
 
# Initialize pygame and create window
pygame.init()

# (Initialize sound). Doesnt work... I don't know why.
#pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
 
 
# Game loop
running = True
while running:
    # Frames per secound (FPS)
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closeing the window
        if event.type == pygame.QUIT:
            running = False
 
   
 
    # Update
 
 
 
    # Draw / Render
    screen.fill(BLACK)
    # after drawing everything you can flip the display!!!!!
    pygame.display.flip()
 
 
pygame.quit()
