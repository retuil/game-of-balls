from math import sqrt

import pygame

from ball import Ball
from border import Border

from level import next_level, create_level


class Board:
    def __init__(self, width, height, left, top, cell_size, r=5, lvl=None, debug=False):
        self.debug = debug

        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.r = r

        self.x = self.left + self.width * self.cell_size // 2 - self.r
        self.y = self.top + self.height * self.cell_size - 2 * self.r - 2
        self.vx = 0
        self.vy = 0

        self.t = 0

        self.all_sprites = pygame.sprite.Group()
        self.balls_sprites = pygame.sprite.Group()
        self.box_sprites = pygame.sprite.Group()
        self.v_box_sprites = pygame.sprite.Group()
        self.box_list = []
        self.up_horizontal_borders = pygame.sprite.Group()
        self.down_horizontal_borders = pygame.sprite.Group()
        self.vertical_borders = pygame.sprite.Group()
        self.borders = pygame.sprite.Group()

        Border(self.left, self.top, self.left + self.width * self.cell_size, self.top, self)
        Border(self.left, self.top + self.height * self.cell_size, self.left + self.width * self.cell_size,
               self.top + self.height * self.cell_size, self)
        Border(self.left, self.top, self.left, self.top + self.height * self.cell_size, self)
        Border(self.left + self.width * self.cell_size, self.top, self.left + self.width * self.cell_size,
               self.top + self.height * self.cell_size, self)

        self.balls = []
        self.count_balls = 0

        self.level = []
        self.score = 1
        if lvl is None:
            self.infinite_level = True
            self.level.append(next_level(self))
        else:
            self.infinite_level = False
            create_level(self, lvl)
            for el in self.level[0]:
                if el is not None:
                    self.v_box_sprites.add(el)
                    self.all_sprites.add(el)
                    self.box_list.append(el)
            self.score += 1

    def render(self, screen, clock, draw, vx_vy):
        c = clock.tick()
        if c > 10:
            c = 1
        self.t += c

        if draw == 2:
            self.balls_sprites.update(c, self)
        elif draw == 1:
            vx = vx_vy[0]
            vy = vx_vy[1]
            if vy >= self.top + self.height * self.cell_size * 0.95:
                vy = self.top + self.height * self.cell_size * 0.95
            vx, vy = vx - self.x - self.r, self.y + self.r - vy - 2
            vx, vy = 150 * vx / sqrt(vx ** 2 + vy ** 2), 150 * vy / sqrt(vx ** 2 + vy ** 2)
            vx, vy = vx + self.x + self.r, self.y + self.r - vy
            pygame.draw.line(screen, pygame.Color('green'),
                             (self.x + self.r, self.y + self.r - 2), (int(vx), int(vy)), width=1)
        self.all_sprites.draw(screen)

        if len(self.balls) < self.count_balls and self.t >= 150:
            self.add_ball()
            self.t = 0

        for i in range(self.height):
            for j in range(self.width):
                x = self.left + self.cell_size * j
                y = self.top + self.cell_size * i
                if (i >= self.height - 1) or (i <= 1):
                    pass
                elif self.debug:
                    pygame.draw.rect(screen, pygame.Color('red'), (x, y, self.cell_size, self.cell_size), width=1)
                else:
                    pygame.draw.rect(screen, (2, 2, 2), (x, y, self.cell_size, self.cell_size), width=1)
        self.balls_sprites.draw(screen)
        self.borders.draw(screen)

        font = pygame.font.Font(None, 25)
        for box in self.box_list:
            text = font.render(f"{box.n}", True, (0, 0, 0))
            text_x = box.rect.x + 5
            text_y = box.rect.y + 5
            screen.blit(text, (text_x, text_y))

    def check(self):
        for i in self.balls:
            if i.vx != 0 and i.vy != 0:
                return False
        return True

    def motion(self, vx, vy):
        self.t = 0
        if self.vx == 0:
            self.count_balls = 1
        else:
            self.x = self.balls[0].rect.x
        for i in self.balls:
            i.kill()
        self.balls = []
        self.vx = vx
        self.vy = vy
        self.add_ball()

    def add_ball(self):
        ball = Ball(self.x, self.y, self.vx, self.vy, self)
        self.balls.append(ball)
