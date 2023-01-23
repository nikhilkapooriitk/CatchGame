import pygame
from pygame.locals import *
from gameBall import GameBall
from playerBall import PlayerBall
from config import *
import random

# Initialize Pygame and create the game window
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Create the player moved ball
player_ball = PlayerBall(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, BALL_SIZE)

# Create the auto moving ball
fraction1, fraction2 = random.choice([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), random.choice([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
game_ball = GameBall(WINDOW_WIDTH*fraction1, WINDOW_HEIGHT*fraction2, BALL_SIZE)

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player_ball.update_position(keys, game_ball)
    game_ball.update_position(player_ball)

    # Check for collision between the two balls
    if (player_ball.x < game_ball.x < player_ball.x + BALL_SIZE and
            player_ball.y < game_ball.y < player_ball.y + BALL_SIZE):
        game_ball.saveData()
        print("You caught the moving ball! You win!")
        running = False

    # Draw the player ball and game ball on the screen
    player_ball.draw(screen)
    game_ball.draw(screen)

    pygame.display.update()
    clock.tick(30)

# Quit Pygame when the game loop ends
pygame.quit()