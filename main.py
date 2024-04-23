import pygame
import time
import random
pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("игра Тир")
icon = pygame.image.load("img/klipartz.com.png")
pygame.display.set_icon(icon)

target_ing = pygame.image.load("img/target.png")
target_width = 72
target_height = 80
x = 0
target_x = random.randint(0,SCREEN_WIDTH - target_width)
target_y = random.randint( 0, SCREEN_HEIGHT - target_height)

color = "light green"
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

wait_time = 1000  # Время ожидания в миллисекундах (0.5 секунд)
start_time = pygame.time.get_ticks()


running = True
while running:
    screen.fill(color)
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                x +=1
            else:
               time.sleep(0.5)
               target_x = random.randint(0, SCREEN_WIDTH - target_width)
               target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    text_x = font.render(f'попал: {x}', True, (0, 0, 0))
    screen.blit(text_x, (50, 50))


    screen.blit(target_ing, (target_x, target_y))
    pygame.display.update()

pygame.quit()