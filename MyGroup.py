import pygame
from MyException import *


#Класс MyGroup необходим для создания группы спрайтов с заданным местоположением в группе и создания общих параметров группы спрайтов
#Спрайт может принадлежать только к одной группе класса MyGroup, количество других групп к которым может принадлежать спрайт не ограничено

class MyGroup(pygame.sprite.Group):
    def __init__(self, *sprites,  indents_between_sprites=[0, 0], edge_indents=[0, 0], sprites_size=[0, 0]):
        super().__init__(*sprites)
        self.indents_between_sprites = self.indent_between_sprites_x, self.indent_between_sprites_y = indents_between_sprites
        self.sorted_sprites = self.sort_sprites()
        self.edge_indent_x, self.edge_indent_y = self.edge_indents = edge_indents
        self.width_sprites, self.height_sprites = self.sprites_size = sprites_size
        self.grouped_sprites = self.sprite_distribution()


    def add(self, *sprites):
        sprites_pos = list(map(lambda x: x.pos_in_group, list(sprites)))
        for sprite_pos in sprites_pos:
            if sprites_pos.count(sprite_pos) != 1:
                raise ErrorAddingToGroup('В группе добавляемых спрайтов есть спрайты с одинаковой позицией')
            self.update(sprite_pos=sprite_pos, change_position='увеличение')
        super().add(*sprites)
        self.sorted_sprites = self.sort_sprites()

    def remove(self, *sprites):
        sprites_pos = list(map(lambda x: x.pos_in_group, list(sprites)))
        for sprite_pos in sprites_pos:
            self.update(sprite_pos=sprite_pos, change_position='уменьшение')
        super().remove(*sprites)
        self.sorted_sprites = self.sort_sprites()

    def sort_sprites(self):
        sprite_list = self.sprites()
        for i in sprite_list:
            for n_sprite in range(len(sprite_list)):
                if sprite_list[n_sprite].pos_in_group > sprite_list[n_sprite + 1].pos_in_group:
                    sprite_list[n_sprite], sprite_list[n_sprite + 1] = sprite_list[n_sprite + 1], sprite_list[n_sprite]
        return sprite_list



    def same_size(self):
        same_size = True
        all_sprites = self.sprites()
        first_size = all_sprites[0].size
        for sprite_size in all_sprites:
            if not sprite_size.size == first_size:
                same_size = False
        return same_size

    def sprite_distribution(self):
        max_width = self.width_sprites - self.edge_indent_x * 2
        groups = [[]]
        fillible_group = 0
        len_of_group = 0
        number_in_group = 0
        for sprite in self.sorted_sprites:
            if number_in_group == 0:
                groups[fillible_group].append(sprite)
                len_of_group += sprite.wight
            else:
                if len_of_group + sprite.wight + self.edge_indent_x <= max_width:
                    groups[fillible_group].append(sprite)
                    len_of_group += sprite.wight + self.edge_indent_x
                else:
                    groups.append([sprite])
                    len_of_group = sprite.wight
                    number_in_group = 0
            number_in_group += 1
        return groups
