import sys
import re


def get_data():
    with open(sys.argv[1], 'r') as f:
        L = list(map(int, re.findall(r'\d+', f.readline())))
        F = [L.count(x) for x in range(9)]
    return F


def solve(days,F):
    for _ in range(days):
        next_day = [0 for _ in range(9)]
        for i in range(1, 10):
            next_day[i-1] = F[(i)%9]
        next_day[6] += F[0]
        F = next_day
    return sum(F)


F = get_data()
print(f'part one: {solve(80, F)}')
print(f'part two: {solve(256, F)}')
