import sys


def get_data():
    with open(sys.argv[1], 'r') as f:
        L = [l.strip().split() for l in f]
    return L



def part_one(L):
    r, c = 0, 0
    for cmd, val in L:
        val = int(val)
        if cmd ==  'forward':
            r += val
        elif cmd == 'up':
            c -= val
        else:
            c += val
    return (r*c)



def part_two(L):
    r, c = 0, 0
    aim = 0
    for cmd, val in L:
        val = int(val)
        if cmd ==  'forward':
            r += int(val)
            c += aim * int(val)
        elif cmd == 'up':
            aim -= int(val)
        else:
            aim += int(val)
    return (r*c)


L = get_data()
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')
