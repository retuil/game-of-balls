from random import randint, shuffle

from game_file.add_ball_bonus import AddBallBonus
from game_file.box import Box


def create_level(board, level):
    if level is not None:
        for i, s in enumerate(level):
            i_level = []
            for j, el in enumerate(s.rstrip().split(',')):
                if el == '.':
                    i_level.append(None)
                elif el == '+':
                    q = AddBallBonus(j, 2 - i, board)
                    i_level.append(q)
                    board.box_sprites.add(q)
                else:
                    q = Box(j, 2 - i, board, int(el))
                    i_level.append(q)
                    board.box_sprites.add(q)
            board.level.append(i_level)


def next_level(board):
    k = 0
    level = [randint(0, 2) * board.score or '.', randint(0, 2) * board.score or '.'] + \
            [board.score] * (board.width - 4) + ['.', '+']
    shuffle(level)
    i_level = []
    for i, el in enumerate(level):
        if el == '.':
            i_level.append(None)
        elif el == '+':
            q = AddBallBonus(i, 2, board)
            i_level.append(q)
            board.v_box_sprites.add(q)
            board.all_sprites.add(q)
            board.box_sprites.add(q)
            board.bonus_list.append(q)
        else:
            q = Box(i, 2, board, int(el))
            i_level.append(q)
            board.v_box_sprites.add(q)
            board.all_sprites.add(q)
            board.box_sprites.add(q)
            board.box_list.append(q)
    board.score += 1
    board.level.append(i_level)


def open_level_file(level):
    if level is None:
        return None
    f = open(f"levels/level_{level}.txt", encoding="utf8")
    level = f.readlines()
    f.close()
    return level
