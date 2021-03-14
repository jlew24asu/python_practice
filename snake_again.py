# Another plagerize pygame for practice by Jeff

import pygame
import sys
import random

pygame.init()

#orangecolor 

display_width = 800
display_height = 600
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Jeff's Snake Game")
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        print(event)
pygame.display.update()
pygame.quit()
quit()

