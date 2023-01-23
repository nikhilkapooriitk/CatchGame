import pygame
from pygame.locals import *
import random
import math
from config import *
import numpy as np
import csv

class GameBall:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.speed = BALL_SPEED
        self.prev_distance_to_playerBall = 0
        self.prev_x = self.x
        self.prev_y = self.y
        self.ball = pygame.Surface((size, size))
        self.ball.fill((0, 255, 0))

        self.rewards = []
        self.total_Reward = 0
        self.total_step = 0
        self.possible_actions = [(BALL_SPEED, 0), (-BALL_SPEED, 0), (0, BALL_SPEED), (0, -BALL_SPEED)] #up,down,left,right
        self.state_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        # self.q_table = np.random.uniform(0, 0.1, (self.state_size[0], self.state_size[1], len(self.possible_actions)))
        
        # Loading the Q-table from a file
        self.q_table = np.load("q_table.npy")
        self.learning_rate = 0.8
        self.discount_factor = 0.95
        self.exploration_rate = 0.1


    def update_position(self, keys, playerBall):
        #update previous position
        self.prev_x = self.x
        self.prev_y = self.y

        #move the ball
        if keys[K_a]:
            self.x -= BALL_SPEED
        if keys[K_d]:
            self.x += BALL_SPEED
        if keys[K_w]:
            self.y -= BALL_SPEED
        if keys[K_s]:
            self.y += BALL_SPEED


    def draw(self, screen):
        # Delete the ball from the previous position
        pygame.draw.rect(screen, (0, 0, 0), (self.prev_x, self.prev_y, self.size, self.size))
        # Draw the ball on the new position
        screen.blit(self.ball, (self.x, self.y))
        

    def checkCollision(self, playerBall):
        if (playerBall.x < self.x < playerBall.x + BALL_SIZE and
                playerBall.y < self.y < playerBall.y + BALL_SIZE):
            return True
        else:
            return False



