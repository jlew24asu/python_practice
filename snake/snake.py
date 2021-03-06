# thanks again to Clear Code https://www.youtube.com/watch?v=QFvqStqPCRU

import pygame
import sys
from pygame.math import Vector2
import random

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            pygame.draw.rect(screen, (183,191,122), block_rect)

class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (126,166,114), fruit_rect)


cell_size = 40
cell_number = 20

pygame.init()
screen = pygame.display.set_mode((cell_number * cell_size, cell_size * cell_number))
clock = pygame.time.Clock()

fruit = FRUIT()
snake = SNAKE()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175,111,70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)

