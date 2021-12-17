import pygame
from MyException import *


class MyGroup(pygame.sprite.Group):
    def __init__(self, *sprites,  indent=0):
        super().__init__(*sprites)
        self.indent = indent  #TODO: сделать автоматическое определение спрайтом своего размера и местоположения по данным группы

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
