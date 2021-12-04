import sys
import re


def get_data():
    with open(sys.argv[1], 'r') as f:
        D = list(map(int, re.findall(r'\d+', f.readline())))
        L = [[[int(d), False] for d in (list(map(int, re.findall(r'\d+', l))))]for l in f if len(l) != 1]
        B = [L[5*n:5*(n+1)] for n in range(len(L)) if len(L[5*n:5*(n+1)]) != 0]
    return D, B


def part_one(D, B):
     # for each number
    for i, num in enumerate(D):
        # go through board and turn to true if some
        for j, board in enumerate(B):
            for k, row in enumerate(board):
                for l, p in enumerate(row):
                    if p[0] == num:
                        B[j][k][l][1] = True
        # check to see if one board has one full row or column of marked numbers
        for j, board in enumerate(B):
            # for each board
            # check if row all True
            win = []
            # transposed board.
            tboard = list(zip(*board))
            for row in board:
                win.append(all([p[1] for p in row]))
            for col in tboard:
                win.append(all([q[1] for q in col]))
            if any(win):
                s = sum(sum([d[0] for d in row if not d[1]]) for row in board)
                return s * num


def part_two(D, B):
    # for each number
    for i, num in enumerate(D):
        # go through board and turn to true if some
        for j, board in enumerate(B):
            for k, row in enumerate(board):
                for l, p in enumerate(row):
                    if p[0] == num:
                        B[j][k][l][1] = True
        # check to see if one board has one full row or column of marked numbers
        for j, board in enumerate(B):
            # for each board
            # check if row all True
            win = []
            # transposed board.
            tboard = list(zip(*board))
            for row in board:
                win.append(all([p[1] for p in row]))
            for col in tboard:
                win.append(all([q[1] for q in col]))
            if any(win) and len(B) != 1:
                del B[j]
            elif any(win) and len(B) == 1:
                s  = sum(sum([d[0] for d in row if not d[1]]) for row in B[0])
                return s*num


D, B = get_data()
print(f'part one: {part_one(D, B)}')
print(f'part two: {part_two(D, B)}')
