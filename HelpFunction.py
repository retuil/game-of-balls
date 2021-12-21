import os
import sys
import pygame
from MyException import *


class HelpFunction():
    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            raise ErrorLoadImage('Изображение с таким именем отсутсвует в папке data')
        image = pygame.image.load(fullname)
        return image