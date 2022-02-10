from math import sqrt

import pygame

from game_file.ball import Ball
from game_file.border import Border
from game_file.level import next_level, create_level


class Board:
    def __init__(self, size, margins, cell_size, screen, r=5, level=None, debug=False):
        self.debug = debug
        self.width, self.height = size[0], size[1]
        self.left, self.top = margins[0], margins[1]
        self.cell_size = cell_size
        self.r = r
        self.x = self.x_ = self.left + self.width * self.cell_size // 2 - self.r
        self.y = self.top + self.height * self.cell_size - 2 * self.r - 2
        self.vx, self.vy = 0, 0
        self.font = pygame.font.SysFont('arial', 25)
        self.stop = False
        self.screen = screen

        self.all_sprites = pygame.sprite.Group()
        self.balls_sprites = pygame.sprite.Group()
        self.balls = []
        self.count_balls = self.count_balls_ = 0
        self.box_sprites = pygame.sprite.Group()
        self.v_box_sprites = pygame.sprite.Group()
        self.box_list = []
        self.up_horizontal_borders = pygame.sprite.Group()
        self.down_horizontal_borders = pygame.sprite.Group()
        self.vertical_borders = pygame.sprite.Group()
        self.borders = pygame.sprite.Group()
        self.bonus_sprites = pygame.sprite.Group()
        self.bonus_list = []

        Border(self.left, self.top, self.left + self.width * self.cell_size, self.top, self)
        Border(self.left, self.top + self.height * self.cell_size, self.left + self.width * self.cell_size,
               self.top + self.height * self.cell_size, self)
        Border(self.left, self.top, self.left, self.top + self.height * self.cell_size, self)
        Border(self.left + self.width * self.cell_size, self.top, self.left + self.width * self.cell_size,
               self.top + self.height * self.cell_size, self)

        self.clock = pygame.time.Clock()

        self.level = []
        self.score = 1
        if level is None:
            self.infinite_level = True
            self.level.append(next_level(self))
        else:
            self.infinite_level = False
            create_level(self, level)
            for el in self.level[0]:
                if el is not None:
                    el.visible(self)
            self.score += 1

        self.timer = 0

    def render(self, draw, aim_coord):
        self.screen.fill((0, 0, 0))
        c = self.clock.tick()
        if c > 10:
            c = 1
        self.timer += c
        if draw == 2:
            self.balls_sprites.update(c, self)
        self.all_sprites.draw(self.screen)
        if len(self.balls) < self.count_balls and self.timer >= 150:
            self.add_ball()
            self.timer = 0
        self.draw_grid()
        self.balls_sprites.draw(self.screen)
        self.borders.draw(self.screen)
        if draw == 1:
            self.draw_aim(aim_coord)
        self.draw_text()
        if self.stop and not self.infinite_level:
            return True, "lose"
        if not self.infinite_level and not len(self.box_sprites) and self.check():
            print(self.score)
            return True, 'Win'
        if self.stop and self.infinite_level:
            return True, self.score
        return False, self.score

    def check(self):
        for i in self.balls:
            if i.vx != 0 or i.vy != 0:
                return False
        return True

    def motion(self, vx, vy):
        self.timer = 0
        self.x = self.x_
        self.count_balls = self.count_balls_
        if self.vx == 0:
            self.count_balls = 1
        else:
            self.x = self.balls[0].rect.x
        self.balls = []
        self.vx, self.vy = vx, vy
        self.add_ball()

    def add_ball(self):
        ball = Ball(self.x, self.y, self.vx, self.vy, self)
        self.balls.append(ball)

    def draw_aim(self, aim_coord):
        aim_x = aim_coord[0]
        aim_y = aim_coord[1]
        if aim_y >= self.top + self.height * self.cell_size * 0.95:
            aim_y = self.top + self.height * self.cell_size * 0.95
        aim_x, aim_y = aim_x - self.x_ - self.r, self.y + self.r - aim_y - 2
        aim_x, aim_y = 150 * aim_x / sqrt(aim_x ** 2 + aim_y ** 2), 150 * aim_y / sqrt(aim_x ** 2 + aim_y ** 2)
        aim_x, aim_y = aim_x + self.x_ + self.r, self.y + self.r - aim_y
        pygame.draw.line(self.screen, pygame.Color('green'),
                         (self.x_ + self.r, self.y + self.r - 2), (int(aim_x), int(aim_y)), width=1)

    def draw_grid(self):
        for i in range(self.height):
            for j in range(self.width):
                x = self.left + self.cell_size * j
                y = self.top + self.cell_size * i
                if (i >= self.height - 1) or (i <= 1):
                    pass
                elif self.debug:
                    pygame.draw.rect(self.screen, pygame.Color('red'), (x, y, self.cell_size, self.cell_size), width=1)
                else:
                    pygame.draw.rect(self.screen, (2, 2, 2), (x, y, self.cell_size, self.cell_size), width=1)

    def draw_text(self):
        for box in self.box_list:
            text = self.font.render(f"{box.n}", True, (0, 0, 0))
            text_x = box.rect.x + 5
            text_y = box.rect.y + 5
            self.screen.blit(text, (text_x, text_y))

        text = self.font.render(f'Счёт: {self.score - 1}', True, pygame.Color('white'))
        self.screen.blit(text, (self.left, self.top + self.height * self.cell_size + 5))

        text = self.font.render(f'Шаров: {self.count_balls_}', True, pygame.Color('white'))
        self.screen.blit(text, (self.left + self.cell_size * 2, self.top + self.height * self.cell_size + 5))