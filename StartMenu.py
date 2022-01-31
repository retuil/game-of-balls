import pygame
from MyException import *
from Button import Button
from MyGroup import MyGroup
from HelpFunction import HelpFunction


class StartMenu:
    def __init__(self):
        screen = pygame.display.set_mode((800, 800))
        screen.fill((255, 255, 255))
        running = True
        group = MyGroup([10, 10], [10, 10], [100, 100], screen)

        #для создания текста на кнопке необходимо передать аргумент text=('текст', цвет(в формате(n, n, n)), шрифт(объект класса Font)

        font = pygame.font.SysFont('arial', 20)
        button = Button(0, group, color='yellow', text=('первая', (0, 0, 0), font))
        button2 = Button(1, group, image='button.png', color='yellow')
        group.draw(screen)
        pygame.display.flip()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    group.check_any_click(event.pos)
        group.draw(screen)
        pygame.display.flip()

# Добавил:
pygame.init()

a = StartMenu()
