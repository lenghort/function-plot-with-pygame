import pygame
import math
import random
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.info("Program started")

def f(x):
    return x ** 2

pygame.init()

w = 600
h = 600

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Draw graph")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((0, 0, 0))

    for x in range(-200, 201):  
        scaled_x = x / 100
        y = f(scaled_x)
        screen_x = int(w / 2 + x)
        screen_y = int(h / 2 - y * 100)
        if 0 <= screen_x < w and 0 <= screen_y < h:
            screen.set_at((screen_x, screen_y), (0, 255, 0))

    pygame.display.flip()

pygame.quit()