import pygame

from game_file.board import Board
from game_file.level import open_level_file


def main():
    pygame.init()
    size = width, height = 550, 800
    screen = pygame.display.set_mode(size)

    start_event(screen, width, height)

    pygame.quit()


def game_event(screen, width, height, level=None):
    level = open_level_file(level)
    board = Board((7, 11), (100, 100), 50, screen, 5, level)
    running = True
    draw, aim_coord = None, None
    r = (False, None)
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
                    if not board.count_balls:
                        board.count_balls_ += 1
                    board.motion(*event.pos)
        r = board.render(draw, aim_coord)
        if r[0]:
            break
        pygame.display.flip()
    if r[0]:
        # r[1] - значение для таблицы рекордов
        start_event(screen, width, height)


def start_event(screen, width, height):
    running = True
    game = False
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render(f'Нажмите для старта', True, pygame.Color('white'))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, pygame.Color('white'), (text_x - 10, text_y - 10,
                                                     text_w + 20, text_h + 20), 1)

    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if (x > text_x - 10) and (x < text_x + text_w + 10) and \
                        (y > text_y - 10) and (y < text_y + text_h + 10):
                    game = True
                    break
        if game:
            break
    if game:
        game_event(screen, width, height)


def end_event(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
