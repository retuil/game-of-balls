import os
import sys

import pygame


def load_image(name, screen, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"'{fullname}' error")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class AddBallBonus(pygame.sprite.Sprite):
    def __init__(self, x, y, board, *group):
        super().__init__(*group)
        self.image = load_image('add_ball_bonus.png', board.screen)
        self.rect = self.image.get_rect()
        self.rect.x = board.left + x * board.cell_size - 1
        self.rect.y = board.top + y * board.cell_size - 1
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, board):
        self.rect.y += board.cell_size
        if self.rect.y >= board.top + (board.height - 1) * board.cell_size:
            board.bonus_list.remove(self)
            self.kill()

    def touch(self, board):
        board.count_balls_ += 1
        board.bonus_list.remove(self)
        self.kill()
