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
    image = load_image('ball.png', -1)

    def __init__(self, vx, vy, board, r=5, *group):
        super().__init__(*group)
        self.image = Ball.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.x = board.left + board.width * board.cell_size // 2 - r
        self.rect.y = board.top + board.height * board.cell_size - 2 * r - 2
        self.x1 = self.rect.x
        self.y1 = self.rect.y
        vx = vx - (board.left + board.width * board.cell_size // 2)
        vy = board.top + board.height * board.cell_size - vy - 2
        vx, vy = vx / (1 * sqrt(vx ** 2 + vy ** 2)), vy / (1 * sqrt(vx ** 2 + vy ** 2))
        self.vx = vx
        self.vy = -vy
        self.v = 800
        self.r = r
        board.all_sprites.add(self)
        board.balls_sprites.add(self)

    def update(self, c, board):
        self.x1 += self.vx * self.v * c / 1000
        self.y1 += self.vy * self.v * c / 1000
        self.rect.x, self.rect.y = int(self.x1), int(self.y1)
        if pygame.sprite.spritecollideany(self, board.vertical_borders):
            if self.rect.x > board.left + board.width // 2:
                self.vx = -abs(self.vx)
            else:
                self.vx = abs(self.vx)
        if pygame.sprite.spritecollideany(self, board.up_horizontal_borders):
            self.vy = abs(self.vy)
        if pygame.sprite.spritecollideany(self, board.down_horizontal_borders):
            if self.vx != 0 or self.vy != 0:  # TODO: Потом условие, что все шары уже выпущены
                if board.u <= len(board.level):
                    board.board.insert(2, board.level[-board.u])
                    del board.board[-1]
                    for j in board.board[2]:
                        if j is not None:
                            board.v_box_sprites.add(j)
                            board.all_sprites.add(j)
                            board.box_list.append(j)
                    board.u += 1
                board.box_sprites.update(board)
            self.vx = 0
            self.vy = 0

        for box in board.box_list:
            if pygame.sprite.collide_mask(self, box):
                if self.rect.x + self.r in range(box.rect.x + 1, box.rect.x + board.cell_size + 1):
                    if self.rect.y + self.r <= box.rect.y + 1:
                        self.vy = -abs(self.vy)
                        box.touch(board)
                    if self.rect.y + self.r >= box.rect.y + board.cell_size + 1:
                        self.vy = abs(self.vy)
                        box.touch(board)
                if self.rect.y + self.r in range(box.rect.y + 1, box.rect.y + board.cell_size + 1):
                    if self.rect.x + self.r <= box.rect.x + 1:
                        self.vx = -abs(self.vx)
                        box.touch(board)
                    if self.rect.x + self.r >= box.rect.x + board.cell_size + 1:
                        self.vx = abs(self.vx)
                        box.touch(board)
