from math import sqrt

import pygame


class Board:
    def __init__(self, width, height, debug=False):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]

        self.left = 50
        self.top = 50
        self.cell_size = 50

        self.debug = debug

        self.balls = []
        self.all_sprites = pygame.sprite.Group()

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen, clock, draw, t=None):
        for i in range(self.height):
            for j in range(self.width):
                x = self.left + self.cell_size * j
                y = self.top + self.cell_size * i
                if (i >= self.height - 1) or (i <= 1):
                    pass
                elif self.board[i][j] == -1:
                    if self.debug:
                        pygame.draw.rect(screen, pygame.Color('red'), (x, y, self.cell_size, self.cell_size), width=1)
                    else:
                        pygame.draw.rect(screen, (2, 2, 2), (x, y, self.cell_size, self.cell_size), width=1)
                else:
                    pygame.draw.rect(screen, pygame.Color('white'), (x, y, self.cell_size, self.cell_size))
        pygame.draw.rect(screen, (200, 200, 200),
                         (self.left, self.top, self.cell_size * self.width, self.cell_size * self.height), width=1)
        if draw == 2:
            c = clock.tick()
            if c > 10:
                c = 1
            self.all_sprites.draw(screen)
            self.all_sprites.update(c)
            for i in range(len(self.balls)):
                if self.balls[i].rect.x <= self.left:
                    self.balls[i].x0 = abs(self.balls[i].x0)
                if self.balls[i].rect.x + 2 * self.balls[i].r >= (self.left + self.cell_size * self.width):
                    self.balls[i].x0 = -abs(self.balls[i].x0)
                if self.balls[i].rect.y <= self.top:
                    self.balls[i].y0 = abs(self.balls[i].y0)
                if self.balls[i].rect.y + 2 * self.balls[i].r >= ((self.top + self.cell_size * self.height) - 1):
                    self.balls[i].x0 = 0
                    self.balls[i].y0 = 0
        elif draw == 1:
            x0 = t[0]
            y0 = t[1]
            x0, y0 = x0 - (self.left + self.width * self.cell_size // 2), self.top + self.height * self.cell_size - y0
            x0, y0 = 150 * x0 / sqrt(x0 ** 2 + y0 ** 2), 150 * y0 / sqrt(x0 ** 2 + y0 ** 2)
            x0, y0 = x0 + (self.left + self.width * self.cell_size // 2), self.top + self.height * self.cell_size - y0
            pygame.draw.line(screen, (30, 30, 30),
                             (self.left + self.width * self.cell_size // 2,
                              self.top + self.height * self.cell_size - 5 - 1), (int(x0), int(y0)), width=1)

    def on_click(self):
        for i in self.balls:
            if i.x0 != 0 and i.y0 != 0:
                return False
        return True
