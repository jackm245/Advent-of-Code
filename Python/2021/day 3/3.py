import sys


def get_data():
    with open(sys.argv[1], 'r') as f:
        L = [l.strip() for l in f]
    return L


def part_one(L):
    T = [''.join([L[j][i] for j in range(len(L))]) for i in range(len(L[0]))]
    B = [max(set(t), key=t.count) for t in T]
    C = [min(set(t), key=t.count) for t in T]
    return int(''.join(B), 2) * int(''.join(C), 2)


def part_two(L):
    O, C = L, L
    for i in range(len(L[0])):
        # oxygen generator rating
        if len(O) > 1:
            O_zeros = len([j for j in O if j[i] == '0'])
            O_ones= len([j for j in O if j[i] == '1'])
            if O_ones >= O_zeros:
                O = [j for j in O if j[i] == '1']
            else:
                O = [j for j in O if j[i] == '0']
        # co2 scrubber rating
        if len(C) > 1:
            C_zeros = len([j for j in C if j[i] == '0'])
            C_ones = len([j for j in C if j[i] == '1'])
            if C_ones >= C_zeros:
                C = [j for j in C if j[i] == '0']
            else:
                C = [j for j in C if j[i] == '1']
    return int(O[0],2) *  int(C[0],2)


L = get_data()
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')
