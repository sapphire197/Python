# Snake Game in Python

A classic Snake Game built using Python and Pygame. This project is structured for professional GitHub maintenance and includes multiple files for modularity.

## Features
- Snake movement and growth
- Food spawning at random locations
- Collision detection with walls and self
- Scoring system
- Game over functionality

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/SnakeGame.git
   ```
2. Navigate to the project directory:
   ```bash
   cd SnakeGame
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the game:
   ```bash
   python src/game.py
   ```

## Project Structure
```
SnakeGame/
├── src/
│   ├── __init__.py
│   ├── game.py
│   ├── snake.py
│   ├── food.py
│   └── config.py
├── assets/
│   ├── apple.png
│   ├── snake_head.png
│   └── snake_body.png
├── tests/
│   ├── test_snake.py
│   ├── test_food.py
│   └── test_game.py
├── README.md
├── requirements.txt
└── LICENSE
```

## Controls
- Arrow Keys: Move the snake
- Quit: Close the game window

## Requirements
- Python 3.7+
- Pygame

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Pull requests are welcome. For significant changes, please open an issue to discuss your ideas first.

---

### **tests/test_snake.py**
Unit tests for the snake module.

```python
import unittest
from src.snake import Snake
from src.config import Config

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.snake = Snake(self.config)

    def test_initial_length(self):
        self.assertEqual(len(self.snake.body), 3)

    def test_move(self):
        initial_head = self.snake.body[0]
        self.snake.move()
        self.assertNotEqual(self.snake.body[0], initial_head)

    def test_grow(self):
        initial_length = len(self.snake.body)
        self.snake.grow()
        self.snake.move()
        self.assertEqual(len(self.snake.body), initial_length + 1)

    def test_collision_with_self(self):
        self.snake.body = [[100, 50], [90, 50], [80, 50], [100, 50]]
        self.assertTrue(self.snake.check_self_collision())
```

### **tests/test_food.py**
Unit tests for the food module.

```python
import unittest
from src.food import Food
from src.snake import Snake
from src.config import Config

class TestFood(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.food = Food(self.config)
        self.snake = Snake(self.config)

    def test_initial_position(self):
        self.assertTrue(0 <= self.food.position[0] < self.config.WIDTH)
        self.assertTrue(0 <= self.food.position[1] < self.config.HEIGHT)

    def test_spawn(self):
        old_position = self.food.position
        self.food.spawn(self.snake.body)
        self.assertNotEqual(self.food.position, old_position)
```

---

### **tests/test_game.py**
Unit tests for the main game logic.

```python
import unittest
from src.game import SnakeGame
from src.config import Config

class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.game = SnakeGame()

    def test_score_initially_zero(self):
        self.assertEqual(self.game.score, 0)

    def test_score_increment(self):
        self.game.score += 1
        self.assertEqual(self.game.score, 1)
```

---

### **assets/**
1. `apple.png`: An image for the food item.
2. `snake_head.png`: An image for the snake's head.
3. `snake_body.png`: An image for the snake's body.

You can create or download these images and place them in the `assets/` directory.

---

### **requirements.txt**
List of required dependencies:
```
pygame==2.5.0
```

---






