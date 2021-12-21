import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 50
        self.top = 50
        self.cell_size = 50

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                x = self.left + self.cell_size * j
                y = self.top + self.cell_size * i
                if self.board[i][j] == -1:
                    pygame.draw.rect(screen, (25, 25, 25), (x, y, self.cell_size, self.cell_size), width=1)
                else:
                    pygame.draw.rect(screen, pygame.Color('white'), (x, y, self.cell_size, self.cell_size))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        for i in range(self.height):
            for j in range(self.width):
                x = self.left + self.cell_size * j
                y = self.top + self.cell_size * i
                if mouse_pos[1] in range(y, y + self.cell_size) and mouse_pos[0] in range(x, x + self.cell_size):
                    print(j, i)
                    return j, i
        return None

    def on_click(self, cell):
        if cell is not None:
            self.board[cell[1]][cell[0]] *= -1
            for i in range(self.width):
                self.board[cell[1]][i] *= -1
            for j in range(self.height):
                self.board[j][cell[0]] *= -1
