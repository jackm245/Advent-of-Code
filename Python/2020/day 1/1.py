import sys

def get_data():
    with open(sys.argv[1], 'r') as f:
        L = [int(l.strip()) for l in f]
    return L


def part_one(L):
    for i in L:
        for j in L:
            if i + j == 2020:
                return i*j


def part_two(L):
    for i in L:
        for j in L:
            for k in L:
                if i + j+ k == 2020:
                    return i*j*k


L = get_data()
#  print(L)
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')
