import pygame
from MyException import *


#Класс MyGroup необходим для создания группы спрайтов с заданным местоположением в группе и создания общих параметров группы спрайтов
#Спрайт может принадлежать только к одной группе класса MyGroup, количество других групп к которым может принадлежать спрайт не ограничено

class MyGroup(pygame.sprite.Group):
    def __init__(self, *sprites,  indent=0, sprites_size=[None, None]):
        super().__init__(*sprites)
        self.indent = indent
        self.width_sprites, self.height_sprites = self.sprites_size = sprites_size

    def add(self, *sprites):
        sprites_pos = list(map(lambda x: x.pos_in_group, list(sprites)))
        for sprite_pos in sprites_pos:
            if sprites_pos.count(sprite_pos) != 1:
                raise ErrorAddingToGroup('В группе добавляемых спрайтов есть спрайты с одинаковой позицией')
            self.update(sprite_pos=sprite_pos, change_position='увеличение')
        super().add(*sprites)

    def remove(self, *sprites):
        sprites_pos = list(map(lambda x: x.pos_in_group, list(sprites)))
        for sprite_pos in sprites_pos:
            self.update(sprite_pos=sprite_pos, change_position='уменьшение')
        super().remove(*sprites)

    def sort_sprites(self):
        sprite_list = self.sprites()
        for i in sprite_list:
            for n_sprite in range(len(sprite_list)):
                if sprite_list[n_sprite].pos_in_group > sprite_list[n_sprite + 1].pos_in_group:
                    sprite_list[n_sprite], sprite_list[n_sprite + 1] = sprite_list[n_sprite + 1], sprite_list[n_sprite]
        return MyGroup(*sprite_list, indent=self.indent, sprites_size=self.sprites_size)