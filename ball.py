import os
import sys
from math import sqrt

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"'{fullname}' error")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Ball(pygame.sprite.Sprite):
    image = load_image('ball.png')

    def __init__(self, x0, y0, board, r=5, *group):
        super().__init__(*group)
        self.image = Ball.image
        self.rect = self.image.get_rect()
        self.rect.x = board.left + board.width * board.cell_size // 2 - r
        self.rect.y = board.top + board.height * board.cell_size - 2 * r - 2
        self.x1 = self.rect.x
        self.y1 = self.rect.y
        x0 = x0 - (board.left + board.width * board.cell_size // 2)
        y0 = board.top + board.height * board.cell_size - y0 - 2
        x0, y0 = x0 / sqrt(x0 ** 2 + y0 ** 2), y0 / sqrt(x0 ** 2 + y0 ** 2)
        self.x0 = x0
        self.y0 = -y0
        self.v = 800
        self.r = r
        board.all_sprites.add(self)

    def update(self, c):
        self.x1 += self.x0 * self.v * c / 1000
        self.y1 += self.y0 * self.v * c / 1000
        self.rect.x, self.rect.y = round(self.x1), round(self.y1)
