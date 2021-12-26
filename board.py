from math import sqrt

import pygame

from border import Border
from box import Box


def create_lvl(board, level):
    if level is not None:
        for i, s in enumerate(level):
            board.level.append([])
            for j, el in enumerate(s.rstrip().split(',')):
                if el == '.':
                    board.level[-1].append(None)
                else:
                    q = Box(j, i + 3 - len(level), board, int(el))
                    board.level[-1].append(q)
                    board.box_sprites.add(q)
        for i, el in enumerate(board.level[-1]):
            if el is not None:
                board.v_box_sprites.add(el)
                board.all_sprites.add(el)
                board.box_list.append(el)

            board.board[2][i] = el


class Board:
    def __init__(self, width, height, lvl=None, debug=False):
        self.width = width
        self.height = height

        self.left = 50
        self.top = 50
        self.cell_size = 50

        self.debug = debug

        self.balls = []
        self.all_sprites = pygame.sprite.Group()
        self.balls_sprites = pygame.sprite.Group()
        self.box_sprites = pygame.sprite.Group()
        self.v_box_sprites = pygame.sprite.Group()
        self.box_list = []
        self.up_horizontal_borders = pygame.sprite.Group()
        self.down_horizontal_borders = pygame.sprite.Group()
        self.vertical_borders = pygame.sprite.Group()
        self.borders = pygame.sprite.Group()

        self.level = []
        self.board = [[None] * self.width for _ in range(self.height)]
        self.u = 2
        create_lvl(self, lvl)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

        Border(self.left, self.top, self.left + self.width * self.cell_size, self.top, self)
        Border(self.left, self.top + self.height * self.cell_size, self.left + self.width * self.cell_size,
               self.top + self.height * self.cell_size, self)
        Border(self.left, self.top, self.left, self.top + self.height * self.cell_size, self)
        Border(self.left + self.width * self.cell_size, self.top, self.left + self.width * self.cell_size,
               self.top + self.height * self.cell_size, self)

    def render(self, screen, clock, draw, t=None):
        if draw == 2:
            c = clock.tick()
            if c > 10:
                c = 1
            self.balls_sprites.update(c, self)
        elif draw == 1:
            x0 = t[0]
            y0 = t[1]
            x0, y0 = x0 - (self.left + self.width * self.cell_size // 2), self.top + self.height * self.cell_size - y0
            x0, y0 = 150 * x0 / sqrt(x0 ** 2 + y0 ** 2), 150 * y0 / sqrt(x0 ** 2 + y0 ** 2)
            x0, y0 = x0 + (self.left + self.width * self.cell_size // 2), self.top + self.height * self.cell_size - y0
            pygame.draw.line(screen, (30, 30, 30),
                             (self.left + self.width * self.cell_size // 2,
                              self.top + self.height * self.cell_size - 5 - 1), (int(x0), int(y0)), width=1)
        self.all_sprites.draw(screen)
        for i in range(self.height):
            for j in range(self.width):
                x = self.left + self.cell_size * j
                y = self.top + self.cell_size * i
                if (i >= self.height - 1) or (i <= 1):
                    pass
                elif self.debug:
                    pygame.draw.rect(screen, pygame.Color('red'), (x, y, self.cell_size, self.cell_size), width=1)
                else:
                    pygame.draw.rect(screen, (2, 2, 2), (x, y, self.cell_size, self.cell_size), width=1)
        self.borders.draw(screen)

        font = pygame.font.Font(None, 25)
        for box in self.box_list:
            text = font.render(f"{box.n}", True, (100, 255, 100))
            text_x = box.rect.x + 5
            text_y = box.rect.y + 5
            screen.blit(text, (text_x, text_y))

    def on_click(self):
        for i in self.balls:
            if i.vx != 0 and i.vy != 0:
                return False
        return True
