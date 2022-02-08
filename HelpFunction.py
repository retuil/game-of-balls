import os
import sys
import pygame
from MyException import *


class HelpFunction():
    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            raise LoadError(f'Изображение с именем \'{name}\' отсутсвует в папке data')
        image = pygame.image.load(fullname)
        return image

    def load_sound(self, name):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            raise LoadError('Звук с таким именем отсутствует в папке data')
        return fullname
