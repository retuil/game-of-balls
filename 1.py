import pygame
from math import sqrt


class ball:
    def __init__(self, width, height, x0, y0):
        self.x = width / 2
        self.y = height - 5
        x0, y0 = x0 - 150, 600 - y0
        x0, y0 = x0 / sqrt(x0 ** 2 + y0 ** 2), y0 / sqrt(x0 ** 2 + y0 ** 2)
        self.x0 = x0
        self.y0 = -y0


def main():
    pygame.init()
    pygame.display.set_caption('Шарики')
    size = width, height = 300, 600
    screen = pygame.display.set_mode(size)
    running = True
    v = 600
    clock = pygame.time.Clock()
    d = False
    balls = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                d = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                d = True
                x0, y0 = event.pos
                balls.append(ball(width, height, x0, y0))
        if d:
            screen.fill(pygame.Color('black'))
            c = clock.tick()
            if c > 10:
                c = 1
            for i in range(len(balls)):
                pygame.draw.circle(screen, pygame.Color('white'), (int(balls[i].x), int(balls[i].y)), 5)
                balls[i].x += balls[i].x0 * v * c / 1000
                balls[i].y += balls[i].y0 * v * c / 1000
                if int(balls[i].x) <= 5:
                    balls[i].x0 = abs(balls[i].x0)
                if int(balls[i].x) >= (width - 5):
                    balls[i].x0 = -abs(balls[i].x0)
                if int(balls[i].y) <= 5:
                    balls[i].y0 = abs(balls[i].y0)
                if int(balls[i].y) >= (height - 5):
                    balls[i].x0 = 0
                    balls[i].y0 = 0
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
