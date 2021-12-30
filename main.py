import pygame
from board import Board
from ball import Ball

if __name__ == '__main__':
    pygame.init()
    size = width, height = 550, 800
    screen = pygame.display.set_mode(size)

    f = open("levels/lvl_1.txt", encoding="utf8")
    lvl = f.readlines()
    f.close()

    board = Board(7, 11, lvl)
    board.set_view(100, 100, 50)
    running = True
    clock = pygame.time.Clock()
    draw = 0
    t = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board.on_click():
                    draw = 1
                    t = event.pos
            if event.type == pygame.MOUSEMOTION and draw == 1:
                if board.on_click():
                    t = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                if board.on_click():
                    draw = 2
                    x0, y0 = event.pos
                    board.balls.append(Ball(x0, y0, board, 5))
                    t = None
                    # screen.fill((0, 0, 0))

        screen.fill((0, 0, 0))
        board.render(screen, clock, draw, t)
        pygame.display.flip()
    pygame.quit()
