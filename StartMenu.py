import pygame
from MyException import *
from Button import Button
from MyGroup import MyGroup


class StartMenu:
    def __init__(self):
        screen = pygame.display.set_mode((800, 800)).fill((0, 0, 0))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        MyGroup.draw(screen)
