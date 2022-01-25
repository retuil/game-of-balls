import pygame
from board import Board

def main():
    pass


def game_event():
    pass


if __name__ == '__main__':
    pygame.init()
    size = width, height = 550, 800
    screen = pygame.display.set_mode(size)

    f = open("levels/lvl_1.txt", encoding="utf8")
    lvl = f.readlines()
    f.close()

    board = Board((7, 11), (100, 100), 50, 5)

    running = True
    draw, vx_vy = None, None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board.check():
                    draw = 1
                    vx_vy = event.pos
            if event.type == pygame.MOUSEMOTION and draw == 1:
                if board.check():
                    vx_vy = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                if board.check():
                    draw = 2
                    board.count_balls += 1
                    board.motion(*event.pos)
        board.render(screen, draw, vx_vy)
        pygame.display.flip()
    pygame.quit()
