import sys


def get_data():
    with open(sys.argv[1], 'r') as f:
        # L = [int(l.strip()) for l in f]
        L = [l.strip() for l in f]
    return L


def part_one(L):
    pass


def part_two(L):
    pass


L = get_data()
#  print(L)
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')
