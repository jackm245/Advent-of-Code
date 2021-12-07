import sys


def get_data():
    with open(sys.argv[1], 'r') as f:
         L = [int(l.strip()) for l in f]
    return L


def part_one(L):
    count = 0
    for i in range(1, len( L)):
        if L[i - 1] < L[i]:
            count += 1
    return count


def part_two(L):
    count = 0
    for i in range(len(L) - 3):
        if sum(L[i:i+3]) < sum(L[i+1:i+4]):
            count += 1
    return count


L = get_data()
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')
