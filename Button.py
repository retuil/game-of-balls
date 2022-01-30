import pygame
from MyException import *
from MyGroup import MyGroup
from HelpFunction import HelpFunction


class Button(pygame.sprite.Sprite):
    def __init__(self, pos_in_group, *groups, text=False, image=False, color=pygame.Color((0, 0, 0)),
                 size=[None, None], pos=[None, None]):
        super().__init__(*groups)
        self.pos_in_group = pos_in_group

        in_main_group = False
        for group in groups:
            if type(group) == MyGroup:
                if not in_main_group:
                    self.main_group = group
                    in_main_group = True
                    group.add(self)
                else:
                    raise ErrorNumberOfMyGroups('Спрайт добавлен более чем в одну группу \"MyGroup\"')
        # if not in_main_group:
        #     raise ErrorNumberOfMyGroups('Спрайт не добавлен в группу \"MyGroup\"')





        error_in_size = ErrorInitSprite('Не задан размер спрайтов в группе')
        if self.main_group:
            my_group_size = self.main_group.sprites_size
            if my_group_size[0] is not None and my_group_size[1] is not None:
                self.width, self.height = self.size = my_group_size
            else:
                raise error_in_size
        elif size[0] is not None and size[1] is not None:
            self.width, self.height = self.size = size
        else:
            raise error_in_size

        # if pos[0] is not None and pos[1] is not None and pos_in_group == 0:
        #     self.left, self.top = self.pos = pos
        #     self.main_group.edge_indents = pos
        # else:

        if text:
            self.text = text
        # Добавил:
        else:
            self.text = None
        if color:
            self.color = pygame.Color(color)
        if image:
            self.image = HelpFunction().load_image(image)  # Передать только имя файла, лежащего в папке data
        else:
            self.image = image

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        if 'sprite_pos' in kwargs.keys():
            if kwargs['sprite_pos'] <= self.pos_in_group:
                if kwargs['change_position'] == 'увеличение':
                    self.pos_in_group += 1
                elif kwargs['change_position'] == 'уменьшение':
                    self.pos_in_group -= 1

    def position(self):
        number_sprite_line = 0
        number_sprite_in_line = 0
        allbreak = False
        for sprite_lines in self.main_group.grouped_sprites:
            for sprite in sprite_lines:
                if sprite == self:
                    self.x = self.main_group.edge_indent_x + self.main_group.indent_between_sprites_x * (
                                number_sprite_in_line) + self.main_group.width_sprites * number_sprite_in_line
                    self.y = self.main_group.edge_indent_y + self.main_group.indent_between_sprites_y * (
                                number_sprite_line) + self.main_group.height_sprites * number_sprite_line
                    self.pos = [self.x, self.y]
                    allbreak = True
                    break
                else:
                    number_sprite_in_line += 1
            if allbreak:
                break
            number_sprite_line += 1
            number_sprite_in_line = 0

        self.rect = (pygame.Rect(*self.pos, *self.size))
        if not self.image:
            self.image = pygame.Surface(self.size)
            self.image.fill(self.color)
        else:
            self.image = pygame.transform.scale(self.image, self.size)

        if self.text:
            text = self.text[0]
            color_text = self.text[1]
            font = self.text[2]
            p_text = font.render(text, True, color_text)
            width_text, height_text = font.size(text)
            if width_text > self.width or height_text > self.height:
                raise TextError('Текст больше кнопки, на которой размещается')
            size_text = ((self.width - width_text) // 2, (self.height - height_text) // 2)
            self.image.blit(p_text, size_text)
