import pygame
from MyException import *
from MyGroup import MyGroup
from HelpFunction import HelpFunction


class Button(pygame.sprite.Sprite):
    def __init__(self, pos_in_group, *groups, size=[None, None], pos=[None, None], text=False, image=False, color=False):
        in_main_group = False
        for group in groups:
            if type(group) == MyGroup:
                if not in_main_group:
                    self.main_group = group
                    in_main_group = True
                else:
                    raise ErrorNumberOfMyGroups('Спрайт добавлен более чем в одну группу \"MyGroup\"')
        if not in_main_group:
            raise ErrorNumberOfMyGroups('Спрайт добавлен более че в одну группу \"MyGroup\"')

        self.pos_in_group = pos_in_group
        super().__init__(*groups)

        error_in_size = ErrorInitSprite('Не задан размер спрайтов в группе')
        if size[0] is None and size[1] is None:
            my_group_size = self.main_group.sprites_size
            if my_group_size[0] is not None and my_group_size[1] is not None:
                self.width, self.height = self.size = my_group_size
            else:
                raise error_in_size
        elif pos_in_group == 0:
            self.width, self.height = self.size = size
            self.main_group.sprites_size = size
        else:
            raise error_in_size

        if pos[0] is not None and pos[1] is not None and pos_in_group == 0:
            self.left, self.top = self.pos = pos
            self.main_group.edge_indents = pos
        else:
            number_sprite_line = 0
            number_sprite_in_line = 0
            allbreak = False
            for sprite_lines in self.main_group.grouped_sprites:
                for sprite in sprite_lines:
                    if sprite == self:
                        self.width = self.main_group.edge_indent_x + self.main_group.indent_between_sprites_x * number_sprite_in_line + self.main_group.wight_sprites * number_sprite_in_line
                        self.height = self.main_group.edge_indent_y + self.main_group.indent_between_sprites_y * number_sprite_line + self.main_group.height_sprites * number_sprite_line
                        break
                        allbreak = True
                    else:
                        number_sprite_in_line += 1
                if allbreak:
                    break
                number_sprite_line += 1

        self.rect = (*self.pos, *self.size)

        if text:
            self.text = text
        if image:
            self.image = HelpFunction.load_image(image)     #Передать только имя файла, лежащего в папке data
        if color:
            self.color = pygame.Color(color)


    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        if 'sprite_pos' in kwargs.keys():
            if kwargs['sprite_pos'] <= self.pos_in_group:
                if kwargs['change_position'] == 'увеличение':
                    self.pos_in_group += 1
                elif kwargs['change_position'] == 'уменьшение':
                    self.pos_in_group -= 1

