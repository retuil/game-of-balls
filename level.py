from random import randint

from box import Box


def create_level(board, level):
    if level is not None:
        for i, s in enumerate(level):
            i_level = []
            for j, el in enumerate(s.rstrip().split(',')):
                if el == '.':
                    i_level.append(None)
                else:
                    q = Box(j, 2 + len(level) - i - len(level), board, int(el))
                    i_level.append(q)
                    board.box_sprites.add(q)
            board.level.append(i_level)


def next_level(board):
    i_level = []
    k = 0
    for i in range(board.width):
        r = randint(1, 8)
        if r < 6 and k <= board.width - 2:
            k += 1
            if r % 4 == 0:
                q = Box(i, 2, board, 2 * board.score)
            else:
                q = Box(i, 2, board, board.score)
            i_level.append(q)
            board.v_box_sprites.add(q)
            board.all_sprites.add(q)
            board.box_sprites.add(q)
            board.box_list.append(q)
        else:
            i_level.append(None)
    board.score += 1
    board.level.append(i_level)


def open_level_file(level):
    if level is None:
        return None
    f = open(f"levels/{level}", encoding="utf8")
    level = f.readlines()
    f.close()
    return level
