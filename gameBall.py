import pygame
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

    def update_position(self, playerBall):
        self.prev_x = self.x
        self.prev_y = self.y

        # get current state
        state = (self.x, self.y)
        state_x, state_y = int(state[0]), int(state[1])

        # exploration-exploitation trade-off
        if random.uniform(0, 1) < self.exploration_rate:
            # explore - choose a random action
            action = random.choice(self.possible_actions)
        else:
            # exploit - choose the action with the highest Q-value
            action = self.possible_actions[np.argmax(self.q_table[state_x][state_y])]


        # update reward of this iteration
        # if collision occur (-1), outside of box(-1), distance increase (1), distance decrease(0.5) 
        next_state = (self.x + action[0], self.y + action[1])
        distance = math.sqrt( (next_state[0] - playerBall.x)**2 + (next_state[1] - playerBall.y)**2 )

        if self.checkCollision(playerBall):
            reward = -3
        elif self.y + self.size > WINDOW_HEIGHT or self.y < 0 or self.x + self.size > WINDOW_WIDTH or self.x < 0:
            reward = -1
        elif distance >= self.prev_distance_to_playerBall:
            reward = 5
        else:
            reward = 0.5

        self.rewards.append(reward)
        self.total_Reward += reward
        self.total_step += 1
        #update Q-value
        self.q_table[state_x][state_y][self.possible_actions.index(action)] = (1 - self.learning_rate) * self.q_table[state_x][state_y][self.possible_actions.index(action)] + self.learning_rate * (reward + self.discount_factor * max(self.q_table[int(next_state[0])][int(next_state[1])]))

        # move the ball
        self.x += action[0]
        self.y += action[1]

        # check if the ball goes outside the window
        if self.x + self.size > WINDOW_WIDTH or self.x < 0:
            self.x -= action[0]
        if self.y + self.size > WINDOW_HEIGHT or self.y < 0:
            self.y -= action[1]

        #update new self.prev_distance_to_playerBall
        self.prev_distance_to_playerBall = distance



    def draw(self, screen):
        # Delete the ball from the previous position
        pygame.draw.rect(screen, (0, 0, 0), (self.prev_x, self.prev_y, self.size, self.size))
        # Draw the ball on the new position
        screen.blit(self.ball, (self.x, self.y))

    def saveData(self):
        #save Q-table
        np.save("q_table.npy",self.q_table)

        #save reward per step of this game
        with open("rewardPerStepPerGame.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.rewards)
        self.rewards.clear()

        #save total reward, total steps and avg reward of this game
        row = [self.total_Reward, self.total_step, self.total_Reward/self.total_step]
        with open("rewardPerGame.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(row)




    def checkCollision(self, playerBall):
        if (playerBall.x < self.x < playerBall.x + BALL_SIZE and
                playerBall.y < self.y < playerBall.y + BALL_SIZE):
            return True
        else:
            return False



