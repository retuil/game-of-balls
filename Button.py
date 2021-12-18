import pygame
from MyException import *
from MyGroup import MyGroup


class Button(pygame.sprite.Sprite):
    def __init__(self, pos_in_group, *groups, size=[None, None], pos=None, text=False, image=False, color=False):
        for group in groups:
            if type(group) == MyGroup:
                self.main_group = group
        self.pos_in_group = pos_in_group
        super().__init__(*groups)
        if size[0] is None and size[1] is None:
            my_group_size = self.main_group.sprites_size
            if my_group_size[0] is not None and my_group_size[1] is not None:
                self.width, self.height = self.size = my_group_size
            else:
                raise ErrorInitSprite('Отсутствуют данные о размере спрайта')
        else:
            self.width, self.height = self.size = size  #TODO: решить проблему определения позиции спрайта с разным размером других спрайтов


    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        if 'sprite_pos' in kwargs.keys():
            if kwargs['sprite_pos'] <= self.pos_in_group:
                if kwargs['change_position'] == 'увеличение':
                    self.pos_in_group += 1
                elif kwargs['change_position'] == 'уменьшение':
                    self.pos_in_group -= 1    #TODO: решить проблему с передаванием в спрайт отсортированной группы
