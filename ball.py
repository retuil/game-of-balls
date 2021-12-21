from math import sqrt


class Ball:
    def __init__(self, x0, y0, board, r=5):
        self.x = board.left + board.width * board.cell_size // 2
        self.y = board.top + board.height * board.cell_size - r - 1
        x0, y0 = x0 - (board.left + board.width * board.cell_size // 2), board.top + board.height * board.cell_size - y0
        x0, y0 = x0 / sqrt(x0 ** 2 + y0 ** 2), y0 / sqrt(x0 ** 2 + y0 ** 2)
        self.x0 = x0
        self.y0 = -y0
        self.v = 800
        self.r = r
