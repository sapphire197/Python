# src/snake.py

# Handles the snake's behavior.

import pygame

class Snake:
    def __init__(self, config):
        self.config = config
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
        self.grow_flag = False

    def move(self):
        head = self.body[0]
        if self.direction == "UP":
            new_head = [head[0], head[1] - self.config.BLOCK_SIZE]
        elif self.direction == "DOWN":
            new_head = [head[0], head[1] + self.config.BLOCK_SIZE]
        elif self.direction == "LEFT":
            new_head = [head[0] - self.config.BLOCK_SIZE, head[1]]
        elif self.direction == "RIGHT":
            new_head = [head[0] + self.config.BLOCK_SIZE, head[1]]
        self.body.insert(0, new_head)
        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False

    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != "DOWN":
            self.direction = "UP"
        elif key == pygame.K_DOWN and self.direction != "UP":
            self.direction = "DOWN"
        elif key == pygame.K_LEFT and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif key == pygame.K_RIGHT and self.direction != "LEFT":
            self.direction = "RIGHT"

    def grow(self):
        self.grow_flag = True

    def check_collision_with_walls(self):
        head = self.body[0]
        return (head[0] < 0 or head[1] < 0 or 
                head[0] >= self.config.WIDTH or head[1] >= self.config.HEIGHT)

    def check_self_collision(self):
        head = self.body[0]
        return head in self.body[1:]

    def check_collision_with_food(self, food):
        return self.body[0] == food.position

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, self.config.SNAKE_COLOR, (*segment, self.config.BLOCK_SIZE, self.config.BLOCK_SIZE))
