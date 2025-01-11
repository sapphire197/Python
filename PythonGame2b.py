# src/board.py

# Handles board initialization and movement logic.

import random
from src.config import Config

class Board:
    def __init__(self):
        self.grid = [[0] * Config.GRID_SIZE for _ in range(Config.GRID_SIZE)]
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        empty_cells = [(r, c) for r in range(Config.GRID_SIZE) for c in range(Config.GRID_SIZE) if self.grid[r][c] == 0]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.grid[r][c] = 2 if random.random() < 0.9 else 4

    def slide_and_merge(self, direction):
        def slide(row):
            row = [tile for tile in row if tile != 0]
            for i in range(len(row) - 1):
                if row[i] == row[i + 1]:
                    row[i] *= 2
                    row[i + 1] = 0
            return [tile for tile in row if tile != 0]

        rotated = False
        if direction in ["up", "down"]:
            self.grid = list(map(list, zip(*self.grid)))
            rotated = True
        if direction in ["right", "down"]:
            self.grid = [row[::-1] for row in self.grid]

        self.grid = [slide(row) + [0] * (Config.GRID_SIZE - len(slide(row))) for row in self.grid]

        if direction in ["right", "down"]:
            self.grid = [row[::-1] for row in self.grid]
        if rotated:
            self.grid = list(map(list, zip(*self.grid)))

    def is_game_over(self):
        if any(0 in row for row in self.grid):
            return False
        for r in range(Config.GRID_SIZE):
            for c in range(Config.GRID_SIZE - 1):
                if self.grid[r][c] == self.grid[r][c + 1] or self.grid[c][r] == self.grid[c + 1][r]:
                    return False
        return True

