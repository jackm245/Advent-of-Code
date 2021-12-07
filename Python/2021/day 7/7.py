import sys
import re


def get_data():
    with open(sys.argv[1], 'r') as f:
        L = list(map(int, re.findall(r'\d+', f.readline())))
    return L


def part_one(L):
    median = sorted(L)[len(L)//2]
    min_fuel = sum([abs(x - median) for x in L])
    return min_fuel


def part_two(L):
    min_fuel = -1
    for i in range(max(L)):
        S = int(sum([(abs(x-i) * (abs(x-i)+1))/2 for x in L]))
        if min_fuel == -1 or S < min_fuel:
            min_fuel = S
    return min_fuel


L = get_data()
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')
