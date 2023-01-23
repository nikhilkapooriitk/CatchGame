import pygame
from config import *
from pygame.locals import *
import math

class PlayerBall:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.speed = BALL_SPEED
        self.prev_x = self.x
        self.prev_y = self.y
        self.ball = pygame.Surface((size, size))
        self.ball.fill((255, 0, 0))

    def update_position(self, keys, GameBall):
        # Save the previous position
        self.prev_x = self.x
        self.prev_y = self.y

        #getting direction
        x_dir, y_dir = GameBall.x - self.x , GameBall.y - self.y
        dir_mod = math.sqrt(x_dir*x_dir + y_dir*y_dir)

        self.x += (BALL_SPEED-1)*x_dir/dir_mod 
        self.y += (BALL_SPEED-1)*y_dir/dir_mod

    def draw(self, screen):
        # Delete the ball from the previous position
        pygame.draw.rect(screen, (0, 0, 0), (self.prev_x, self.prev_y, self.size, self.size))
        # Draw the ball on the new position
        screen.blit(self.ball, (self.x, self.y))
