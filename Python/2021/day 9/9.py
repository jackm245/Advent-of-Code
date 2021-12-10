import sys
from collections import deque
from math import prod


def get_data():
    with open(sys.argv[1], 'r') as f:
        # L = [int(l.strip()) for l in f]
        L = [l.strip() for l in f]
    return L


def part_one(L):
    # horizontal
    height = len(L)
    width = len(L[0])
    risk_levels = []
    for r, l in enumerate(L):
        for c, num in enumerate(l):
            # if in corner
            # top left
            #  if r == 0 and c == 0:
                #  if num < L[r+1][c] and num < L[r][c+1]:
                    #  risk_levels.append(num)
            #  # top right
            #  elif r == 0 and c == width-1:
                #  if num < L[r+1][c] and num < L[r][c-1]:
                    #  risk_levels.append(num)
            #  # bottom left
            #  elif r == height-1 and c == 0:
                #  if num < l[r-1][c] and num < L[r][c+1]:
                    #  risk_levels.append(num)
            #  # bottom right
            #  elif r == height-1 and c == width-1:
                #  if num < L[r-1][c] and num < L[r][c-11]:
                    #  risk_levels.append(num)
            #  # top edge
            #  elif r == 0:
                #  if num < L[r+1][c] and num < L[r][c-1] and num < L[r][c+1]:
                    #  risk_levels.append(num)
            #  # right
            #  elif c == width-1:
                #  if num < L[r+1][c] and num < L[r-1][c] and num < L[r][c-1]:
                    #  risk_levels.append(num)
            #  # bottom
            #  elif r == height-1:
                #  if num < L[r-1][c] and num < L[r][c+1] and num < L[r][c-1]:
                    #  risk_levels.append(num)
            #  # left edge
            #  elif c == 0:
                #  if num < L[r-1][c] and num < L[r+1][c] and num < L[r][c+1]:
                    #  risk_levels.append(num)
            #  else:
                #  if num < L[r-1][c] and num < L[r+1][c] and num < L[r][c-1] and num < L[r][c+1]:
                    #  risk_levels.append(num)
            A = []
            for d in range(4):
                 # up down left right
                rr = r + [-1, 0, 1, 0][d]
                cc = c + [0, 1, 0, -1][d]
                if 0<=rr<=height-1 and 0<=cc<=width-1:
                    A.append(L[rr][cc] > num)
            if all(A):
                risk_levels.append(num)
    return sum(list(map( int, risk_levels))) + len(risk_levels)



def part_two(L):
    # breadth-first search
    BS = []
    SEEN = set()
    height = len(L)
    width = len(L[0])
    G = [list(map(int, l)) for l in L]
    for r, l in enumerate(G):
        for c, num in enumerate(l):
            if (r, c) not in SEEN and G[r][c] != 9:
                size = 0
                queue = deque()
                queue.append((r, c))
                while len(queue) > 0:
                    r, c = queue.popleft()
                    if not (r, c) in SEEN:
                        SEEN.add((r, c))
                        size += 1
                        for d in range(4):
                            dr = r+[-1, 0, 1, 0][d]
                            dc = c+[0, 1, 0, -1][d]
                            if 0<=dr<=height-1 and 0<=dc<=width-1 and G[dr][dc]!= 9:
                                queue.append((dr, dc))
                BS.append(size)
    print(sorted(BS)[-3:])
    return prod(sorted(BS)[-3:])



L = get_data()
#  print(L)
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')
