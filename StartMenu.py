import pygame
from MyException import *
from Button import Button
from SortedGroup import SortedGroup
from MyGroup import MyGroup
from HelpFunction import HelpFunction


class StartMenu:
    def ChouseLevel(self):
        screen = pygame.display.set_mode((800, 800))
        screen.fill((255, 255, 255))
        running = True
        group = SortedGroup([10, 10], [10, 10], [100, 100], screen)
        enemy_group = MyGroup()

        #для создания текста на кнопке необходимо передать аргумент text=('текст', цвет(в формате(n, n, n)), шрифт(объект класса Font)

        font = pygame.font.SysFont('arial', 20)
        button = Button(0, group, color='yellow', text=('1', (0, 0, 0), font))
        button2 = Button(1, group, color='yellow', text=('2', (0, 0, 0), font))
        button3 = Button(2, group, color='yellow', text=('3', (0, 0, 0), font))
        button4 = Button(3, group, color='yellow', text=('4', (0, 0, 0), font))
        button5 = Button(4, group, color='yellow', text=('5', (0, 0, 0), font))
        button6 = Button(5, group, color='yellow', text=('6', (0, 0, 0), font))
        button7 = Button(6, group, color='yellow', text=('7', (0, 0, 0), font))
        button8 = Button(7, group, color='yellow', text=('8', (0, 0, 0), font))
        button9 = Button(8, group, color='yellow', text=('9', (0, 0, 0), font))
        button10 = Button(9, group, color='yellow', text=('10', (0, 0, 0), font))
        button11 = Button(10, group, color='yellow', text=('11', (0, 0, 0), font))
        button12 = Button(11, enemy_group, color='yellow', pos=(100, 600), size=(600, 100), action=self.a)
        group.draw(screen)
        enemy_group.draw(screen)
        pygame.display.flip()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    group.check_any_click(event.pos)
                    enemy_group.check_any_click(event.pos)
        group.draw(screen)
        pygame.display.flip()


    def a(self):
        print('УРА')


# Добавил:
pygame.init()

a = StartMenu()
a.ChouseLevel()
