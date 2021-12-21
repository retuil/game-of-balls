from math import sqrt

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Ball(pygame.sprite.Sprite):
    image = load_image('ball.png')

    def __init__(self, x0, y0, board, r=5, *group):
        super().__init__(*group)
        self.x = board.left + board.width * board.cell_size // 2
        self.y = board.top + board.height * board.cell_size - r - 1
        x0, y0 = x0 - (board.left + board.width * board.cell_size // 2), board.top + board.height * board.cell_size - y0
        x0, y0 = x0 / sqrt(x0 ** 2 + y0 ** 2), y0 / sqrt(x0 ** 2 + y0 ** 2)
        self.x0 = x0
        self.y0 = -y0
        self.v = 800
        self.r = r
