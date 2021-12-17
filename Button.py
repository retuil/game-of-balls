import pygame
from MyException import *


class Button(pygame.sprite.Sprite):
    def __init__(self, *group, pos_in_group=0, size=None, pos=None, text=False, image=False, color=False):
        self.pos_in_group = pos_in_group  #TODO: определить все переменные
        super().__init__(*group)

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        if kwargs['sprite_pos'] <= self.pos_in_group:
            if kwargs['change_position'] == 'увеличение':
                self.pos_in_group += 1
            elif kwargs['change_position'] == 'уменьшение':
                self.pos_in_group -= 1