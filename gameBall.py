import pygame
import random
import math
from config import *

class GameBall:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.speed = BALL_SPEED
        self.prev_x = self.x
        self.prev_y = self.y
        self.ball = pygame.Surface((size, size))
        self.ball.fill((0, 255, 0))

    def update_position(self, playerBall):
        # Save the previous position
        self.prev_x = self.x
        self.prev_y = self.y

        perpendicularVector = [-playerBall.y + self.y , playerBall.x - self.x ]
        modOfVector = math.sqrt(perpendicularVector[0]*perpendicularVector[0] + perpendicularVector[1]*perpendicularVector[1])

        step1 = random.uniform(-BALL_SPEED,BALL_SPEED)
        step2 = math.sqrt(BALL_SPEED - abs(step1))
        self.x += BALL_SPEED * perpendicularVector[0]/modOfVector
        self.y += BALL_SPEED * perpendicularVector[1]/modOfVector

        # Check if the ball goes outside the window and change direction
        if self.x + self.size > WINDOW_WIDTH or self.x < 0:
            self.speed = -self.speed
        if self.y + self.size > WINDOW_HEIGHT or self.y < 0:
            self.speed = -self.speed

    def draw(self, screen):
        # Delete the ball from the previous position
        pygame.draw.rect(screen, (0, 0, 0), (self.prev_x, self.prev_y, self.size, self.size))
        # Draw the ball on the new position
        screen.blit(self.ball, (self.x, self.y))
