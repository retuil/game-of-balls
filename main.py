import pygame

from board import Board
from level import open_level_file


def main():
    pygame.init()
    size = width, height = 550, 800
    screen = pygame.display.set_mode(size)

    game_event(screen)

    pygame.quit()


def game_event(screen, level=None):
    level = open_level_file(level)
    board = Board((7, 11), (100, 100), 50, 5, level)
    running = True
    draw, aim_coord = None, None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board.check():
                    draw = 1
                    aim_coord = event.pos
            if event.type == pygame.MOUSEMOTION and draw == 1:
                if board.check():
                    aim_coord = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                if board.check():
                    draw = 2
                    board.count_balls += 1
                    board.motion(*event.pos)
        board.render(screen, draw, aim_coord)
        pygame.display.flip()


if __name__ == '__main__':
    main()
