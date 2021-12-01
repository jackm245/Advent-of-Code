import sys

def get_data():
    with open(sys.argv[1], 'r') as f:
        # L = [int(l.strip()) for l in f]
        L = [l.strip() for l in f]
    return L


def part_one(L):
    count = 0
    width = len(L[0])
    height = len(L)
    j = 0
    for i in range(height):
        if L[i][j%width] == '#':
            count += 1
        j += 3
    return count


def part_two(L):
    trees = 1
    width = len(L[0])
    height = len(L)
    RD = [(1,1), (3,1), (5,1), (7, 1), (1, 2)]
    for right, down in RD:
        j = 0
        count = 0
        for i in range(0, height, down):
            if L[i][j%width] == '#':
                count += 1
            j += right
        trees *= count
    return trees

# 264 too low
L = get_data()
#  print(L)
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')
