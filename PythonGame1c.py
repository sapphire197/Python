# src/food.py

# Handles the food's behavior.

import pygame
import random

class Food:
    def __init__(self, config):
        self.config = config
        self.position = [random.randint(0, (self.config.WIDTH // self.config.BLOCK_SIZE) - 1) * self.config.BLOCK_SIZE,
                         random.randint(0, (self.config.HEIGHT // self.config.BLOCK_SIZE) - 1) * self.config.BLOCK_SIZE]

    def spawn(self, snake_body):
        while True:
            new_position = [random.randint(0, (self.config.WIDTH // self.config.BLOCK_SIZE) - 1) * self.config.BLOCK_SIZE,
                            random.randint(0, (self.config.HEIGHT // self.config.BLOCK_SIZE) - 1) * self.config.BLOCK_SIZE]
            if new_position not in snake_body:
                self.position = new_position
                break

    def draw(self, screen):
        pygame.draw.rect(screen, self.config.FOOD_COLOR, (*self.position, self.config.BLOCK_SIZE, self.config.BLOCK_SIZE))
