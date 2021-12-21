import pygame


class Board:
    # создание поля
    def __init__(self, width, height, debug=False):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 50
        self.top = 50
        self.cell_size = 50
        self.debug = debug
        self.balls = []

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen, clock, draw):
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
        if draw:
            c = clock.tick()
            if c > 10:
                c = 1
            for i in range(len(self.balls)):
                pygame.draw.circle(screen, pygame.Color('white'), (int(self.balls[i].x), int(self.balls[i].y)),
                                   self.balls[i].r)
                self.balls[i].x += self.balls[i].x0 * self.balls[i].v * c / 1000
                self.balls[i].y += self.balls[i].y0 * self.balls[i].v * c / 1000
                if int(self.balls[i].x) <= self.balls[i].r + self.left:
                    self.balls[i].x0 = abs(self.balls[i].x0)
                if int(self.balls[i].x) >= ((self.left + self.cell_size * self.width) - self.balls[i].r):
                    self.balls[i].x0 = -abs(self.balls[i].x0)
                if int(self.balls[i].y) <= self.balls[i].r + self.top:
                    self.balls[i].y0 = abs(self.balls[i].y0)
                if int(self.balls[i].y) >= ((self.top + self.cell_size * self.height) - self.balls[i].r - 1):
                    self.balls[i].x0 = 0
                    self.balls[i].y0 = 0

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        for i in range(self.height):
            for j in range(self.width):
                x = self.left + self.cell_size * j
                y = self.top + self.cell_size * i
                if (mouse_pos[1] in range(y, y + self.cell_size) and mouse_pos[0] in range(x, x + self.cell_size)) and (
                        1 < i < self.height - 1):
                    return j, i
        return None

    def on_click(self, cell):
        if cell is not None:
            self.board[cell[1]][cell[0]] *= -1
            for i in range(self.width):
                self.board[cell[1]][i] *= -1
            for j in range(self.height):
                self.board[j][cell[0]] *= -1
