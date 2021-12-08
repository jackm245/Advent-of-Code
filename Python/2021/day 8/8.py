import sys
import itertools


def get_data():
    with open(sys.argv[1], 'r') as f:
        L = [l.strip() for l in f]
        D = []
        for l in L:
            x = l.strip().split(' | ')
            D.append([x[0].split(), x[1].split()])
    return D


def part_one(L):
    # 0 = 6 segments
    # 1 = 2
    # 2 = 5
    # 3 = 5
    # 4 = 4
    # 5 = 5
    # 6 = 6
    # 7 = 3
    # 8 = 7
    # 9 = 6
    return sum([sum([1 for val in out_vals if len(val) in [2, 3, 4, 7]]) for in_vals, out_vals in L])


def part_two(L):
    # [a, b, c, d, e, f, g]
    # [d, e, a, f, g, b, c]
    ans = 0
    for in_vals, out_vals in L:
        vals = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        one = [i for i in in_vals if len(i) == 2][0]
        four = [i for i in in_vals if len(i) == 4][0]
        seven = [i for i in in_vals if len(i) == 3][0]
        eight = [i for i in in_vals if len(i) == 7][0]
        nine = [i for i in in_vals if len(i) == 6 and all([x in i for x in four])][0]
        six = [i for i in in_vals if len(i) == 6 and len([x for x in one if x in i]) == 1][0]
        zero = [i for i in in_vals if len(i) == 6 and i != nine and i != six][0]
        two = [i for i in in_vals if len(i) == 5 and [i for i in vals if i not in nine][0] in i][0]
        three = [i for i in in_vals if len(i) == 5 and i != two and all([x in i for x in one])][0]
        five = [i for i in in_vals if len(i) == 5 and i != two and i != three][0]
        D = {zero:0, one:1, two:2, three:3, four:4, five:5, six:6, seven:7, eight:8, nine:9}
        val = ''
        for out_val in out_vals:
            for p in [''.join(i) for i in itertools.permutations(out_val)]:
                if p in D.keys():
                    val += str(D[p])
        ans += int(val)
    return ans


L = get_data()
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')
