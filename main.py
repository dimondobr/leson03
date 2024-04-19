import pygame
import time
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("игра Тир")
icon = pygame.image.load("img/klipartz.com.png")
pygame.display.set_icon(icon)

target_ing = pygame.image.load("img/target.png")
target_width = 72
target_height = 80

target_x = random.randint(0,SCREEN_WIDTH - target_width)
target_y = random.randint( 0, SCREEN_HEIGHT - target_height)

color = "light green"


running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_ing, (target_x, target_y))
    pygame.display.update()

pygame.quit()