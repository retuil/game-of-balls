import pygame
from Button import Button
from SortedGroup import SortedGroup
from MyGroup import MyGroup

from game_file.board import Board
from game_file.level import open_level_file

def start_event():
    global screen, width, height
    screen.fill((0, 0, 0))
    running = True
    enemy_group1 = MyGroup()
    font1 = pygame.font.SysFont('arial', 40)
    text1 = font1.render("Welcome to", True, (119, 221, 119))
    text_x1 = width // 2 - text1.get_width() // 2
    text_y1 = height // 5 - text1.get_height() * 1.5
    screen.blit(text1, (text_x1, text_y1))
    font2 = pygame.font.SysFont('arial', 90)
    text2 = font2.render("GAME OF BALL", True, (66, 255, 0))
    text_x2 = width // 2 - text2.get_width() // 2
    text_y2 = height // 3 - text1.get_height() * 2
    screen.blit(text2, (text_x2, text_y2))
    b_width = width - 28
    b_height = height // 8
    start_button = Button(0, enemy_group1, color=(0, 165, 80), pos=(width // 2 - b_width // 2, height // 1.264),
                          size=(b_width, b_height),
                          action=choice_mod_event,
                          text=('Начать', (0, 0, 0), pygame.font.SysFont('arial', 40)))
    enemy_group1.draw(screen)
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                click = enemy_group1.check_any_click(event.pos)
                if click[0]:
                    if click[1] is not None:
                        click[1]()
                    running = False
                    break


def in_developing():
    global screen, width, height
    running = True
    clock = pygame.time.Clock()
    screen2 = pygame.Surface(screen.get_size())
    screen2.blit(screen, (0, 0))
    font = pygame.font.SysFont('arial', 90)
    text = font.render("В разработке", True, (248, 0, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10, text.get_width() + 20, text.get_height() + 20))
    screen.blit(text, (text_x, text_y))
    pygame.display.flip()
    time = 0
    while running:
        time += clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False
        if time >= 1000:
            running = False
            screen.fill((0, 0, 0))
            screen.blit(screen2, (0, 0))
            pygame.display.flip()
            return True



def choice_mod_event():
    global screen, width, height
    screen.fill((0, 0, 0))
    running = True
    font = pygame.font.SysFont('arial', height // 15)
    group = SortedGroup((0, height // 10), (width // 27.5, height // 4.7), (width - 50, height // 8), screen)
    button_p = Button(0, group, text=('Продолжить игру', (0, 0, 0), font), color=(0, 165, 80),
                      action=in_developing)
    button_s = Button(1, group, text=('Начать новую игру', (0, 0, 0), font), color=(0, 165, 80),
                      action=choice_level_event)
    button_t = Button(2, group, text=('Рекорды', (0, 0, 0), font), color=(0, 165, 80),
                      action=in_developing)
    group.draw(screen)
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                click = group.check_any_click(event.pos)
                if click[0]:
                    running = False
                    if click[1] is not None:
                        if click[1]():
                            running = True
                    break


def choice_level_event():
    global screen, width, height
    screen.fill((0, 0, 0))
    running = True
    group = SortedGroup([width // 30, height // 80], [width // 55, height // 6.6], [width // 6, height // 8.8], screen)
    enemy_group = MyGroup()

    font = pygame.font.SysFont('arial', 40)
    text = font.render("Выберите уровень", True, (100, 255, 100))
    text_x = 550 // 2 - text.get_width() // 2
    text_y = height // 22
    screen.blit(text, (text_x, text_y))

    # для создания текста на кнопке необходимо передать аргумент
    # text=('текст', цвет(в формате(n, n, n)), шрифт(объект класса Font)

    font = pygame.font.SysFont('arial', 20)
    button = Button(0, group, color='yellow', text=('1', (0, 0, 0), font), action=in_developing)
    button2 = Button(1, group, color='yellow', text=('2', (0, 0, 0), font), action=in_developing)
    button3 = Button(2, group, color='yellow', text=('3', (0, 0, 0), font), action=in_developing)
    button4 = Button(3, group, color='yellow', text=('4', (0, 0, 0), font), action=in_developing)
    button5 = Button(4, group, color='yellow', text=('5', (0, 0, 0), font), action=in_developing)
    button6 = Button(5, group, color='yellow', text=('6', (0, 0, 0), font), action=in_developing)
    button7 = Button(6, group, color='yellow', text=('7', (0, 0, 0), font), action=in_developing)
    button8 = Button(7, group, color='yellow', text=('8', (0, 0, 0), font), action=in_developing)
    button9 = Button(8, group, color='yellow', text=('9', (0, 0, 0), font), action=in_developing)
    button10 = Button(9, group, color='yellow', text=('10', (0, 0, 0), font), action=in_developing)
    button11 = Button(10, group, color='yellow', text=('11', (0, 0, 0), font), action=in_developing)
    button12 = Button(11, group, color='yellow', text=('12', (0, 0, 0), font), action=in_developing)
    button13 = Button(12, group, color='yellow', text=('13', (0, 0, 0), font), action=in_developing)
    button14 = Button(13, group, color='yellow', text=('14', (0, 0, 0), font), action=in_developing)
    button15 = Button(14, group, color='yellow', text=('15', (0, 0, 0), font), action=in_developing)
    button16 = Button(15, group, color='yellow', text=('16', (0, 0, 0), font), action=in_developing)
    button17 = Button(16, group, color='yellow', text=('17', (0, 0, 0), font), action=in_developing)
    button18 = Button(17, group, color='yellow', text=('18', (0, 0, 0), font), action=in_developing)
    button19 = Button(18, group, color='yellow', text=('19', (0, 0, 0), font), action=in_developing)
    button20 = Button(19, group, color='yellow', text=('20', (0, 0, 0), font), action=in_developing)
    button21 = Button(20, group, color='yellow', text=('21', (0, 0, 0), font), action=in_developing)
    button22 = Button(21, group, color='yellow', text=('22', (0, 0, 0), font), action=in_developing)
    button23 = Button(22, group, color='yellow', text=('23', (0, 0, 0), font), action=in_developing)
    button24 = Button(23, group, color='yellow', text=('24', (0, 0, 0), font), action=in_developing)
    button25 = Button(24, group, color='yellow', text=('25', (0, 0, 0), font), action=in_developing)
    buttonI = Button(0, enemy_group, color=(11, 218, 81), pos=(width // 55, height // 1.21),
                     size=(width - width // 24, height // 8), action=game_event,
                     text=('Бесконечный режим', (0, 0, 0), pygame.font.SysFont('arial', 20)))
    group.draw(screen)
    enemy_group.draw(screen)
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                click1 = group.check_any_click(event.pos)
                click2 = enemy_group.check_any_click(event.pos)
                if click1[0]:
                    running = False
                    if click1[1] is not None:
                        if click1[1]():
                            running = True
                    break
                elif click2[0]:
                    running = False
                    if click2[1] is not None:
                        if click2[1]():
                            running = True
                    break


def game_event(level=None):
    global screen, width, height
    level = open_level_file(level)
    board = Board((7, 11), (100, 100), 50, screen, 5, level)
    running = True
    draw, aim_coord = None, None
    r = (False, None)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board.check():
                    draw = 1
                    aim_coord = event.pos
            if event.type == pygame.MOUSEMOTION and draw == 1:
                if board.check():
                    aim_coord = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                if board.check():
                    draw = 2
                    if not board.count_balls:
                        board.count_balls_ += 1
                    board.motion(*event.pos)
        r = board.render(draw, aim_coord)
        if r[0]:
            break
        pygame.display.flip()
    if r[0]:
        # r[1] - значение для таблицы рекордов
        start_event()

#
# def start_event():
#     global screen, width, height
#     running = True
#     game = False
#     screen.fill((0, 0, 0))
#     font = pygame.font.Font(None, 50)
#     text = font.render(f'Нажмите для старта', True, pygame.Color('white'))
#     text_x = width // 2 - text.get_width() // 2
#     text_y = height // 2 - text.get_height() // 2
#     text_w = text.get_width()
#     text_h = text.get_height()
#     screen.blit(text, (text_x, text_y))
#     pygame.draw.rect(screen, pygame.Color('white'), (text_x - 10, text_y - 10,
#                                                      text_w + 20, text_h + 20), 1)
#
#     pygame.display.flip()
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONUP:
#                 x, y = event.pos
#                 if (x > text_x - 10) and (x < text_x + text_w + 10) and \
#                         (y > text_y - 10) and (y < text_y + text_h + 10):
#                     game = True
#                     break
#         if game:
#             break
#     if game:
#         game_event()


def end_event():
    global screen, width, height
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def main():
    start_event()
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 550, 800
    screen = pygame.display.set_mode(size)
    main()
