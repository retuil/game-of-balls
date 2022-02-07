import os
import sys

import pygame


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"'{fullname}' error")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Box(pygame.sprite.Sprite):
    image1 = load_image('box_1.png')
    image2 = load_image('box_2.png')
    image3 = load_image('box_3.png')
    image4 = load_image('box_4.png')
    image5 = load_image('box_5.png')
    image6 = load_image('box_6.png')
    image7 = load_image('box_7.png')
    image = {
        0: image1,
        1: image2,
        2: image3,
        3: image4,
        4: image5,
        5: image6,
        6: image7,
    }

    def __init__(self, x, y, board, n, *group):
        super().__init__(*group)
        self.image = Box.image1
        self.rect = self.image.get_rect()
        self.rect.x = board.left + x * board.cell_size - 1
        self.rect.y = board.top + y * board.cell_size - 1
        self.n = n
        self.image = Box.image[self.n % 7]

    def update(self, board):
        self.rect.y += board.cell_size
        if self.rect.y >= board.top + (board.height - 2) * board.cell_size:
            board.stop = True

    def touch(self, board):
        self.n -= 1
        if self.n <= 0:
            board.box_list.remove(self)
            self.kill()
        else:
            self.image = Box.image[self.n % 7]

    def visible(self, board):
        board.v_box_sprites.add(self)
        board.all_sprites.add(self)
        board.box_list.append(self)
