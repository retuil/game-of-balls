import os
import sys
from math import sqrt
from HelpFunction import HelpFunction

import pygame

from game_file.level import next_level


# def load_image(name, colorkey=None):
#     fullname = os.path.join('data', name)
#     if not os.path.isfile(fullname):
#         print(f"'{fullname}' error")
#         sys.exit()
#     image = pygame.image.load(fullname)
#     return image


class Ball(pygame.sprite.Sprite):
    image = HelpFunction().load_image('ball.png', -1)

    def __init__(self, x, y, vx, vy, board, *group):
        super().__init__(*group)

        self.wall_collision_sound = pygame.mixer.Sound(HelpFunction().load_sound('wall_collision_sound.mp3'))
        self.block_collision_sound = pygame.mixer.Sound(HelpFunction().load_sound('block_collision_sound.mp3'))
        self.dead_ball_sound = pygame.mixer.Sound(HelpFunction().load_sound('dead_ball.mp3'))

        self.image = Ball.image
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.x1 = self.rect.x
        self.y1 = self.rect.y
        if vy >= board.top + board.height * board.cell_size * 0.95:
            vy = board.top + board.height * board.cell_size * 0.95
        vx, vy = vx - board.x - board.r, board.y + board.r - vy - 2
        vx, vy = vx / sqrt(vx ** 2 + vy ** 2), -vy / sqrt(vx ** 2 + vy ** 2)

        self.vx, self.vy = vx, vy
        self.v = 750
        self.mask = pygame.mask.from_surface(self.image)
        self.history = [None]

        board.all_sprites.add(self)
        board.balls_sprites.add(self)



    def update(self, c, board):
        self.x1 += self.vx * self.v * c / 1000
        self.y1 += self.vy * self.v * c / 1000
        self.rect.x, self.rect.y = int(self.x1), int(self.y1)

        if self.x1 < board.left - board.cell_size or self.x1 > board.left + board.cell_size * (board.width + 1) or \
                self.y1 < board.top - board.cell_size or self.y1 > board.top + board.cell_size * (board.height + 1):
            self.rect.x = self.x1 = board.left + board.width * board.cell_size // 2
            self.rect.y = self.y1 = board.top + board.cell_size * (board.height - 0.25)
            self.vx = 0
            self.vy = abs(self.vy)
        if pygame.sprite.spritecollideany(self, board.vertical_borders):
            if self.rect.x > board.left + board.width // 2:
                self.vx = -abs(self.vx)
            else:
                self.vx = abs(self.vx)
            self.history.append(None)
            self.wall_collision_sound.play()
        if pygame.sprite.spritecollideany(self, board.up_horizontal_borders):
            self.vy = abs(self.vy)
            self.history.append(None)
            self.wall_collision_sound.play()
        if pygame.sprite.spritecollideany(self, board.down_horizontal_borders) or \
                self.rect.y >= board.top + board.height * board.cell_size + 2 * board.r:
            self.dead_ball_sound.play()
            self.vx = 0
            self.vy = 0
            self.history.append(None)
            if self == board.balls[0]:
                board.x_ = board.balls[0].rect.x

            if (board.count_balls == len(board.balls)) and board.check():
                if board.infinite_level:
                    board.box_sprites.update(board)
                    next_level(board)
                elif board.score <= len(board.level):
                    for j in board.level[board.score - 1]:
                        if j is not None:
                            j.visible(board)
                    board.score += 1
                    board.box_sprites.update(board)

            self.kill()

        for box in board.box_list:
            if pygame.sprite.collide_rect(self, box):
                self.block_collision_sound.play()
                if self.rect.x + board.r in range(box.rect.x + 1 - board.r, box.rect.x + board.cell_size + 1 + board.r):
                    if self.rect.y <= box.rect.y + board.r + 1:
                        self.vy = -abs(self.vy)
                        if self.history[-1] != box:
                            box.touch(board)
                            self.history.append(box)
                            break
                    if self.rect.y + board.r >= box.rect.y + board.cell_size - board.r + 1:
                        self.vy = abs(self.vy)
                        if self.history[-1] != box:
                            box.touch(board)
                            self.history.append(box)
                            break

                if self.rect.y + board.r in range(box.rect.y + 1 - board.r, box.rect.y + board.cell_size + 1 + board.r):
                    if self.rect.x <= box.rect.x + board.r + 1:
                        self.vx = -abs(self.vx)
                        if self.history[-1] != box:
                            box.touch(board)
                            self.history.append(box)
                            break
                    if self.rect.x + board.r >= box.rect.x + board.cell_size - board.r + 1:
                        self.vx = abs(self.vx)
                        if self.history[-1] != box:
                            box.touch(board)
                            self.history.append(box)
                            break
        if (self.rect.x < board.left - board.cell_size) or \
                (self.rect.x > board.left + board.width * board.cell_size + board.cell_size) or \
                (self.rect.y < board.top - board.cell_size) or \
                (self.rect.y > board.top + board.height * (board.cell_size + 1) + board.cell_size):
            print(1)
            self.vx = 0
            self.vy = 0
            self.kill()

        for bonus in board.bonus_list:
            if pygame.sprite.collide_mask(self, bonus):
                bonus.touch(board)
