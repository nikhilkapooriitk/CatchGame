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
        #update previous position
        self.prev_y = self.y
        self.prev_x = self.x

        #move the ball        
        if keys[K_LEFT]:
            self.x -= BALL_SPEED
        if keys[K_RIGHT]:
            self.x += BALL_SPEED
        if keys[K_UP]:
            self.y -= BALL_SPEED
        if keys[K_DOWN]:
            self.y += BALL_SPEED

    def draw(self, screen):
        # Delete the ball from the previous position
        pygame.draw.rect(screen, (0, 0, 0), (self.prev_x, self.prev_y, self.size, self.size))
        # Draw the ball on the new position
        screen.blit(self.ball, (self.x, self.y))
