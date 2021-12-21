import pygame
from board import Board
from ball import Ball


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    board = Board(8, 11)
    board.set_view(100, 100, 50)
    running = True
    clock = pygame.time.Clock()
    draw = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                draw = True
                x0, y0 = event.pos
                board.balls.append(Ball(x0, y0, board, 5))
        screen.fill((0, 0, 0))
        board.render(screen, clock, draw)
        pygame.display.flip()
    pygame.quit()
