import pygame
from MyException import *
from Button import Button
from MyGroup import MyGroup


class StartMenu:
    def __init__(self):
        screen = pygame.display.set_mode((800, 800))
        screen.fill((255, 255, 255))
        running = True
        group = MyGroup([10, 10], [10, 10], [50, 100])
        button = Button(0, group, color='yellow')
        button = Button(1, group, color='yellow')
        group.draw(screen)
        pygame.display.flip()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        group.draw(screen)
        pygame.display.flip()

a = StartMenu()