# Another plagerize pygame for practice by Jeff

import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()

orangecolor = (255, 123, 7)
blackcolor = (0, 0, 0)
redcolor = (213, 50, 80)
greencolor = (0, 255, 0)
bluecolor = (50, 153, 213) 

display_width = 800
display_height = 600
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Jeff's Snake Game")
snake_block = 10
snake_speed = 15
snake_list = []

#defines snake structure and position
def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,orangecolor, [x[0], x[1], snake_block, snake_block])

def snakegame():
    game_over = False
    game_end = False
    x1 = display_width / 2
    y1 = display_height / 2

    #when snake moves
    x1_change = 0 
    y1_change = 0


    #defines lenght of snake
    snake_list = []
    lenght_of_snake = 1

    #food element
    foodx = round(random.randrange(0, display_width - snake_block) / 10) * 10
    foody = round(random.randrange(0, display_height - snake_block) / 10) * 10
    
    while not game_over:
        while game_end == True:
            dis.fill(blackcolor)
            font_style = pygame.font.SysFont("comicsansms", 25)
            mesg = font_style.render("You Lost Badly. Want to try again? Press P", True, redcolor)
            dis.blit(mesg, [display_width /6, display_height / 3])

            #display score
            score = lenght_of_snake - 1
            score_font = pygame.font.SysFont("comicsansms", 40)
            value = score_font.render("Your Score: " + str(score), True, greencolor)
            dis.blit(value, [display_width /3, display_height / 5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        snakegame()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_end = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_DOWN:
                    x1_change = snake_block
                    y1_change = 0
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_end = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blackcolor)
        pygame.draw.rect(dis, greencolor, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        #game end senario
        if len(snake_list) > lenght_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_end = True
        snake(snake_block, snake_list)
        pygame.display.update()
        #when snake eats food, lenght up by 1
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10) * 10
            foody = round(random.randrange(0, display_height - snake_block) / 10) * 10
            lenght_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()

snakegame()