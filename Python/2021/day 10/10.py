import sys


def get_data():
    with open(sys.argv[1], 'r') as f:
        L = [[b for b in l.strip()] for l in f]
    return L


def part_one(L):
    O = ['(', '[', '{', '<']
    C = [')', ']', '}', '>']
    score = {')':3, ']':57, '}':1197, '>':25137}
    ans = 0
    for l in L:
        open = []
        for b in l:
            if b in O:
                open.append(b)
            elif not open or C.index(b) != O.index(open[-1]):
                ans += score[b]
                CORRUPT.append(l)
                break
            else:
                del open[-1]
    return ans


def part_two(L):
    #  print(CORRUPT)
    O = ['(', '[', '{', '<']
    C = [')', ']', '}', '>']
    cscore = {')':1, ']':2, '}':3, '>':4}
    scores = []
    for l in L:
        open = []
        if l not in CORRUPT:
            #  print(l)
            for b in l:
                if b in O:
                    open.append(b)
                else:
                    #  print(b)
                    del open[-1]
                #  print(open)
        ro = reversed(open)
        closing = [C[O.index(i)] for i in ro]
        #  print(closing)
        score = 0
        for c in closing:
            score *= 5
            score += cscore[c]
        if score != 0:
            scores.append(score)
    return sorted(scores)[len(scores) // 2]


CORRUPT = []
L = get_data()
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')
