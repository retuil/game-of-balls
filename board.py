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
                board.all_sprites.add(el)

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
        self.horizontal_borders = pygame.sprite.Group()
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
            for i in range(len(self.balls)):
                if self.balls[i].rect.y + 2 * self.balls[i].r >= ((self.top + self.cell_size * self.height) - 1):
                    if self.balls[i].vx != 0 and self.balls[i].vy != 0:
                        if self.u <= len(self.level):
                            self.board.insert(2, self.level[-self.u])
                            del self.board[-1]
                            for j in self.board[2]:
                                if j is not None:
                                    self.box_sprites.add(j)
                                    self.all_sprites.add(j)
                            self.u += 1
                        self.box_sprites.update(self)

        elif draw == 1:
            x0 = t[0]
            y0 = t[1]
            x0, y0 = x0 - (self.left + self.width * self.cell_size // 2), self.top + self.height * self.cell_size - y0
            x0, y0 = 150 * x0 / sqrt(x0 ** 2 + y0 ** 2), 150 * y0 / sqrt(x0 ** 2 + y0 ** 2)
            x0, y0 = x0 + (self.left + self.width * self.cell_size // 2), self.top + self.height * self.cell_size - y0
            pygame.draw.line(screen, (30, 30, 30),
                             (self.left + self.width * self.cell_size // 2,
                              self.top + self.height * self.cell_size - 5 - 1), (int(x0), int(y0)), width=1)

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
        # pygame.draw.rect(screen, (200, 200, 200),
        #                  (self.left, self.top, self.cell_size * self.width, self.cell_size * self.height), width=1)
        self.all_sprites.draw(screen)
        self.borders.draw(screen)

    def on_click(self):
        for i in self.balls:
            if i.vx != 0 and i.vy != 0:
                return False
        return True
