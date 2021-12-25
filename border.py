import pygame


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2, board):
        super().__init__(board.all_sprites)
        if x1 == x2:
            self.add(board.vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.image.fill(pygame.Color('white'))
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(board.horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.image.fill(pygame.Color('white'))
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)
        self.add(board.borders)
