import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEISHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEISHT))

pygame.display.set_caption("игра Тир")
icon = pygame.image.load("img/klipartz.com.png")
pygame.display.set_icon(icon)

target_ing = pygame.image.load("img/target.png")
target_width = 72
target_height = 80

target_x = random.randint(0,SCREEN_WIDTH - target_width)
target_y = random.randint( 0, SCREEN_HEISHT - target_height)

color = "light green"


running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x - target_width and target_y < mouse_y < target_y - target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEISHT - target_height)
    screen.blit(target_ing, (target_x, target_y))
    pygame.display.update()

pygame.quit()