import pygame
from pygame.locals import *

# Initialize Pygame and create the game window
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Create the stationary and moving balls
stationary_ball = pygame.Surface((50, 50))
moving_ball = pygame.Surface((50, 50))

stationary_ball.fill((255, 0, 0))
moving_ball.fill((0, 255, 0))

# Set the initial positions of the balls on the screen
stationary_ball_pos = (width/2, height/2)
moving_ball_pos = (width/2, 50)

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Move the moving ball in a random direction
    moving_ball_pos = (moving_ball_pos[0] + 5, moving_ball_pos[1] + 5)

    # Check for collision between the two balls
    if (stationary_ball_pos[0] < moving_ball_pos[0] < stationary_ball_pos[0] + 50 and
            stationary_ball_pos[1] < moving_ball_pos[1] < stationary_ball_pos[1] + 50):
        print("You caught the moving ball! You win!")
        running = False

    # Update the positions of the balls on the screen
    screen.blit(stationary_ball, stationary_ball_pos)
    screen.blit(moving_ball, moving_ball_pos)
    pygame.display.update()
    clock.tick(30)

# Quit Pygame when the game loop ends
pygame.quit()
