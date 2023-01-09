# Import the necessary Pygame modules in your Python script
import sys
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the display window and clock
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing DVD Logo")
clock = pygame.time.Clock()

# Load the DVD logo image and create a Pygame surface for it
logo_image = pygame.image.load("logo-blue.png")
logo_rect = logo_image.get_rect()

# Set the initial position and velocity of the logo
logo_rect.x = screen_width / 2
logo_rect.y = screen_height / 2
velocity = [1, 1]

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    # Update the position of the logo
    logo_rect.x += velocity[0]
    logo_rect.y += velocity[1]

    # Check if the logo has hit the edge of the window
    if logo_rect.left < 0:
        velocity[0] = -velocity[0]
        logo_image = pygame.image.load("logo-blue.png")
    if logo_rect.right > screen_width:
        velocity[0] = -velocity[0]
        logo_image = pygame.image.load("logo-green.png")
    if logo_rect.top < 0:
        velocity[1] = -velocity[1]
        logo_image = pygame.image.load("logo-red.png")
    if logo_rect.bottom > screen_height:
        velocity[1] = -velocity[1]
        logo_image = pygame.image.load("logo-yellow.png")


    # Clear the screen and draw the logo
    screen.fill((255, 255, 255))
    screen.blit(logo_image, logo_rect)


    # Update the display and wait for next frame
    pygame.display.flip()
    clock.tick(60)
