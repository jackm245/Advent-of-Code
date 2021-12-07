import sys
import re


def get_data():
    with open(sys.argv[1], 'r') as f:
        D = list(map(int, re.findall(r'\d+', f.readline())))
        L = [[[int(d), False] for d in (list(map(int, re.findall(r'\d+', l))))]for l in f if len(l) != 1]
        B = [L[5*n:5*(n+1)] for n in range(len(L)) if len(L[5*n:5*(n+1)]) != 0]
    return D, B


def part_one(D, B):
    for num in D:
        for j, board in enumerate(B):
            for k, row in enumerate(board):
                for l, p in enumerate(row):
                    if p[0] == num:
                        B[j][k][l][1] = True
            tboard = list(zip(*board))
            wins = [all([p[1] for p in row]) for row in board] + [all([q[1] for q in col]) for col in tboard]
            if any(wins):
                return num * sum(sum([d[0] for d in row if not d[1]]) for row in board)


def part_two(D, B):
    for num in D:
        for j, board in enumerate(B):
            for k, row in enumerate(board):
                for l, p in enumerate(row):
                    if p[0] == num:
                        B[j][k][l][1] = True
        for j, board in enumerate(B):
            tboard = list(zip(*board))
            wins = [all([p[1] for p in row]) for row in board] + [all([q[1] for q in col]) for col in tboard]
            if any(wins) and len(B) != 1:
                del B[j]
            elif any(wins) and len(B) == 1:
                return num * sum(sum([d[0] for d in row if not d[1]]) for row in B[0])


D, B = get_data()
print(f'part one: {part_one(D, B)}')
print(f'part two: {part_two(D, B)}')
