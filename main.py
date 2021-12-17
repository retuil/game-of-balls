import pygame
from MyException import *
from Button import Button
from MyGroup import MyGroup


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False