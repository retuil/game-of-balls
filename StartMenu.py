import pygame
from MyException import *
from Button import Button
from MyGroup import MyGroup


class StartMenu:
    def __init__(self):
        screen = pygame.display.set_mode((800, 800))
        screen.fill((255, 255, 255))
        running = True
        group = MyGroup()
        button = Button(0, group, size=[50, 100], pos=[10, 10], color='yellow', screen=screen)
        group.draw(screen)
        pygame.display.flip()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        group.draw(screen)
        pygame.display.flip()

a = StartMenu()