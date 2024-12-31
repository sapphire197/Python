# src/game.py

# Handles the main game logic.

import pygame
import sys
from src.snake import Snake
from src.food import Food
from src.config import Config

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.config = Config()
        self.screen = pygame.display.set_mode((self.config.WIDTH, self.config.HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.config)
        self.food = Food(self.config)
        self.score = 0

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.config.FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.snake.change_direction(event.key)

    def update(self):
        self.snake.move()
        if self.snake.check_collision_with_walls() or self.snake.check_self_collision():
            print(f"Game Over! Final Score: {self.score}")
            pygame.quit()
            sys.exit()
        if self.snake.check_collision_with_food(self.food):
            self.score += 1
            self.snake.grow()
            self.food.spawn(self.snake.body)

    def render(self):
        self.screen.fill(self.config.BACKGROUND_COLOR)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.draw_score()
        pygame.display.flip()

    def draw_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, self.config.TEXT_COLOR)
        self.screen.blit(score_text, (10, 10))

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
