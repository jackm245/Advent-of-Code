def get_data(filename):
    with open(filename, 'r') as F:
        L = F.readline().split(',')
        # remove newline chara
        L[-1] = L[-1][:-1]
        L = list(map(int, L))
    return L


def part_one(L):
    for pos in range(0, len(L), 4):
        if L[pos] == 99:
            return L[0]
        in1 = L[L[pos+1]]
        in2 = L[L[pos+2]]
        if L[pos] == 1:
            res = in1+in2
        elif L[pos] == 2:
            res = in1*in2
        else:
            print(f'error not opcode {L[pos]}')
            print(L)
        L[L[pos+3]]=res


def part_two(L):
    for i in range(100):
        for j in range(100):
            L[1] = i
            L[2] = j
            if part_one(L) == 19690720:
                return 100 * i + j


def main():
    filename = 'last_state.in'
    L = get_data(filename)
    print(f'part 1: {part_one(L)}')
    print(f'part 2 : {part_two(L)}')


if __name__ == '__main__':
    main()

