import pygame
from MyGroup import MyGroup
from MyException import *


#Класс MyGroup необходим для создания группы спрайтов с заданным местоположением в группе и создания общих параметров группы спрайтов
#Спрайт может принадлежать только к одной группе класса SortedGroup, количество других групп к которым может принадлежать спрайт не ограничено

class SortedGroup(MyGroup):
    def __init__(self, indents_between_sprites, edge_indents, sprites_size, screen, *sprites):
        self.screen_size = screen.get_size()
        self.indents_between_sprites = self.indent_between_sprites_x, self.indent_between_sprites_y = indents_between_sprites
        self.edge_indent_x, self.edge_indent_y = self.edge_indents = edge_indents
        self.width_sprites, self.height_sprites = self.sprites_size = sprites_size
        pygame.sprite.AbstractGroup.__init__(self)
        self.add(*sprites)
        self.sorted_sprites = self.sort_sprites()
        self.grouped_sprites = self.sprite_distribution()


    def add(self, *sprites):
        sprites_pos = list(map(lambda x: x.pos_in_group, list(sprites)))
        for sprite_pos in sprites_pos:
            # if sprites_pos.count(sprite_pos) != 1:
            #     raise ErrorAddingToGroup('В группе добавляемых спрайтов есть спрайты с одинаковой позицией')
            self.update(sprite_pos=sprite_pos, change_position='увеличение')
        super().add(*sprites)
        self.sorted_sprites = self.sort_sprites()
        self.grouped_sprites = self.sprite_distribution()

    def remove(self, *sprites):
        sprites_pos = list(map(lambda x: x.pos_in_group, list(sprites)))
        for sprite_pos in sprites_pos:
            self.update(sprite_pos=sprite_pos, change_position='уменьшение')
        super().remove(*sprites)
        self.sorted_sprites = self.sort_sprites()
        self.grouped_sprites = self.sprite_distribution()

    def sort_sprites(self):
        sprite_list = self.sprites()
        for i in sprite_list:
            for n_sprite in range(len(sprite_list)):
                if n_sprite + 1 < len(sprite_list) and\
                        sprite_list[n_sprite].pos_in_group > sprite_list[n_sprite + 1].pos_in_group:
                    sprite_list[n_sprite], sprite_list[n_sprite + 1] = sprite_list[n_sprite + 1], sprite_list[n_sprite]
        return sprite_list



    # def same_size(self):
    #     same_size = True
    #     all_sprites = self.sprites()
    #     first_size = all_sprites[0].size
    #     for sprite_size in all_sprites:
    #         if not sprite_size.size == first_size:
    #             same_size = False
    #     return same_size

    def sprite_distribution(self):
        max_width = self.screen_size[0] - self.edge_indent_x * 2
        groups = [[]]
        fillible_group = 0
        len_of_group = 0
        number_in_group = 0
        for sprite in self.sorted_sprites:
            if number_in_group == 0:
                groups[fillible_group].append(sprite)
                len_of_group += self.width_sprites
            elif len_of_group + self.width_sprites + self.edge_indent_x <= max_width:
                groups[fillible_group].append(sprite)
                len_of_group += self.width_sprites + self.edge_indent_x
            else:
                groups.append([sprite])
                len_of_group = self.width_sprites
                number_in_group = 0
                fillible_group += 1
            number_in_group += 1
        return groups

    def draw(self, surface):
        for sprite in self.sorted_sprites:
            sprite.position()
        super().draw(surface)

