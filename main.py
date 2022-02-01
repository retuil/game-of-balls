import pygame
from MyException import *
from Button import Button
from SortedGroup import SortedGroup
from MyGroup import MyGroup
from HelpFunction import HelpFunction


class StartProgram:
    def __init__(self):
        self.StartScreen()

    def StartScreen(self):
        screen = pygame.display.set_mode((550, 800))
        screen.fill((0, 0, 0))
        running = True
        enemy_group1 = MyGroup()
        font1 = pygame.font.SysFont('arial', 40)
        text1 = font1.render("Welcome to", True, (119, 221, 119))
        text_x1 = 550 // 2 - text1.get_width() // 2
        text_y1 = 100
        screen.blit(text1, (text_x1, text_y1))
        font2 = pygame.font.SysFont('arial', 90)
        text2 = font2.render("GAME OF BALL", True, (66, 255, 0))
        text_x2 = 550 // 2 - text2.get_width() // 2
        text_y2 = 160
        screen.blit(text2, (text_x2, text_y2))
        start_button = Button(0, enemy_group1, color=(0, 165, 80), pos=(10, 660), size=(530, 100), action=self.ChouseLevel,
                         text=('Начать', (0, 0, 0), pygame.font.SysFont('arial', 40)))
        enemy_group1.draw(screen)
        pygame.display.flip()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    enemy_group1.check_any_click(event.pos)
        pygame.display.flip()

    def ChouseLevel(self):
        screen = pygame.display.set_mode((550, 800))
        screen.fill((0, 0, 0))
        running = True
        group = SortedGroup([10, 10], [10, 120], [90, 90], screen)
        enemy_group = MyGroup()

        font = pygame.font.SysFont('arial', 40)
        text = font.render("Выберите уровень", True, (100, 255, 100))
        text_x = 550 // 2 - text.get_width() // 2
        text_y = 25
        screen.blit(text, (text_x, text_y))


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
        button12 = Button(11, group, color='yellow', text=('12', (0, 0, 0), font))
        button13 = Button(12, group, color='yellow', text=('13', (0, 0, 0), font))
        button14 = Button(13, group, color='yellow', text=('14', (0, 0, 0), font))
        button15 = Button(14, group, color='yellow', text=('15', (0, 0, 0), font))
        button16 = Button(15, group, color='yellow', text=('16', (0, 0, 0), font))
        button17 = Button(16, group, color='yellow', text=('17', (0, 0, 0), font))
        button18 = Button(17, group, color='yellow', text=('18', (0, 0, 0), font))
        button19 = Button(18, group, color='yellow', text=('19', (0, 0, 0), font))
        button20 = Button(19, group, color='yellow', text=('20', (0, 0, 0), font))
        button21 = Button(20, group, color='yellow', text=('21', (0, 0, 0), font))
        button22 = Button(21, group, color='yellow', text=('22', (0, 0, 0), font))
        button23 = Button(22, group, color='yellow', text=('23', (0, 0, 0), font))
        button24 = Button(23, group, color='yellow', text=('24', (0, 0, 0), font))
        button25 = Button(24, group, color='yellow', text=('25', (0, 0, 0), font))
        buttonI = Button(0, enemy_group, color=(11, 218, 81), pos=(10, 660), size=(530, 100), action=self.a,
                         text=('Бесконечный режим', (0, 0, 0), pygame.font.SysFont('arial', 20)))
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
StartProgram()
