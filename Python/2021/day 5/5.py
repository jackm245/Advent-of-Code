import sys


def get_data():
    with open(sys.argv[1], 'r') as f:
        L = [[list(map(int, x.split(','))) for x in l.strip().split(' -> ')] for l in f]
    return L


def part_one(L):
    grid = {}
    for line in L:
        x1, y1 = line[0]
        x2, y2 = line[1]
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        if x1 == x2 or y1 == y2:
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    if (x, y) not in grid:
                        grid[(x, y)] = 0
                    grid[(x, y)] += 1
    ans = len([int(i) for i in grid.values() if i  > 1])
    return ans


def part_two(L):
    grid = {}
    for line in L:
        x1, y1 = line[0]
        x2, y2 = line[1]
        dx = x2 - x1
        dy = y2 - y1
        for i in range(max(abs(dx), abs(dy))+1):
            x = x1+(0 if dx == 0 else dx/(abs(dx)))*i
            y = y1+(0 if dy == 0 else dy/(abs(dy)))*i
            if (x, y) not in grid:
                grid[(x, y)] = 0
            grid[(x, y)] += 1
    ans = len([int(i) for i in grid.values() if i  > 1])
    return ans


L = get_data()
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')
