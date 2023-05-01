import pygame
import random
import sys

# Define constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 10
FONT_SIZE = 36
FPS = 20

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Set up the clock
clock = pygame.time.Clock()

# Define the Snake class
class Snake:
    def __init__(self):
        self.length = 1
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        self.positions = [(x, y), (x - BLOCK_SIZE, y), (x - (2 * BLOCK_SIZE), y)]
        self.direction = (1, 0)
        self.color = GREEN
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, direction):
        if self.length > 1 and (direction[0] * -1, direction[1] * -1) == self.direction:
            return
        else:
            self.direction = direction

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x * BLOCK_SIZE)), (cur[1] + (y * BLOCK_SIZE)))
        if new[0] < 0 or new[0] >= SCREEN_WIDTH or new[1] < 0 or new[1] >= SCREEN_HEIGHT:
            self.reset()
        elif new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        self.positions = [(x, y), (x - BLOCK_SIZE, y), (x - (2 * BLOCK_SIZE), y)]
        self.direction = (1, 0)
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, self.color, r)

    def handle_keys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.turn((0, -1))
            elif event.key == pygame.K_DOWN:
                self.turn((0, 1))
            elif event.key == pygame.K_LEFT:
                self.turn((-1, 0))
            elif event.key == pygame.K_RIGHT:
                self.turn((1, 0))

    def handle_collisions(self, food):
        if self.get_head_position() == food.position:
            self.length += 1
            self.score += 1
            food.spawn()
        elif self.score > 0 and self.get_head_position() in self.positions[1:]:
            self.reset()

# Define the Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.spawn()

    def spawn(self):
        x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.position = (x, y)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(surface, self.color, r)

# Define the Text class
class Text:
    def __init__(self, text, color, font_size, x, y):
        self.font = pygame.font.SysFont(None, font_size)
        self.text = self.font.render(text, True, color)
        self.rect = self.text.get_rect()
        self.rect.center = (x, y)

    def draw(self, surface):
        surface.blit(self.text, self.rect)

# Set up the game
snake = Snake()
food = Food()
score_text = Text(f'Score: {snake.score}', WHITE, FONT_SIZE, SCREEN_WIDTH / 2, 20)

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            snake.handle_keys(event)

    # Update the game state
    snake.move()
    snake.handle_collisions(food)
    score_text = Text(f'Score: {snake.score}', WHITE, FONT_SIZE, SCREEN_WIDTH / 2, 20)

    # Draw the game
    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)
    score_text.draw(screen)
    pygame.display.update()

    # Wait for the next frame
    clock.tick(FPS)