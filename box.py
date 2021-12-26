import os
import sys

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"'{fullname}' error")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Box(pygame.sprite.Sprite):
    image1 = load_image('box_1.png')
    image2 = load_image('box_2.png')

    def __init__(self, x, y, board, n, *group):
        super().__init__(*group)
        self.image = Box.image1
        self.rect = self.image.get_rect()
        self.rect.x = board.left + (x + 1) * board.cell_size - 1
        self.rect.y = board.top + (y + 1) * board.cell_size - 1
        self.n = n

    def update(self, board):
        self.rect.y += board.cell_size
