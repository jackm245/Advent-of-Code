def get_input(filename):
    with open(filename, 'r') as f:
        L = [int(l.strip()) for l in f]
    return L


def part_one(L):
    return sum([(f//3)-2 for f in L])


def part_two(L):
    fuel = 0
    for f in L:
        while (f//3)-2 > 0:
            f = (f//3)-2
            fuel += f
    return fuel


def main():
    data = get_input('data.in')
    print(f'Part 1: {part_one(data)}')
    print(f'Part 2: {part_two(data)}')


if __name__ == '__main__':
    main()


