import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Шарики')
    size = width, height = 300, 600
    screen = pygame.display.set_mode(size)
    screen2 = pygame.Surface(screen.get_size())
    running = True
    v = 200
    clock = pygame.time.Clock()
    d = False
    x, y = 0, 0
    balls = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                d = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                d = True
                x, y = event.pos
                x, y = x - 150, 600 - y
                balls.append([150, 595, x / y, -1])
        if d:
            screen.fill(pygame.Color('black'))
            c = clock.tick()
            if c > 10:
                c = 1
            for i in range(len(balls)):
                pygame.draw.circle(screen, pygame.Color('white'), (int(balls[i][0]), int(balls[i][1])), 5)
                balls[i][0] += balls[i][2] * v * c / 1000
                balls[i][1] += balls[i][3] * v * c / 1000
                if int(balls[i][0]) <= 5:
                    balls[i][2] = abs(balls[i][2])
                if int(balls[i][0]) >= (width - 5):
                    balls[i][2] = -abs(balls[i][2])
                if int(balls[i][1]) <= 5:
                    balls[i][3] = abs(balls[i][3])
                if int(balls[i][1]) >= (height - 5):
                    balls[i][2] = 0
                    balls[i][3] = 0
        pygame.display.flip()
    pygame.quit()
